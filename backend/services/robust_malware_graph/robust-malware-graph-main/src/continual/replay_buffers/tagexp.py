# --------------------------------------------------------------------------- #
# src/continual/replay_buffers/tagexp.py
# --------------------------------------------------------------------------- #
"""
TagExpBuffer
============
**Exponential-age–weighted** 리플레이 버퍼.

개념
-----
* 스트림에서 본 샘플의 **age = (total_seen - t_insert)**
  → 재생 확률 ∝ *exp(-λ · age)*  (λ > 0).
* λ ↑  ⇒ **최근** 샘플 가중 ↑ (long-term forgetting 완화 ↔ stability / plasticity 균형).
* capacity 초과 시 **가장 오래된** 슬롯을 순환(overwrite) – RingBuffer 기반.

파라미터
---------
λ (decay_rate) : float, default 0.001
    age 1 증가 시 가중치가 `exp(-λ)` 배로 감소.
    (예: λ=0.001, age=1000 → 가중치 ≈ 0.37)

사용 예시
---------
>>> buf = TagExpBuffer(capacity=20_000, decay_rate=5e-4)
>>> for sample in stream:
...     buf.add(sample)
>>> batch = buf.sample(256)          # 최근 데이터 bias
"""

from __future__ import annotations

import math
import random
import warnings
from typing import Any, Dict, List, Sequence, Tuple

from .base import BaseReplayBuffer


__all__ = ["TagExpBuffer"]


class TagExpBuffer(BaseReplayBuffer):
    """`exp(-λ·age)` 가중치로 *biased* 샘플링하는 리플레이 버퍼."""

    def __init__(
        self,
        capacity: int,
        *,
        decay_rate: float = 1e-3,
        seed: int = 42,
        collate_fn=None,
    ) -> None:
        if capacity is None or capacity < 1:
            raise ValueError("TagExpBuffer requires positive `capacity`.")
        if decay_rate <= 0:
            raise ValueError("decay_rate(λ) must be > 0.")
        super().__init__(capacity=capacity, collate_fn=collate_fn, seed=seed)
        self.decay_rate = float(decay_rate)
        # 삽입 시점(time-step) 기록
        self._insert_steps: List[int] = []
        self.total_seen: int = 0  # 전체 스트림 카운터

    # ------------------------------------------------------------------ #
    # 필수 오버라이드
    # ------------------------------------------------------------------ #
    def _insert(self, sample: Dict[str, Any]) -> None:
        """
        RingBuffer-style 순환 저장: capacity 초과 시 가장 오래된 샘플 덮어쓰기.
        """
        if len(self._storage) < self.capacity:
            self._storage.append(sample)
            self._insert_steps.append(self.total_seen)
        else:
            # 덮어쓸 위치 = (total_seen % capacity)
            idx = self.total_seen % self.capacity
            self._storage[idx] = sample
            self._insert_steps[idx] = self.total_seen
        self.total_seen += 1

    def _sample_indices(self, k: int) -> List[int]:
        """
        비복원(weighted-without-replacement) 샘플링.

        P(i) ∝ exp(-λ·age_i), where age_i = total_seen - step_i.
        """
        n = len(self._storage)
        k = min(k, n)
        if k == 0:  # pragma: no cover – empty buffer handled upstream
            return []

        # ---------------- compute weights ---------------- #
        ages = [self.total_seen - t_i for t_i in self._insert_steps]
        weights = [math.exp(-self.decay_rate * age) for age in ages]

        # ----------- weighted-without-replacement --------- #
        # reservoir-style 뽑기: key = u^{1/weight}
        keys: List[Tuple[float, int]] = []
        for idx, w in enumerate(weights):
            # u ∈ (0,1] – avoid log(0)
            u = self.rng.random()
            while u == 0.0:  # pragma: no cover
                u = self.rng.random()
            key = u ** (1.0 / w)
            keys.append((key, idx))

        # 가장 큰 k개 key 선택
        keys.sort(reverse=True, key=lambda x: x[0])
        return [idx for _, idx in keys[:k]]

    # ------------------------------------------------------------------ #
    # Checkpoint helpers
    # ------------------------------------------------------------------ #
    def state_dict(self) -> Dict[str, Any]:
        state = super().state_dict()
        state.update(
            {
                "insert_steps": self._insert_steps,
                "total_seen": self.total_seen,
                "decay_rate": self.decay_rate,
            }
        )
        return state

    def load_state_dict(self, state: Dict[str, Any]) -> None:
        super().load_state_dict(state)
        self._insert_steps = list(state["insert_steps"])
        self.total_seen = int(state["total_seen"])
        self.decay_rate = float(state["decay_rate"])

    # ------------------------------------------------------------------ #
    # Convenience
    # ------------------------------------------------------------------ #
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(capacity={self.capacity}, "
            f"size={len(self)}, λ={self.decay_rate:g}, total_seen={self.total_seen})"
        )
