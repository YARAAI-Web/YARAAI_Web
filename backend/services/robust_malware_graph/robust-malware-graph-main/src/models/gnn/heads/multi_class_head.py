# src/models/gnn/heads/multi_class_head.py
#
# ┌───────────────────────────────────────────────────────────────┐
# │ Multi-Class MLP Head                                         │
# │  Linear(in_dim → hidden_dim) → GELU → Dropout(p)             │
# │                 → Linear(hidden_dim → num_classes)           │
# └───────────────────────────────────────────────────────────────┘

from typing import Optional

import torch
from torch import nn
import torch.nn.functional as F


class MultiClassMLPHead(nn.Module):
    """
    다중 클래스(Multi-Class) 분류용 MLP 헤드.

    Forward 시 두 층(Linear → GELU → Dropout → Linear)으로 로짓을 만든 뒤
    • `return_logits=False` → softmax 확률 반환
    • `return_logits=True`  → 원본 로짓 반환

    Notes
    -----
    * 학습 단계에서 CrossEntropyLoss(=`logits`) 사용을 권장합니다.
    * `predict`는 argmax(class id)만 반환합니다.

    Parameters
    ----------
    num_classes : int
        예측할 클래스 수 (≥2).
    in_dim : int, default 256
        입력 임베딩 차원.
    hidden_dim : int, default 128
        첫 번째 FC 층 차원.
    dropout : float, default 0.2
        비선형 이후에 적용할 dropout 확률.
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
        if num_classes < 2:
            raise ValueError("`num_classes`(>=2) is required for multi-class tasks.")

        self.fc1 = nn.Linear(in_dim, hidden_dim, bias=bias)
        self.act = nn.GELU()
        self.drop = nn.Dropout(dropout) if dropout > 0.0 else nn.Identity()
        self.fc2 = nn.Linear(hidden_dim, num_classes, bias=bias)

        # 가중치 초기화(Xavier)
        for layer in (self.fc1, self.fc2):
            nn.init.xavier_uniform_(layer.weight)
            if bias:
                nn.init.zeros_(layer.bias)

    # --------------------------------------------------------------------- #

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
            그래프/샘플 임베딩.
        return_logits : bool, default False
            True → softmax 없이 로짓 반환.

        Returns
        -------
        Tensor
            shape (B, C) – 확률(or 로짓).
        """
        h = self.act(self.fc1(z))
        h = self.drop(h)
        logits = self.fc2(h)  # (B, C)

        if return_logits:
            return logits
        return F.softmax(logits, dim=-1)

    # --------------------------------------------------------------------- #

    @torch.no_grad()
    def predict(self, z: torch.Tensor) -> torch.Tensor:
        """
        Argmax class id 예측 헬퍼. (B,) 정수 텐서 반환.
        """
        logits = self.forward(z, return_logits=True)
        return logits.argmax(dim=-1)


# (선택) 프로젝트 레지스트리에 자동 등록
try:
    from . import register_head  # pragma: no cover

    register_head("multi_class_mlp")(MultiClassMLPHead)
except ImportError:
    pass
