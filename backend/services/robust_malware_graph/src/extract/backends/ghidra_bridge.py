"""
robust‑malware‑graph – GhidraBridge backend
───────────────────────────────────────────
Headless **GHIDRA** integration through the `ghidra_bridge` Python package.
This backend sits at the *heavy* end of the spectrum (similar to Angr) but
brings GHIDRA's proven analysis capabilities – decompiler, symbol recovery,
indirect flow resolution – to the extraction pipeline while keeping the same
schema contract as other backends.

Why a *bridge* instead of launching headless analyzers via CLI?
  • **Speed** – a live GHIDRA instance stays warm across samples, avoiding JVM
    spin‑up cost when the pipeline batches thousands of binaries.
  • **Flexibility** – access to the full Java API enables richer metadata
    (e.g. demangled names, data‑flow casts) compared with CLI JSON dumps.
  • **Interactivity** – security analysts can attach to the same workspace in
    GUI mode during debugging without affecting the automated run.

Prerequisites
~~~~~~~~~~~~~
* Install GHIDRA ≥ 11 and launch once to accept EULA.
* `pip install ghidra‑bridge` (tested with 5.2).
* Run the following **one‑time** GHIDRA script to start the bridge listener:

```python
# Inside GHIDRA Script Manager (Python)
from ghidra_bridge_server import BridgeServer
BridgeServer(port=18001, responseTimeout=600).start()
```

`GhidraBridge` then connects via socket (`localhost:18001` by default).

Limitations
~~~~~~~~~~~
* Requires JVM + GHIDRA instance reachable; pipeline must handle fallback to
  Capstone/Radare2 if connection fails.
* Syscall extraction is heuristic (searches for known syscall mnemonics).

Example
~~~~~~~
>>> from src.extract.backends.ghidra_bridge import GhidraBridge
>>> gb = GhidraBridge("/bin/ls")
>>> print(gb.build_fcg()["functions"][0])
{"id":0,"name":"main","addr":"0x4012d0","external":False}
"""

from __future__ import annotations

import json
import logging
import multiprocessing as mp
import socket
import sys
import time
from pathlib import Path
from types import FrameType
from typing import Any, Dict, List, Tuple

try:
    import ghidra_bridge  # type: ignore – external
except ModuleNotFoundError as exc:  # pragma: no cover
    raise ImportError("ghidra_bridge package not found – install via pip") from exc

# ────────────────────────────────────────────────────────────────
# Logger helper (fallback style)
# ────────────────────────────────────────────────────────────────
try:
    from src.common.utils import get_logger
except ModuleNotFoundError:  # standalone fallback
    def get_logger(name: str):  # noqa: D401
        logging.basicConfig(level=logging.INFO,
                            format="[%(levelname)s] %(name)s: %(message)s")
        return logging.getLogger(name)

_LOG = get_logger(__name__)

# ╔═══════════════════════════════════════════════════════════════╗
# ║  Timeout helpers                                              ║
# ╚═══════════════════════════════════════════════════════════════╝

def _sigterm_handler(signum: int, frame: FrameType | None) -> None:  # noqa: D401
    _LOG.error("ghidra analysis timed‑out – exiting (sig=%d)", signum)
    sys.exit(2)


def _run_in_subprocess(fn, args: Tuple, timeout: int):  # noqa: ANN001, D401
    ctx = mp.get_context("spawn")
    q: mp.Queue = ctx.Queue()

    def _target(queue: mp.Queue, fun, fun_args):  # noqa: ANN001
        signal = __import__("signal")
        signal.signal(signal.SIGTERM, _sigterm_handler)
        signal.signal(signal.SIGALRM, _sigterm_handler)
        signal.alarm(timeout)
        try:
            res = fun(*fun_args)
            queue.put((True, res))
        except Exception as exc:  # pylint: disable=broad-except
            queue.put((False, str(exc)))
        finally:
            signal.alarm(0)

    p = ctx.Process(target=_target, args=(q, fn, args))
    p.start()
    p.join(timeout + 3)

    if not q.empty():
        ok, payload = q.get_nowait()
        if ok:
            return payload
        raise RuntimeError(payload)
    p.terminate()
    raise TimeoutError("ghidra analysis exceeded %d s" % timeout)


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Core façade                                                  ║
# ╚═══════════════════════════════════════════════════════════════╝

