# SPDX-License-Identifier: MIT
"""self_gcl.py
========================================
Self‑Supervised Graph Contrastive Wrapper
----------------------------------------
This module implements **SelfGraphCL**, a reusable PyTorch‐Geometric wrapper
for *Graph Contrastive Learning* (GraphCL, ICML 2020).  It receives *two*
randomly augmented views of the **same hetero‑graph** and optimises the
InfoNCE loss so that the corresponding graph‑level embeddings are pulled
together while the rest of the batch is pushed apart.

Key Features
~~~~~~~~~~~~
* Embedding backbone remains **pluggable** – pass any ``nn.Module`` that maps a
  :class:`torch_geometric.data.Batch` to a tensor of shape ``[B, emb_dim]``.
* Lightweight **projection head** (MLP → L2‑normalise) as in SimCLR.
* Handles **distributed** training out‑of‑the‑box (optionally gathers
  representations from other GPUs before computing the similarity matrix).
* Gracefully degrades when the batch size is 1 (returns zero loss).

Example
-------
>>> encoder = RGCNEncoder(in_dim=128, hidden_dim=256, num_layers=3)
>>> gcl = SelfGraphCL(encoder)
>>> loss_dict = gcl(g1_batch, g2_batch)   # two augmented views
>>> loss_dict['loss'].backward()
"""
from __future__ import annotations

import math
from typing import Dict, Optional, Tuple

import torch
from torch import Tensor, nn
import torch.nn.functional as F
from torch_geometric.data import Batch

__all__ = [
    "SelfGraphCL",
]


# ---------------------------------------------------------------------------
# Helper: NT‑Xent / InfoNCE
# ---------------------------------------------------------------------------

def _info_nce(z1: Tensor, z2: Tensor, temperature: float = 0.2) -> Tensor:
    """Return **scalar** InfoNCE loss for two batches of *paired* embeddings.

    Args
    ----
    z1, z2: ``[B, D]`` tensors (already *row‑wise* L2 normalised).  **Same
        graph** appears at the *same index* across the two views.
    temperature: Softmax temperature in **radians**.  Lower → tougher positives.
    """
    assert z1.shape == z2.shape, "z1 / z2 must share shape"
    bsz = z1.size(0)
    if bsz == 0:
        raise ValueError("Empty batch")
    if bsz == 1:
        # Contrastive loss is undefined for batch=1; return 0 to avoid NaN
        return z1.new_zeros(())

    # Cosine similarity matrix: each view against concat(z1,z2) → [B, 2B]
    z = torch.cat([z1, z2], dim=0)  # [2B, D]
    sim = F.cosine_similarity(z1.unsqueeze(1), z.unsqueeze(0), dim=-1) / temperature  # [B, 2B]
    sim2 = F.cosine_similarity(z2.unsqueeze(1), z.unsqueeze(0), dim=-1) / temperature  # [B, 2B]

    # Positive logits are the *other* view at same index
    pos_idx = torch.arange(bsz, device=z1.device)
    pos_logits_1 = sim.gather(1, pos_idx.view(-1, 1) + bsz)  # z1 vs z2
    pos_logits_2 = sim2.gather(1, pos_idx.view(-1, 1))        # z2 vs z1

    # Denominator: all 2B samples (incl. positive) – same as SimCLR
    loss_1 = -torch.log(torch.exp(pos_logits_1) / sim.exp().sum(dim=1, keepdim=True))
    loss_2 = -torch.log(torch.exp(pos_logits_2) / sim2.exp().sum(dim=1, keepdim=True))

    return (loss_1.mean() + loss_2.mean()) * 0.5


# ---------------------------------------------------------------------------
# Projection head
# ---------------------------------------------------------------------------

class _ProjHead(nn.Module):
    """2‑layer MLP → BatchNorm → l2‑norm as used in SimCLR."""

    def __init__(self, in_dim: int, out_dim: int = 256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, in_dim, bias=False),
            nn.BatchNorm1d(in_dim),
            nn.ReLU(inplace=True),
            nn.Linear(in_dim, out_dim, bias=True),
        )

    def forward(self, x: Tensor) -> Tensor:  # noqa: D401
        x = self.net(x)
        return F.normalize(x, p=2, dim=1)


# ---------------------------------------------------------------------------
# Main module
# ---------------------------------------------------------------------------

class SelfGraphCL(nn.Module):
    """Supervised Graph Contrastive Learning wrapper."""

    def __init__(
        self,
        encoder: nn.Module,
        *,
        proj_dim: int = 256,
        temperature: float = 0.2,
        gather_distributed: bool = False,
    ) -> None:
        """Parameters
        ----------
        encoder
            **Backbone GNN** that maps :class:`torch_geometric.data.Batch`
            → ``[B, D]`` graph‑level embedding.
        proj_dim
            Output dimension of the projection head.
        temperature
            Temperature τ in InfoNCE; commonly 0.1–0.5.
        gather_distributed
            If *True*, embeddings are gathered across GPUs before loss calc.
        """
        super().__init__()
        self.encoder = encoder
        # Infer embed size by a quick dummy forward (lazy resolution)
        self._proj_head: Optional[_ProjHead] = None
        self.proj_dim = proj_dim
        self.temperature = temperature
        self.gather_distributed = gather_distributed

    # ---------------------------------------------------------------------
    # Private helpers
    # ---------------------------------------------------------------------

    def _maybe_build_head(self, emb: Tensor) -> None:
        if self._proj_head is None:
            self._proj_head = _ProjHead(emb.size(-1), self.proj_dim).to(emb.device)

    @staticmethod
    def _distributed_gather(x: Tensor) -> Tensor:  # noqa: D401
        if not torch.distributed.is_initialized():
            return x
        # All‑gather without gradients to save memory
        xs = [torch.zeros_like(x) for _ in range(torch.distributed.get_world_size())]
        torch.distributed.all_gather(xs, x.contiguous())
        return torch.cat(xs, dim=0)

    # ---------------------------------------------------------------------
    # Forward
    # ---------------------------------------------------------------------

    def forward(self, g1: Batch, g2: Batch, *, return_emb: bool = False) -> Dict[str, Tensor]:
        """Compute InfoNCE loss between *two augmented views* of a graph batch.

        Returns a dict with at least **'loss'** and, if *return_emb* is True,
        also **'emb'** containing the *projected* representation (for logging).
        """
        # Graph‑to‑embedding
        z1_raw = self.encoder(g1)  # [B, D]
        z2_raw = self.encoder(g2)  # [B, D]

        # Lazy projection head build
        self._maybe_build_head(z1_raw)
        assert self._proj_head is not None  # for mypy
        z1 = self._proj_head(z1_raw)
        z2 = self._proj_head(z2_raw)

        # Optionally gather across GPUs
        if self.gather_distributed:
            z1 = SelfGraphCL._distributed_gather(z1)
            z2 = SelfGraphCL._distributed_gather(z2)

        loss = _info_nce(z1, z2, self.temperature)
        out: Dict[str, Tensor] = {"loss": loss}
        if return_emb:
            out["emb"] = torch.cat([z1, z2], dim=0)
        return out

    # ---------------------------------------------------------------------
    # Convenience: Encoder‐only inference
    # ---------------------------------------------------------------------

    @torch.no_grad()
    def encode(self, g: Batch) -> Tensor:  # noqa: D401
        """Return *raw* graph embeddings without contrastive projection."""
        return self.encoder(g)
