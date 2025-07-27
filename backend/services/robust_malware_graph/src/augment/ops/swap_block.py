"""
CodeBlockSwap (PyG)
===================
`bb`(basic-block) 노드 feature를 서로 **교차(swap)** 하여
· CFG 구조(edge)는 그대로 두고,
· 블록 임베딩만 뒤바꾸어
모델이 “코드 순서” 대신 **구조·문맥 정보**에 집중하도록 유도하는 증강 기법.

조건
-----
* 노드 타입 **'bb'** 가 존재해야 동작 (없으면 증강 skip)
* swap 은 **특성만** 교환; 엣지 / 노드 id 는 그대로 유지
"""

from __future__ import annotations

import math
import numbers
from typing import Any, List

import numpy as np
import torch
from torch_geometric.data import Data, HeteroData

from augment import register_op
from augment.base import SimpleAug, AugmentBase

import logging
LOGGER = logging.getLogger(__name__)


@register_op
class CodeBlockSwap(SimpleAug, AugmentBase):
    """Random basic-block feature swapper for PyG graphs."""

    def __init__(
        self,
        prob_pair: float = 0.2,
        seed: int | None = None,
        **kwargs: Any,
    ) -> None:
        if not isinstance(prob_pair, numbers.Real) or not 0.0 <= prob_pair <= 1.0:
            raise ValueError("prob_pair must be a float in [0, 1]")
        self.prob_pair: float = float(prob_pair)
        self._rng = (
            np.random.RandomState(seed)
            if seed is not None
            else np.random.RandomState()
        )

        super().__init__(prob_pair=self.prob_pair, seed=seed, **kwargs)

    # ------------------------------------------------------------------ #
    # AugmentBase 인터페이스                                             #
    # ------------------------------------------------------------------ #
    def __call__(self, g: Data | HeteroData) -> Data | HeteroData:  # type: ignore[override]
        """
        Returns
        -------
        torch_geometric.data.Data | HeteroData
            `bb` 노드 feature 가 일부 교차된 **새 그래프**.
        """
        if math.isclose(self.prob_pair, 0.0):
            return g  # 증강 스킵

        LOGGER.debug("CodeBlockSwap: start | prob_pair=%.3f", self.prob_pair)

        sg = g.clone()  # 구조 공유 + feature 딥 카피

        if isinstance(sg, Data):
            self._swap_on_store(sg)  # homogeneous 그래프를 'bb' 로 간주
        elif isinstance(sg, HeteroData):
            if "bb" not in sg.node_types:
                return sg
            self._swap_on_store(sg["bb"])
        else:  # pragma: no cover
            raise TypeError(
                "CodeBlockSwap supports torch_geometric Data or HeteroData, "
                f"got {type(sg)}"
            )

        LOGGER.debug("CodeBlockSwap: end")
        return sg

    # ------------------------------------------------------------------ #
    # 내부 유틸: 단일 node store(Data 또는 HeteroData['bb'])에 swap 적용    #
    # ------------------------------------------------------------------ #
    def _swap_on_store(self, store: Any) -> None:
        """store (= bb node-store)에 feature-swap을 적용."""
        num_bb = store.num_nodes
        if num_bb < 2:
            return

        # (1) 교환할 노드 수 계산
        n_swap_nodes = int(num_bb * self.prob_pair)
        n_swap_nodes = n_swap_nodes if n_swap_nodes % 2 == 0 else n_swap_nodes - 1
        if n_swap_nodes < 2:
            n_swap_nodes = 2  # 최소 1쌍

        LOGGER.debug("CodeBlockSwap: swapping %d pairs", n_swap_nodes // 2)

        # (2) 무작위로 대상 노드 선택 후 셔플 → 페어링
        idx_pool = self._rng.choice(num_bb, size=n_swap_nodes, replace=False)
        self._rng.shuffle(idx_pool)

        # (3) 교환 대상 feature 키
        keys: List[str] = [
            k for k, v in store.items()
            if torch.is_tensor(v) and v.size(0) == num_bb
        ]
        if not keys:
            return  # 교환할 특성 없음

        # (4) 페어 단위로 feature 교환
        for i in range(0, n_swap_nodes, 2):
            a, b = int(idx_pool[i]), int(idx_pool[i + 1])
            for k in keys:
                feat: torch.Tensor = store[k]
                tmp = feat[a].clone()
                feat[a] = feat[b]
                feat[b] = tmp
