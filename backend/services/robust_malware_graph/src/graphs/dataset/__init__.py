"""
src.graphs.dataset
==================

공개 API
--------
from graphs.dataset import (
    GraphDataset,      # PyTorch Dataset 래퍼
    split_by_time,     # 시간 기반 train/val/test 분할
    split_random,      # stratified k-fold 기반 분할
)

빠른 예시
~~~~~~~~
>>> ds = GraphDataset("/data/robust", split="train")
>>> train_loader = DataLoader(ds, batch_size=4,
...                           collate_fn=GraphDataset.collate_fn)

>>> # meta.csv 를 이용해 시계열 분할
>>> split_by_time(Path("meta.csv"), Path("graphs"), Path("splits"),
...               cut_date="2024-06-01", val_ratio=0.1, test_ratio=0.1)
"""

from __future__ import annotations

from typing import List

try:  # optional heavy dependency on torch
    from .graph_dataset import GraphDataset, collect_dataset_metadata
except Exception:  # pragma: no cover - optional
    GraphDataset = None  # type: ignore
    def collect_dataset_metadata(*args, **kwargs):  # type: ignore
        raise ImportError("GraphDataset requires torch and related packages")
from .split_generator import split_by_time, split_random

__all__: List[str] = [
    "GraphDataset",
    "collect_dataset_metadata",
    "split_by_time",
    "split_random",
]
