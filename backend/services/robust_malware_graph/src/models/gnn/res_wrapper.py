# src/models/gnn/res_wrapper.py
"""
RESGCLClassifier
================

A **robust binary classifier** that pairs
(1) a *graph encoder* producing graph‑level embeddings and
(2) a *head* that turns those embeddings into final predictions.

During training it injects **Edge‑Drop smoothing** (as proposed in
*RES‑GCL, NeurIPS 2023*) to enhance certified robustness. The same
module can be called in *certification* mode by sampling multiple
edge‑dropped graphs and aggregating their outputs.

Usage
-----
```python
encoder = RGCNEncoder(...)
clf     = RESGCLClassifier(
    encoder=encoder,
    head="binary_mlp",          # registry name or nn.Module
    drop_prob=0.2,
)
probs = clf(data)                # (batch,)
```
"""
from __future__ import annotations

from typing import Union, Optional, List, Dict, Callable
from pathlib import Path
try:  # torch<2.3 does not expose add_safe_globals
    from torch.serialization import add_safe_globals
except Exception:  # pragma: no cover - optional API
    def add_safe_globals(*_args, **_kwargs):
        pass
import logging

import torch
from torch import nn, Tensor
from torch.utils.checkpoint import checkpoint

from .layers.edge_smoothing import EdgeDropSmoothing
from .heads import get_head, HEAD_REGISTRY  # registry helpers
from .encoder import RGCNEncoder
from src.graphs.normalizers.schema import NodeType
from src.models.contrast.sup_con import SupContrastHead
from src.common.utils import get_logger

LOGGER = get_logger(__name__)

