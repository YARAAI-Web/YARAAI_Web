"""
robust‑malware‑graph – AngrEngine backend
─────────────────────────────────────────
A thin wrapper around **angr** that standardises *one‑shot* extraction of
AST, CFG, FCG and SysCall information for the high‑level view extractors
(`ASTExtractor`, `CFGExtractor`, `FCGExtractor`, `SysCallExtractor`).

Design goals
~~~~~~~~~~~~
1. **Stateless** – every call is independent; no global caches shared
   between processes.  Long‑running pipelines spawn many workers, thus a
   light construction cost is preferred over coarse memoisation.
2. **Timeout‑safe** – heavy binaries (≫10 MB, packed, obfuscated) can hang
   data‑flow passes.  We therefore run each analysis in a *separate* child
   process so that the parent can terminate it on timeout.
3. **Schema‑aware** – helper methods return *Python dicts* that already
   conform to the JSON schema expected by downstream validators
   (`src.extract.validators.schema`).  No post‑processing required in
   individual Extractors.

Dependencies
~~~~~~~~~~~~
* angr >= 9.2.29
* capstone (through angr)
* archinfo (through angr)

Example
~~~~~~~
>>> from pathlib import Path
>>> from src.extract.backends.angr_engine import AngrEngine
>>> eng = AngrEngine(Path("/bin/ls"))
>>> cfg = eng.build_cfg()
>>> print(len(cfg["nodes"]), "basic blocks parsed")
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

import archinfo  # type: ignore – external
import angr  # type: ignore – external

# ────────────────────────────────────────────────────────────────
# Project‑level logger (fallback to stdlib if common.utils missing)
# ────────────────────────────────────────────────────────────────
try:
    from src.common.utils import get_logger  # local helper
except ModuleNotFoundError:  # standalone fallback
    def get_logger(name: str) -> logging.Logger:  # noqa: D401 (simple)
        logging.basicConfig(level=logging.INFO,
                            format="[%(levelname)s] %(name)s: %(message)s")
        return logging.getLogger(name)

_LOG = get_logger(__name__)


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Utility: run_with_timeout – isolated child process runner    ║
# ╚═══════════════════════════════════════════════════════════════╝

def _sigterm_handler(signum: int, frame: FrameType | None) -> None:  # noqa: D401
    """Immediate exit on SIGTERM/SIGALRM inside the worker."""
    _LOG.error("analysis timed‑out – killing angr worker (%d)", signum)
    sys.exit(2)


def _run_in_subprocess(fn, args: Tuple, timeout: int):  # noqa: ANN001, D401
    """Helper to execute *fn*(*args) in a forked process with timeout."""
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
    p.join(timeout + 2)  # grace period

    if not q.empty():
        ok, payload = q.get_nowait()
        if ok:
            return payload
        raise RuntimeError(payload)

    # queue empty → likely hung; terminate
    p.terminate()
    raise TimeoutError("analysis exceeded %d s" % timeout)


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Core Engine                                                  ║
# ╚═══════════════════════════════════════════════════════════════╝

class AngrEngine:  # noqa: D101 – docstring at top of file

    # ------------------------------------------------------------------
    def __init__(self,
                 binary: Path | str,
                 *,
                 auto_load_libs: bool = False,
                 arch: str | None = None,
                 load_options: Dict[str, Any] | None = None,
                 analysis_timeout: int = 300) -> None:
        self.binary = Path(binary)
        if not self.binary.is_file():
            raise FileNotFoundError(self.binary)

        self.analysis_timeout = analysis_timeout
        load_opts = load_options or {}
        load_opts.setdefault("auto_load_libs", auto_load_libs)
        if arch is not None:
            load_opts.setdefault("arch", archinfo.arch_from_id(arch))

        # Suppress noisy warnings (e.g., SimOS warnings on unusual binaries)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.project = angr.Project(self.binary.as_posix(), **load_opts)

        _LOG.debug("AngrEngine initialised – %s (arch=%s, libs=%s)",
                   self.binary.name, self.project.arch, auto_load_libs)

    # ════════════════════════════════════════════════════════════
    #  Public façade
    # ════════════════════════════════════════════════════════════
    def build_ast(self) -> Dict[str, Any]:
        """Extract a minimal *instruction‑level* AST tree.

        Schema (per `validators.schema.ASTSchema`)
        ----------------------------------------
        {
          "nodes": [
            {"id": 0, "type": "inst", "tokens": ["mov", "eax", "1"], "parent": null},
            ...
          ],
          "entry": <root‑id>
        }
        """
        return _run_in_subprocess(_ast_worker, (self.binary.as_posix(),), self.analysis_timeout)

    def build_cfg(self) -> Dict[str, Any]:
        """Return **CFGFast** basic‑block graph."""
        return _run_in_subprocess(_cfg_worker, (self.binary.as_posix(),), self.analysis_timeout)

    def build_fcg(self) -> Dict[str, Any]:
        """Return function‑call graph (FCG) with demangled names."""
        return _run_in_subprocess(_fcg_worker, (self.binary.as_posix(),), self.analysis_timeout)

    def extract_syscalls(self) -> List[Dict[str, Any]]:
        """Scan the binary for explicit `syscall` instructions and VEX events."""
        return _run_in_subprocess(_syscall_worker, (self.binary.as_posix(),), self.analysis_timeout)


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Worker impl – executed in separate process                   ║
# ╚═══════════════════════════════════════════════════════════════╝

def _load_project(path: str, **kwargs):  # noqa: ANN001
    return angr.Project(path, auto_load_libs=False, **kwargs)

# ------------------------------------------------------------------
# [1] AST worker (very lightweight – disassembly tokens only)
# ------------------------------------------------------------------

def _ast_worker(path: str):  # noqa: ANN001
    proj = _load_project(path)
    cfg = proj.analyses.CFGFast(normalize=True)

    nodes: List[Dict[str, Any]] = []
    node_id = 0
    id_map: Dict[Tuple[int, int], int] = {}  # (func_addr, ins_addr) → id

    for func in cfg.kb.functions.values():
        for block in func.blocks:
            for ins in block.capstone.insns:
                tok = [ins.mnemonic] + [op.strip() for op in ins.op_str.split(',')] if ins.op_str else [ins.mnemonic]
                nid = node_id
                id_map[(func.addr, ins.address)] = nid
                nodes.append({
                    "id": nid,
                    "type": "inst",
                    "tokens": tok,
                    "parent": None,  # filled later
                })
                node_id += 1

    # parent mapping (instruction sequence → linear parent)
    for (faddr, _), nid in id_map.items():
        func = cfg.kb.functions[faddr]
        insns = [i for b in func.blocks for i in b.capstone.insns]
        for idx, ins in enumerate(insns):
            if idx == 0:
                continue
            cur_id = id_map[(func.addr, ins.address)]
            prev_id = id_map[(func.addr, insns[idx - 1].address)]
            nodes[cur_id]["parent"] = prev_id

    entry_id = 0 if nodes else None
    return {"nodes": nodes, "entry": entry_id}


# ------------------------------------------------------------------
# [2] CFG worker (CFGFast → basic block graph)
# ------------------------------------------------------------------

def _cfg_worker(path: str):  # noqa: ANN001
    proj = _load_project(path)
    cfg = proj.analyses.CFGFast(normalize=True)

    nlist: List[Dict[str, Any]] = []
    elist: List[Dict[str, Any]] = []

    for node in cfg.graph.nodes:
        nlist.append({
            "id": node.addr,
            "addr": hex(node.addr),
            "size": node.size,
        })

    for src, dst, data in cfg.graph.edges(data=True):
        elist.append({
            "src": src.addr,
            "dst": dst.addr,
            "type": data.get("jumpkind", "unresolved"),
        })

    return {
        "nodes": nlist,
        "edges": elist,
        "entry": hex(proj.entry),
    }


# ------------------------------------------------------------------
# [3] FCG worker (function‑level call graph)
# ------------------------------------------------------------------

def _fcg_worker(path: str):  # noqa: ANN001
    proj = _load_project(path)
    cfg = proj.analyses.CFGFast(normalize=True)

    fnodes: List[Dict[str, Any]] = []
    calls: List[Dict[str, Any]] = []
    addr2id: Dict[int, int] = {}

    # collect functions
    for idx, func in enumerate(cfg.kb.functions.values()):
        addr2id[func.addr] = idx
        fnodes.append({
            "id": idx,
            "name": func.name,
            "addr": hex(func.addr),
            "external": func.is_plt or func.is_simprocedure or func.is_syscall,
        })

    # collect call edges
    for caller in cfg.kb.functions.values():
        for cs in caller.get_call_sites():
            dests = caller.get_call_target(cs)
            if dests is None:
                continue
            for dst_addr in dests:
                call_type = "lib" if cfg.kb.functions[dst_addr].is_plt else "direct"
                calls.append({
                    "src": addr2id[caller.addr],
                    "dst": addr2id.get(dst_addr, -1),
                    "type": call_type,
                })

    return {
        "functions": fnodes,
        "calls": calls,
        "entry": addr2id.get(cfg.kb.functions.function(addr=proj.entry).addr, 0) if proj.entry else 0,
    }


# ------------------------------------------------------------------
# [4] Syscall extraction worker
# ------------------------------------------------------------------

def _syscall_worker(path: str):  # noqa: ANN001
    proj = _load_project(path)
    cfg = proj.analyses.CFGFast(normalize=True)

    syscalls: List[Dict[str, Any]] = []

    for func in cfg.kb.functions.values():
        for block in func.blocks:
            for ins in block.capstone.insns:
                if ins.mnemonic.lower() in ("syscall", "svc", "int"):
                    syscalls.append({
                        "name": ins.mnemonic.lower(),
                        "addr": hex(ins.address),
                        "args": [],  # arg recovery skipped for speed
                    })
    return syscalls


__all__ = [
    "AngrEngine",
]
# 파일 맨 아래 추가 ────────────────────────────────────────────────
from types import SimpleNamespace

def extract_ast(                       # noqa: D401 – 백엔드 공개 API
    sample_path: str | Path,
    *,
    timeout: int = 120,
    normalize_unicode: bool = True,    # 현재는 no-op(호환용)
    keep_tmp: bool = False,            # 현재는 no-op(호환용)
):
    """
    One-shot AST 추출 래퍼.  ASTExtractor 가 기대하는
    (functions → nodes) 형태로 변환해 돌려준다.
    """
    eng = AngrEngine(sample_path, analysis_timeout=timeout)
    ast_dict = eng.build_ast()
    return [
        SimpleNamespace(
            name="global",
            nodes=[
                SimpleNamespace(
                    type=n["type"],
                    tokens=n["tokens"],
                    parent=n["parent"],
                )
                for n in ast_dict["nodes"]
            ],
        )
    ]

__all__.append("extract_ast")
