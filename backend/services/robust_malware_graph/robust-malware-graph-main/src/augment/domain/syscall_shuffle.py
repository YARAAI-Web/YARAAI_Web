"""
SysCallShuffle (PyG)
====================
SysCall 노드 시퀀스를 `win` 길이 윈도우마다 무작위로 퍼뮤트(shuffle)하여
행위 흐름을 교란하는 증강 연산.

전제
----
* HeteroData 타입에 노드 타입 **'syscall'** 이 존재
* 각 노드에
    • seq_key : 호출 순서(int)   (기본 'seq_id')
    • tid_key : 스레드 ID(int)   (기본 'tid', 선택)
  가 저장되어 있다고 가정.

Parameters
----------
win  : int   – 슬라이딩 윈도우 크기(≥2)
prob : float – 각 윈도우를 퍼뮤트할 확률 [0,1]
seq_key      – 순서 저장 키
tid_key      – 스레드 ID 키(None ⇒ 전체를 하나의 시퀀스로 간주)
seed : int|None – NumPy RNG 시드
"""
from __future__ import annotations

import numbers
from typing import Any, Dict, List

import numpy as np
import torch
from torch_geometric.data import HeteroData

from augment import register_op
from augment.base import SimpleAug, AugmentBase


@register_op
class SysCallShuffle(SimpleAug, AugmentBase[HeteroData]):
    """Sliding-window SysCall 순서 섞기(PyG)."""

    # --------------------------- init --------------------------------- #
    def __init__(
        self,
        win: int = 3,
        prob: float = 0.5,
        seq_key: str = "seq_id",
        tid_key: str | None = "tid",
        seed: int | None = None,
        **kwargs: Any,
    ):
        if not isinstance(win, numbers.Integral) or win < 2:
            raise ValueError("win 은 2 이상 정수여야 합니다.")
        if not 0.0 <= prob <= 1.0:
            raise ValueError("prob 은 [0,1] 범위여야 합니다.")

        self.win = int(win)
        self.prob = float(prob)
        self.seq_key = seq_key
        self.tid_key = tid_key
        self._rng = (
            np.random.RandomState(seed)
            if seed is not None
            else np.random.RandomState()
        )

        super().__init__(
            win=self.win,
            prob=self.prob,
            seq_key=self.seq_key,
            tid_key=self.tid_key,
            seed=seed,
            **kwargs,
        )

    # -------------------- 내부: feature 재배치 ------------------------- #
    @staticmethod
    def _permute_features(
        node_data: Dict[str, torch.Tensor],
        indices: List[int],
        perm: np.ndarray,
    ) -> None:
        """주어진 인덱스 집합을 perm 순서로 재배치(in-place)."""
        device = next(iter(node_data.values())).device
        idx_t = torch.as_tensor(indices, device=device)
        for k, feat in node_data.items():
            shuffled = feat[idx_t[perm]].clone()
            feat[idx_t] = shuffled

    # ------------------------ AugmentBase ----------------------------- #
    def __call__(self, data: HeteroData) -> HeteroData:  # type: ignore[override]
        # 필요 조건 확인
        if (
            self.prob == 0.0
            or "syscall" not in data.node_types
            or self.seq_key not in data["syscall"]
        ):
            return data

        g: HeteroData = data.clone()

        node_data = g["syscall"]
        seq_ids: torch.Tensor = node_data[self.seq_key]

        # ---- 1) 스레드 그룹 만들기 ----
        if self.tid_key and self.tid_key in node_data:
            tids = node_data[self.tid_key]
            unique_tids = tids.unique()
            groups: List[torch.Tensor] = [
                (tids == tid).nonzero(as_tuple=False).squeeze(-1) for tid in unique_tids
            ]
        else:
            groups = [torch.arange(g["syscall"].num_nodes, device=seq_ids.device)]

        # ---- 2) 각 그룹별 윈도우 퍼뮤트 ----
        for idx_tensor in groups:
            if idx_tensor.numel() < self.win:
                continue

            # seq_id 기준 정렬
            sorted_idx = idx_tensor[seq_ids[idx_tensor].argsort()]

            # 슬라이딩 윈도우
            for start in range(0, len(sorted_idx) - self.win + 1, self.win):
                if self._rng.rand() >= self.prob:
                    continue  # 이 윈도우는 skip

                window_indices = sorted_idx[start : start + self.win].tolist()
                perm = self._rng.permutation(self.win)
                self._permute_features(node_data, window_indices, perm)

        return g
