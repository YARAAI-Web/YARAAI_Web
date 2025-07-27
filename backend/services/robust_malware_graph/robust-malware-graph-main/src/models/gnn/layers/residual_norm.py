# src/models/gnn/layers/residual_norm.py
"""
ResidualNorm
============

A generic **Add & Norm** wrapper that turns any GNN (or dense) layer into:

    y = Norm( x + Drop( SubLayer(x, …) ) )

Benefits
--------
* Residual connection keeps gradients flowing in deep GNN stacks.
* Normalisation (LayerNorm / BatchNorm) stabilises feature statistics.
* Dropout between them offers regularisation for better generalisation.

Example
-------
>>> from torch_geometric.nn import GCNConv
>>> from src.models.gnn.layers.residual_norm import ResidualNorm
>>>
>>> conv = GCNConv(128, 128)
>>> block = ResidualNorm(conv, in_dim=128, dropout=0.1, norm_type="layer")
>>> y = block(x, edge_index)  # signature transparently mirrors conv
"""

from __future__ import annotations

from typing import Any, Mapping, Tuple

import torch
from torch import nn, Tensor


class ResidualNorm(nn.Module):
    """Add-Drop-Norm wrapper around an arbitrary sub-layer."""

    _NORMS = {
        "layer": nn.LayerNorm,      # feature-wise (per node)
        "batch": nn.BatchNorm1d,    # batch-wise
        "none":  lambda *_: nn.Identity(),
    }

    def __init__(
        self,
        sublayer: nn.Module,
        in_dim: int,
        *,
        dropout: float = 0.0,
        norm_type: str = "layer",
    ):
        """
        Parameters
        ----------
        sublayer : nn.Module
            Layer whose first output is an updated feature tensor.
        in_dim : int
            Feature dimension fed into both sublayer and norm.
        dropout : float, default 0.0
            Dropout *p* applied to sublayer output before residual add.
        norm_type : {"layer", "batch", "none"}, default "layer"
            Normalisation variant applied after the residual addition.
        """
        super().__init__()
        if norm_type not in self._NORMS:
            raise ValueError(f"`norm_type` must be one of {list(self._NORMS)}")

        self.sublayer = sublayer
        self.drop = nn.Dropout(dropout) if dropout > 0.0 else nn.Identity()
        self.norm: nn.Module = self._NORMS[norm_type](in_dim)

    # ------------------------------------------------------------------ #
    def forward(self, x: Tensor | Mapping[str, Tensor], *args: Any, **kwargs: Any):
        """
        Pass-through that keeps the sublayer’s original signature.

        Returns
        -------
        Same as `sublayer`, but the first returned tensor is
        residual-added and normalised.
        """
        out = self.sublayer(x, *args, **kwargs)

        # sublayer may return a Tensor or a tuple; handle both
        if isinstance(out, tuple):
            h, *rest = out
        else:
            h, rest = out, []

        if isinstance(h, Mapping) and isinstance(x, Mapping):
            h = {k: self.drop(v) for k, v in h.items()}
            y = {k: self.norm(x[k] + h[k]) for k in h}
        else:
            h = self.drop(h)
            y = self.norm(x + h)

        return (y, *rest) if rest else y

    # ------------------------------------------------------------------ #
    def extra_repr(self) -> str:  # pragma: no cover
        name = type(self.norm).__name__
        p = self.drop.p if isinstance(self.drop, nn.Dropout) else 0.0
        return f"sublayer={type(self.sublayer).__name__}, norm={name}, dropout={p}"
