# src/models/gnn/heads/regression_head.py
#
# ┌───────────────────────────────────────────────────────────────┐
# │ Regression MLP Head                                          │
# │  Linear(in_dim → hidden_dim) → GELU → Dropout(p)             │
# │                 → Linear(hidden_dim → out_dim)               │
# └───────────────────────────────────────────────────────────────┘

from typing import Optional

import torch
from torch import nn


class RegressionMLPHead(nn.Module):
    """
    연속 값 예측(회귀)용 MLP 헤드.

    ──────────────────────────────────────────────────────────────
        z (B, in_dim)
            │
            ▼
        Linear  in_dim → hidden_dim
            │
          GELU
            │
        Dropout(p)
            │
            ▼
        Linear  hidden_dim → out_dim
            │
            ▼
        ŷ (B, out_dim)
    ──────────────────────────────────────────────────────────────

    Parameters
    ----------
    out_dim : int, default 1
        출력 차원(예: 다중 회귀면 2 이상).
    in_dim : int, default 256
        입력 임베딩 차원.
    hidden_dim : int, default 128
        첫 번째 FC 층 차원.
    dropout : float, default 0.2
        비선형 뒤에 적용할 dropout 확률.
    bias : bool, default True
        선형층 bias 사용 여부.
    """

    def __init__(
        self,
        out_dim: int = 1,
        in_dim: int = 256,
        hidden_dim: int = 128,
        dropout: float = 0.2,
        bias: bool = True,
    ):
        super().__init__()
        if out_dim <= 0:
            raise ValueError("`out_dim` must be a positive integer.")

        self.fc1 = nn.Linear(in_dim, hidden_dim, bias=bias)
        self.act = nn.GELU()
        self.drop = nn.Dropout(dropout) if dropout > 0.0 else nn.Identity()
        self.fc2 = nn.Linear(hidden_dim, out_dim, bias=bias)

        # Xavier 초기화
        for layer in (self.fc1, self.fc2):
            nn.init.xavier_uniform_(layer.weight)
            if bias:
                nn.init.zeros_(layer.bias)

    # ------------------------------------------------------------------ #

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        """
        Parameters
        ----------
        z : Tensor, shape (B, in_dim)

        Returns
        -------
        Tensor
            shape (B, out_dim) — 예측 연속값.
        """
        h = self.act(self.fc1(z))
        h = self.drop(h)
        return self.fc2(h)  # (B, out_dim)

    # ------------------------------------------------------------------ #

    @torch.no_grad()
    def predict(self, z: torch.Tensor) -> torch.Tensor:
        """
        추론 단계 편의 메서드 (그대로 forward 호출).
        """
        return self.forward(z)


# (선택) 프로젝트 레지스트리에 자동 등록
try:
    from . import register_head  # pragma: no cover

    register_head("regression_mlp")(RegressionMLPHead)
except ImportError:
    pass
