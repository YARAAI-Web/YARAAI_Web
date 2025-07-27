"""
auto_aug.rewarders
==================
AutoAug 탐색용 **보상 함수(Rewarder)** 모듈.

● 클래스
    • BaseRewarder            – 추상 베이스
    • AlignmentReward         – "Alignment ↓, Uniformity ↓" 를 한 점수로
    • ContrastiveLossReward   – NT-Xent(InfoNCE) Loss ↓

공통 초기화 인자
----------------
    encoder      : nn.Module
    data_loader  : torch.utils.data.DataLoader
    device       : torch.device | str
    subset_ratio : float (0~1)  ← 1 == 전체 batch 소비, 0.1 == 10 %

사용 예시
---------
>>> rewarder = AlignmentReward(
...     encoder=model,
...     data_loader=val_loader,
...     device="cuda",
... )
>>> policy, logp, ent = controller.sample_policy()
>>> r = rewarder(policy)   # float 보상
"""

from __future__ import annotations

import math
from abc import ABC, abstractmethod
from typing import List, Sequence

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

from augment import build_view
from augment.base import AugmentBase


# ──────────────────────────────────────────────────────────────
# 1. 추상 베이스
# ──────────────────────────────────────────────────────────────
class BaseRewarder(ABC):
    """AutoAug 탐색에서 policy(ops 리스트)를 → scalar reward 로 변환."""

    def __init__(
        self,
        encoder: torch.nn.Module,
        data_loader: DataLoader,
        device: str | torch.device = "cpu",
        subset_ratio: float = 1.0,
    ) -> None:
        self.encoder = encoder.to(device)
        self.data_loader = data_loader
        self.device = torch.device(device)
        self.subset_ratio = max(0.0, min(1.0, subset_ratio))

    # ---------------------------------------------------------
    # Template: policy_ops → reward(float)
    # ---------------------------------------------------------
    def __call__(self, policy_ops: List[AugmentBase]) -> float:
        self.encoder.eval()
        reward_sum, num_batches = 0.0, 0

        # subset_ratio < 1 이면 일부 batch 무작위 샘플
        tot_batches = len(self.data_loader)
        take_batches = max(1, int(tot_batches * self.subset_ratio))
        batch_indices = (
            torch.randperm(tot_batches)[:take_batches].tolist()
            if self.subset_ratio < 1.0
            else range(tot_batches)
        )

        with torch.no_grad():
            for i, batch in enumerate(tqdm(self.data_loader, disable=True)):
                if i not in batch_indices:
                    continue
                reward_sum += self._batch_reward(batch, policy_ops)
                num_batches += 1

        return reward_sum / num_batches

    # ---------------------------------------------------------
    # 하위 클래스가 구현해야 할 부분
    # ---------------------------------------------------------
    @abstractmethod
    def _batch_reward(
        self,
        batch,
        policy_ops: Sequence[AugmentBase],
    ) -> float: ...


# ──────────────────────────────────────────────────────────────
# 2. Alignment + Uniformity 보상
# ──────────────────────────────────────────────────────────────
class AlignmentReward(BaseRewarder):
    r"""
    Wang et al.(ICML 2020) GraphCL 지표

    Align = E [‖z₁ − z₂‖₂²]              (작을수록 좋음)
    Uni.  = E [exp(−2‖z‖₂²)] (전체 임베딩 분포) (작을수록 좋음)

    reward =  − (α · Align + β · Uni)

    기본 α=1, β=1.
    """

    def __init__(
        self,
        encoder: torch.nn.Module,
        data_loader: DataLoader,
        device: str | torch.device = "cpu",
        subset_ratio: float = 1.0,
        alpha: float = 1.0,
        beta: float = 1.0,
    ):
        super().__init__(encoder, data_loader, device, subset_ratio)
        self.alpha = alpha
        self.beta = beta

    # ---------------------------------------------------------
    # 내부 계산
    # ---------------------------------------------------------
    def _batch_reward(self, batch, policy_ops) -> float:
        # graph batch to device (PyG Data/HeteroData ↔ custom collate assumed)
        batch = batch.to(self.device) if hasattr(batch, "to") else batch

        # (1) 뷰 생성
        view_gen = build_view("StandardPair", ops_a=policy_ops, ops_b=policy_ops)
        g1, g2 = view_gen(batch)

        # (2) 임베딩
        z1 = self.encoder(g1)
        z2 = self.encoder(g2)

        # (3) Alignment
        align = (z1 - z2).pow(2).sum(dim=1).mean()

        # (4) Uniformity
        z_all = torch.cat([z1, z2], dim=0)
        sq_norm = z_all.pow(2).sum(dim=1)
        uni = torch.exp(-2 * sq_norm).mean()

        return -(self.alpha * align.item() + self.beta * uni.item())


# ──────────────────────────────────────────────────────────────
# 3. NT-Xent(Contrastive) Loss 보상
# ──────────────────────────────────────────────────────────────
class ContrastiveLossReward(BaseRewarder):
    """
    NT-Xent (SimCLR / GraphCL) Loss ↓ = Reward ↑

    reward =  − NT-XentLoss
    """

    def __init__(
        self,
        encoder: torch.nn.Module,
        data_loader: DataLoader,
        device: str | torch.device = "cpu",
        subset_ratio: float = 1.0,
        temperature: float = 0.2,
    ):
        super().__init__(encoder, data_loader, device, subset_ratio)
        self.temperature = temperature

    # ---------------------------------------------------------
    # InfoNCE / NT-Xent
    # ---------------------------------------------------------
    def _nt_xent(self, z1: torch.Tensor, z2: torch.Tensor) -> torch.Tensor:
        """Batch-wise NT-Xent loss (SimCLR style)."""
        z = F.normalize(torch.cat([z1, z2], dim=0), dim=1)  # (2B,D)
        sim = torch.mm(z, z.t()) / self.temperature          # cosine sim / τ
        B = z1.size(0)
        mask = torch.eye(2 * B, dtype=torch.bool, device=z.device)
        sim = sim.masked_fill_(mask, -9e15)

        # positive pairs: diag(B, B)
        pos = torch.cat(
            [torch.diag(sim, B), torch.diag(sim, -B)], dim=0
        )  # (2B,)
        loss = -pos + torch.logsumexp(sim, dim=1)
        return loss.mean()

    # ---------------------------------------------------------
    # 내부 계산
    # ---------------------------------------------------------
    def _batch_reward(self, batch, policy_ops) -> float:
        batch = batch.to(self.device) if hasattr(batch, "to") else batch
        view_gen = build_view("StandardPair", ops_a=policy_ops, ops_b=policy_ops)
        g1, g2 = view_gen(batch)

        z1 = self.encoder(g1)
        z2 = self.encoder(g2)
        loss = self._nt_xent(z1, z2)
        return -loss.item()  # Loss ↓ → Reward ↑


__all__ = [
    "BaseRewarder",
    "AlignmentReward",
    "ContrastiveLossReward",
]
