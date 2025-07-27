from __future__ import annotations
"""ASTExtractor
================

Parse the **Abstract Syntax Tree (AST)** of each function contained in a PE/ELF
binary and serialise it to a compact JSON file that can later be converted to a
heterogeneous graph.  The extractor wraps a low‑level backend (default: `angr`)
so that switching disassembly engines is transparent to callers.  It follows
the common interface defined in :pyclass:`src.extract.base.ExtractorBase`.

Overview
--------
```
┌──────────────┐    execute()    ┌──────────────────┐
│  ASTExtractor│ ──────────────▶│  angr_engine.AST │  (IDA, r2, …)
└──────────────┘                 └──────────────────┘
         │ run() dict                     │ list[FunctionAST]
         ▼                                ▼
      save() JSON  ◀──────────── format_ast() ──────────────┐
                           ┌───────────────┐               │
                           │ utils.sha256_file│  derive SHA  │
                           └───────────────┘               │
```

Key design choices
~~~~~~~~~~~~~~~~~~
* **Schema‑first** – each node is normalised to the *minimal* set of
  attributes that downstream loaders actually use; this avoids huge JSONs.
* **Streaming I/O** – large ASTs (100k+ nodes) are dumped with the
  built‑in ``json`` module using chunked writing to keep memory usage low.
* **Graceful degradation** – if the preferred backend times out or raises, we
  fall back to the simpler Capstone‑only extractor that yields a flatter AST
  (statement‑level instead of expression‑level).

Example output (pretty‑printed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```json
{
  "metadata": {
    "sha256": "deadbeef…",
    "backend": "angr",
    "num_nodes": 1284,
    "build_time": "2025-06-20T04:20:11+09:00"
  },
  "nodes": [
    {"id": 0, "type": "Function", "tokens": ["main"], "parent": null},
    {"id": 1, "type": "Return",   "tokens": ["0"],     "parent": 0  }
  ]
}
```
"""

from datetime import datetime, timezone
import json
import logging
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional
from types import SimpleNamespace

from .. import utils as u  # temp dir, hash_file, tqdm, etc.
from ..base import ExtractorBase
from ..constants import VIEW_AST  # e.g. "ast"
from ..backends import angr_engine, capstone_disasm  # type: ignore

logger = logging.getLogger(__name__)

__all__ = ["ASTExtractor"]


