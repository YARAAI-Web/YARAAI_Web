"""
EdgeDrop (PyG)
==============
그래프의 **엣지를 무작위 삭제**(= keep 확률로 보존)하여
뷰(view) 간 구조적 다양성을 주입합니다. GraphCL·SimGRACE 등
contrastive 프레임워크에서 널리 쓰이는 증강 연산.

Parameters
----------
keep_prob : float | Mapping[str, float], default 0.8
    - float  → 모든 relation 타입에 동일 확률 적용
    - dict   → {'rel_type': p, ...} 개별 지정
      (존재하지 않는 rel_type 은 '*' 또는 float 기본값 사용)
seed : int | None, default None
    재현성용 NumPy RNG 시드 (None → 전역 RNG 사용)

Example
-------
>>> from augment import build_op
>>> edge_drop = build_op("EdgeDrop", keep_prob=0.7)
>>> data_aug = edge_drop(data_raw)          # data_raw: Data 또는 HeteroData
"""

from __future__ import annotations

import math
import numbers
from typing import Any, Dict, Mapping

import logging
LOGGER = logging.getLogger(__name__)

import numpy as np
import torch
from torch_geometric.data import Data, HeteroData

from augment import register_op
from augment.base import SimpleAug, AugmentBase


@register_op
class EdgeDrop(SimpleAug, AugmentBase):
    """Random edge-keep operator for PyTorch Geometric graphs."""

    def __init__(
        self,
        keep_prob: float | Mapping[str, float] = 0.8,
        seed: int | None = None,
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
        self._rng = (
            np.random.RandomState(seed)
            if seed is not None
            else np.random.RandomState()
        )

        super().__init__(keep_prob=self.keep_prob, seed=seed, **kwargs)

    # ------------------------------------------------------------------ #
    # AugmentBase 인터페이스
    # ------------------------------------------------------------------ #
    def __call__(self, g: Data | HeteroData) -> Data | HeteroData:  # type: ignore[override]
        """
        Parameters
        ----------
        g : torch_geometric.data.Data | HeteroData
            입력 그래프 (in-place 수정 ❌)

        Returns
        -------
        torch_geometric.data.Data | HeteroData
            Edge-dropped 그래프 (원본과 같은 device)
        """
        if math.isclose(self.keep_prob.get("*", 1.0), 1.0) and all(
            math.isclose(p, 1.0) for p in self.keep_prob.values()
        ):
            # 삭제 확률이 0이면 그대로 반환
            return g

        LOGGER.debug("EdgeDrop: start | keep_prob=%s", self.keep_prob)
        sg = g.clone()  # 구조 공유 + feature 딥 카피

        # ────────────────────────────────────────────────────────────── #
        # (1) homogeneous Data                                          #
        # ────────────────────────────────────────────────────────────── #
        if isinstance(sg, Data):
            p = self.keep_prob.get("*", 1.0)
            before = sg.num_edges
            self._drop_on_store(sg, p)
            LOGGER.debug("EdgeDrop: Data edges %d -> %d", before, sg.num_edges)

        # ────────────────────────────────────────────────────────────── #
        # (2) heterogeneous HeteroData                                   #
        # ────────────────────────────────────────────────────────────── #
        elif isinstance(sg, HeteroData):
            for etype in sg.edge_types:
                # etype: tuple (src_ntype, rel_type, dst_ntype)
                rel_type = etype[1]
                p = self.keep_prob.get(rel_type, self.keep_prob.get("*", 1.0))
                before = sg[etype].num_edges
                self._drop_on_store(sg[etype], p)
                LOGGER.debug(
                    "EdgeDrop: etype %s edges %d -> %d",
                    etype,
                    before,
                    sg[etype].num_edges,
                )

        else:  # pragma: no cover
            raise TypeError(
                "EdgeDrop supports torch_geometric Data or HeteroData, "
                f"got {type(sg)}"
            )

        LOGGER.debug("EdgeDrop: end")
        return sg

    # ------------------------------------------------------------------ #
    # 내부 유틸: 단일 edge store(Data 또는 HeteroData[etype])에 드롭 적용
    # ------------------------------------------------------------------ #
    def _drop_on_store(self, store: Any, keep_p: float) -> None:
        """주어진 edge store(Data 또는 HeteroData[etype])에 edge-drop 적용."""
        num_e = store.num_edges
        if num_e == 0 or math.isclose(keep_p, 1.0):
            return

        mask_np = self._rng.rand(num_e) < keep_p
        if not mask_np.any():  # 모든 엣지가 삭제된 경우 최소 1개 보존
            mask_np[self._rng.randint(0, num_e)] = True
        mask = torch.from_numpy(mask_np).to(torch.bool)

        # edge_index 필터링 (shape: [2, E])
        edge_index = store.edge_index
        store.edge_index = edge_index[:, mask]

        # edge-level 특성 동기화
        for key, val in list(store.items()):
            if key == "edge_index":
                continue
            if torch.is_tensor(val) and val.size(0) == num_e:
                store[key] = val[mask]