class GhidraBridge:  # noqa: D101 – full docstring above

    SYSCALL_MNEM = {"syscall", "svc", "int"}

    def __init__(self,
                 binary: Path | str,
                 *,
                 bridge_host: str = "127.0.0.1",
                 bridge_port: int = 18001,
                 analysis_timeout: int = 600,
                 open_timeout: int = 15):
        self.binary = Path(binary)
        if not self.binary.is_file():
            raise FileNotFoundError(self.binary)
        self.bridge_host = bridge_host
        self.bridge_port = bridge_port
        self.analysis_timeout = analysis_timeout
        self.open_timeout = open_timeout

    # ════════════════════════════════════════════════════════════
    #  Public façade – same as other backends
    # ════════════════════════════════════════════════════════════
    def build_ast(self) -> Dict[str, Any]:
        return _run_in_subprocess(_ast_worker,
                                  (self.binary.as_posix(), self._bridge_info()),
                                  self.analysis_timeout)

    def build_cfg(self) -> Dict[str, Any]:
        return _run_in_subprocess(_cfg_worker,
                                  (self.binary.as_posix(), self._bridge_info()),
                                  self.analysis_timeout)

    def build_fcg(self) -> Dict[str, Any]:
        return _run_in_subprocess(_fcg_worker,
                                  (self.binary.as_posix(), self._bridge_info()),
                                  self.analysis_timeout)

    def extract_syscalls(self) -> List[Dict[str, Any]]:
        return _run_in_subprocess(_syscall_worker,
                                  (self.binary.as_posix(), self._bridge_info()),
                                  self.analysis_timeout)

    # ------------------------------------------------------------------
    def _bridge_info(self) -> Tuple[str, int, int]:
        return (self.bridge_host, self.bridge_port, self.open_timeout)


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Worker implementations – run inside isolated process         ║
# ╚═══════════════════════════════════════════════════════════════╝

# ------------------------------------------------------------------
# Helper – connect to bridge & import useful GHIDRA classes
# ------------------------------------------------------------------

def _connect_bridge(host: str, port: int, timeout: int):  # noqa: ANN001
    start = time.time()
    while True:
        try:
            br = ghidra_bridge.GhidraBridge(namespace=None, connect_to=(host, port))
            return br
        except (socket.error, ConnectionRefusedError):
            if time.time() - start > timeout:
                raise RuntimeError("Cannot connect to ghidra_bridge on %s:%d" % (host, port))
            time.sleep(1)


# ------------------------------------------------------------------
#  [AST] worker – linear listing from instruction iterator
# ------------------------------------------------------------------

def _ast_worker(path: str, bridge_info):  # noqa: ANN001
    host, port, to = bridge_info
    br = _connect_bridge(host, port, to)
    gh = br.remote
    prog = gh.import_auto(path)
    gh.analyze_all(prog)  # ensure basic analysis done

    listing = prog.getListing()
    inst_iter = listing.getInstructions(True)

    nodes: List[Dict[str, Any]] = []
    parent: int | None = None
    idx = 0
    while inst_iter.hasNext():
        ins = inst_iter.next()
        mnemonic = ins.getMnemonicString()
        ops = [str(op) for op in ins.getOpObjects()] if ins.getNumOperands() else []
        tokens = [mnemonic] + ops
        nodes.append({
            "id": idx,
            "type": "inst",
            "tokens": tokens,
            "parent": parent,
        })
        parent = idx
        idx += 1
    br.disconnect()
    return {"nodes": nodes, "entry": 0 if nodes else None}


