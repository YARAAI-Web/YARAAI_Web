"""Remap node IDs and remove isolates."""

from __future__ import annotations

class Relabeler:
    """Ensure node IDs are contiguous and prune isolated nodes."""
    pass
"""
src.graphs.builders.relabeler
=============================

Relabeler
---------
>>> new_g, maps = relabel(g, remove_isolated=True)

Parameters
----------
g : Data | HeteroData
remove_isolated : bool, default True
    in-/out-degree가 모두 0인 노드를 버릴지 여부.
inplace : bool, default False
    True ⇒ 입력 객체를 직접 수정(메모리 절약).

Returns
-------
new_g : Data | HeteroData
maps  : dict[str, torch.Tensor]
    node_type 별 (old_id → new_id or -1) 텐서.
"""

from typing import Dict, Tuple

import torch
from torch_geometric.data import Data, HeteroData


# ─────────────────────────────────────────────────────────────────────
# public API
# ─────────────────────────────────────────────────────────────────────
def relabel(
    g: Data | HeteroData,
    *,
    remove_isolated: bool = True,
    inplace: bool = False,
) -> Tuple[Data | HeteroData, Dict[str, torch.Tensor]]:
    """단일/이종 그래프 모두 지원."""
    if isinstance(g, HeteroData):
        return _relabel_hetero(g, remove_isolated, inplace)
    return _relabel_homo(g, remove_isolated, inplace)


# ─────────────────────────────────────────────────────────────────────
# internal helpers
# ─────────────────────────────────────────────────────────────────────
def _make_new_ids(mask: torch.Tensor) -> torch.Tensor:
    """True→ keep. False→ drop(→-1)."""
    new_id = torch.full_like(mask, -1, dtype=torch.long)
    new_id[mask] = torch.arange(
        mask.sum(),
        dtype=torch.long,
        device=mask.device,
    )
    return new_id


def _apply_reindex(edge_idx: torch.Tensor, src_map: torch.Tensor, dst_map: torch.Tensor):
    src, dst = edge_idx
    src = src_map[src]
    dst = dst_map[dst]
    keep = (src >= 0) & (dst >= 0)
    return torch.stack([src[keep], dst[keep]], dim=0)


# ---------------------------------------------------------------------
# (1) 단일-타입 Data
# ---------------------------------------------------------------------
def _relabel_homo(
    g: Data,
    remove_isolated: bool,
    inplace: bool,
) -> Tuple[Data, Dict[str, torch.Tensor]]:
    if not inplace:
        g = g.clone()

    N = g.num_nodes
    mask = torch.zeros(N, dtype=torch.bool)
    mask[g.edge_index[0]] = True
    mask[g.edge_index[1]] = True
    if not remove_isolated:
        mask[:] = True

    id_map = _make_new_ids(mask)
    g.edge_index = _apply_reindex(g.edge_index, id_map, id_map)
    _reindex_node_attrs(g, id_map)

    g.num_nodes = int(mask.sum())
    return g, {"": id_map}  # 빈 문자열 키 = 단일 타입


# ---------------------------------------------------------------------
# (2) HeteroData
# ---------------------------------------------------------------------
def _relabel_hetero(
    g: HeteroData,
    remove_isolated: bool,
    inplace: bool,
) -> Tuple[HeteroData, Dict[str, torch.Tensor]]:
    if not inplace:
        g = g.clone()

    id_maps: Dict[str, torch.Tensor] = {}
    # 1) 노드-타입별 keep mask
    for ntype in g.node_types:
        N = g[ntype].num_nodes
        mask = torch.zeros(N, dtype=torch.bool)
        # 모든 relation 에 대해 차수 계산
        for (src_t, _rel, dst_t) in g.edge_types:
            store = g[(src_t, _rel, dst_t)]
            if src_t == ntype:
                mask[store.edge_index[0]] = True
            if dst_t == ntype:
                mask[store.edge_index[1]] = True
        if not remove_isolated:
            mask[:] = True
        id_maps[ntype] = _make_new_ids(mask)
        _reindex_node_attrs(g[ntype], id_maps[ntype])  # in-place attr 자리맞춤

    # 2) edge_index 재매핑 & 고아 edge 제거
    for key in g.edge_types:
        src_t, _rel, dst_t = key
        store = g[key]
        store.edge_index = _apply_reindex(
            store.edge_index,
            id_maps[src_t],
            id_maps[dst_t],
        )

    # 3) num_nodes 업데이트
    for ntype, m in id_maps.items():
        g[ntype].num_nodes = int((m >= 0).sum())

    return g, id_maps


# ---------------------------------------------------------------------
# 공통 : 노드 속성 재배치(padding 0)
# ---------------------------------------------------------------------
def _reindex_node_attrs(store, id_map: torch.Tensor) -> None:
    keep = id_map >= 0
    idx_new = id_map[keep]
    for k, v in list(store.items()):
        if k in ("num_nodes",):
            continue
        if isinstance(v, torch.Tensor) and v.size(0) == keep.size(0):
            store[k] = v[keep]
        elif isinstance(v, list) and len(v) == keep.size(0):
            store[k] = [v[i] for i in torch.nonzero(keep, as_tuple=False).flatten()]
