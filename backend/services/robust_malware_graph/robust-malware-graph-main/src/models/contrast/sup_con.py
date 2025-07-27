# SPDX-License-Identifier: MIT
"""sup_con.py
====================
Supervised Contrastive Head (SupCon)
-----------------------------------
This module provides a **SupContrastHead** class implementing the Supervised
Contrastive loss (a.k.a. NT‑Xent with label positives) as proposed by Khosla et
al., *Supervised Contrastive Learning*, NeurIPS 2020.

It is designed to receive **graph‑level embeddings** produced by
``SelfGraphCL``/``RGCNEncoder`` (shape ``[B, in_dim]``) together with the
sample labels and return the loss needed for fine‑tuning.

Key features
~~~~~~~~~~~~
* Supports **single‑label** and **multi‑label** classification scenarios.
* Optional **projection MLP** (1‑layer by default) before similarity
  calculation.
* Temperature τ is a learnable parameter by default (set
  ``learnable_temp=False`` to fix it).
* Handles uneven class distributions; samples with *no* positives are masked
  out of the loss to avoid ``nan``.

Example
~~~~~~~
>>> head = SupContrastHead(in_dim=256, proj_dim=128)
>>> z = torch.randn(32, 256)           # embeddings
>>> y = torch.randint(0, 5, (32,))     # labels (int)
>>> loss = head(z, y)

"""
from __future__ import annotations

from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F

__all__ = [
    "SupContrastHead",
]


def _normalize(tensor: torch.Tensor) -> torch.Tensor:
    """L2‑normalize the last dimension."""
    return F.normalize(tensor, p=2.0, dim=-1, eps=1e-12)


class SupContrastHead(nn.Module):
    """Supervised contrastive head.

    Parameters
    ----------
    in_dim : int
        Dimensionality of input embeddings ``z``.
    proj_dim : int, default 128
        Dimensionality of projection head output.  ``proj_dim == in_dim`` will
        skip the projection layer.
    temperature : float, default 0.07
        Initial temperature for NT‑Xent loss.
    learnable_temp : bool, default True
        If *True* the temperature becomes a learnable scalar parameter.
    """

    def __init__(
        self,
        in_dim: int,
        proj_dim: int = 128,
        temperature: float = 0.07,
        *,
        learnable_temp: bool = True,
    ) -> None:
        super().__init__()

        self.use_proj = proj_dim != in_dim
        if self.use_proj:
            self.proj = nn.Sequential(
                nn.Linear(in_dim, proj_dim, bias=False),
                nn.GELU(),
                nn.Linear(proj_dim, proj_dim, bias=False),
            )
            out_dim = proj_dim
        else:
            self.proj = nn.Identity()
            out_dim = in_dim

        self.temperature = nn.Parameter(torch.tensor(temperature)) if learnable_temp else torch.tensor(temperature)
        self.out_dim: int = out_dim  # exposed for downstream modules

    # ---------------------------------------------------------------------
    # Public API
    # ---------------------------------------------------------------------
    def forward(
        self,
        z: torch.Tensor,
        y: torch.Tensor,
        mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:  # returns loss only
        """Compute supervised contrastive loss.

        Parameters
        ----------
        z : torch.Tensor
            Input embeddings of shape ``[B, in_dim]``.
        y : torch.Tensor
            Labels.  *Single‑label*: shape ``[B]`` with dtype long/int.
            *Multi‑label*: shape ``[B, L]`` with dtype bool / float.
        mask : torch.Tensor | None, optional
            Optional binary mask of shape ``[B]`` indicating which samples to
            include (1include).  Useful for ignoring padded / invalid inputs.
        Returns
        -------
        torch.Tensor
            A scalar loss tensor.
        """
        if z.dim() != 2:
            raise ValueError(f"Expected z shape [B, D], got {z.shape}")
        if y is None:
            raise ValueError("Labels are required for supervised contrastive loss")
        if z.size(0) != y.size(0):
            raise ValueError("z and y must have the same batch size")
        if mask is not None:
            if mask.dim() != 1:
                raise ValueError("mask shape must be [B]")
            if mask.size(0) != z.size(0):
                raise ValueError("mask must have the same batch size as z")

        device = z.device
        z = _normalize(self.proj(z))  # [B, d]
        B = z.size(0)

        # ------------------------------------------------------------------
        # Build positive‑pair mask M ∈ {0,1}^{B×B}
        # ------------------------------------------------------------------
        with torch.no_grad():
            if y.dim() == 1:  # single‑label
                # y[:,None] == y[None,:] : broadcast compare
                M = (y.unsqueeze(0) == y.unsqueeze(1)).to(device)  # [B, B]
            elif y.dim() == 2:  # multi‑label (binary‑indicator matrix)
                # Consider positive if intersection is non‑empty
                M = (y @ y.T) > 0  # [B, B]
            else:
                raise ValueError("Unsupported y shape – expect [B] or [B,L]")

            # Exclude self‑contrast
            M.fill_diagonal_(False)

            if mask is not None:
                mask = mask.to(torch.bool)
                M &= mask.unsqueeze(0) & mask.unsqueeze(1)

        # ------------------------------------------------------------------
        # Compute similarity logits
        # ------------------------------------------------------------------
        sim = torch.div(torch.matmul(z, z.T), self.temperature)  # [B, B]
        # For numerical stability – subtract max per‑row
        sim = sim - torch.max(sim, dim=1, keepdim=True)[0].detach()

        # ------------------------------------------------------------------
        # Loss: average over *anchor* samples having ≥1 positive.
        # ------------------------------------------------------------------
        exp_sim = torch.exp(sim)  # [B, B]
        denom = exp_sim.sum(dim=1) - 1.0  # subtract self term which has exp(0)=1
        denom = denom.clamp_min(1e-9)

        # Numerator: sum over positives for each anchor
        pos_exp = (exp_sim * M).sum(dim=1)

        # Filter anchors with at least one positive
        valid_anchor = pos_exp > 0
        if not valid_anchor.any():
            # Should rarely happen, fallback to zero loss to keep graph
            return torch.zeros([], device=device, requires_grad=True)

        loss = -torch.log(pos_exp[valid_anchor] / denom[valid_anchor]).mean()
        return loss

    # ------------------------------------------------------------------
    # Optional utility
    # ------------------------------------------------------------------
    @torch.no_grad()
    def embed(self, z: torch.Tensor) -> torch.Tensor:
        """Return *normalized* projection output for inference/visualisation."""
        return _normalize(self.proj(z))
