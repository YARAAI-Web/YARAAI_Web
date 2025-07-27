# robust-malware-graph / src / explain / cfg_explainer / selector.py
# --------------------------------------------------------------------------- #
#  🎯  Gumbel-Mask Selector
#
#  CFGExplainer 1단계: “어떤 노드(또는 경로)를 살릴 것인가?”
#  — differentiable binary mask m ∈ {0,1}^N 를 학습해
#    • 목표 모형(score_fn) 예측 f(G ⊙ m) 의 변화(정보 보존) ↘ minimal
#    • 마스크 sparsity(‖m‖₁) ↘  (즉, 적은 노드만으로도 예측 유지)
#
#  • 핵심 기법: Gumbel-Sigmoid(Concrete Bernoulli) + Information Bottleneck
#
#      L = α · CE( f(G⊙m), f(G) )          # Fidelity (cross-entropy or MSE)
#        + β · ‖m‖₁ / N                    # Sparsity (ℓ₁ penalty)
#
#    – f(G)       : full-graph score (detach) — class logit or prob
#    – f(G⊙m)     : masked-graph score
#    – α, β       : trade-off hyper-params (default α=1, β=2e-2)
#
#  • 사용 예
#      >>> selector = GumbelMaskSelector(view="cfg").to("cuda")
#      >>> optim = torch.optim.Adam(selector.parameters(), lr=2e-3)
#      >>> for step in range(1_000):
#      ...     loss, m_prob = selector.step(cfg_g, score_fn, optim)
#      >>> hard_mask = (m_prob > 0.5).nonzero(as_tuple=False).view(-1)
#
#  • 의존
#      torch ≥ 2.0, torch_geometric ≥ 2.x, (optional) tqdm
# --------------------------------------------------------------------------- #
from __future__ import annotations

import math
from typing import Callable, Tuple
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.data import HeteroData

try:
    from tqdm.auto import tqdm  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    tqdm = lambda x, **kwargs: x  # type: ignore


# --------------------------------------------------------------------------- #
#                              Sampling helpers                               #
# --------------------------------------------------------------------------- #
def _sample_gumbel(shape, eps: float = 1e-20, device=None):
    """Gumbel(0,1) noise."""
    U = torch.rand(shape, device=device)
    return -torch.log(-torch.log(U + eps) + eps)


def gumbel_sigmoid(logits: torch.Tensor, tau: float, hard: bool) -> torch.Tensor:
    """
    Binary Concrete (≃ Hard-Sigmoid w/ Gumbel) sample.

    Returns probabilistic mask ∈ (0,1) or hard {0,1}.
    """
    g = _sample_gumbel(logits.shape, device=logits.device)
    y_soft = torch.sigmoid((logits + g) / tau)

    if hard:
        # straight-through
        y_hard = (y_soft > 0.5).float()
        return y_hard.detach() - y_soft.detach() + y_soft
    return y_soft


# --------------------------------------------------------------------------- #
#                        Hetero graph edge helpers                            #
# --------------------------------------------------------------------------- #
def iter_edge_types(g: HeteroData, view: str | None = None):
    """Yield edge types in ``g`` whose relation matches ``view``.

    When ``view`` is ``None`` all edge types are yielded.
    """
    for etype in g.edge_types:
        if view is None or etype[1] == view:
            yield etype


def edge_mask_to_global(
    g: HeteroData, masks: dict[str, torch.Tensor], view: str | None
) -> torch.Tensor:
    """Concatenate per-edge-type masks following ``iter_edge_types`` order.

    ``None`` concatenates masks for all edge types.
    """
    outs = []
    for et in iter_edge_types(g, view):
        outs.append(masks[str(et)])
    return torch.cat(outs) if outs else torch.empty(0)


