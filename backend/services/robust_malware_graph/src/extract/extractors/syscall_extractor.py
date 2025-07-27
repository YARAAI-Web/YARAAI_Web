from __future__ import annotations

"""SysCallExtractor
===================
Static recovery of *system‑call* usage from PE/ELF binaries.

*Updated to use the new view‑identifier constants (`VIEW_SYSCALL`).*
"""

from pathlib import Path
import json
import hashlib
import logging
import multiprocessing.pool as mpool
from typing import Any, Dict, List, Set

try:
    import angr  # heavy import; only used when extract() is called
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    angr = None  # type: ignore

from ..constants import VIEW_SYSCALL  # <‑‑ NEW constant import
from ..base import ExtractorBase  # shared interface
from src.common.utils import ensure_dir

__all__ = ["SysCallExtractor"]


class SysCallExtractor(ExtractorBase):
    """Recover system‑call usage and dump to ``*.syscalls.json``."""

    VIEW: str = VIEW_SYSCALL  # <‑‑ registry‑friendly identifier
    name: str = "syscall"    # kept for backward‑compat / logging
    output_suffix: str = ".syscalls.json"
    default_timeout: int = 60  # seconds

    def _output_path(self, binary_path: Path) -> Path:
        sha256 = hashlib.sha256(binary_path.read_bytes()).hexdigest()
        return self.cache_dir / f"{sha256}{self.output_suffix}"

    # ---------------------------------------------------------------------
    # Core worker (runs inside the thread‑pool so we can enforce a timeout)
    # ---------------------------------------------------------------------
    @staticmethod
    def _recover_worker(binary_path: str) -> Dict[str, Any]:
        if angr is None:  # pragma: no cover - import guard
            raise ImportError("angr is required for SysCallExtractor")
        proj = angr.Project(binary_path, auto_load_libs=False)
        arch = proj.arch.name
        os_hint = proj.loader.main_object.os

        cfg = proj.analyses.CFGFast(normalize=True)

        global_set: Set[str] = set()
        functions: Dict[str, Dict[str, Any]] = {}

        for addr, func in cfg.kb.functions.items():
            hist: Dict[str, int] = {}
            for block in func.blocks:
                for insn in block.capstone.insns:
                    if insn.mnemonic.startswith("sys"):  # e.g., "syscall"
                        sc_name = "syscall"  # x86‑64 generic
                    elif getattr(proj.arch, "syscall_instructions", None) and insn.insn.id in proj.arch.syscall_instructions:
                        sc_name = "syscall"
                    else:
                        continue

                    hist[sc_name] = hist.get(sc_name, 0) + 1
                    global_set.add(sc_name)

            if hist:
                functions[hex(addr)] = {
                    "name": func.name,
                    "syscalls": hist,
                }

        return {
            "arch": arch,
            "os": os_hint,
            "functions": functions,
            "global": {"unique_syscalls": sorted(global_set)},
        }

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def extract(self, binary_path: str | Path, *, force: bool = False) -> Path:
        """Run extraction and return path to the JSON artefact."""
        binary_path = Path(binary_path)
        out_path = self._output_path(binary_path)

        if out_path.exists() and not force:
            return out_path

        ensure_dir(out_path.parent)

        sha256 = hashlib.sha256(binary_path.read_bytes()).hexdigest()
        try:
            with mpool.ThreadPool(1) as pool:
                async_res = pool.apply_async(self._recover_worker, (str(binary_path),))
                data = async_res.get(self.default_timeout)
        except TimeoutError:
            logging.warning("[SysCallExtractor] Timeout on %s", binary_path)
            data = {"error": "timeout"}

        data.update({
            "binary_sha256": sha256,
            "backend": "angr",
            "view": self.VIEW,  # use constant‑based id
        })

        out_path.write_text(json.dumps(data, indent=2))
        return out_path

    def run(self, sample_path: Path) -> Dict[str, Any]:
        json_path = self.extract(sample_path)
        return json.loads(Path(json_path).read_text())
