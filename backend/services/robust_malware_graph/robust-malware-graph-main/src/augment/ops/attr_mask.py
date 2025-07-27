"""
AttrMask (PyG)
==============
노드-레벨 **속성 마스킹** 증강 연산.

* GraphCL·SimGRACE 류의 self-supervised GNN 학습에서 dropout 대체/보완용으로 자주 쓰입니다.
* torch_geometric.data.Data 뿐 아니라 torch_geometric.data.HeteroData(heterograph) 모두 지원합니다.

Parameters
----------
p : float, default 0.1
    • 각 노드가 지정된 feature 열이 **마스킹(0 값)될 확률**
      0.0 ⇒ 아무 것도 안 지움, 1.0 ⇒ 모두 지움
cols : list[str] | None, default None
    • 마스킹할 노드 data 필드명 목록
      None/빈 리스트 ⇒ 노드가 보유한 **모든** tensor 특성을 대상으로 함
seed : int | None, default None
    재현성용 NumPy RNG 시드 (None ⇒ 전역 RNG 사용)

Example
-------
>>> from augment import build_op
>>> attr_mask = build_op("AttrMask", p=0.15, cols=["opcode_emb", "api_emb"])
>>> data_aug = attr_mask(data_raw)          # data_raw: Data 또는 HeteroData
"""

from __future__ import annotations

import math
import numbers
from typing import Any, List

import logging
LOGGER = logging.getLogger(__name__)

import numpy as np
import torch
from torch_geometric.data import Data, HeteroData

from augment import register_op
from augment.base import SimpleAug, AugmentBase


@register_op
class AttrMask(SimpleAug, AugmentBase):
    """Random feature-masking operator for PyTorch Geometric graphs."""

    def __init__(
        self,
        p: float = 0.1,
        cols: List[str] | None = None,
        seed: int | None = None,
        **kwargs: Any,
    ) -> None:
        if not isinstance(p, numbers.Real) or not 0.0 <= p <= 1.0:
            raise ValueError("p must be a float in [0, 1]")
        self.p: float = float(p)
        self.cols: List[str] | None = list(cols) if cols else None
        self._rng = (
            np.random.RandomState(seed)
            if seed is not None
            else np.random.RandomState()
        )

        # SimpleAug → name / hyperparams() 자동 제공
        super().__init__(p=self.p, cols=self.cols, seed=seed, **kwargs)

    # ------------------------------------------------------------------ #
    # AugmentBase 인터페이스
    # ------------------------------------------------------------------ #
    def __call__(self, g: Data | HeteroData) -> Data | HeteroData:  # type: ignore[override]
        """
        Parameters
        ----------
        g : torch_geometric.data.Data | HeteroData
            입력 그래프( in-place 수정 ❌ ).

        Returns
        -------
        torch_geometric.data.Data | HeteroData
            지정 특성이 마스킹된 **새로운** 그래프 인스턴스.
        """
        if math.isclose(self.p, 0.0):
            # 아무 것도 안 지울 때는 원본 그대로 반환
            return g

        LOGGER.debug(
            "AttrMask: start | p=%.3f cols=%s", self.p, self.cols
        )

        sg = g.clone()  # 구조 공유 + feature 딥 카피

        # ────────────────────────────────────────────────────────────── #
        # (1) homogeneous Data                                        #
        # ────────────────────────────────────────────────────────────── #
        if isinstance(sg, Data):
            self._mask_on_store(sg, num_nodes=sg.num_nodes)

        # ────────────────────────────────────────────────────────────── #
        # (2) heterogeneous HeteroData                                 #
        # ────────────────────────────────────────────────────────────── #
        elif isinstance(sg, HeteroData):
            for ntype in sg.node_types:
                store = sg[ntype]
                self._mask_on_store(store, num_nodes=store.num_nodes)

        else:  # pragma: no cover
            raise TypeError(
                "AttrMask supports torch_geometric Data or HeteroData, "
                f"got {type(sg)}"
            )

        LOGGER.debug("AttrMask: end")
        return sg

    # ------------------------------------------------------------------ #
    # 내부 유틸: 단일 node store(Data 또는 HeteroData[ntype])에 마스킹 적용
    # ------------------------------------------------------------------ #
    def _mask_on_store(self, store: Any, num_nodes: int) -> None:
        """주어진 node store(Data 또는 HeteroData[ntype])에 feature-mask 적용."""
        if num_nodes == 0:
            return

        # store.keys() → 현재 저장된 모든 속성명
        keys = list(store.keys())
        target_keys = keys if not self.cols else [k for k in keys if k in self.cols]
        if not target_keys:
            return

        # 노드 단위 마스크 생성 (True ⇒ 마스킹)
        mask_np = self._rng.rand(num_nodes) < self.p
        if not mask_np.any():  # 모든 노드가 보존되면 최소 1개 강제 마스킹
            mask_np[self._rng.randint(0, num_nodes)] = True
        mask_bool = torch.from_numpy(mask_np).to(torch.bool)
        LOGGER.debug(
            "AttrMask: masking %d / %d nodes on store %s",
            int(mask_bool.sum()),
            num_nodes,
            getattr(store, 'name', 'unknown'),
        )

        for key in target_keys:
            feat = store[key]
            if not torch.is_tensor(feat) or feat.size(0) != num_nodes:
                continue  # shape 불일치 또는 tensor 아님 → skip

            mask = mask_bool.to(feat.device)
            masked_feat = feat.clone()
            # 첫 번째 차원(N)에 대해 브로드캐스팅
            if masked_feat.dim() == 1:           # (N,)
                masked_feat[mask] = 0
            else:                                # (N, D, …)
                masked_feat[mask, ...] = 0
            store[key] = masked_feat
