"""
robust-malware-graph – Radare2Bridge backend
────────────────────────────────────────────
A *middle‑weight* backend that wraps **radare2** (via **r2pipe**) to offer
AST / CFG / FCG / SysCall extraction when Angr is too heavy and Capstone is
not enough.  It relies on `aaa` (full auto‑analysis) and JSON commands so the
result is deterministic and easy to parse.

Requirements
~~~~~~~~~~~~
* radare2 >= 5.8 (built with json‑libs)
* r2pipe (Python) >= 1.6

Design choices
~~~~~~~~~~~~~~
1. **Fork‑with‑Timeout** – any r2 analysis runs in a separate process with a
   hard timeout so stuck binaries don’t block the pipeline.
2. **Schema‑ready output** – methods return dicts/lists that match validators
   in `src.extract.validators.schema` just like other backends.
3. **Best‑effort heuristics** – we prefer *speed* over full accuracy (e.g.,
   indirect calls are skipped; CFG edges are taken from `agj` basic blocks).

Example
~~~~~~~
>>> from pathlib import Path
>>> from src.extract.backends.radare2_bridge import Radare2Bridge
>>> r2b = Radare2Bridge(Path("/bin/echo"))
>>> meta_cfg = r2b.build_cfg()
>>> print(len(meta_cfg["nodes"]), "basic blocks found")
"""

from __future__ import annotations

import json
import logging
import multiprocessing as mp
import signal
import sys
import warnings
from pathlib import Path
from types import FrameType
from typing import Any, Dict, List, Tuple

try:
    import r2pipe  # type: ignore – external
except ModuleNotFoundError as exc:  # pragma: no cover
    raise ImportError("r2pipe is required for Radare2Bridge backend") from exc

# ────────────────────────────────────────────────────────────────
# Logger helper (inline fallback)
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
# ║  Timeout wrapper helpers                                      ║
# ╚═══════════════════════════════════════════════════════════════╝

def _sigterm_handler(signum: int, frame: FrameType | None) -> None:  # noqa: D401
    _LOG.error("radare2 analysis timed‑out – exiting (sig=%d)", signum)
    sys.exit(2)


def _run_in_subprocess(fn, args: Tuple, timeout: int):  # noqa: ANN001, D401
    ctx = mp.get_context("spawn")
    q: mp.Queue = ctx.Queue()

    def _target(queue: mp.Queue, fun, fun_args):  # noqa: ANN001
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
    p.join(timeout + 2)

    if not q.empty():
        ok, payload = q.get_nowait()
        if ok:
            return payload
        raise RuntimeError(payload)

    p.terminate()
    raise TimeoutError("analysis exceeded %d s" % timeout)


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Core class façade                                            ║
# ╚═══════════════════════════════════════════════════════════════╝

class Radare2Bridge:  # noqa: D101 – see module docstring

    MAX_INSNS = 1_000_000

    def __init__(self,
                 binary: Path | str,
                 *,
                 analysis_timeout: int = 300,
                 r2_flags: Tuple[str, ...] = ("-2",)):  # -2: quiet, skip initrc
        self.binary = Path(binary)
        if not self.binary.is_file():
            raise FileNotFoundError(self.binary)
        self.analysis_timeout = analysis_timeout
        self.r2_flags = r2_flags
        _LOG.debug("Radare2Bridge init – %s (timeout=%ds)", self.binary.name, analysis_timeout)

    # ════════════════════════════════════════════════════════════
    #  Public methods
    # ════════════════════════════════════════════════════════════
    def build_ast(self) -> Dict[str, Any]:
        """Linear disassembly tokens – AST‑compatible."""
        return _run_in_subprocess(_ast_worker,
                                  (self.binary.as_posix(), self.r2_flags),
                                  self.analysis_timeout)

    def build_cfg(self) -> Dict[str, Any]:
        return _run_in_subprocess(_cfg_worker,
                                  (self.binary.as_posix(), self.r2_flags),
                                  self.analysis_timeout)

    def build_fcg(self) -> Dict[str, Any]:
        return _run_in_subprocess(_fcg_worker,
                                  (self.binary.as_posix(), self.r2_flags),
                                  self.analysis_timeout)

    def extract_syscalls(self) -> List[Dict[str, Any]]:
        return _run_in_subprocess(_syscall_worker,
                                  (self.binary.as_posix(), self.r2_flags),
                                  self.analysis_timeout)


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Worker implementations (run in isolated process)             ║
# ╚═══════════════════════════════════════════════════════════════╝

# ------------------------------------------------------------------
#  Helper – open r2 and run auto‑analysis
# ------------------------------------------------------------------

