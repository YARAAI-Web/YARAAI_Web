# src/models/gnn/__init__.py
"""
GNN package initializer
=======================

This top‑level ``gnn`` package exposes the most frequently used classes
(encoders, wrappers, heads registry) and **auto‑imports** its sub‑modules so
that their side‑effect registrations (e.g. ``heads.register_head``) are in
place immediately after a single
``import src.models.gnn as gnn``.

Highlights
----------
* Re‑exports
  • ``RGCNEncoder`` (graph backbone)
  • ``RESGCLClassifier`` (robust classifier wrapper)
  • ``heads`` registry helpers (``get_head``, ``available_heads``)
* Automatically scans ``layers`` & ``heads`` sub‑packages so users don’t
  have to import each file manually.
* Keeps the public namespace clean while still allowing direct sub‑package
  access via ``src.models.gnn.layers`` or ``src.models.gnn.heads``.
"""

from __future__ import annotations

import importlib
import pkgutil
from types import ModuleType
from typing import TYPE_CHECKING, List

# ---------------------------------------------------------------------------
# Public re‑exports (defined *after* auto‑imports) ---------------------------
# ---------------------------------------------------------------------------

__all__: List[str] = []  # will be filled later

# ---------------------------------------------------------------------------
# Auto‑import all sub‑modules to register layers / heads via side‑effects ----
# ---------------------------------------------------------------------------

def _auto_import_submodules(pkg: ModuleType) -> None:
    """Recursively import all sub‑modules (excluding tests & private)."""
    for modinfo in pkgutil.walk_packages(pkg.__path__, prefix=f"{pkg.__name__}."):
        if modinfo.ispkg or modinfo.name.split(".")[-1].startswith("_"):
            # skip sub‑packages (handled recursively) and private modules
            continue
        importlib.import_module(modinfo.name)


# Import child packages so they exist under this namespace
importlib.import_module(__name__ + ".layers")  # noqa: E402
importlib.import_module(__name__ + ".heads")   # noqa: E402

# Auto‑import their children (files)
_auto_import_submodules(importlib.import_module(__name__ + ".layers"))
_auto_import_submodules(importlib.import_module(__name__ + ".heads"))

# ---------------------------------------------------------------------------
# Re‑export key symbols ------------------------------------------------------
# ---------------------------------------------------------------------------

from .encoder import RGCNEncoder  # noqa: E402, F401
from .res_wrapper import RESGCLClassifier  # noqa: E402, F401
from .heads import get_head, available_heads  # noqa: E402, F401

__all__ += [
    "RGCNEncoder",
    "RESGCLClassifier",
    "get_head",
    "available_heads",
]