class ASTExtractor(ExtractorBase):
    """Parse a binary and serialise its function‑level ASTs.

    Parameters
    ----------
    backend : str, default "angr"
        Name of the backend to use ("angr" | "capstone").
    timeout : int, default 120
        Per‑sample hard timeout in seconds.
    normalize_unicode : bool, default True
        Whether to NFC‑normalise extracted tokens (avoids str mismatches).
    keep_tmp : bool, default False
        Retain temporary disassembly artifacts on disk (for debugging).
    """

    VIEW = VIEW_AST  #: directory under ``data/views``

    # ---------------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------------

    def __init__(
        self,
        *,
        backend: str = "angr",
        timeout: int = 120,
        normalize_unicode: bool = True,
        keep_tmp: bool = False,
    ) -> None:
        super().__init__()
        self.timeout = timeout
        self.backend_name = backend.lower()
        self.normalize_unicode = normalize_unicode
        self.keep_tmp = keep_tmp

        if self.backend_name == "angr":
            self.backend = angr_engine
        elif self.backend_name == "capstone":
            self.backend = capstone_disasm
        else:
            raise ValueError(f"Unsupported backend: {backend}")

    # ------------------------------------------------------------------
    # Private helper: build AST via engine class (when extract_ast missing)
    # ------------------------------------------------------------------
    def _extract_via_engine(self, sample_path: Path):  # noqa: D401
        """Fallback path: instantiates the engine class directly and wraps the
        raw ``build_ast`` dict into the FunctionAST list expected by the
        flattener below.
        """
        if self.backend_name == "angr":
            eng = angr_engine.AngrEngine(sample_path, analysis_timeout=self.timeout)
        else:
            eng = capstone_disasm.CapstoneDisasm(sample_path)

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
                    for n in ast_dict.get("nodes", [])
                ],
            )
        ]

    # ------------------------------------------------------------------
    # Core API
    # ------------------------------------------------------------------

    def run(self, sample_path: Path) -> Dict[str, Any]:  # noqa: D401, override
        """Run the backend and return a *Python* dict that follows the schema."""
        logger.info("[AST] Parsing %s using backend=%s", sample_path, self.backend_name)
        sha256 = u.sha256_file(sample_path)

        # ------------------------------------------------------------------
        # 1) Try preferred backend → extract_ast()
        # ------------------------------------------------------------------
        try:
            if hasattr(self.backend, "extract_ast"):
                func_asts = self.backend.extract_ast(  # type: ignore[attr-defined]
                    sample_path,
                    timeout=self.timeout,
                    normalize_unicode=self.normalize_unicode,
                    keep_tmp=self.keep_tmp,
                )
            else:
                raise AttributeError("backend lacks extract_ast() helper")
            backend_used = self.backend_name

        # ------------------------------------------------------------------
        # 2) If backend is missing the helper entirely
        # ------------------------------------------------------------------
        except AttributeError:
            logger.debug("%s has no extract_ast() – falling back to engine wrapper", self.backend_name)
            func_asts = self._extract_via_engine(sample_path)
            backend_used = self.backend_name

        # ------------------------------------------------------------------
        # 3) Runtime failure → switch to capstone as best‑effort
        # ------------------------------------------------------------------
        except Exception as exc:  # pylint: disable=broad-except
            logger.warning("Backend %s failed for %s → %s", self.backend_name, sample_path, exc)
            logger.debug(traceback.format_exc())
            if self.backend_name != "capstone":
                logger.info("Falling back to capstone backend …")
                func_asts = capstone_disasm.extract_ast(  # type: ignore[attr-defined]
                    sample_path,
                    timeout=self.timeout,
                    normalize_unicode=self.normalize_unicode,
                    keep_tmp=self.keep_tmp,
                )
                backend_used = "capstone"
            else:
                raise

        # ------------------------------------------------------------------
        # Flatten FunctionAST → node list with stable numeric ids
        # ------------------------------------------------------------------
        nodes: List[Dict[str, Any]] = []
        nid = 0
        for f in func_asts:
            fid = nid
            nodes.append({
                "id": fid,
                "type": "Function",
                "tokens": [f.name],
                "parent": None,
            })
            nid += 1
            for n in f.nodes:
                nodes.append({
                    "id": nid,
                    "type": n.type,
                    "tokens": n.tokens,
                    "parent": fid if n.parent is None else n.parent + fid + 1,
                })
                nid += 1

        result: Dict[str, Any] = {
            "metadata": {
                "sha256": sha256,
                "backend": backend_used,
                "num_nodes": len(nodes),
                "build_time": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
            },
            "nodes": nodes,
        }
        return result

    # ------------------------------------------------------------------
    # Adapter for ExtractorBase
    # ------------------------------------------------------------------

    def extract(self, sample_path: Path) -> Dict[str, Any]:  # type: ignore[override]
        """Alias for :meth:`run` to satisfy :class:`ExtractorBase`."""
        return self.run(sample_path)

    # ------------------------------------------------------------------
    # I/O helpers
    # ------------------------------------------------------------------
    def save(self, result: Dict[str, Any], out_path: Path) -> None:
        """Write *result* to ``out_path`` in UTF‑8 JSON format."""
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as fp:
            json.dump(result, fp, ensure_ascii=False, separators=(",", ":"))
        logger.debug("Saved AST JSON → %s (%d nodes)", out_path, result["metadata"]["num_nodes"])

    def load(self, out_path: Path) -> Dict[str, Any]:  # type: ignore[override]
        """Read JSON and return a Python dict."""
        with out_path.open("r", encoding="utf-8") as fp:
            return json.load(fp)

    # ------------------------------------------------------------------
    # Convenience wrapper for CLI/pipelines
    # ------------------------------------------------------------------
    def __call__(self, sample_path: Path, *, out_dir: Optional[Path] = None) -> Path:  # type: ignore[override]
        """Run + save → return output path."""
        if out_dir is None:
            out_dir = Path("data") / "views" / self.VIEW
        sha256 = u.sha256_file(sample_path)
        out_path = out_dir / f"{sha256}.json"
        if out_path.exists():
            logger.info("[AST] Cache hit – %s", out_path)
            return out_path

        result = self.run(sample_path)
        self.save(result, out_path)
        return out_path


# -------------------------------------------------------------------------
# View registry integration (used by src.extract.extractors.view_registry)
# -------------------------------------------------------------------------

try:
    # Lazy import to avoid circular deps when registry imports this module
    from .view_registry import register_view  # noqa: E402

    register_view("ast", ASTExtractor, force=True)  # noqa: E402
except ImportError:
    # ASTExtractor can still be used without the global registry
    pass
