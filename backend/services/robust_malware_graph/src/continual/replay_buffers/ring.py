# --------------------------------------------------------------------------- #
# src/continual/replay_buffers/ring.py
# --------------------------------------------------------------------------- #
"""
RingBuffer
==========
고정 길이 **순환(원형) 버퍼**.  FIFO 큐와 달리 삭제·삽입 없이
단순 인덱스 갱신으로 가장 오래된 슬롯을 덮어씁니다.

특징
-----
* **Sliding window** — 최신 `capacity` 개 샘플만 유지
* **상수 시간** 삽입
* 체크포인트 시 `write_idx` 직렬화

상속 구조
---------
`BaseReplayBuffer` → `RingBuffer`
"""

from __future__ import annotations

from typing import Any, Dict, List

from .base import BaseReplayBuffer


__all__ = ["RingBuffer"]


class RingBuffer(BaseReplayBuffer):
    """고정 크기 순환 버퍼(FIFO, overwrite-in-place)."""

    def __init__(
        self,
        capacity: int,
        *,
        seed: int = 42,
        collate_fn=None,
    ) -> None:
        if capacity is None or capacity < 1:
            raise ValueError("RingBuffer requires a positive `capacity`.")
        super().__init__(capacity=capacity, collate_fn=collate_fn, seed=seed)
        self.write_idx: int = 0  # 다음에 덮어쓸 위치

    # ------------------------------------------------------------------ #
    # 필수 오버라이드
    # ------------------------------------------------------------------ #
    def _insert(self, sample: Dict[str, Any]) -> None:
        if len(self._storage) < self.capacity:
            # 아직 가득 차지 않았으면 append
            self._storage.append(sample)
        else:
            # 가득 찼으면 원형 인덱스 위치를 덮어쓰기
            self._storage[self.write_idx] = sample
        self.write_idx = (self.write_idx + 1) % self.capacity

    def _sample_indices(self, k: int) -> List[int]:
        k = min(k, len(self._storage))
        return self.rng.sample(range(len(self._storage)), k)

    # ------------------------------------------------------------------ #
    # Checkpoint helpers
    # ------------------------------------------------------------------ #
    def state_dict(self) -> Dict[str, Any]:
        state = super().state_dict()
        state["write_idx"] = self.write_idx
        return state

    def load_state_dict(self, state: Dict[str, Any]) -> None:
        super().load_state_dict(state)
        self.write_idx = state["write_idx"]

    # ------------------------------------------------------------------ #
    # Convenience
    # ------------------------------------------------------------------ #
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(capacity={self.capacity}, "
            f"size={len(self)}, write_idx={self.write_idx})"
        )
