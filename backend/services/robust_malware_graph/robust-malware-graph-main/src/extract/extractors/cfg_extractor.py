from __future__ import annotations

"""CFGExtractor
================
Collects a binary’s Control‑Flow Graph (CFG) and serialises it into a compact
JSON file.  The extractor now depends on the new *view* constants introduced in
``src.extract.constants`` so that the registry can look up the correct view
identifier without legacy aliases.
"""

from dataclasses import dataclass, field
import json
import multiprocessing as mp
import shutil
import signal
from pathlib import Path
from typing import Any, Dict, Iterable, List, ClassVar

import networkx as nx

# NEW: canonical view identifier (supersedes DEFAULT_CFG_VIEW)
from ..constants import DEFAULT_VIEWS_DIR, VIEW_CFG  # noqa: E402  pylint: disable=wrong-import-position

try:
    import angr  # type: ignore
except ImportError:  # pragma: no cover – lazy import for CPU‑only envs
    angr = None  # pylint: disable=invalid-name

__all__ = ["CFGExtractor"]

# --------------------------------------------------------------------------- #
# Interface
# --------------------------------------------------------------------------- #

@dataclass(slots=True)
class CFGExtractor:  # pylint: disable=too-many-instance-attributes
    """Recover control‑flow graph (CFG) and serialise it to JSON."""

    # The registry inspects this attribute to match the extractor to the view
    VIEW: ClassVar[str] = VIEW_CFG  # <- **key change**

    out_dir: Path = DEFAULT_VIEWS_DIR / VIEW_CFG
    backend: str = "angr"
    jobs: int = 1
    timeout: int = 300  # seconds per binary
    cache: bool = True
    detail_level: str = "basic"  # reserved for future

    # internal fields (not part of __init__ signature)
    _pool: mp.pool.Pool | None = field(init=False, default=None, repr=False)

    def __post_init__(self) -> None:
        """Ensure ``out_dir`` defaults to the standard view cache."""
        object.__setattr__(self, "out_dir", self.out_dir or DEFAULT_VIEWS_DIR / self.VIEW)

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def run(self, sample_path: Path) -> Dict[str, Any]:
        """Extract CFG data for *sample_path* and return a Python dict."""
        json_path = self._extract_single(Path(sample_path))
        return json.loads(Path(json_path).read_text())

    def __call__(self, *binaries: Path | str) -> List[Path]:  # noqa: D401
        """Extract CFG(s) for one or more binaries.

        Parameters
        ----------
        *binaries:
          One or multiple paths to PE/ELF files.

        Returns
        -------
        list[Path]
          Paths to *JSON* files.
        """
        paths: List[Path] = [Path(b) for b in binaries]
        self.out_dir.mkdir(parents=True, exist_ok=True)

        if self.jobs <= 1 or len(paths) == 1:
            return [self._extract_single(p) for p in paths]

        # Multiprocess for I/O‑heavy tasks (angr initialisation is CPU‑light)
        with mp.Pool(processes=self.jobs, initializer=_init_worker) as pool:
            res = pool.map(self._extract_single, paths)
        return res

    # ------------------------------------------------------------------ #
    # Worker function (per binary)
    # ------------------------------------------------------------------ #

    def _extract_single(self, path: Path) -> Path:  # noqa: C901 – readability
        json_path = self.out_dir / f"{path.name}.cfg.json"

        if self.cache and json_path.exists() and json_path.stat().st_mtime > path.stat().st_mtime:
            return json_path  # up‑to‑date

        if self.backend == "angr":
            data = self._extract_angr(path)
        else:
            raise ValueError(f"Unsupported backend: {self.backend}")

        json_path.write_text(json.dumps(data, separators=(",", ":")))
        return json_path

    # ------------------------------------------------------------------ #
    # Backends
    # ------------------------------------------------------------------ #

    def _extract_angr(self, path: Path) -> Dict[str, Any]:  # noqa: D401
        if angr is None:
            raise RuntimeError("angr is not installed – `pip install angr`.")

        # Honour per‑binary timeout using *alarm* to avoid hangs inside angr
        def _timeout_handler(_signum: int, _frame: Any) -> None:  # noqa: ANN001
            raise TimeoutError(f"angr CFGFast timed‑out after {self.timeout}s")

        prev_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(self.timeout)
        try:
            proj = angr.Project(path.as_posix(), auto_load_libs=False)  # type: ignore[arg-type]
            cfg = proj.analyses.CFGFast(normalize=True, data_references=False)
        finally:
            signal.alarm(0)  # disable
            signal.signal(signal.SIGALRM, prev_handler)

        graph: nx.DiGraph = cfg.graph

        node_id_map: Dict[int, int] = {}
        nodes_json: List[Dict[str, Any]] = []
        for idx, n in enumerate(graph.nodes):
            node_id_map[n.addr] = idx
            nodes_json.append(
                {
                    "id": idx,
                    "addr": n.addr,
                    "function": n.function_address,  # will resolve later
                    "size": n.size,
                    "blocks": len(n.block_addrs),
                    "is_syscall_stub": n.is_syscall_stub,
                }
            )

        # Resolve function names lazily (avoid O(#nodes²) lookups)
        for node in nodes_json:
            try:
                func = cfg.kb.functions[node["function"]]
                node["function"] = func.name
            except KeyError:
                node["function"] = hex(node["function"])

        edges_json: List[Dict[str, Any]] = []
        for src, dst, data in graph.edges(data=True):
            edges_json.append(
                {
                    "src": node_id_map[src.addr],
                    "dst": node_id_map[dst.addr],
                    "type": data.get("jumpkind", "jmp"),
                }
            )

        return {
            "binary": str(path),
            "backend": self.backend,
            "arch": proj.arch.name,
            "nodes": nodes_json,
            "edges": edges_json,
        }

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #

    def clean(self) -> None:
        """Delete all cached CFG JSON files in :pyattr:`out_dir`."""
        if self.out_dir.exists():
            shutil.rmtree(self.out_dir)
            self.out_dir.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------------------------- #
# Multiprocessing helpers
# --------------------------------------------------------------------------- #

def _init_worker() -> None:  # pragma: no cover – worker bootstrap
    signal.signal(signal.SIGINT, signal.SIG_IGN)  # Let main handle ^C
