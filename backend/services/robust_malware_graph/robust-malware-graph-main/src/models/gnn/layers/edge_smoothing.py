# src/models/gnn/layers/edge_smoothing.py
"""
EdgeDropSmoothing
=================
그래프의 edge_index (및 선택적 edge_attr)에 **무작위 edge-drop**을 적용해
모델의 **강건성·인증 반경**을 높이는 레이어.

* training=True  → p 확률로 엣지를 삭제
* eval 모드     → 드롭 비활성화(원본 그래프 유지)

Parameters
----------
drop_prob : float, default 0.2
    삭제할 엣지 비율 *p* (0 ≤ p < 1).
force_undirected : bool, default True
    True 면 `torch_geometric.utils.dropout_edge`의 undirected 모드 사용
    (한 쌍의 양방향 엣지를 동시에 드롭).

Notes
-----
- 내부 구현은 `torch_geometric.utils.dropout_edge`를 Thin wrapper 로 호출합니다.
- PyG dependency 가 없을 경우 ImportError 를 발생시켜 조기에 알립니다.
"""

from __future__ import annotations

from typing import Optional, Tuple

import torch
from torch import nn, Tensor

try:
    # → PyG ≥2.4
    from torch_geometric.utils import dropout_edge
except ImportError:  # pragma: no cover
    dropout_edge = None


class EdgeDropSmoothing(nn.Module):
    r"""Random edge dropout layer for robustness smoothing."""

    def __init__(self, drop_prob: float = 0.2, force_undirected: bool = True):
        super().__init__()
        if not (0.0 <= drop_prob < 1.0):
            raise ValueError("`drop_prob` must be in the range [0, 1).")
        self.drop_prob = float(drop_prob)
        self.force_undirected = bool(force_undirected)

    # ------------------------------------------------------------------ #

    def forward(
        self,
        edge_index: Tensor,
        edge_attr: Optional[Tensor] = None,
        *,
        drop_prob: Optional[float] = None,
        training: Optional[bool] = None,
    ) -> Tuple[Tensor, Optional[Tensor]]:
        """
        Parameters
        ----------
        edge_index : Tensor, shape (2, E)
            COO-format edge indices.
        edge_attr : Tensor | None, shape (E, F)
            엣지 특성 행렬(선택).
        drop_prob : float | None, optional
            None → self.drop_prob 사용.
        training : bool | None, optional
            None → self.training 플래그 사용.

        Returns
        -------
        (edge_index', edge_attr')
            드롭 후 엣지 인덱스와 특성.
        """
        if dropout_edge is None:  # pragma: no cover
            raise ImportError(
                "EdgeDropSmoothing requires 'torch_geometric'. "
                "Install via `pip install torch-geometric`."
            )

        p = self.drop_prob if drop_prob is None else float(drop_prob)
        is_training = self.training if training is None else bool(training)

        # eval 모드 또는 p==0 → 원본 유지
        if not is_training or p <= 0.0:
            return edge_index, edge_attr

        # PyG util 호출 (mask 계산 & sub-index 생성)
        out_index, edge_mask = dropout_edge(
            edge_index,
            p=p,
            force_undirected=self.force_undirected,
            training=True,
        )
        out_attr = edge_attr[edge_mask] if edge_attr is not None else None
        return out_index, out_attr

    # ------------------------------------------------------------------ #

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"{self.__class__.__name__}(drop_prob={self.drop_prob}, "
            f"force_undirected={self.force_undirected})"
        )
