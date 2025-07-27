from __future__ import annotations

from src.augment.view_generators.standard_pair import StandardPair

"""src.augment.basic
====================
Light‑weight helpers that expose *canonical* augmentation recipes used by the
Robust‑Malware‑Graph project.
The intent is to hide the low‑level details of wiring individual augmentation
operations (**ops**) into *two‑view* generators required by **GraphCL**‑style
contrastive pre‑training.  Down‑stream code can therefore obtain a fully
configured transform with a single line::
    from augment.basic import get_default_graphcl_transforms
    transform = get_default_graphcl_transforms()
and pass it directly to a ``GraphDataset`` or ``DataLoader`` as the
``transform`` argument.
All operations rely on *PyTorch Geometric* objects and conform to
``Callable[[Data | HeteroData], Data | HeteroData]``.  Each op class derives
from :class:`src.augment.base.AugmentBase`.
"""
from typing import List, Sequence
# ────────────────────────────────────────────────────────────────────────────────
# Project‑local imports – kept *inside* the function to avoid hard dependency
# issues when users introspect this module without having installed every
# optional backend.
# ────────────────────────────────────────────────────────────────────────────────
__all__ = [
    "get_default_graphcl_transforms",
]# ════════════════════════════════════════════════════════════════════════════════
# Public helpers
# ════════════════════════════════════════════════════════════════════════════════
def get_default_graphcl_transforms(
    *,
    node_drop_p: float = 0.90,
    edge_drop_p: float = 0.80,
    attr_mask_p: float = 0.10,
    target_node: str | None = None,
    inject_api_dist: str = "popular",
    inject_api_k: int = 2,
    swap_prob_pair: float = 0.15,
) -> "StandardPair":
    """Return the **GraphCL** default *two‑view* generator.
    The recipe follows the augmentation mix suggested in the original
    GraphCL paper ("Graph Contrastive Learning with Augmentations",
    *ICML 2020*) while adding domain‑specific ops that are useful for binary
    analysis.
    Parameters
    ----------
    node_drop_p
        Probability of deleting a node (and all incident edges).
    edge_drop_p
        Probability of randomly removing an edge.
    attr_mask_p
        Probability of zero‑ing a node feature vector.
    target_node
        Node type reserved from dropping when ``NodeDrop`` is applied. If
        ``None`` the behaviour is unchanged.
    inject_api_dist
        Sampling strategy for :class:`InjectAPICall` (``"popular"``,
        ``"rarity"`` or ``"uniform"``).
    inject_api_k
        Number of synthetic API‑call nodes to inject.
    swap_prob_pair
        Probability of swapping a pair of basic blocks (CFG‑level op).
    Returns
    -------
    StandardPair
        Callable that, when invoked on a *single* graph, yields **two**
        stochastically augmented views ``(g₁, g₂)``.
    """
    # Lazy imports so that *basic.py* does not enforce heavy dependencies when
    # the caller only wants to *inspect* available helpers.
    from .ops.drop_node import NodeDrop  # noqa: WPS433 (internal import)
    from .ops.drop_edge import EdgeDrop  # noqa: WPS433
    from .ops.attr_mask import AttrMask  # noqa: WPS433
    from .ops.inject_call import InjectAPICall  # noqa: WPS433
    from .ops.swap_block import CodeBlockSwap  # noqa: WPS433
    from .view_generators.standard_pair import StandardPair  # noqa: WPS433
    # ------------------------------------------------------------------
    # Define *complementary* op sequences for the two views.  The exact
    # probabilities are heuristically chosen – feel free to override them via
    # the function arguments.
    # ------------------------------------------------------------------
    ops_a: Sequence = [
        NodeDrop(node_drop_p, target_node=target_node),
        EdgeDrop(edge_drop_p),
        AttrMask(attr_mask_p),
    ]
    ops_b: Sequence = [
        EdgeDrop(edge_drop_p),  # increased difficulty
        AttrMask(attr_mask_p * 0.5),  # milder masking
        InjectAPICall(dist=inject_api_dist, k=inject_api_k),
        CodeBlockSwap(prob_pair=swap_prob_pair),
    ]
    return StandardPair(ops_a=list(ops_a), ops_b=list(ops_b))
