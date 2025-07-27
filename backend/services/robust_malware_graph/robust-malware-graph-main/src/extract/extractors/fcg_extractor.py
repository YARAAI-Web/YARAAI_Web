from __future__ import annotations

"""FCGExtractor
================

Function‑Call‑Graph (FCG) extractor for PE/ELF binaries.

*Updated to use the new view‑identifier constants.*
"""

from dataclasses import dataclass, field
import json
import hashlib
import logging
import multiprocessing as mp
import os
import tempfile
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional

import networkx as nx  # type: ignore

try:
    import angr  # type: ignore
except ImportError:  # pragma: no cover – lazy import for CPU‑only envs
    angr = None  # noqa: N818

# ---------------------------------------------------------------------------
#  View constant (registry uses this)
# ---------------------------------------------------------------------------

from ..constants import VIEW_FCG  # NEW – aligned with constants.py

# ---------------------------------------------------------------------------
#  Configuration dataclass
# ---------------------------------------------------------------------------


@dataclass(slots=True)
class FCGExtractConfig:
    """Configuration for :class:`FCGExtractor`."""

    timeout: int = 120               # seconds per binary
    backend: str = "angr"            # currently only angr is supported
    jobs: int = max(os.cpu_count() or 1, 1)
    cache_dir: Path = Path("~/.robust_malware_graph/cache/fcg").expanduser()
    force_rebuild: bool = False      # ignore cached artefacts


# ---------------------------------------------------------------------------
#  Abstract backend definition
# ---------------------------------------------------------------------------


class _AbstractFCGBackend(ABC):
    """Backend interface to recover FCG from a binary."""

    @abstractmethod
    def build_fcg(self, bin_path: Path, timeout: int) -> nx.DiGraph:  # noqa: D401
        """Return an *nx.DiGraph* where nodes are function addresses (int)."""

    @abstractmethod
    def arch(self, bin_path: Path) -> str:  # noqa: D401
        """Return architecture string (e.g., ``'x86_64'``)."""


# ---------------------------------------------------------------------------
#  angr backend implementation
# ---------------------------------------------------------------------------


class _AngrBackend(_AbstractFCGBackend):
    """angr‑based FCG recovery backend."""

    _lock: mp.Lock = mp.Lock()  # prevent concurrent project creation

    def build_fcg(self, bin_path: Path, timeout: int) -> nx.DiGraph:  # noqa: D401
        with self._lock:
            project = angr.Project(str(bin_path), auto_load_libs=False)  # type: ignore[arg-type]
        cfg = project.analyses.CFGFast(
            normalize=True,
            data_references=False,
            force_complete_scan=False,
            show_progressbar=False,
            resolve_indirect_jumps=True,
            timeout=timeout,  # type: ignore[arg-type]
        )
        g = nx.DiGraph()
        for f in cfg.kb.functions.values():
            g.add_node(f.addr, name=f.name, is_external=f.is_plt)
            for call_dst in f.block_addrs_set:  # crude scan for call sites
                node = cfg.model.get_any_node(call_dst)
                if node is None:
                    continue
                for succ in node.successors:
                    if succ.function_address is None:
                        continue
                    g.add_edge(f.addr, succ.function_address, kind="call")
        return g

    def arch(self, bin_path: Path) -> str:  # noqa: D401
        with self._lock:
            project = angr.Project(str(bin_path), auto_load_libs=False)  # type: ignore[arg-type]
        return project.arch.name  # type: ignore[return-value]


# ---------------------------------------------------------------------------
#  Helper functions
# ---------------------------------------------------------------------------

