# --------------------------------------------------------------------------- #
# src/continual/replay_buffers/base.py
# --------------------------------------------------------------------------- #
"""
BaseReplayBuffer
================
온라인 / 증분(continual) 학습에서 *재현‧혼합* 샘플을 저장·제공하는
**공통 인터페이스**를 정의합니다. 모든 버퍼(Reservoir, Ring, TagExp …)는
본 클래스를 상속해 `_insert()` / `_sample_indices()` 두 메서드만
구현하면 됩니다.

Key conventions
---------------
* 한 ‘샘플(sample)’은 **dict** 로 표현되며 최소한
  ``data`` (torch_geometric.data.(Hetero)Data) 와
  ``y`` (torch.Tensor) 키를 포함합니다.
* 추가 필드(`task_id`, `meta` …)는 임의로 포함될 수 있으며
  → 버퍼는 *원형 그대로* 저장·반환합니다.
* 내부 저장 구조는 **list** 로 고정해 단순성 ↑.  GPU 로의 이동은
  learner 가 담당(`to_device` 호출)합니다.
* 스레드 세이프티(thread-safety)가 필수라면 상속 클래스에서
  ``threading.Lock`` 등을 추가해 주세요.

Example
-------
>>> buf = ReservoirBuffer(capacity=10_000)
>>> buf.add(sample)
>>> batch = buf.sample(batch_size=128)   # dict 로 collate
"""

from __future__ import annotations

import random
import warnings
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Sequence

import torch
from torch_geometric.data import Batch, Data, HeteroData

__all__ = ["BaseReplayBuffer", "collate_graph_samples"]


# --------------------------------------------------------------------------- #
# Collate helper – PyG Data / HeteroData 지원
# --------------------------------------------------------------------------- #
def collate_graph_samples(samples: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    """
    리스트 형태 `samples` 를 **단일 dict(batch)** 로 묶어 반환합니다.

    * ``data``          → ``torch_geometric.data.Batch.from_data_list``
    * 텐서형 키         → ``torch.stack`` (dim=0)
    * 기타 파이썬 객체   → 리스트로 묶어 그대로 유지
    """
    if len(samples) == 0:  # pragma: no cover
        raise ValueError("Cannot collate an empty list of samples.")

    # --------------------------- graph --------------------------- #
    first_graph = samples[0]["data"]
    graphs = [s["data"] for s in samples]

    if isinstance(first_graph, (Data, HeteroData)):
        batched_graph = Batch.from_data_list(graphs)
    else:  # pragma: no cover
        raise TypeError(f"Unsupported graph type: {type(first_graph)}")

    # --------------------------- other keys ---------------------- #
    batch_dict: Dict[str, Any] = {"data": batched_graph}
    keys = set(samples[0].keys()) - {"data"}

    for k in keys:
        vals = [s[k] for s in samples]
        if torch.is_tensor(vals[0]):
            try:
                batch_dict[k] = torch.stack(vals, dim=0)
            except RuntimeError:
                # 스칼라 텐서(0-dim) → unsqueeze
                batch_dict[k] = torch.stack(
                    [v.unsqueeze(0) if v.dim() == 0 else v for v in vals], dim=0
                )
        else:
            # JSON 직렬화 가능 객체 등은 리스트로 유지
            batch_dict[k] = vals
    return batch_dict


# --------------------------------------------------------------------------- #
# Base class
# --------------------------------------------------------------------------- #
class BaseReplayBuffer(ABC):
    r"""
    Parameters
    ----------
    capacity : int
        최대 저장 샘플 수. `None` 이면 제한 없음(단 메모리 주의).
    collate_fn : Callable, default ``collate_graph_samples``
        ``sample()`` 호출 시 다수의 샘플을 batch 로 묶는 함수.
    seed : int, default 42
        내부 RNG 초기값(샘플링 재현성).
    """

    def __init__(
        self,
        capacity: int | None,
        collate_fn: Callable[[Sequence[Dict[str, Any]]], Dict[str, Any]]
        | None = None,
        *,
        seed: int = 42,
    ) -> None:
        self.capacity = capacity
        self._storage: List[Dict[str, Any]] = []
        self.rng = random.Random(seed)
        self.collate_fn = collate_fn or collate_graph_samples

    # ----------------------- public API ----------------------- #
    def add(self, sample: Dict[str, Any]) -> None:
        """단일 `sample` 을 버퍼에 추가."""
        self._validate_sample(sample)
        self._insert(sample)

    def extend(self, samples: Sequence[Dict[str, Any]]) -> None:
        """여러 샘플을 한꺼번에 추가."""
        for s in samples:
            self.add(s)

    def sample(
        self,
        batch_size: int,
        *,
        as_collated: bool = True,
    ) -> Dict[str, Any] | List[Dict[str, Any]]:
        """
        랜덤(또는 서브클래스 정의 방식) 추출.

        Returns
        -------
        collated : dict | list
            * `as_collated=True`  → collate_fn(dict)
            * `as_collated=False` → 샘플 리스트
        """
        if batch_size < 1:
            raise ValueError("batch_size must be positive.")

        if len(self) == 0:
            warnings.warn("Sampling from an **empty** replay buffer.", RuntimeWarning)
            return self.collate_fn([]) if as_collated else []

        indices = self._sample_indices(batch_size)
        samples = [self._storage[i] for i in indices]

        return self.collate_fn(samples) if as_collated else samples

    # ---------------------- state IO -------------------------- #
    def state_dict(self) -> Dict[str, Any]:
        """Checkpoint용 – RNG state와 저장 샘플을 dict 로 반환."""
        return {
            "capacity": self.capacity,
            "storage": self._storage,
            "rng_state": self.rng.getstate(),
        }

    def load_state_dict(self, state: Dict[str, Any]) -> None:
        """Checkpoint 로드."""
        self.capacity = state["capacity"]
        self._storage = list(state["storage"])
        self.rng.setstate(state["rng_state"])

    # -------------------- convenience ------------------------- #
    def clear(self) -> None:
        """버퍼 초기화(샘플 모두 제거)."""
        self._storage.clear()

    def __len__(self) -> int:  # noqa: D401
        """현재 저장된 샘플 수."""
        return len(self._storage)

    # -------------------- protected --------------------------- #
    @staticmethod
    def _validate_sample(sample: Dict[str, Any]) -> None:
        if "data" not in sample or "y" not in sample:
            raise KeyError("Sample dict must contain at least 'data' and 'y' keys.")

    # ------ 아래 두 메서드를 상속 클래스에서 필수 구현 ------ #
    @abstractmethod
    def _insert(self, sample: Dict[str, Any]) -> None:
        """저장 구조에 sample 삽입 (capacity 관리 포함)."""

    @abstractmethod
    def _sample_indices(self, k: int) -> List[int]:
        """`k` 개 인덱스를 반환(중복 허용 X)."""


# --------------------------------------------------------------------------- #
# Naïve (FIFO) 구현 예시 – Reference
# --------------------------------------------------------------------------- #
class FifoBuffer(BaseReplayBuffer):
    """가장 간단한 FIFO(Queue) 예시. capacity 초과 시 맨 앞 삭제."""

    def _insert(self, sample: Dict[str, Any]) -> None:
        if self.capacity is not None and len(self._storage) >= self.capacity:
            # 맨 앞 제거
            self._storage.pop(0)
        self._storage.append(sample)

    def _sample_indices(self, k: int) -> List[int]:
        k = min(k, len(self._storage))
        return self.rng.sample(range(len(self._storage)), k)