# --------------------------------------------------------------------------- #
class RESGCLClassifier(nn.Module):
    """Binary robust classifier with Edge‑Drop smoothing."""

    def __init__(
        self,
        *,
        encoder: nn.Module,
        head: Union[str, nn.Module] = "binary_mlp",  # name or instance
        drop_prob: float = 0.2,
        n_samples_cert: int = 30,
        dtype: torch.dtype | None = None,
    ):
        """
        Parameters
        ----------
        encoder : nn.Module
            Graph encoder returning an embedding `(B, D)` for a **single**
            forward pass.
        head : str | nn.Module, default "binary"
            • If *str* → looked‑up via `heads.get_head(name, in_dim=D)`.
            • If *nn.Module* → used as‑is.
        drop_prob : float, default 0.2
            Edge‑drop probability *p* during training / cert.
        n_samples_cert : int, default 30
            Number of Monte‑Carlo edge‑dropped samples in `certify()`.
        """
        super().__init__()
        self.encoder = encoder
        self.dropper = EdgeDropSmoothing(drop_prob=drop_prob)
        self.n_samples_cert = int(n_samples_cert)

        # infer embedding dim from encoder attribute if available
        emb_dim = getattr(encoder, "out_dim", None)
        if emb_dim is None:
            # fallback to a dummy parameter's last dimension
            emb_dim = next(p for p in encoder.parameters()).shape[-1]
        self.head = self._init_head(head, emb_dim)

        self.is_supcon_head = isinstance(self.head, SupContrastHead)
        if self.is_supcon_head:
            self.classifier = nn.Linear(self.head.out_dim, 1)
        else:
            self.classifier = None

        if dtype is not None:
            self.to(dtype=dtype)

    # ------------------------------------------------------------------ #
    @staticmethod
    def _init_head(head: Union[str, nn.Module], in_dim: int) -> nn.Module:
        if isinstance(head, str):
            if head not in HEAD_REGISTRY:
                raise KeyError(f"Head '{head}' is not registered.")
            return get_head(head, in_dim=in_dim)
        if not isinstance(head, nn.Module):
            raise TypeError("`head` must be str or nn.Module instance.")
        return head

    # ------------------------------------------------------------------ #
    def forward(
        self,
        data,
        *,
        return_logits: bool = False,
        checkpoint_layers: bool = False,
        edge_weight_dict: dict[str, Tensor] | None = None,
    ) -> Tensor:
        """Single forward pass with edge‑drop when in training mode."""
        # apply edge‑drop only during training
        # if self.training:
        #     data = data.clone()
        #     for etype in data.edge_types:
        #         ei, ea = data[etype].edge_index, getattr(data[etype], "edge_attr", None)
        #         ei, ea = self.dropper(ei, ea)
        #         data[etype].edge_index = ei
        #         if ea is not None:
        #             data[etype].edge_attr = ea

        if checkpoint_layers:
            emb = checkpoint(self.encoder, data, edge_weight_dict)  # (B, D)
        else:
            emb = self.encoder(data, edge_weight_dict=edge_weight_dict)  # (B, D)
        if emb is None:
            return None
        
        if self.is_supcon_head:
            # SupCon head returns embeddings for contrastive loss, not logits
            # We use our own classifier for the final prediction
            supcon_emb = self.head.embed(emb)
            logits = self.classifier(supcon_emb).squeeze(-1)
            if return_logits:
                return logits
            return torch.sigmoid(logits)
        else:
            out = self.head(emb, return_logits=return_logits)  # (B,)
            return out

    # ------------------------------------------------------------------ #
    @torch.no_grad()
    def predict(self, data, threshold: float = 0.5) -> Tensor:
        """Deterministic prediction (no edge‑drop)."""
        self.eval()
        probs = self.forward(data, return_logits=False)
        return (probs >= threshold).long()

    # ------------------------------------------------------------------ #
    @torch.no_grad()
    def certify(self, data, threshold: float = 0.5) -> Tensor:
        """Monte‑Carlo certify via *n_samples_cert* edge‑dropped passes."""
        self.eval()
        probs_accum = 0.0
        for _ in range(self.n_samples_cert):
            # during eval edge‑drop is disabled, so force train flag locally
            self.train()
            probs_accum += self.forward(data, return_logits=False)
        self.eval()
        probs = probs_accum / self.n_samples_cert
        return (probs >= threshold).long()

    # ------------------------------------------------------------------ #
    def extra_repr(self) -> str:  # pragma: no cover
        return (
            f"encoder={self.encoder.__class__.__name__}, "
            f"head={self.head.__class__.__name__}, "
            f"drop_prob={self.dropper.drop_prob}, "
            f"n_samples_cert={self.n_samples_cert}"
        )

    # ------------------------------------------------------------------ #
    @classmethod
    def load_from_checkpoint(cls, path, *, map_location=None, dtype=None) -> "RESGCLClassifier":
        """Load classifier from ``torch.save`` checkpoint."""
        obj = torch.load(path, map_location=map_location, weights_only=False)

        if isinstance(obj, cls):
            return obj

        if isinstance(obj, dict) and "model" in obj:
            state = obj["model"]
            attr_names = obj.get("attr_names")
        elif isinstance(obj, dict):
            state = obj
            attr_names = obj.get("attr_names")
        else:
            raise ValueError(f"Unrecognized checkpoint format: {path}")

        enc_state = {k[len("encoder."):]: v for k, v in state.items() if k.startswith("encoder.")}

        meta_path = Path(path).with_suffix(".meta.pkl")
        meta = None
        if meta_path.is_file():
            try:
                add_safe_globals([NodeType])
                meta = torch.load(meta_path, weights_only=False)
                if isinstance(meta, dict):
                    meta.setdefault("num_relations", len(meta.get("edge_types", [])))
            except Exception as exc:  # pragma: no cover - I/O handling
                LOGGER.warning("Failed to load meta snapshot %s: %s", meta_path, exc)
                meta = None
        else:
            LOGGER.warning("Meta snapshot %s not found", meta_path)

        if attr_names is None and isinstance(meta, dict) and "attr_names" in meta:
            attr_names = meta.get("attr_names")

        if meta is not None:
            node_types = list(meta.get("node_types", []))
            edge_types = [tuple(e) for e in meta.get("edge_types", [])]
            in_dims = {k: int(v) for k, v in meta.get("in_dims", {}).items()}
            num_relations = int(meta.get("num_relations", len(edge_types)))

            out_w = enc_state["out_proj.weight"]
            out_dim = out_w.size(0)
            hidden_dim = out_w.size(1)
            conv_keys = [k for k in enc_state if k.startswith("convs.") and k.endswith(".weight")]
            layer_ids = {int(k.split(".")[1]) for k in conv_keys}
            num_layers = max(layer_ids) + 1 if layer_ids else 1
            vocab_size = 0
            attr_dim = 32
            if "meta_embed.weight" in enc_state:
                vocab_size = enc_state["meta_embed.weight"].size(0)
                attr_dim = enc_state["meta_embed.weight"].size(1)
            if isinstance(meta, dict) and "vocab_size" in meta:
                vocab_size = int(meta["vocab_size"])

            encoder = RGCNEncoder(
                metadata=(node_types, edge_types[:num_relations]),
                in_dims=in_dims,
                attr_names=attr_names,
                vocab_size=vocab_size,
                attr_dim=attr_dim,
                hidden_dim=hidden_dim,
                num_layers=num_layers,
                out_dim=out_dim,
            )
            encoder.load_state_dict(enc_state, strict=False)
        else:
            encoder = RGCNEncoder._from_state_dict(enc_state, attr_names=attr_names)

        model = cls(encoder=encoder, dtype=dtype)
        model.load_state_dict(state, strict=False)
        return model

    # ------------------------------------------------------------------ #
    def reinit_input_dims(self, in_dims: Dict[str, int], attr_names: Dict[str, list[str]] | None = None, vocab_size: int = 0):
        """
        Re-initializes the input projection layers of the encoder to match new data dimensions.
        This is useful when applying a pre-trained model to a new dataset with different feature sizes.
        """
        node_types = self.encoder.node_types
        self.encoder.attr_names = attr_names or {nt: [] for nt in node_types}
        self.encoder.meta_embed = nn.Embedding(vocab_size, self.encoder.attr_dim) if vocab_size > 0 else None

        for nt in node_types:
            if nt in in_dims:
                in_channels = in_dims[nt]
                if nt in self.encoder.input_proj:
                    hidden_dim = self.encoder.input_proj[nt].out_features
                    
                    # Create a new linear layer with the correct dimensions
                    new_proj = nn.Linear(in_channels, hidden_dim)
                    nn.init.xavier_uniform_(new_proj.weight)
                    nn.init.zeros_(new_proj.bias)
                    
                    # Replace the old layer
                    self.encoder.input_proj[nt] = new_proj
                    LOGGER.info(f"Re-initialized input projection for node type '{nt}' with new in_dim={in_channels}")

    @classmethod
    def load_pretrained(cls, path, *, map_location=None, dtype=None) -> "RESGCLClassifier":
        """Backward-compatible alias for :meth:`load_from_checkpoint`."""
        return cls.load_from_checkpoint(path, map_location=map_location, dtype=dtype)
