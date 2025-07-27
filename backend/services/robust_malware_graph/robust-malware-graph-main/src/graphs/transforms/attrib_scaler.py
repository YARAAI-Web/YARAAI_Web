"""
src.graphs.transforms.attrib_scaler
===================================

AttributeScaler
---------------
‣ 그래프 노드·엣지 **연속형 텐서 속성**을 학습-친화적 범위로 변환.

기능
~~~~
• fit(graphs, attr_keys)     : μ/σ 또는 min/max 추정
• transform(graph)           : in-place 스케일
• inverse_transform(graph)   : 원래 값 복원
• quantize(graph, bits=8/16) : 0–255 / 0–65535 정수 양자화

지원 모드
~~~~~~~~
mode = {"standard", "minmax"}

사용 예
~~~~~~
>>> scaler = AttributeScaler(mode="standard")
>>> scaler.fit(train_graphs, attr_keys=["x", "feat"])
>>> g = scaler.transform(g)
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Dict, Iterable, List, Literal, Sequence

import torch
from torch_geometric.data import Data, HeteroData

from ..utils import get_logger

GraphT = Data | HeteroData
Mode = Literal["standard", "minmax"]

_LOG = get_logger("transforms.scaler")


class AttributeScaler:
    """
    Parameters
    ----------
    mode : {'standard','minmax'}
    eps  : float, default 1e-6
        분모 0 방지 값.
    """

    def __init__(self, mode: Mode = "standard", eps: float = 1e-6) -> None:
        self.mode = mode
        self.eps = eps
        # 통계 {attr_key: (mean, std)} or (min, max)
        self.stats: Dict[str, tuple[torch.Tensor, torch.Tensor]] = {}

    # ------------------------------------------------------------------ #
    # 통계 적합
    # ------------------------------------------------------------------ #
    def fit(self, graphs: Iterable[GraphT], *, attr_keys: Sequence[str]) -> "AttributeScaler":
        sums, sq_sums, counts = {}, {}, {}
        mins, maxs = {}, {}

        for g in graphs:
            stores = [g] if isinstance(g, Data) else [g[nt] for nt in g.node_types]
            for st in stores:
                for k in attr_keys:
                    if k not in st:
                        continue
                    v = st[k].float()
                    if self.mode == "standard":
                        sums[k] = sums.get(k, 0.0) + v.sum(dim=0)
                        sq_sums[k] = sq_sums.get(k, 0.0) + (v**2).sum(dim=0)
                        counts[k] = counts.get(k, 0) + v.size(0)
                    else:  # minmax
                        mins[k] = torch.minimum(mins.get(k, v[0]), v.min(dim=0).values)
                        maxs[k] = torch.maximum(maxs.get(k, v[0]), v.max(dim=0).values)

        for k in attr_keys:
            if self.mode == "standard":
                mean = sums[k] / counts[k]
                var = sq_sums[k] / counts[k] - mean**2
                std = torch.sqrt(torch.clamp(var, min=self.eps))
                self.stats[k] = (mean, std)
            else:
                self.stats[k] = (mins[k], maxs[k])

        _LOG.info("AttributeScaler fit done: %s", {k: tup[0].shape for k, tup in self.stats.items()})
        return self

    # ------------------------------------------------------------------ #
    # 변환 / 역변환
    # ------------------------------------------------------------------ #
    def _apply(self, g: GraphT, inverse: bool = False) -> GraphT:
        stores = [g] if isinstance(g, Data) else [g[nt] for nt in g.node_types]
        for st in stores:
            for k, (a, b) in self.stats.items():
                if k not in st:
                    continue
                v = st[k].float()
                if self.mode == "standard":
                    st[k] = (v * b + a) if inverse else (v - a) / (b + self.eps)
                else:  # minmax
                    st[k] = v * (b - a + self.eps) + a if inverse else (v - a) / (b - a + self.eps)
        return g

    def transform(self, g: GraphT) -> GraphT:
        return self._apply(g, inverse=False)

    def inverse_transform(self, g: GraphT) -> GraphT:
        return self._apply(g, inverse=True)

    # ------------------------------------------------------------------ #
    # 양자화
    # ------------------------------------------------------------------ #
    @staticmethod
    def quantize(g: GraphT, *, bits: int = 8, attr_keys: Sequence[str] = ("x",)) -> GraphT:
        qmax = 2**bits - 1
        stores = [g] if isinstance(g, Data) else [g[nt] for nt in g.node_types]
        for st in stores:
            for k in attr_keys:
                if k in st:
                    v = st[k]
                    v = torch.clamp(v, 0, 1)  # assume scaled [0,1]
                    st[k] = (v * qmax).round().to(torch.uint8 if bits == 8 else torch.int16)
        return g

    # ------------------------------------------------------------------ #
    # 저장 / 로드
    # ------------------------------------------------------------------ #
    def save(self, path: Path) -> None:
        torch.save({"mode": self.mode, "stats": self.stats}, path)

    @classmethod
    def load(cls, path: Path) -> "AttributeScaler":
        obj = torch.load(path, weights_only=False)
        inst = cls(mode=obj["mode"])
        inst.stats = obj["stats"]
        return inst