# ------------------------------------------------------------------
#  [CFG] worker – GHIDRA basic blocks graph via Function Graph
# ------------------------------------------------------------------

def _cfg_worker(path: str, bridge_info):  # noqa: ANN001
    host, port, to = bridge_info
    br = _connect_bridge(host, port, to)
    gh = br.remote
    prog = gh.import_auto(path)
    gh.analyze_all(prog)

    fg_service = gh.getFunctionGraphService()
    cfg_nodes: List[Dict[str, Any]] = []
    cfg_edges: List[Dict[str, Any]] = []
    node_idx = 0
    addr2id: Dict[int, int] = {}

    for fn in prog.getFunctionManager().getFunctions(True):
        graph = fg_service.getFunctionGraph(fn)
        for bb in graph.iterator():
            addr = int(bb.getMinAddress().getOffset())
            addr2id[addr] = node_idx
            cfg_nodes.append({"id": node_idx, "addr": hex(addr), "size": bb.getNumInstructions()})
            node_idx += 1
        for edge in graph.getEdges():
            src = int(edge.getSource().getMinAddress().getOffset())
            dst = int(edge.getDestination().getMinAddress().getOffset())
            if src in addr2id and dst in addr2id:
                cfg_edges.append({"src": addr2id[src], "dst": addr2id[dst], "type": "flow"})
    br.disconnect()
    return {"nodes": cfg_nodes, "edges": cfg_edges, "entry": 0}


# ------------------------------------------------------------------
#  [FCG] worker – getExternalReferences + calls
# ------------------------------------------------------------------

def _fcg_worker(path: str, bridge_info):  # noqa: ANN001
    host, port, to = bridge_info
    br = _connect_bridge(host, port, to)
    gh = br.remote
    prog = gh.import_auto(path)
    gh.analyze_all(prog)

    functions = []
    calls = []
    addr2id: Dict[int, int] = {}
    fmgr = prog.getFunctionManager()
    for idx, fn in enumerate(fmgr.getFunctions(True)):
        addr2id[int(fn.getEntryPoint().getOffset())] = idx
        functions.append({
            "id": idx,
            "name": fn.getName(),
            "addr": hex(int(fn.getEntryPoint().getOffset())),
            "external": fn.isExternal(),
        })
    # iterate again for call references
    for fn in fmgr.getFunctions(True):
        src_id = addr2id[int(fn.getEntryPoint().getOffset())]
        for ref in fn.getReferenceManager().getReferencesFrom(fn.getEntryPoint()):
            if ref.getReferenceType().isCall():
                dst = ref.getToAddress()
                if dst is None:
                    continue
                daddr = int(dst.getOffset())
                if daddr not in addr2id:
                    # auto‑add callee stub
                    addr2id[daddr] = len(functions)
                    functions.append({
                        "id": len(functions),
                        "name": f"sub_{daddr:x}",
                        "addr": hex(daddr),
                        "external": False,
                    })
                calls.append({"src": src_id, "dst": addr2id[daddr], "type": "direct"})
    br.disconnect()
    return {"functions": functions, "calls": calls, "entry": 0}


# ------------------------------------------------------------------
#  [Syscall] worker – scan instructions for syscall‑like mnemonics
# ------------------------------------------------------------------

def _syscall_worker(path: str, bridge_info):  # noqa: ANN001
    host, port, to = bridge_info
    br = _connect_bridge(host, port, to)
    gh = br.remote
    prog = gh.import_auto(path)
    gh.analyze_all(prog)

    listing = prog.getListing()
    inst_iter = listing.getInstructions(True)
    syscalls: List[Dict[str, Any]] = []
    while inst_iter.hasNext():
        ins = inst_iter.next()
        mnem = ins.getMnemonicString().lower()
        if mnem in GhidraBridge.SYSCALL_MNEM:
            syscalls.append({
                "name": mnem,
                "addr": hex(int(ins.getAddress().getOffset())),
                "args": [],
            })
    br.disconnect()
    return syscalls


__all__ = ["GhidraBridge"]
