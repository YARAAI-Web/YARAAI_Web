"""
RandomPair (PyG)
================
`op_pool` 에서 무작위로 **k 개**의 증강 연산을 샘플링하여
g₁, g₂ 각각에 적용하는 뷰 생성기.

특징
-----
* 호출 시마다 **서로 다른 Op·순서**가 선택돼 뷰 다양성이 극대화
* `unique=False` 로 두 뷰에 *같은* Op 시퀀스를 쓰게 하거나,
  `replace=True` 로 중복 선택(샘플링 with replacement) 도 가능
* NumPy RNG 시드(`seed`)로 완전 재현 가능

Parameters
----------
op_pool : list[AugmentBase]
    사용할 증강 연산 후보 풀 (NodeDrop, EdgeDrop, …)
k : int, default 2
    한 뷰에 적용할 연산 개수
replace : bool, default False
    True  → 샘플링 *with* replacement (op_pool < k 여도 OK)
    False → 샘플링 *without* replacement
unique : bool, default True
    True  → g₁, g₂ 에 **서로 다른** 시퀀스 샘플링
    False → 동일 시퀀스를 g₁, g₂ 에 적용
seed : int | None, default None
    NumPy RNG 시드 (None → 전역 RNG)

지원 그래프
------------
* `torch_geometric.data.Data`
* `torch_geometric.data.HeteroData`
"""

from __future__ import annotations

import copy
from typing import List, Sequence

import numpy as np
from torch_geometric.data import Data, HeteroData

from augment import register_view
from augment.base import AugmentBase, ViewGenerator


@register_view
class RandomPair(ViewGenerator):
    """무작위 Op 시퀀스 기반 두 뷰 생성기."""

    def __init__(
        self,
        op_pool: List[AugmentBase],
        k: int = 2,
        replace: bool = False,
        unique: bool = True,
        seed: int | None = None,
    ) -> None:
        if not op_pool:
            raise ValueError("op_pool must contain at least one AugmentBase instance.")
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        if not replace and k > len(op_pool):
            raise ValueError("k cannot exceed len(op_pool) when replace=False.")

        self.op_pool = op_pool
        self.k = int(k)
        self.replace = bool(replace)
        self.unique = bool(unique)
        self._rng = (
            np.random.RandomState(seed)
            if seed is not None
            else np.random.RandomState()
        )

    # ------------------------------------------------------------------ #
    # 내부: 시퀀스 샘플링
    # ------------------------------------------------------------------ #
    def _sample_ops(self) -> List[AugmentBase]:
        """k 개 Op 무작위 선택 → *deepcopy* 로 반환해 side-effect 방지."""
        indices: Sequence[int] = (
            self._rng.choice(len(self.op_pool), size=self.k, replace=self.replace)
        )
        # Op 자체가 상태(state)를 가질 수 있으므로 deepcopy
        return [copy.deepcopy(self.op_pool[i]) for i in indices]

    # ------------------------------------------------------------------ #
    # ViewGenerator 인터페이스
    # ------------------------------------------------------------------ #
    def __call__(
        self, g: Data | HeteroData
    ) -> tuple[Data | HeteroData, Data | HeteroData]:
        """원본 그래프 → (aug g1, aug g2)"""

        # 그래프 복제
        g1 = copy.deepcopy(g)
        g2 = copy.deepcopy(g)

        # 시퀀스 샘플링
        if self.unique:
            ops_seq_1 = self._sample_ops()
            ops_seq_2 = self._sample_ops()
        else:
            ops_seq_1 = ops_seq_2 = self._sample_ops()

        # 적용
        for op in ops_seq_1:
            g1 = op(g1)  # type: ignore[arg-type]
        for op in ops_seq_2:
            g2 = op(g2)  # type: ignore[arg-type]

        return g1, g2

    # ------------------------------------------------------------------ #
    # 메타데이터 (옵션)
    # ------------------------------------------------------------------ #
    @property
    def name(self) -> str:  # noqa: D401
        return self.__class__.__name__

    def hyperparams(self):
        return {
            "k": self.k,
            "replace": self.replace,
            "unique": self.unique,
            "op_pool": [op.name for op in self.op_pool],
        }
