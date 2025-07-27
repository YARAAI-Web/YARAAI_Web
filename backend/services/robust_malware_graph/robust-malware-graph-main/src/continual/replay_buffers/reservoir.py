# --------------------------------------------------------------------------- #
# src/continual/replay_buffers/reservoir.py
# --------------------------------------------------------------------------- #
"""
ReservoirBuffer
===============
*Vitter'85 reservoir sampling* 알고리즘 기반 재현 버퍼.

특징
-----
1. **Uniform guarantee**
   지금까지 *본(total_seen)* 샘플 중 **capacity 개**를
   항상 균등 확률로 유지합니다.
2. **상수 시간 삽입**
   새 샘플마다 난수 1회 → 기존 저장 중 1개 치환 여부 결정.
3. **메타데이터** (`total_seen`)
   체크포인트 복원을 위해 ``state_dict``에 함께 직렬화.

Notes
-----
* capacity 가 ``None`` 이면 사실상 *무제한* 버퍼(FIFO 아님)로 동작.
* ``sample`` 은 무작위 추출(중복 X)만 지원—스트리밍 학습 시 일반적 요구.
"""

from __future__ import annotations

from typing import Any, Dict, List, Sequence

from .base import BaseReplayBuffer


__all__ = ["ReservoirBuffer"]


class ReservoirBuffer(BaseReplayBuffer):
    """Uniform reservoir-sampling 기반 리플레이 버퍼."""

    def __init__(
        self,
        capacity: int,
        *,
        seed: int = 42,
        collate_fn=None,
    ) -> None:
        if capacity is None or capacity < 1:
            raise ValueError("ReservoirBuffer requires a positive `capacity`.")
        super().__init__(capacity=capacity, collate_fn=collate_fn, seed=seed)
        self.total_seen: int = 0  # 스트림에서 본 총 샘플 수

    # --------------------------------------------------------------------- #
    # BaseReplayBuffer 필수 메서드 구현
    # --------------------------------------------------------------------- #
    def _insert(self, sample: Dict[str, Any]) -> None:
        """
        Vitter's Algorithm R
        --------------------
        * t = total_seen (0-indexed)
        * j ∼ Uniform[0, t]
        * if j < capacity → storage[j] ← sample
        """
        if self.capacity is None:  # pragma: no cover
            self._storage.append(sample)
            self.total_seen += 1
            return

        if len(self._storage) < self.capacity:
            # 버퍼가 가득 차기 전까지는 그대로 push
            self._storage.append(sample)
        else:
            j = self.rng.randint(0, self.total_seen)
            if j < self.capacity:
                self._storage[j] = sample
        self.total_seen += 1

    def _sample_indices(self, k: int) -> List[int]:
        k = min(k, len(self._storage))
        return self.rng.sample(range(len(self._storage)), k)

    # --------------------------------------------------------------------- #
    # Checkpoint helpers – total_seen 추가 직렬화
    # --------------------------------------------------------------------- #
    def state_dict(self) -> Dict[str, Any]:
        state = super().state_dict()
        state["total_seen"] = self.total_seen
        return state

    def load_state_dict(self, state: Dict[str, Any]) -> None:
        super().load_state_dict(state)
        self.total_seen = state["total_seen"]

    # --------------------------------------------------------------------- #
    # Convenience – stats
    # --------------------------------------------------------------------- #
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(capacity={self.capacity}, "
            f"size={len(self)}, total_seen={self.total_seen})"
        )
