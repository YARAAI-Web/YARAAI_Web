# SPDX-License-Identifier: MIT
"""sgcn_kd.py
===============================
Student‑SGCN w/ Knowledge Distillation
-------------------------------------
Light‑weight **Simplified Graph Convolution Network** (SGCN) classifier that
learns from a high‑capacity teacher (e.g. RES‑GCL) via **Knowledge
Distillation (KD)** à la Hinton et al., 2015.

The goal is to provide a *CPU‑friendly* model (≈ 0.5 M params) that keeps most
of the accuracy of the large teacher while reducing latency ≫10×.

Usage Example
-------------
```python
from src.models.distill.sgcn_kd import StudentSGCN
model = StudentSGCN(in_dim=128,
                    hid_dims=[256,128],
                    num_classes=1,
                    alpha=0.6,
                    temperature=4.0)

out = model(data)                     # inference → logits
loss = model.kd_loss(out, teacher_out, labels)
```

Notes
-----
* **Layer**: `torch_geometric.nn.SGConv` (no expensive attention)
* **Input**: sparse adjacency (edge_index) & node feature matrix `x128`.
  During graph‑level classification we perform global mean pooling.
* **KD Loss**: `loss = α·CE(y, s) + (1−α)·T²·KL(p_t, p_s)`
    * `p_s = softmax(logits_s / T)`, `p_t = softmax(logits_t / T)`
    * Supports binary / multi‑class via `num_classes`.
* **Multi‑Label** tasks: set `multi_label=True` to use BCE+KL instead.
"""
from __future__ import annotations

from typing import List, Tuple, Union, Dict, Optional
import logging
from pathlib import Path

import torch
from torch import nn
import torch.nn.functional as F
from torch_geometric.nn import SGConv, global_mean_pool
from torch_geometric.data import Data, Batch

__all__ = ["StudentSGCN"]


