# src/models/gnn/layers/gumbel_mask.py
"""
GumbelMask
==========

Learnable **hard 0/1 mask** using the Gumbel-Sigmoid (Binary Concrete)
re-parameterisation with an optional **straight-through (ST) estimator**.

Typical use-cases
-----------------
* Edge / node / feature pruning for robust GNNs
* Differentiable feature selection
* Any scenario needing a Bernoulli sampler that is back-prop-able

Forward behaviour
-----------------
training=True
    ỹ = sigmoid((logits + gumbel) / τ)        # soft (0,1)
    if straight_through:
        y  = (ỹ > 0.5).float()               # hard 0/1
        y += ỹ - ỹ.detach()                 # soft grads
    else:
        y  = ỹ                               # purely soft
training=False
    y  = (logits >= 0).float()                # deterministic hard

Regularisation
--------------
`l0_loss()` returns 𝔼[‖mask‖₀] = σ(logits).
Add λ·`mask.l0_loss().mean()` to the task loss to promote sparsity.

References
----------
* Maddison et al., *The Concrete Distribution* (ICLR 2017)
* Jang et al., *Categorical Reparameterization with Gumbel-Softmax* (ICLR 2017)
"""

from __future__ import annotations

import math
from typing import Tuple

import torch
from torch import nn, Tensor


# -------------------------------------------------------------------------- #
# helpers
# -------------------------------------------------------------------------- #
def _sample_gumbel(shape: Tuple[int, ...], eps: float = 1e-10, *, device=None) -> Tensor:
    """Draw i.i.d. samples from Gumbel(0, 1)."""
    u = torch.rand(shape, device=device)
    return -torch.log(-torch.log(u + eps) + eps)


def _gumbel_sigmoid(logits: Tensor, temperature: float) -> Tensor:
    """Binary Concrete sample in (0, 1)."""
    g = _sample_gumbel(logits.shape, device=logits.device)
    return torch.sigmoid((logits + g) / temperature)


# -------------------------------------------------------------------------- #
# main module
# -------------------------------------------------------------------------- #
class GumbelMask(nn.Module):
    r"""Differentiable 0/1 mask via Gumbel-Sigmoid."""

    def __init__(
        self,
        size: Tuple[int, ...] | int,
        *,
        init_prob: float = 0.5,
        temperature: float = 1.0,
        straight_through: bool = True,
        learnable: bool = True,
    ):
        """
        Parameters
        ----------
        size : int | tuple[int, ...]
            Output mask shape.
        init_prob : float, default 0.5
            Initial Bernoulli probability (0 < p < 1).
        temperature : float, default 1.0
            Gumbel-Sigmoid temperature τ (> 0).
        straight_through : bool, default True
            If True, returns hard mask with ST gradients in training mode.
        learnable : bool, default True
            If False, logits are frozen (useful for fixed masks).
        """
        super().__init__()

        if not (0.0 < init_prob < 1.0):
            raise ValueError("`init_prob` must be in (0, 1).")
        if temperature <= 0.0:
            raise ValueError("`temperature` must be > 0.")

        size = (size,) if isinstance(size, int) else tuple(size)
        logits_init = math.log(init_prob) - math.log(1.0 - init_prob)

        self.logits = nn.Parameter(torch.full(size, logits_init), requires_grad=learnable)
        self.temperature = float(temperature)
        self.straight_through = bool(straight_through)

    # ------------------------------------------------------------------ #
    def forward(self) -> Tensor:
        """Return mask tensor (hard 0/1 or soft (0,1) depending on mode)."""
        if self.training:
            y_soft = _gumbel_sigmoid(self.logits, self.temperature)
            if self.straight_through:
                y_hard = (y_soft > 0.5).float()
                return y_hard + (y_soft - y_soft.detach())  # ST trick
            return y_soft
        # eval: deterministic
        return (self.logits >= 0).float()

    # ------------------------------------------------------------------ #
    # utilities
    # ------------------------------------------------------------------ #
    @torch.no_grad()
    def hard(self) -> Tensor:
        """Deterministic hard mask irrespective of `self.training`."""
        return (self.logits >= 0).float()

    def l0_loss(self) -> Tensor:
        r"""Expected L₀ penalty E[‖mask‖₀] = σ(logits)."""
        return torch.sigmoid(self.logits)

    def set_temperature(self, tau: float) -> None:
        """Update temperature τ (must be > 0)."""
        if tau <= 0.0:
            raise ValueError("temperature must be > 0.")
        self.temperature = float(tau)

    # ------------------------------------------------------------------ #
    def extra_repr(self) -> str:  # pragma: no cover
        return (
            f"size={tuple(self.logits.shape)}, "
            f"τ={self.temperature}, "
            f"ST={self.straight_through}, "
            f"learnable={self.logits.requires_grad}"
        )
