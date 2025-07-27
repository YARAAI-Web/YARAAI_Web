"""
src.graphs.transforms.pruner
============================

GraphPruner
-----------
⟦사용 시나리오⟧
1. 모델 Inference/XAI → 노드 중요도 `score ∈ ℝ^N` (float) 산출
2. GraphPruner(scores, thresh=0.05).apply(g)
   ├─ score < thresh   ▶ 노드 제거
   └─ 남김: edge & 텐서/리스트 속성도 함께 슬라이스

옵션
~~~~
• mode = {"threshold", "topk"}           : 기준 방식
• remove_isolated : True  → 고아 노드(drop) / False → 유지
• keep_edge_attrs : {"all","mask","none"}
    - "mask"  : edge_mask 반환
    - "none"  : edge attrs 제거해 가벼운 그래프 확보

호환
~~~~
PyG `Data` / `HeteroData` 모두 지원
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

import torch
from torch_geometric.data import Data, HeteroData

from ..builders.relabeler import _apply_reindex, _make_new_ids, _reindex_node_attrs

GraphT = Data | HeteroData


class GraphPruner:
    """
    Parameters
    ----------
    scores : torch.Tensor | Dict[str, torch.Tensor]
        • Data            : shape `[N]`
        • HeteroData      : {node_type: [N_t]}
    mode : {'threshold','topk'}
    thresh : float
        mode='threshold' → score < thresh 제거
    topk : int
        mode='topk'      → 상위 k 유지
    remove_isolated : bool, default True
    keep_edge_attrs : {'all','mask','none'}, default 'all'
    """

    def __init__(
        self,
        scores,
        *,
        mode: str = "threshold",
        thresh: float = 0.0,
        topk: int = 100,
        remove_isolated: bool = True,
        keep_edge_attrs: str = "all",
    ):
        self.scores = scores
        self.mode = mode
        self.thresh = thresh
        self.topk = topk
        self.remove_isolated = remove_isolated
        self.keep_edge_attrs = keep_edge_attrs
        assert mode in {"threshold", "topk"}
        assert keep_edge_attrs in {"all", "mask", "none"}

    # ------------------------------------------------------------------ #
    def apply(self, g: GraphT, *, inplace: bool = False) -> GraphT:
        if isinstance(g, HeteroData):
            return self._apply_hetero(g, inplace)
        return self._apply_homo(g, inplace)

    # ------------------------------------------------------------------ #
    # 단일-타입 그래프
    # ------------------------------------------------------------------ #
    def _apply_homo(self, g: Data, inplace: bool) -> Data:
        if not inplace:
            g = g.clone()

        score = self.scores.to(g.edge_index.device)
        if self.mode == "threshold":
            keep = score >= self.thresh
        else:  # top-k
            k = min(self.topk, score.size(0))
            _, idx = torch.topk(score, k)
            keep = torch.zeros_like(score, dtype=torch.bool)
            keep[idx] = True

        id_map = _make_new_ids(keep)
        g.edge_index = _apply_reindex(g.edge_index, id_map, id_map)

        if self.keep_edge_attrs == "mask":
            g.edge_mask = torch.full((g.edge_index.size(1),), True)
        elif self.keep_edge_attrs == "none":
            for k in list(g.keys()):
                if k.startswith("edge") and k != "edge_index":
                    g.pop(k)

        _reindex_node_attrs(g, id_map)
        g.num_nodes = int(keep.sum())
        if self.keep_edge_attrs == "mask":
            return g, keep, g.edge_mask  # type: ignore[return-value]
        return g

    # ------------------------------------------------------------------ #
    # HeteroData
    # ------------------------------------------------------------------ #
    def _apply_hetero(self, g: HeteroData, inplace: bool) -> HeteroData:
        if not inplace:
            g = g.clone()

        node_keep: Dict[str, torch.Tensor] = {}
        id_maps: Dict[str, torch.Tensor] = {}

        # 1) 노드 필터링
        for ntype in g.node_types:
            device = getattr(g[ntype], "device", None)
            if device is None:
                for val in g[ntype].values():
                    if isinstance(val, torch.Tensor):
                        device = val.device
                        break
            if device is None:
                device = torch.device("cpu")
            score = self.scores[ntype].to(device)
            if self.mode == "threshold":
                keep = score >= self.thresh
            else:
                k = min(self.topk, score.size(0))
                _, idx = torch.topk(score, k)
                keep = torch.zeros_like(score, dtype=torch.bool)
                keep[idx] = True
            node_keep[ntype] = keep
            id_maps[ntype] = _make_new_ids(keep)
            _reindex_node_attrs(g[ntype], id_maps[ntype])

        # 2) 엣지 리매핑 & 필터
        for src_t, rel, dst_t in g.edge_types:
            store = g[(src_t, rel, dst_t)]
            ei_new = _apply_reindex(store.edge_index, id_maps[src_t], id_maps[dst_t])
            keep_edge = ei_new[0] >= 0  # src/dst 정상인 엣지
            store.edge_index = ei_new[:, keep_edge]

            if self.keep_edge_attrs == "mask":
                store.edge_mask = keep_edge
            elif self.keep_edge_attrs == "none":
                for k in list(store.keys()):
                    if k != "edge_index":
                        store.pop(k)

        # 3) isolated 유지 여부
        if self.remove_isolated:
            for ntype, keep in node_keep.items():
                g[ntype].num_nodes = int(keep.sum())
        else:
            for ntype in g.node_types:
                g[ntype].num_nodes = int(g[ntype].x.size(0))

        return g
