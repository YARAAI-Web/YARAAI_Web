# SPDX-License-Identifier: MIT
"""src.models.contrast package
=================================
Convenience exports & registry for contrastive heads / wrappers.

Usage
-----
>>> from src.models.contrast import get_contrast
>>> ModelCls = get_contrast("self_gcl")
>>> model = ModelCls(...)

The mapping covers
* **SelfGraphCL**  – GraphCL‑style *self‑supervised* contrast
* **SupContrastHead** – Supervised contrastive head (SupCon)
"""
from __future__ import annotations

from typing import Dict, Type

from .self_gcl import SelfGraphCL  # type: ignore F401
from .sup_con import SupContrastHead  # type: ignore F401

__all__ = [
    "SelfGraphCL",
    "SupContrastHead",
    "CONTRAST_REGISTRY",
    "get_contrast",
]

# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
CONTRAST_REGISTRY: Dict[str, Type] = {
    # self‑supervised variants
    "self_gcl": SelfGraphCL,
    "graphcl": SelfGraphCL,
    # supervised variants
    "sup_con": SupContrastHead,
    "supcontrast": SupContrastHead,
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def get_contrast(name: str):
    """Return the contrastive **class** mapped to *name*.

    >>> from src.models.contrast import get_contrast
    >>> SelfGCL = get_contrast("self_gcl")
    >>> model = SelfGCL(encoder, proj_dim=128)
    """
    key = name.lower()
    if key not in CONTRAST_REGISTRY:
        raise KeyError(
            f"Unknown contrastive module '{name}'. Available: {list(CONTRAST_REGISTRY)}"
        )
    return CONTRAST_REGISTRY[key]


def available() -> list[str]:
    """List registered contrastive module names."""
    return list(CONTRAST_REGISTRY)
