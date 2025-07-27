# ---------------------------------------------------------------------------
# src/continual/learner/__init__.py
# ---------------------------------------------------------------------------
"""Unified interface for continual-learning learners.

Exports
-------
* L2PLearner   – Prompt-based continual learner
* SupConLearner – Online Supervised-Contrastive learner
* EWCLearner   – Elastic-Weight-Consolidation learner
* get_learner  – String key → learner factory
* register_learner – Runtime registry extender
"""

from __future__ import annotations

from typing import Any, Dict, Type

# --------------------------------------------------------------------------- #
# concrete learners
# --------------------------------------------------------------------------- #
from .l2p_learner import L2PLearner
from .supcon_cl import SupConLearner
from .ewc_learner import EWCLearner

__all__ = [
    "L2PLearner",
    "SupConLearner",
    "EWCLearner",
    "get_learner",
    "register_learner",
    "LEARNER_REGISTRY",
]

# --------------------------------------------------------------------------- #
# registry utilities
# --------------------------------------------------------------------------- #
LEARNER_REGISTRY: Dict[str, Type] = {
    "l2p": L2PLearner,
    "supcon": SupConLearner,
    "ewc": EWCLearner,
}


def register_learner(key: str, cls: Type, *, overwrite: bool = False) -> None:
    """Add a new learner class to the registry.

    Parameters
    ----------
    key : str
        Unique identifier used to retrieve the learner.
    cls : Type
        Learner class to register.
    overwrite : bool, default False
        Allow replacing an existing entry if True.
    """
    k = key.lower()
    if not overwrite and k in LEARNER_REGISTRY:
        raise KeyError(f"learner key '{k}' already registered")
    LEARNER_REGISTRY[k] = cls


def get_learner(name: str, /, *args: Any, **kwargs: Any):
    """Instantiate a learner by registry key.

    Example
    -------
    >>> learner = get_learner(
    ...     "l2p",
    ...     encoder=my_encoder,
    ...     head=my_head,
    ...     device="cuda",
    ... )
    """
    key = name.lower()
    if key not in LEARNER_REGISTRY:
        raise KeyError(
            f"Unknown learner '{name}'. "
            f"Available: {', '.join(LEARNER_REGISTRY)}"
        )
    return LEARNER_REGISTRY[key](*args, **kwargs)
