# src/models/gnn/heads/multi_label_head.py
from typing import Optional

import torch
from torch import nn


class MultiLabelMLPHead(nn.Module):
    """
    다중 라벨(Multi-Label) 분류 헤드.

        Linear(in_dim → hidden_dim) ──► GELU ──► Dropout(p)
                                          └──► Linear(hidden_dim → num_classes)

    각 클래스별 로짓에 시그모이드를 씌워 독립 확률을 반환합니다.

    Parameters
    ----------
    in_dim : int, default 256
        입력 임베딩 차원.
    num_classes : int
        예측할 라벨 수.
    hidden_dim : int, default 128
        첫 번째 FC 층의 출력 차원.
    dropout : float, default 0.2
        비선형 뒤에 적용할 dropout 확률.
    bias : bool, default True
        선형층 bias 사용 여부.
    """

    def __init__(
        self,
        num_classes: int,
        in_dim: int = 256,
        hidden_dim: int = 128,
        dropout: float = 0.2,
        bias: bool = True,
    ):
        super().__init__()
        if num_classes <= 0:
            raise ValueError("`num_classes` must be a positive integer.")

        self.fc1 = nn.Linear(in_dim, hidden_dim, bias=bias)
        self.act = nn.GELU()
        self.drop = nn.Dropout(dropout) if dropout > 0.0 else nn.Identity()
        self.fc2 = nn.Linear(hidden_dim, num_classes, bias=bias)

        # Xavier 초기화
        for m in (self.fc1, self.fc2):
            nn.init.xavier_uniform_(m.weight)
            if bias:
                nn.init.zeros_(m.bias)

    def forward(
        self,
        z: torch.Tensor,
        *,
        return_logits: bool = False,
    ) -> torch.Tensor:
        """
        Parameters
        ----------
        z : Tensor, shape (B, in_dim)
        return_logits : bool, default False
            True면 σ 적용 전 로짓 반환.

        Returns
        -------
        Tensor
            shape (B, C) — σ 확률(또는 로짓).
        """
        x = self.act(self.fc1(z))
        x = self.drop(x)
        logits = self.fc2(x)  # (B, C)
        if return_logits:
            return logits
        return torch.sigmoid(logits)

    @torch.no_grad()
    def predict(
        self,
        z: torch.Tensor,
        threshold: float = 0.5,
    ) -> torch.Tensor:
        """
        확률값을 threshold 기준 0/1 레이블로 변환.

        Returns
        -------
        Tensor
            shape (B, C) — {0,1} 정수형.
        """
        probs = self.forward(z)
        return (probs >= threshold).long()


# (선택) 레지스트리 등록
try:
    from . import register_head  # pragma: no cover

    register_head("multi_label_mlp")(MultiLabelMLPHead)
except ImportError:
    pass