class StudentSGCN(nn.Module):
    """Light‑weight SGCN classifier with KD support.

    Parameters
    ----------
    in_dim : int
        Input node feature dimension.
    hid_dims : list[int] | None, default ``[256, 128]``
        Hidden dimensions for each SGConv layer (last element may equal
        ``num_classes`` – final linear replaced by SGConv).
    num_classes : int, default 1
        Output dimension. 1 → binary logits.
    dropout : float, default 0.1
        Dropout after each hidden layer.
    cached : bool, default True
        Whether to cache the normalized adjacency in SGConv (memory ↑, speed ↑).
    alpha : float, default 0.5
        Weight for *ground‑truth* CE/BCE part of KD loss.
    temperature : float, default 4.0
        Softmax temperature for KD.
    multi_label : bool, default False
        If ``True`` uses BCE/BCEWithLogits + sigmoid KL for multi‑label tasks.
    """

    def __init__(
        self,
        in_dim: int,
        hid_dims: Optional[List[int]] = None,
        num_classes: int = 1,
        dropout: float = 0.1,
        cached: bool = True,
        alpha: float = 0.5,
        temperature: float = 4.0,
        multi_label: bool = False,
    ) -> None:
        super().__init__()
        assert 0.0 <= alpha <= 1.0, "alpha must be in [0,1]"
        self.alpha = alpha
        self.T = temperature
        self.multi_label = multi_label
        hid_dims = hid_dims or [256, 128]

        dims = [in_dim] + hid_dims
        self.convs = nn.ModuleList(
            SGConv(dims[i], dims[i + 1], K=2, cached=cached)
            for i in range(len(dims) - 1)
        )
        self.dropout = dropout

        self.classifier = nn.Linear(dims[-1], num_classes)

    # --------------------------------------------------------------------- #
    # Forward
    # --------------------------------------------------------------------- #
    def forward(self, data: Union[Data, Batch]) -> torch.Tensor:
        """Compute **graph‑level** logits.

        If ``data`` is a ``Batch`` (`pyg_batch`), global mean pooling aggregates
        node embeddings into graph representation.
        """
        x, edge_index, batch = data.x, data.edge_index, data.batch
        for conv in self.convs:
            x = conv(x, edge_index)
            x = F.relu(x)
            x = F.dropout(x, p=self.dropout, training=self.training)

        # Graph‑level pooling & classification
        g = global_mean_pool(x, batch)
        logits = self.classifier(g)  # (B, C)
        return logits.squeeze(-1) if logits.shape[1] == 1 else logits

    # --------------------------------------------------------------------- #
    # Knowledge Distillation Loss
    # --------------------------------------------------------------------- #
    def kd_loss(
        self,
        student_logits: torch.Tensor,
        teacher_logits: torch.Tensor,
        labels: torch.Tensor,
        reduction: str = "mean",
    ) -> torch.Tensor:
        """KD loss = α·CE + (1−α)·T²·KL.

        Parameters
        ----------
        student_logits : Tensor, shape (B, C)
        teacher_logits : Tensor, shape (B, C)
        labels : Tensor, shape (B,) or (B, C)
        reduction : "mean" | "sum" | "none"
        """
        if self.multi_label:
            ce = F.binary_cross_entropy_with_logits(
                student_logits, labels.float(), reduction=reduction
            )
            p_s = torch.sigmoid(student_logits / self.T)
            p_t = torch.sigmoid(teacher_logits / self.T)
            kl = F.kl_div(p_s.log(), p_t, reduction=reduction)
        else:
            ce = F.cross_entropy(student_logits, labels.long(), reduction=reduction)
            p_s = F.log_softmax(student_logits / self.T, dim=-1)
            p_t = F.softmax(teacher_logits / self.T, dim=-1)
            kl = F.kl_div(p_s, p_t, reduction=reduction)

        loss = self.alpha * ce + (1.0 - self.alpha) * (self.T**2) * kl
        return loss

    # --------------------------------------------------------------------- #
    # Convenience Wrapper (train‑step style)
    # --------------------------------------------------------------------- #
    def forward_train(
        self,
        data: Union[Data, Batch],
        labels: torch.Tensor,
        teacher_logits: torch.Tensor,
        reduction: str = "mean",
    ) -> Dict[str, torch.Tensor]:
        """Single train step helper returning loss + predictions."""
        stud_logits = self.forward(data)
        loss = self.kd_loss(stud_logits, teacher_logits, labels, reduction)
        return {
            "loss": loss,
            "logits": stud_logits,
        }

    # ------------------------------------------------------------------ #
    @classmethod
    def load_from_checkpoint(
        cls, path, *, map_location=None, dtype=None
    ) -> "StudentSGCN":
        """Load model from a :func:`torch.save` checkpoint.

        The method supports checkpoints saved as ``{'model': state_dict}`` or
        plain ``state_dict`` dictionaries.  If ``path.with_suffix('.meta.pkl')``
        exists, it will be loaded to attach auxiliary fields such as
        ``attr_names`` and ``in_dims`` for later use.
        """

        obj = torch.load(path, map_location=map_location, weights_only=False)

        if isinstance(obj, cls):
            model = obj
            state = None
        elif isinstance(obj, dict) and "model" in obj:
            state = obj["model"]
        elif isinstance(obj, dict):
            state = obj
        else:
            raise ValueError(f"Unrecognized checkpoint format: {path}")

        meta_path = Path(path).with_suffix(".meta.pkl")
        meta = None
        if meta_path.is_file():
            try:
                meta = torch.load(meta_path, map_location="cpu", weights_only=False)
            except Exception as exc:  # pragma: no cover - I/O handling
                logging.warning("Failed to load meta snapshot %s: %s", meta_path, exc)

        if state is not None:
            hid_dims = []
            i = 0
            while f"convs.{i}.lin.weight" in state:
                hid_dims.append(state[f"convs.{i}.lin.weight"].size(0))
                i += 1

            if "classifier.weight" in state:
                num_classes = state["classifier.weight"].size(0)
            else:
                num_classes = 1

            w0 = state.get("convs.0.lin.weight")
            if w0 is None:
                raise RuntimeError("Checkpoint missing 'convs.0.lin.weight'")
            in_dim = w0.size(1)

            model = cls(in_dim=in_dim, hid_dims=hid_dims, num_classes=num_classes)
            model.load_state_dict(state, strict=False)

        if isinstance(meta, dict):
            setattr(model, "attr_names", meta.get("attr_names"))
            setattr(model, "in_dims", meta.get("in_dims"))

        if dtype is not None:
            model = model.to(dtype=dtype)
        return model
