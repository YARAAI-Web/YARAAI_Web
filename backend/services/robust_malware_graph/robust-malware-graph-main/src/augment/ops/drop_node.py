"""
NodeDrop (PyG)
==============
임의의 노드를 제거하여 그래프 구조를 희석(thinning) – 
*InfoNCE* 기반 Contrastive 학습에서 **뷰 다양성**을 확보하는 고전적 증강 기법.

● 동작
    - (노드 타입별) 주어진 `keep_prob` 확률로 **노드를 유지**
    - 삭제된 노드에 인접한 엣지도 자동 삭제
    - 타입별 최소 1개 노드 보존 안전장치 포함
"""

from __future__ import annotations

import math
import numbers
from typing import Any, Dict, Mapping, Tuple

import logging
LOGGER = logging.getLogger(__name__)

import logging

import numpy as np
import torch
from torch_geometric.data import Data, HeteroData

from .. import register_op
from ..base import SimpleAug, AugmentBase


def _get_store_device(store: Mapping[str, Any]) -> torch.device:
    """Return device of the first tensor in the storage."""
    for v in store.values():
        if torch.is_tensor(v):
            return v.device
    return torch.device("cpu")


@register_op
class NodeDrop(SimpleAug, AugmentBase):
    """
    Random node *keep* operator for PyTorch Geometric graphs.

    Parameters
    ----------
    keep_prob : float | Mapping[str, float], default 0.8
        Probability of *keeping* a node. 0.0 → 삭제 100 %, 1.0 → 보존 100 %.
        Dict 형식이면 각 노드 타입별 개별 확률 지정.
    seed : int | None, default None
        RNG 시드. None이면 전역 NumPy RNG 사용.
    target_node : str | None, optional
        Node type that must retain at least one instance. Only relevant for
        ``HeteroData`` graphs.
    """

    def __init__(
        self,
        keep_prob: float | Mapping[str, float] = 0.8,
        seed: int | None = None,
        target_node: str | None = None,
        **kwargs: Any,
    ) -> None:
        # ── keep_prob 검증 및 dict 변환 ────────────────────────────────────
        if isinstance(keep_prob, numbers.Real):
            if not 0.0 <= keep_prob <= 1.0:
                raise ValueError("keep_prob(float) must be in [0, 1]")
            keep_prob = {"*": float(keep_prob)}
        else:
            for p in keep_prob.values():
                if not 0.0 <= p <= 1.0:
                    raise ValueError("keep_prob dict values must be in [0, 1]")

        self.keep_prob: Dict[str, float] = dict(keep_prob)
        self.target_node = target_node
        self._rng = (
            np.random.RandomState(seed)
            if seed is not None
            else np.random.RandomState()
        )

        super().__init__(keep_prob=self.keep_prob, seed=seed, target_node=target_node, **kwargs)

    # ------------------------------------------------------------------ #
    # AugmentBase 인터페이스
    # ------------------------------------------------------------------ #
    def __call__(self, g: Data | HeteroData) -> Data | HeteroData:  # type: ignore[override]
        """
        Parameters
        ----------
        g : torch_geometric.data.Data | HeteroData
            입력 그래프 (in-place 수정 ❌).

        Returns
        -------
        torch_geometric.data.Data | HeteroData
            Node-dropped 새 그래프.
        """
        LOGGER.debug(
            "NodeDrop: start | keep_prob=%s target_node=%s",
            self.keep_prob,
            self.target_node,
        )
        sg = g.clone()  # 구조 공유 + feature 깊은 복사

        if isinstance(sg, Data):
            p = self.keep_prob.get("*", 1.0)
            mask = self._drop_nodes_data(sg, p)
            sg.num_nodes = int(mask.sum())

        elif isinstance(sg, HeteroData):
            # 1) 노드 타입별 keep-mask 및 인덱스 매핑 계산
            masks: Dict[str, torch.Tensor] = {}
            maps: Dict[str, torch.Tensor] = {}
            for ntype in sg.node_types:
                p = self.keep_prob.get(ntype, self.keep_prob.get("*", 1.0))
                device = _get_store_device(sg[ntype])
                target_idx = 0 if ntype == self.target_node else None
                mask, mapping = self._make_mask_mapping(
                    sg[ntype].num_nodes, p, device, target_idx
                )
                masks[ntype], maps[ntype] = mask, mapping
                self._apply_node_mask(sg[ntype], mask)      # 노드 속성 필터링

            # 2) 에지 타입별 갱신
            for etype in sg.edge_types:
                src_t, rel_t, dst_t = etype
                self._filter_edges(
                    store=sg[etype],
                    src_map=maps[src_t],
                    dst_map=maps[dst_t],
                )
        else:  # pragma: no cover
            raise TypeError(
                "NodeDrop supports torch_geometric Data or HeteroData, "
                f"got {type(sg)}"
            )

        if isinstance(g, Data):
            LOGGER.debug(
                "NodeDrop: Data nodes %d -> %d",
                g.num_nodes,
                sg.num_nodes,
            )
        elif isinstance(g, HeteroData):
            msg = {
                nt: (int(g[nt].num_nodes), int(sg[nt].num_nodes))
                for nt in g.node_types
            }
            LOGGER.debug("NodeDrop: Hetero nodes %s", msg)

        LOGGER.debug("NodeDrop: end")
        return sg

    # ------------------------------------------------------------------ #
    # 내부 유틸 (homogeneous) ------------------------------------------- #
    # ------------------------------------------------------------------ #
    def _drop_nodes_data(self, data: Data, keep_p: float) -> torch.Tensor:
        """homogeneous Data용 노드 삭제 + 에지 갱신."""
        target_idx = 0 if self.target_node is not None else None
        device = _get_store_device(data)
        mask, mapping = self._make_mask_mapping(
            data.num_nodes, keep_p, device, target_idx
        )
        # 노드 특성 필터링
        self._apply_node_mask(data, mask)
        # 에지 필터링 및 재인덱싱
        self._filter_edges(data, mapping, mapping)
        return mask

    # ------------------------------------------------------------------ #
    # 마스크 & 매핑 생성 -------------------------------------------------- #
    # ------------------------------------------------------------------ #
    def _make_mask_mapping(
        self,
        num_nodes: int,
        keep_p: float,
        device: torch.device,
        target_idx: int | None = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """노드 keep-mask (bool)와 old→new 인덱스 매핑(-1=삭제) 반환."""
        if num_nodes == 0 or math.isclose(keep_p, 1.0):
            mask = torch.ones(num_nodes, dtype=torch.bool, device=device)
        else:
            mask_np = self._rng.rand(num_nodes) < keep_p  # True = keep
            if not mask_np.any():                        # 최소 1개 보존
                mask_np[self._rng.randint(0, num_nodes)] = True
            mask = torch.from_numpy(mask_np).to(device=device, dtype=torch.bool)

        # old → new index (삭제 노드는 -1)
        if target_idx is not None:
            mask = ensure_target_node(mask, target_idx)

        mapping = -torch.ones(num_nodes, dtype=torch.long, device=device)
        mapping[mask] = torch.arange(mask.sum(), device=device)
        return mask, mapping

    # ------------------------------------------------------------------ #
    # 노드 속성 필터 ----------------------------------------------------- #
    # ------------------------------------------------------------------ #
    @staticmethod
    def _apply_node_mask(store: Any, mask: torch.Tensor) -> None:
        """Data 또는 HeteroData[ntype]에서 노드-레벨 속성을 마스킹."""
        num_nodes = mask.size(0)
        for key, val in list(store.items()):
            if key == "edge_index":
                continue
            if torch.is_tensor(val) and val.size(0) == num_nodes:
                store[key] = val[mask]
        store.num_nodes = int(mask.sum())

    # ------------------------------------------------------------------ #
    # 에지 필터 및 재인덱싱 --------------------------------------------- #
    # ------------------------------------------------------------------ #
    def _filter_edges(
        self,
        store: Any,
        src_map: torch.Tensor,
        dst_map: torch.Tensor,
    ) -> None:
        """edge_index 재구성 및 edge-level 속성 동기화."""
        edge_index = store.edge_index
        src, dst = edge_index[0], edge_index[1]
        num_e = src.size(0)

        # ── 노드 범위를 벗어난 엣지 필터링 ──────────────────────────────
        valid = (
            (src >= 0)
            & (src < src_map.size(0))
            & (dst >= 0)
            & (dst < dst_map.size(0))
        )
        if (~valid).any():
            logging.warning(
                "NodeDrop filtered %d out-of-range edges", int((~valid).sum())
            )
        src = src[valid]
        dst = dst[valid]

        # ── 삭제 노드와 연결된 엣지 필터링 ────────────────────────────
        keep = (src_map[src] != -1) & (dst_map[dst] != -1)

        # edge_index 재인덱싱
        new_ei = torch.stack(
            [src_map[src[keep]], dst_map[dst[keep]]], dim=0
        )

        # 원본 에지에 대한 최종 마스크 (edge attributes filtering)
        final_mask = keep

        # ── 삭제 후 남은 엣지가 없으면 self-loop 생성 ─────────────────────
        if new_ei.numel() == 0:
            if torch.equal(src_map, dst_map):
                num_nodes = int((src_map != -1).sum())
                idx = torch.arange(num_nodes, device=edge_index.device)
                new_ei = torch.stack([idx, idx], dim=0)

        store.edge_index = new_ei

        # edge-level 특성 동기화
        for key, val in list(store.items()):
            if key == "edge_index":
                continue
            if torch.is_tensor(val) and val.size(0) == num_e:
                store[key] = val[valid][final_mask]
