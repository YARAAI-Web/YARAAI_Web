# robust-malware-graph / src / explain / pg_explainer.py
# --------------------------------------------------------------------------- #
#  ✨  Parametric Graph Explainer
#
#  Minimal implementation of PGExplainer-style edge masking.  The module
#  computes edge-wise mask probabilities from node embeddings via a small
#  MLP and samples them with the Gumbel-Softmax trick.
# --------------------------------------------------------------------------- #
from __future__ import annotations

from typing import Dict, Iterable, Mapping

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.data import Data, HeteroData

from .cfg_explainer.selector import gumbel_sigmoid, iter_edge_types, edge_mask_to_global
from .utils.hetero import EdgeType


from src.common.utils import get_logger

LOGGER = get_logger(__name__)


class PGExplainer(nn.Module):
    @staticmethod
    def _replace_dots_with_underscores(s: str) -> str:
        return s.replace('.', '_')
    """Simple PGExplainer for heterogeneous graphs.

    ``view`` may be ``None`` to operate on the full graph.  Edge scoring MLPs
    are created per edge type from ``in_dims`` and ``edge_types``.  When
    explaining a plain :class:`~torch_geometric.data.Data` graph the MLP stored
    under the ``"default"`` key is used.
    """

    def __init__(
        self,
        model: nn.Module,
        in_dims: Dict[str, int],
        edge_types: Iterable[EdgeType],
        node_types: Iterable[str] | None = None,
        view: str | None = "cfg",
        device: str | torch.device | None = None,
        init_bias: float = 1.0,
        tau_start: float = 1.0,
        hidden_dim: int = 64,
        num_layers: int = 2,
        dropout: float = 0.2,
        norm_type: str = "batch",
    ) -> None:
        """Initialize the explainer.

        Parameters
        ----------
        model : nn.Module
            GNN model being explained.
        in_dims : Dict[str, int]
            Input dimension per node type.
        node_types : Iterable[str], optional
            All node types that may be encountered. If provided, ensures all
            node types are accounted for in `in_dims`.
        edge_types : Iterable[EdgeType]
            Edge types present in the graphs to be explained.
        view : str | None, optional
            Edge relation to explain. ``None`` uses all edge types.
        device : str | torch.device | None, optional
            Device for parameters and buffers.
        init_bias : float, optional
            Initial bias value for the last ``nn.Linear`` layer in each MLP.
        tau_start : float, optional
            Initial value for the temperature ``tau``.
        hidden_dim : int, optional
            Hidden size for the edge scoring MLP.
        num_layers : int, optional
            Number of MLP layers.
        dropout : float, optional
            Dropout rate for the explainer's MLP. Set to 0 to disable.
        norm_type : str, optional
            Type of normalization to use in the explainer's MLP ('none', 'batch', 'layer').
        """
        super().__init__()
        self.model = model
        self.view = view
        self.init_bias = init_bias

        enc = getattr(model, "encoder", None)
        embed_dim = (
            enc.out_proj.in_features
            if enc is not None and isinstance(getattr(enc, "out_proj", None), nn.Linear)
            else max(in_dims.values(), default=0)
        )
        self.embed_dim = embed_dim

        if node_types:
            for nt in node_types:
                in_dims.setdefault(nt, embed_dim)
        for nt in in_dims:
            in_dims[nt] = embed_dim

        self.edge_mlps = nn.ModuleDict()
        for src_t, rel, dst_t in edge_types:
            src_t_name = str(src_t).split(".")[-1].lower()
            rel_name = str(rel).split(".")[-1].lower()
            dst_t_name = str(dst_t).split(".")[-1].lower()
            key = f"{src_t_name}_{rel_name}_{dst_t_name}"

            input_dim = in_dims.get(src_t_name, embed_dim) + in_dims.get(
                dst_t_name, embed_dim
            )

            layers = []
            current_dim = input_dim
            for i in range(num_layers):
                if i < num_layers - 1:
                    layers.append(nn.Linear(current_dim, hidden_dim))
                    if norm_type == "batch":
                        layers.append(nn.BatchNorm1d(hidden_dim))
                    elif norm_type == "layer":
                        layers.append(nn.LayerNorm(hidden_dim))
                    layers.append(nn.ReLU())
                    if dropout > 0:
                        layers.append(nn.Dropout(p=dropout))
                    current_dim = hidden_dim
                else:
                    layers.append(nn.Linear(current_dim, 1))

            nn.init.constant_(layers[-1].bias, init_bias)
            self.edge_mlps[key] = nn.Sequential(*layers)

        self.register_buffer("tau", torch.tensor(tau_start))
        self.device = torch.device(device or "cpu")
        self.to(self.device)

    # ------------------------------------------------------------------ #
    def forward(
        self,
        graph: Data | HeteroData,
        embeddings: torch.Tensor | Mapping[str, torch.Tensor] | None = None,
        *,
        tau: float | None = None,
        hard: bool = False,
    ) -> torch.Tensor:
        """Return probabilistic edge mask for ``self.view``.

        When ``self.view`` is ``None`` a mask for all edge types is returned.
        """
        τ = float(self.tau if tau is None else tau)

        if isinstance(graph, Data):
            x = embeddings if embeddings is not None else graph.x
            src, dst = graph.edge_index
            h = torch.cat([x[src], x[dst]], dim=-1)
            logits = self.edge_mlps["default"](h).view(-1)
            return gumbel_sigmoid(logits, τ, hard)

        x_dict: Dict[str, torch.Tensor]
        if embeddings is None:
            x_dict = {ntype: graph[ntype].x for ntype in graph.node_types}
        elif isinstance(embeddings, Mapping):
            # For HeteroData, device must be obtained from a tensor within the graph
            device = graph[graph.edge_types[0]].edge_index.device
            x_dict = {k: v.to(device) for k, v in embeddings.items()}
        else:
            raise TypeError("embeddings must map node types to tensors")

        if not x_dict:
            LOGGER.warning("x_dict is empty in PGExplainer.forward.")
            return torch.empty(
                0, device=self.tau.device
            )  # Return empty tensor if no embeddings

        LOGGER.debug(
            f"DEBUG (PGExplainer.forward): x_dict dimensions: {{nt: x_dict[nt].shape for nt in x_dict}}"
        )

        masks: Dict[str, torch.Tensor] = {}
        for etype in iter_edge_types(graph, self.view):
            LOGGER.debug(f"DEBUG (PGExplainer.forward): Raw etype elements: src={etype[0]}, rel={etype[1]}, dst={etype[2]}")
            src, dst = graph[etype].edge_index

            # Ensure node features exist for source and destination node types
            if etype[0] not in x_dict or etype[2] not in x_dict:
                LOGGER.warning(
                    f"Missing node features for edge type {etype} in PGExplainer.forward. Skipping."
                )
                continue

            LOGGER.debug(
                f"DEBUG (PGExplainer.forward): x_dict[{etype[0]}] shape: {x_dict[etype[0]].shape}"
            )
            LOGGER.debug(
                f"DEBUG (PGExplainer.forward): x_dict[{etype[2]}] shape: {x_dict[etype[2]].shape}"
            )

            h = torch.cat([x_dict[etype[0]][src], x_dict[etype[2]][dst]], dim=-1)
            LOGGER.debug(f"DEBUG (PGExplainer.forward): h dimension: {h.shape}")
            src_t_name = str(etype[0]).split('.')[-1].lower()
            rel_name = str(etype[1]).split('.')[-1].lower()
            dst_t_name = str(etype[2]).split('.')[-1].lower()
            key = f"{src_t_name}_{rel_name}_{dst_t_name}"
            mlp = self.edge_mlps[key]
            logits = mlp(h).view(-1)
            masks[str(etype)] = gumbel_sigmoid(logits, τ, hard)
        return edge_mask_to_global(graph, masks, self.view)

    # ------------------------------------------------------------------ #
    def loss(
        self,
        full_score: torch.Tensor,
        masked_score: torch.Tensor,
        mask_prob: torch.Tensor,
        *,
        alpha: float = 1.0,
        beta: float = 2e-2,
        gamma: float = 0.0,
        loss_type: str = "bce",
    ) -> torch.Tensor:
        """Information bottleneck style loss."""
        if loss_type == "bce":
            target_prob = torch.sigmoid(full_score.detach()).clamp(1e-4, 1 - 1e-4)
            fidelity = F.binary_cross_entropy_with_logits(
                masked_score,
                target_prob,
                reduction="mean",
            )
        elif loss_type == "mse":
            fidelity = F.mse_loss(
                torch.sigmoid(masked_score),
                torch.sigmoid(full_score.detach())
            )
        elif loss_type == "smooth_l1":
            fidelity = F.smooth_l1_loss(masked_score, full_score.detach())
        else:
            raise ValueError("loss_type must be 'bce', 'mse', or 'smooth_l1'")
        sparsity = mask_prob.mean()
        mask = mask_prob.clamp(1e-6, 1 - 1e-6)
        entropy = -(mask * mask.log() + (1 - mask) * (1 - mask).log()).mean()
        return alpha * fidelity + beta * sparsity + gamma * entropy

    # ------------------------------------------------------------------ #
    def get_node_saliency(
        self,
        graph: Data | HeteroData,
        mask_prob: torch.Tensor | Dict[str, torch.Tensor],
    ) -> Dict[str, torch.Tensor]:
        """Aggregate edge importance into node scores.

        If ``self.view`` is ``None`` saliency is aggregated over all edge types.
        """
        if isinstance(graph, Data):
            mask = (
                mask_prob
                if isinstance(mask_prob, torch.Tensor)
                else next(iter(mask_prob.values()))
            )
            score = torch.zeros(graph.num_nodes, device=mask.device)
            src, dst = graph.edge_index
            score.index_add_(0, src, mask)
            score.index_add_(0, dst, mask)
            return {"node": score}

        # If mask_prob is a global tensor, split it per edge type.
        if isinstance(mask_prob, torch.Tensor):
            ptr = 0
            masks = {}
            for et in iter_edge_types(graph, self.view):
                num_e = graph[et].edge_index.size(1)
                masks[str(et)] = mask_prob[ptr : ptr + num_e]
                ptr += num_e
        else:
            masks = mask_prob

        scores = {
            ntype: torch.zeros(
                graph[ntype].num_nodes, device=next(iter(masks.values())).device
            )
            for ntype in graph.node_types
        }
        for et in iter_edge_types(graph, self.view):
            mask = masks[str(et)]
            src, dst = graph[et].edge_index
            scores[et[0]].index_add_(0, src, mask)
            scores[et[2]].index_add_(0, dst, mask)
        return scores
