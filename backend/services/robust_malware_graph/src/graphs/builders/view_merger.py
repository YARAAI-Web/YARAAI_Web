"""
src.graphs.builders.view_merger
===============================

ViewMerger
----------
여러 **정규화된** PyG `Data / HeteroData` 뷰를 *단순 합집합*으로 병합합니다.

* 특징
  • 뷰 간 **cross-edge** 생성 ❌ (그대로 유지)
  • 노드 ID 충돌 방지를 위해 **타입별 global offset**만 부여
  • 속성(attr) 키가 일치하지 않으면 **0/None 패딩** 후 `torch.cat` 또는 `list.extend`
  • 반환값: 병합된 `HeteroData` 와 *(view,name) → offset* 딕셔너리

용도
----
- 여러 뷰를 한 그래프에 “겹치지 않고” 담고 싶을 때
- `HeteroGraphBuilder` 수준의 깊은 스티칭이 필요 없는 경우
"""

from __future__ import annotations

import itertools
import logging
from collections import defaultdict
from typing import Dict, List, Tuple

import torch
from torch_geometric.data import Data, HeteroData

from ..normalizers.schema import EDGE_REL_ID
from ..utils import get_logger

_View = Data | HeteroData
_Offsets = Dict[str, Dict[str, int]]  # {view: {node_type: offset}}


class ViewMerger:
    """
    Parameters
    ----------
    log_level : int, default logging.INFO
    """

    def __init__(self, log_level: int = logging.INFO) -> None:
        self.log = get_logger("builder.view_merger", log_level)
        self._views: Dict[str, _View] = {}
        self._offsets: _Offsets = defaultdict(dict)     # in-memory cache

    # --------------------------------------------------------------------- #
    # public
    # --------------------------------------------------------------------- #
    def add_view(self, view_name: str, g: _View) -> None:
        """
        Notes
        -----
        • `g` 는 반드시 *Normalizer* 를 거쳐 스키마가 맞춰져 있어야 합니다.
        """
        if view_name in self._views:
            raise ValueError(f"view '{view_name}' already registered")
        self._views[view_name] = g
        self.log.debug("Add view '%s'  node_types=%s", view_name, list(g.node_types))

    def build(self) -> Tuple[HeteroData, _Offsets]:
        """모든 뷰를 합집합해 단일 `HeteroData` 로 반환."""
        if not self._views:
            raise RuntimeError("No views added")

        out = HeteroData()

        # 1) 타입별 global offset 계산
        self._compute_offsets()

        # 2) 노드 스토어 병합
        self._concat_node_stores(out)

        # 3) 엣지 스토어 병합 (offset 적용)
        self._concat_edge_stores(out)

        return out, self._offsets

    # ------------------------------------------------------------------ #
    # internals
    # ------------------------------------------------------------------ #
    def _compute_offsets(self) -> None:
        ctr: Dict[str, int] = defaultdict(int)  # node_type → next_global
        for vname, g in self._views.items():
            for ntype in g.node_types:
                self._offsets[vname][ntype] = ctr[ntype]
                ctr[ntype] += g[ntype].num_nodes
        self.log.debug("Global offsets per type: %s", dict(ctr))

    # ------------------------------------------------------------------ #
    def _concat_node_stores(self, out: HeteroData) -> None:
        for ntype in {nt for g in self._views.values() for nt in g.node_types}:
            stores = []
            for vname, g in self._views.items():
                if ntype not in g.node_types:
                    continue
                st = g[ntype]
                stores.append(st)

            if not stores:
                continue

            # 모든 attr 키 집합
            keys = set(itertools.chain.from_iterable(s.keys() for s in stores))
            tgt = out[ntype]
            for k in keys:
                parts: List = []
                for st in stores:
                    if k in st:
                        parts.append(st[k])
                    else:  # padding
                        if isinstance(st[next(iter(st.keys()))], torch.Tensor):
                            pad_shape = list(st[next(iter(st.keys()))].shape)
                            pad_shape[0] = st.num_nodes
                            parts.append(torch.zeros(pad_shape))
                        else:
                            parts.extend([None] * st.num_nodes)
                tgt[k] = torch.cat(parts) if isinstance(parts[0], torch.Tensor) else list(parts)

    # ------------------------------------------------------------------ #
    def _concat_edge_stores(self, out: HeteroData) -> None:
        tmp_edges: Dict[Tuple[str, str, str], List[torch.Tensor]] = defaultdict(list)
        tmp_attrs: Dict[Tuple[str, str, str], Dict[str, List[torch.Tensor]]] = defaultdict(lambda: defaultdict(list))

        for vname, g in self._views.items():
            for (src_t, rel_t, dst_t) in g.edge_types:
                st = g[(src_t, rel_t, dst_t)]
                ofs_src = self._offsets[vname][src_t]
                ofs_dst = self._offsets[vname][dst_t]
                ei = st.edge_index.clone()
                ei[0] += ofs_src
                ei[1] += ofs_dst
                tmp_edges[(src_t, rel_t, dst_t)].append(ei)

                for k, v in st.items():
                    if k == "edge_index":
                        continue
                    tmp_attrs[(src_t, rel_t, dst_t)][k].append(v)

        # store > concat
        for key, lst in tmp_edges.items():
            ei = torch.cat(lst, dim=1)
            store = out[key]
            store.edge_index = ei
            # edge_type 없으면 채움
            if "edge_type" not in store:
                store.edge_type = torch.full(
                    (ei.shape[1],),
                    EDGE_REL_ID[key[1]],
                    dtype=torch.long,
                )
            for k, ts in tmp_attrs[key].items():
                store[k] = torch.cat(ts)