def _open_r2(path: str, flags: Tuple[str, ...]):  # noqa: ANN001
    warnings.filterwarnings("ignore", category=RuntimeWarning)  # noisy ctypes
    r2 = r2pipe.open(path, flags=list(flags))
    r2.cmd("aaa")  # full analysis (functions, xrefs, graph)
    return r2

# ------------------------------------------------------------------
#  [1] AST worker
# ------------------------------------------------------------------

def _ast_worker(path: str, flags: Tuple[str, ...]):  # noqa: ANN001
    r2 = _open_r2(path, flags)
    insns = r2.cmdj(f"pdj {Radare2Bridge.MAX_INSNS}") or []
    r2.quit()

    nodes: List[Dict[str, Any]] = []
    parent: int | None = None
    for idx, ins in enumerate(insns):
        opcode = ins.get("opcode", "")
        tokens = opcode.replace(",", " ").split()
        nodes.append({
            "id": idx,
            "type": "inst",
            "tokens": tokens,
            "parent": parent,
        })
        parent = idx
    return {"nodes": nodes, "entry": 0 if nodes else None}


# ------------------------------------------------------------------
#  [2] CFG worker – uses `agj` basic block graph
# ------------------------------------------------------------------

def _cfg_worker(path: str, flags: Tuple[str, ...]):  # noqa: ANN001
    r2 = _open_r2(path, flags)
    blocks = r2.cmdj("agj") or []
    r2.quit()

    nlist: List[Dict[str, Any]] = []
    elist: List[Dict[str, Any]] = []
    addr2id: Dict[int, int] = {}
    for idx, blk in enumerate(blocks):
        addr2id[blk["addr"]] = idx
        nlist.append({
            "id": idx,
            "addr": hex(blk["addr"]),
            "size": blk.get("size", 0),
        })

    for idx, blk in enumerate(blocks):
        for edge_key, etype in (("jump", "cond"), ("fail", "seq")):
            tgt = blk.get(edge_key)
            if tgt and tgt in addr2id:
                elist.append({"src": idx, "dst": addr2id[tgt], "type": etype})

    return {"nodes": nlist, "edges": elist, "entry": 0}


# ------------------------------------------------------------------
#  [3] FCG worker – based on `aflj` + xrefs
# ------------------------------------------------------------------

def _fcg_worker(path: str, flags: Tuple[str, ...]):  # noqa: ANN001
    r2 = _open_r2(path, flags)
    funcs = r2.cmdj("aflj") or []

    functions: List[Dict[str, Any]] = []
    addr2id: Dict[int, int] = {}
    for idx, f in enumerate(funcs):
        addr2id[f["offset"]] = idx
        functions.append({
            "id": idx,
            "name": f.get("name", f"sub_{f['offset']:x}"),
            "addr": hex(f["offset"]),
            "external": bool(f.get("isplt", False) or f.get("islib", False)),
        })

    calls: List[Dict[str, Any]] = []
    for f in funcs:
        fid = addr2id[f["offset"]]
        r2.cmd(f"s {f['offset']}")
        cro = r2.cmdj("agCj") or []  # callgraph edges from current fn
        for e in cro:
            dst = e.get("addr") or e.get("to")
            if dst is None:
                continue
            if dst not in addr2id:
                addr2id[dst] = len(functions)
                functions.append({
                    "id": len(functions),
                    "name": f"sub_{dst:x}",
                    "addr": hex(dst),
                    "external": False,
                })
            calls.append({
                "src": fid,
                "dst": addr2id[dst],
                "type": "direct",
            })
    r2.quit()
    entry = addr2id.get(funcs[0]["offset"], 0) if funcs else 0
    return {"functions": functions, "calls": calls, "entry": entry}


# ------------------------------------------------------------------
#  [4] Syscall worker – scan instruction mnemonics
# ------------------------------------------------------------------

def _syscall_worker(path: str, flags: Tuple[str, ...]):  # noqa: ANN001
    r2 = _open_r2(path, flags)
    insns = r2.cmdj(f"pdj {Radare2Bridge.MAX_INSNS}") or []
    r2.quit()

    syscalls: List[Dict[str, Any]] = []
    for ins in insns:
        mnem = ins.get("mnemonic") or ins.get("type", "").lower()
        opcode = ins.get("opcode", "").lower()
        if any(k in opcode for k in ("syscall", "svc", "int")) or mnem in {"swi", "syscall"}:
            syscalls.append({
                "name": opcode.split()[0] if opcode else mnem,
                "addr": hex(ins.get("offset", 0)),
                "args": [],
            })
    return syscalls


__all__ = [
    "Radare2Bridge",
]
