# src/models/gnn/heads/binary_mlp_head.py
from typing import Optional

import torch
from torch import nn


class BinaryMLPHead(nn.Module):
    """
    두 층 MLP(binary) 분류 헤드

        Linear(in_dim → hidden_dim) ──► GELU ──► Dropout(p) ──► Linear(hidden_dim → 1)

    Parameters
    ----------
    in_dim : int, optional (default=256)
        입력 임베딩 차원.
    hidden_dim : int, optional (default=128)
        첫 번째 FC 층의 출력(중간) 차원.
    dropout : float, optional (default=0.2)
        GELU 뒤에 적용할 dropout 확률.
    bias : bool, optional (default=True)
        각 선형층의 bias 사용 여부.
    """

    def __init__(
        self,
        in_dim: int = 256,
        hidden_dim: int = 128,
        dropout: float = 0.2,
        bias: bool = True,
    ):
        super().__init__()

        self.fc1 = nn.Linear(in_dim, hidden_dim, bias=bias)
        self.act = nn.GELU()
        self.drop = nn.Dropout(dropout) if dropout > 0.0 else nn.Identity()
        self.fc2 = nn.Linear(hidden_dim, 1, bias=bias)

        # 가중치 초기화
        for m in (self.fc1, self.fc2):
            nn.init.xavier_uniform_(m.weight)
            if bias:
                nn.init.zeros_(m.bias)

    def forward(self, z: torch.Tensor, *, return_logits: bool = False) -> torch.Tensor:
        """
        Parameters
        ----------
        z : Tensor, shape (B, in_dim)
        return_logits : bool, default False
            True면 σ 이전 raw logit 반환.

        Returns
        -------
        Tensor
            shape (B,) – 확률(또는 로짓).
        """
        x = self.act(self.fc1(z))
        x = self.drop(x)
        logits = self.fc2(x).squeeze(-1)
        if return_logits:
            return logits
        return torch.sigmoid(logits)

    @torch.no_grad()
    def predict(self, z: torch.Tensor, threshold: float = 0.5) -> torch.Tensor:
        """
        확률을 0/1 레이블로 변환하는 헬퍼.
        """
        probs = self.forward(z)
        return (probs >= threshold).long()


# (선택) 프로젝트 레지스트리에 등록
try:
    from . import register_head  # pragma: no cover

    register_head("binary_mlp")(BinaryMLPHead)
except ImportError:
    pass