def _sha256(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            buf = f.read(chunk)
            if not buf:
                break
            h.update(buf)
    return h.hexdigest()


def _ensure_cache_dir(d: Path) -> None:
    d.mkdir(parents=True, exist_ok=True)


def _load_from_cache(out_path: Path) -> Optional[dict[str, Any]]:
    if out_path.exists():
        try:
            with out_path.open("r", encoding="utf-8") as fp:
                return json.load(fp)
        except Exception:
            out_path.unlink(missing_ok=True)
    return None


def _dump_json(data: dict[str, Any], out_path: Path) -> None:
    tmp = Path(tempfile.mkstemp(dir=out_path.parent, suffix=".tmp")[1])
    try:
        with tmp.open("w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False)
        tmp.replace(out_path)
    finally:
        tmp.unlink(missing_ok=True)


def _graph_to_json(g: nx.DiGraph, sha256: str, arch: str, backend: str) -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    for nid, attrs in g.nodes(data=True):
        nodes.append(
            {
                "addr": nid,
                "name": attrs.get("name"),
                "is_external": bool(attrs.get("is_external")),
                "size": attrs.get("size", 0),
            }
        )
    edges: list[dict[str, Any]] = []
    for src, dst, attrs in g.edges(data=True):
        edges.append({"src": src, "dst": dst, "kind": attrs.get("kind", "call")})
    return {
        "meta": {"sha256": sha256, "arch": arch, "backend": backend},
        "nodes": nodes,
        "edges": edges,
    }


# ---------------------------------------------------------------------------
#  Public extractor API
# ---------------------------------------------------------------------------


class FCGExtractor:  # pylint: disable=too-few-public-methods
    """High‑level wrapper exposing *extract* and *bulk* APIs."""

    # Registry hook — view identifier that ``view_registry`` looks for
    VIEW: str = VIEW_FCG  # NEW

    _backends: dict[str, _AbstractFCGBackend] = {"angr": _AngrBackend()}

    def __init__(self, config: FCGExtractConfig | None = None):
        self.cfg = config or FCGExtractConfig()
        if self.cfg.backend not in self._backends:
            raise ValueError(f"Unsupported backend: {self.cfg.backend}")
        _ensure_cache_dir(self.cfg.cache_dir)
        self.backend = self._backends[self.cfg.backend]
        self.log = logging.getLogger(self.__class__.__name__)

    # ------------------------------------------------------------------
    #  In-memory API used by the pipeline
    # ------------------------------------------------------------------

    def run(self, sample_path: Path) -> Dict[str, Any]:  # noqa: D401
        """Return JSON-compatible dict for the given binary."""
        json_path = self.extract(sample_path)
        return json.loads(Path(json_path).read_text())

    # ------------------------------------------------------------------
    #  Single‑binary API
    # ------------------------------------------------------------------

    def extract(self, bin_path: Path | str, *, out_path: Path | None = None) -> Path:
        """Recover FCG and return path to JSON artefact."""
        bin_path = Path(bin_path).expanduser().resolve()
        sha256 = _sha256(bin_path)
        out_path = out_path or self.cfg.cache_dir / f"{sha256}.fcg.json"

        if not self.cfg.force_rebuild:
            cached = _load_from_cache(out_path)
            if cached is not None:
                self.log.debug("Cache hit for %s -> %s", bin_path, out_path)
                return out_path

        self.log.info("Extracting FCG from %s", bin_path)
        start = time.perf_counter()
        g = self.backend.build_fcg(bin_path, timeout=self.cfg.timeout)
        elapsed = time.perf_counter() - start
        self.log.info(
            "Extraction finished in %.2fs with %d nodes / %d edges",
            elapsed,
            g.number_of_nodes(),
            g.number_of_edges(),
        )

        meta_json = _graph_to_json(
            g,
            sha256,
            self.backend.arch(bin_path),
            self.cfg.backend,
        )
        _dump_json(meta_json, out_path)
        return out_path

    # ------------------------------------------------------------------
    #  Bulk API
    # ------------------------------------------------------------------

    def bulk_extract(self, paths: List[Path | str]) -> List[Path]:
        paths = [Path(p).expanduser().resolve() for p in paths]
        with mp.Pool(processes=self.cfg.jobs) as pool:
            return pool.map(self.extract, paths)


# ---------------------------------------------------------------------------
#  CLI entry‑point
# ---------------------------------------------------------------------------

if __name__ == "__main__":  # pragma: no cover – simple smoke‑test wrapper
    import argparse

    parser = argparse.ArgumentParser(description="Function‑Call‑Graph extractor")
    parser.add_argument("binary", type=Path, nargs="+", help="Path to PE/ELF binary/binaries")
    parser.add_argument("-o", "--out", type=Path, default=None, help="Output JSON path (single binary mode)")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout in seconds per binary [default: 120]")
    parser.add_argument("--backend", type=str, default="angr", help="Backend engine [default: angr]")
    parser.add_argument(
        "--jobs", type=int, default=max(os.cpu_count() or 1, 1), help="Parallel jobs for bulk mode"
    )
    parser.add_argument("--force", action="store_true", help="Ignore cache and rebuild")

    args = parser.parse_args()
    cfg = FCGExtractConfig(timeout=args.timeout, backend=args.backend, jobs=args.jobs, force_rebuild=args.force)
    extractor = FCGExtractor(cfg)

    if len(args.binary) == 1:
        output = extractor.extract(args.binary[0], out_path=args.out)
        print(output)
    else:
        outputs = extractor.bulk_extract(args.binary)
        print("\n".join(str(p) for p in outputs))