# --------------------------------------------------------------------------- #
#                             Main Selector class                             #
# --------------------------------------------------------------------------- #
class GumbelMaskSelector(nn.Module):
    """Trainable **edge** mask using Concrete Bernoulli."""

    def __init__(
        self,
        view: str = "cfg",
        *,
        init_bias: float | None = -1.0,
        tau_start: float = 2.0,
        tau_min: float = 0.5,
        tau_decay: float = 0.995,
        device: str | torch.device | None = None,
    ) -> None:
        super().__init__()
        self.view = view
        self.init_bias = init_bias
        self.logits = nn.ParameterDict()
        self.register_buffer("tau", torch.tensor(tau_start))
        self.tau_min = tau_min
        self.tau_decay = tau_decay
        self.to(device or "cpu")

    # ------------------------------------------------------------------ #
    @property
    def initialized(self) -> bool:
        return len(self.logits) > 0

    # ------------------------------------------------------------------ #
    def _init_params(self, g: "HeteroData") -> None:
        """Create per-edge-type logits if missing."""
        for etype in iter_edge_types(g, self.view):
            key = str(etype)
            if key not in self.logits:
                num_edges = g[etype].edge_index.size(1)
                bias = float(self.init_bias) if self.init_bias is not None else 0.0
                device = self.tau.device
                self.logits[key] = nn.Parameter(
                    torch.full((num_edges,), bias, device=device)
                )

    # ------------------------------------------------------------------ #
    #                     Core forward / sample / loss                   #
    # ------------------------------------------------------------------ #
    def forward(self, g: "HeteroData", tau: float | None = None) -> torch.Tensor:
        """Sample a probabilistic edge mask for ``self.view``."""
        if not self.initialized:
            self._init_params(g)

        τ = float(self.tau if tau is None else tau)
        masks = {}
        for etype in iter_edge_types(g, self.view):
            logits = self.logits[str(etype)]
            masks[str(etype)] = gumbel_sigmoid(logits, τ, False)
        return edge_mask_to_global(g, masks, self.view)

    # ------------------------------- loss --------------------------------- #
    def loss(
        self,
        full_score: torch.Tensor,
        masked_score: torch.Tensor,
        mask_prob: torch.Tensor,
        *,
        alpha: float = 1.0,
        beta: float = 2e-2,
        loss_type: str = "bce",
    ) -> torch.Tensor:
        """Information Bottleneck–style loss."""
        if loss_type == "bce":
            fidelity = F.binary_cross_entropy_with_logits(
                masked_score, torch.sigmoid(full_score.detach())
            )
        elif loss_type == "mse":
            fidelity = F.mse_loss(masked_score, full_score.detach())
        else:
            raise ValueError("loss_type must be 'bce' or 'mse'")

        sparsity = mask_prob.mean()
        return alpha * fidelity + beta * sparsity

    # --------------------------- single step API -------------------------- #
    def step(
        self,
        graph: Data | HeteroData,
        full_graph_score: torch.Tensor,
        score_fn: Callable[[Data | HeteroData], torch.Tensor],
        optimizer: torch.optim.Optimizer,
        *,
        alpha: float = 1.0,
        beta: float = 2e-2,
        hard: bool = False,
        loss_type: str = "bce",
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        """Perform 1 optimization step on ``graph``."""
        if not self.initialized:
            # This should be initialized on the full graph before calling this
            raise RuntimeError("Selector not initialized.")

        optimizer.zero_grad()

        # Use the pre-computed score for the full graph
        full_score = full_graph_score
        masks = {}
        τ = float(self.tau)
        for etype in iter_edge_types(graph, self.view):
            logits = self.logits[str(etype)]
            masks[str(etype)] = gumbel_sigmoid(logits, τ, hard)
        m_prob = edge_mask_to_global(graph, masks, self.view)

        # Temporarily mask edge stores in-place to avoid cloning the graph
        original: dict[str, dict[str, torch.Tensor]] = {}
        for etype_str, mask in masks.items():
            etype = eval(etype_str)
            keep = mask > 0.5
            if keep.sum() == 0:
                if len(mask) > 0:
                    keep[mask.argmax()] = True
                else:
                    continue

            store = graph[etype]
            backup: dict[str, torch.Tensor] = {}
            for k, v in store.items():
                if torch.is_tensor(v) and v.size(0) == mask.size(0):
                    backup[k] = v
                    store[k] = v[keep]
            original[etype_str] = backup

        masked_score = score_fn(graph)

        # Restore original edge stores
        for etype_str, backup in original.items():
            etype = eval(etype_str)
            store = graph[etype]
            for k, v in backup.items():
                store[k] = v

        loss = self.loss(full_score, masked_score, m_prob, alpha=alpha, beta=beta, loss_type=loss_type)
        loss.backward()
        optimizer.step()

        self.tau.mul_(self.tau_decay).clamp_(min=self.tau_min)

        with torch.no_grad():
            fidelity = F.binary_cross_entropy_with_logits(masked_score, torch.sigmoid(full_score))
            sparsity = m_prob.mean()
            deletion = torch.sigmoid(full_score) - torch.sigmoid(masked_score)

        del masked_score, m_prob
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        return loss.detach(), fidelity, sparsity, deletion

    # ------------------------------------------------------------------ #
    #                         Utility convenience                         #
    # ------------------------------------------------------------------ #
    def train_loop(
        self,
        graph: Data | HeteroData,
        score_fn: Callable[[Data | HeteroData], torch.Tensor],
        epochs: int = 1_000,
        *,
        lr: float = 2e-3,
        alpha: float = 1.0,
        beta: float = 2e-2,
        hard: bool = False,
        show_progress: bool = True,
        loss_type: str = "bce",
        plot_path: Path | str | None = None,
    ) -> torch.Tensor:
        """
        Simple helper for quick-and-dirty training in notebooks.
        """
        if not self.initialized:
            self._init_params(graph)

        optim = torch.optim.Adam(self.parameters(), lr=lr)
        iterator = tqdm(range(epochs), disable=not show_progress, desc="Selector train")

        fidelities, sparsities, deletions = [], [], []

        # Pre-compute the full graph score once to save memory inside the loop
        with torch.no_grad():
            full_score = score_fn(graph).detach()

        for _ in iterator:
            loss, fid, spars, delt = self.step(
                graph,
                full_score,
                score_fn,
                optim,
                alpha=alpha,
                beta=beta,
                hard=hard,
                loss_type=loss_type,
            )
            fidelities.append(fid.item())
            sparsities.append(spars.item())
            deletions.append(delt.item())
            iterator.set_postfix(loss=loss.item(), tau=float(self.tau))

        if plot_path is not None:
            from matplotlib import pyplot as plt
            from src.common.utils import ensure_dir

            plot_path = Path(plot_path)
            ensure_dir(plot_path.parent)
            epochs_r = range(1, len(fidelities) + 1)
            plt.figure()
            plt.plot(epochs_r, fidelities, label="fidelity")
            plt.plot(epochs_r, sparsities, label="sparsity")
            plt.plot(epochs_r, deletions, label="deletion")
            plt.xlabel("Epoch")
            plt.legend()
            plt.tight_layout()
            plt.savefig(plot_path)
            plt.close()

        with torch.no_grad():
            final_mask_prob = self.forward(graph)
        return final_mask_prob

    # ---------------------- export to hard index mask --------------------- #
    def hard_selection(self, g: "HeteroData", thresh: float = 0.5) -> dict[str, torch.Tensor]:
        """Return selected edge indices per edge type."""
        if not self.initialized:
            self._init_params(g)
        out: dict[str, torch.Tensor] = {}
        for etype in iter_edge_types(g, self.view):
            prob = torch.sigmoid(self.logits[str(etype)])
            out[str(etype)] = (prob > thresh).nonzero(as_tuple=False).view(-1)
        return out

    # -------------------------- dunder helpers ---------------------------- #
    def __repr__(self) -> str:  # pragma: no cover
        if self.initialized:
            probs = torch.cat([torch.sigmoid(p) for p in self.logits.values()])
            p_mean = probs.mean().item()
        else:
            p_mean = float("nan")
        return f"{self.__class__.__name__}(view={self.view}, p≈{p_mean:.2%}, τ={float(self.tau):.2f})"
