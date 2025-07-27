# SPDX-License-Identifier: MIT
"""src.models package
============================================
Top‑level *model registry* and convenience exports.

This root package glues together sub‑modules such as
``src.models.gnn``, ``src.models.contrast``, ``src.models.distill`` and
``src.models.llm_embed`` – exposing a *single* registry interface so that
experiment scripts can instantiate any component by a simple string key.

Example
-------
>>> from src.models import get_model
>>> Encoder = get_model("rgcn_encoder")
>>> enc = Encoder(in_dim=128, hid_dim=256)

Lazy‑import is employed to keep startup time & dependency footprint low; the
actual class is only imported the first time it is requested.
"""
from __future__ import annotations

from importlib import import_module
from types import ModuleType
from typing import Any, Dict, List, Type, Union, Callable

# --------------------------------------------------------------------------- #
# Internal mapping: *lower‑case key* → "module.path:ClassName" | Class object
# --------------------------------------------------------------------------- #
_MODEL_REGISTRY: Dict[str, Union[str, Type[Any]]] = {
    # 1. GNN backbones / classifiers
    "rgcn_encoder": "src.models.gnn.encoder:RGCNEncoder",
    "res_gcl": "src.models.gnn.res_wrapper:RESGCLClassifier",

    # 2. Contrastive modules
    "self_gcl": "src.models.contrast.self_gcl:SelfGraphCL",
    "graphcl": "src.models.contrast.self_gcl:SelfGraphCL",  # alias
    "sup_con": "src.models.contrast.sup_con:SupContrastHead",
    "supcontrast": "src.models.contrast.sup_con:SupContrastHead",

    # 3. Distilled / lightweight classifiers
    "sgcn_student": "src.models.distill.sgcn_kd:StudentSGCN",
    "student_sgcn": "src.models.distill.sgcn_kd:StudentSGCN",
    "sgcn_kd": "src.models.distill.sgcn_kd:StudentSGCN",

    # 4. Token‑level code LLM embedder
    "code_llm_embed": "src.models.llm_embed:CodeLLMNodeFeat",
    "llm_embed": "src.models.llm_embed:CodeLLMNodeFeat",
}

# --------------------------------------------------------------------------- #
# Registry helper utilities
# --------------------------------------------------------------------------- #

def _resolve(path: str) -> Type[Any]:
    """Import *module* and return the attribute specified after the colon."""
    module_path, attr = path.split(":", 1)
    module: ModuleType = import_module(module_path)
    return getattr(module, attr)


def get_model(name: str) -> Type[Any]:
    """Return the **class** registered under *name* (case‑insensitive).

    The returned object is **not** instantiated – caller can pass custom
    constructor args. Raises *KeyError* if the key is unknown.
    """
    key = name.lower()
    if key not in _MODEL_REGISTRY:
        raise KeyError(
            f"Unknown model key '{name}'. Available keys: {list_models()}"
        )

    entry = _MODEL_REGISTRY[key]
    if isinstance(entry, str):
        # Lazy‑import and overwrite cache
        entry = _resolve(entry)
        _MODEL_REGISTRY[key] = entry
    return entry  # type: ignore[return-value]


def register_model(name: str | List[str], cls: Type[Any]) -> None:
    """Add *cls* to the registry under one or multiple *name* aliases."""
    if isinstance(name, str):
        name = [name]
    for alias in name:
        alias_l = alias.lower()
        if alias_l in _MODEL_REGISTRY:
            raise ValueError(f"Alias '{alias}' already registered.")
        _MODEL_REGISTRY[alias_l] = cls


def list_models() -> List[str]:
    """Return a sorted list of available registry keys."""
    return sorted(_MODEL_REGISTRY)


# --------------------------------------------------------------------------- #
# Re‑export most‑used classes for convenience / IDE discovery
# (Safe import – ignore if optional dependencies missing)
# --------------------------------------------------------------------------- #
try:
    from src.models.gnn.encoder import RGCNEncoder  # noqa: F401
    from src.models.gnn.res_wrapper import RESGCLClassifier  # noqa: F401
except (ImportError, ModuleNotFoundError):
    pass

try:
    from src.models.contrast.self_gcl import SelfGraphCL  # noqa: F401
    from src.models.contrast.sup_con import SupContrastHead  # noqa: F401
except (ImportError, ModuleNotFoundError):
    pass

try:
    from src.models.distill.sgcn_kd import StudentSGCN  # noqa: F401
except (ImportError, ModuleNotFoundError):
    pass

try:
    from src.models.llm_embed import CodeLLMNodeFeat  # noqa: F401
except (ImportError, ModuleNotFoundError):
    pass

__all__: List[str] = [
    # helper fns
    "get_model",
    "register_model",
    "list_models",
    # common classes (if available)
    "RGCNEncoder",
    "RESGCLClassifier",
    "SelfGraphCL",
    "SupContrastHead",
    "StudentSGCN",
    "CodeLLMNodeFeat",
]

# Package version (bumped manually / by CI)
__version__ = "0.1.0"
