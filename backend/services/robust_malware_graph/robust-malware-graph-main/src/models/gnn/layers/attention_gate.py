# src/models/gnn/layers/attention_gate.py
"""
AttentionGate
=============

Light-weight **node / edge gating layer** for PyG-style tensors.

Design goals
------------
* **Plug-and-play** – takes `(x, edge_index[, batch])` and returns gated
  node features plus optional edge weights.
* **Node–level gate**:  σ( **wₙ · xᵢ** )  ∈ (0,1) → xᵢ′ = αᵢ · xᵢ
* **Edge–level gate**:  σ( **wₑ · [xᵢ‖xⱼ]** )  ∈ (0,1) → used as
  attention/edge weight in downstream message passing.
* Single fully-connected layer per gate (cheap) – matches the spec that
  “Linear를 복수로 사용하는 형태”로 구현하며 중요 노드/엣지에 가중치를
  부여하는 역할을 수행합니다.

Parameters
----------
in_dim : int, default 256
    Feature dimension of each node.
node_gate : bool, default True
    Whether to learn node-wise gates.
edge_gate : bool, default True
    Whether to learn edge-wise gates.
edge_share : bool, default True
    Share a single linear layer for both ``(src,dst)`` and ``(dst,src)`` pairs.
    Set ``False`` to learn direction-specific weights with two separate
    projections.
"""

from __future__ import annotations

import torch
from torch import nn, Tensor
from typing import Optional, Tuple


class AttentionGate(nn.Module):
    """Node / edge attention gate layer."""

    def __init__(
        self,
        in_dim: int = 256,
        *,
        node_gate: bool = True,
        edge_gate: bool = True,
        edge_share: bool = True,
    ):
        super().__init__()

        self.node_gate = node_gate
        self.edge_gate = edge_gate
        self.edge_share = edge_share

        if node_gate:
            self.node_fc = nn.Linear(in_dim, 1, bias=True)
            nn.init.xavier_uniform_(self.node_fc.weight)
            nn.init.zeros_(self.node_fc.bias)

        if edge_gate:
            edge_in = in_dim * 2
            if edge_share:
                self.edge_fc = nn.Linear(edge_in, 1, bias=True)
                nn.init.xavier_uniform_(self.edge_fc.weight)
                nn.init.zeros_(self.edge_fc.bias)
            else:
                self.edge_fc_src2dst = nn.Linear(edge_in, 1, bias=True)
                self.edge_fc_dst2src = nn.Linear(edge_in, 1, bias=True)
                for m in (self.edge_fc_src2dst, self.edge_fc_dst2src):
                    nn.init.xavier_uniform_(m.weight)
                    nn.init.zeros_(m.bias)

    # ------------------------------------------------------------------ #
    def forward(
        self,
        x: Tensor,                   # (N, F)
        edge_index: Tensor,          # (2, E)
        batch: Optional[Tensor] = None,
        *,
        return_alpha: bool = False,
    ) -> Tuple[Tensor, Tensor, Optional[Tensor]]:
        """
        Returns
        -------
        x_out : Tensor, shape (N, F)
            Gated node features.
        edge_index : Tensor
            Unchanged if ``edge_share=True``; otherwise concatenated with its
            reversed counterpart resulting in shape ``(2, 2E)``.
        edge_alpha : Tensor | None, shape (E,) or (2E,)
            Edge weights in ``(0, 1)`` if ``edge_gate=True``. When
            ``edge_share=False`` the returned vector contains forward and
            reverse weights consecutively.
        """
        # ------------------- node gate ------------------- #
        if self.node_gate:
            node_alpha = torch.sigmoid(self.node_fc(x)).squeeze(-1)  # (N,)
            x_out = x * node_alpha.unsqueeze(-1)
        else:
            node_alpha = None
            x_out = x

        # ------------------- edge gate ------------------- #
        edge_alpha: Optional[Tensor] = None
        if self.edge_gate:
            src, dst = edge_index
            feat_fwd = torch.cat([x[src], x[dst]], dim=-1)  # (E, 2F)

            if self.edge_share:
                edge_alpha = torch.sigmoid(self.edge_fc(feat_fwd)).squeeze(-1)  # (E,)
            else:
                # forward (src -> dst)
                alpha_fwd = torch.sigmoid(
                    self.edge_fc_src2dst(feat_fwd)
                ).squeeze(-1)  # (E,)

                # reverse (dst -> src)
                feat_rev = torch.cat([x[dst], x[src]], dim=-1)  # (E, 2F)
                alpha_rev = torch.sigmoid(
                    self.edge_fc_dst2src(feat_rev)
                ).squeeze(-1)  # (E,)

                edge_index = torch.cat([edge_index, edge_index.flip(0)], dim=1)  # (2, 2E)
                edge_alpha = torch.cat([alpha_fwd, alpha_rev], dim=0)  # (2E,)
        # ------------------------------------------------- #

        if return_alpha:
            return x_out, node_alpha, edge_alpha
        return x_out, edge_index, edge_alpha

    # ------------------------------------------------------------------ #
    def extra_repr(self) -> str:  # pragma: no cover
        return (
            f"in_dim={self.node_fc.in_features if self.node_gate else '—'}, "
            f"node_gate={self.node_gate}, "
            f"edge_gate={self.edge_gate}, "
            f"edge_share={self.edge_share}"
        )
