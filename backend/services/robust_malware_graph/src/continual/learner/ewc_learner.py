# ---------------------------------------------------------------------------
# src/continual/learner/ewc_learner.py
# ---------------------------------------------------------------------------
"""Elastic-Weight-Consolidation(EWC) learner for malware-graph continual learning.

* backbone  : Frozen ❌ (fine-tuned ⭕) – encoder도 학습하지만
              이전 task 로 학습된 weight 에 멀어지면 penalty.
* penalty   : ½ λ ∑_i F_i (θ_i − θ_i*)²    ← diagonal Fisher (online)
* supported : Class-IL / Task-IL  (task_id 전달 시 별도 head bank 가능)

Typical usage
-------------
>>> learner = EWCLearner(encoder, head, ewc_lambda=5.0)
>>> for task_id, dl in enumerate(task_loaders):
...     for batch in dl:            # online/mini-batch
...         learner.observe({**batch, "task_id": task_id})
...     learner.consolidate(dl)     # ← Fisher 추정 & θ* 저장
>>> acc = learner.evaluate(test_batch)
"""
from __future__ import annotations

import pathlib
from collections import defaultdict
from datetime import datetime
from itertools import islice
from typing import Any, Dict, Mapping, Optional, Tuple

import torch
import torch.nn.functional as F
from torch import Tensor, nn
from torch_geometric.data import Batch

from src.continual.learner.adapters import to_device
from src.continual.utils import set_random_seed


# --------------------------------------------------------------------------- #
# Utility
# --------------------------------------------------------------------------- #
def _iter_params(model: nn.Module):
    """(name, Parameter) generator – gradients **and** data required."""
    for n, p in model.named_parameters():
        if p.requires_grad:
            yield n, p


# --------------------------------------------------------------------------- #
# EWC Learner
# --------------------------------------------------------------------------- #
class EWCLearner(nn.Module):
    """Online Elastic-Weight-Consolidation learner."""

    def __init__(
        self,
        *,
        encoder: nn.Module,
        head: nn.Module | Mapping[int, nn.Module],
        lr: float = 1e-3,
        weight_decay: float = 1e-4,
        ewc_lambda: float = 5.0,
        fisher_n_samples: int = 256,
        grad_clip: Optional[float] = 1.0,
        device: str | torch.device = "cuda",
        seed: int = 42,
    ) -> None:
        super().__init__()
        set_random_seed(seed)
        self.device = torch.device(device)

        # modules ----------------------------------------------------------- #
        self.encoder = encoder
        if isinstance(head, Mapping):
            self.head_bank = nn.ModuleDict({str(t): h for t, h in head.items()})
            self._shared_head = None
        else:
            self.head_bank = nn.ModuleDict()
            self._shared_head = head

        # optim ------------------------------------------------------------- #
        self._optim = torch.optim.AdamW(
            [p for p in self.parameters() if p.requires_grad],
            lr=lr,
            weight_decay=weight_decay,
        )
        self.grad_clip = grad_clip

        # EWC bookkeeping --------------------------------------------------- #
        self.ewc_lambda = ewc_lambda
        self.fisher_n_samples = fisher_n_samples
        self.prev_task_params: list[Dict[str, Tensor]] = []
        self.prev_task_fishers: list[Dict[str, Tensor]] = []

        self.to(self.device)

    # --------------------------------------------------------------------- #
    # helpers
    # --------------------------------------------------------------------- #
    def _select_head(self, task_id: Optional[int]) -> nn.Module:
        if self._shared_head is not None:
            return self._shared_head
        if task_id is None:
            raise ValueError("task_id required when head bank used")
        return self.head_bank[str(int(task_id))]

    def _ewc_penalty(self) -> Tensor:
        """Σ_t ½ λ Σ_i F_t,i (θ_i−θ_t*,i)²"""
        if not self.prev_task_params:
            return torch.tensor(0.0, device=self.device)

        penalty = 0.0
        for params_star, fisher in zip(self.prev_task_params, self.prev_task_fishers):
            for name, p in _iter_params(self):
                if name not in fisher:
                    continue
                diff = p - params_star[name]
                penalty += (fisher[name] * diff.pow(2)).sum()
        return 0.5 * self.ewc_lambda * penalty

    # --------------------------------------------------------------------- #
    # training step
    # --------------------------------------------------------------------- #
    def observe(self, batch: Dict[str, Any]) -> Tensor:
        """One optimisation step; returns total loss (bce+ewc)."""
        self.train()
        batch = to_device(batch, self.device)

        # forward ---------------------------------------------------------- #
        z = self.encoder(batch["data"])            # (B,D)
        logits = self._select_head(batch.get("task_id"))(z)
        y = batch["y"].float().view_as(logits)
        bce = F.binary_cross_entropy_with_logits(logits, y)

        loss = bce + self._ewc_penalty()

        # backward --------------------------------------------------------- #
        self._optim.zero_grad(set_to_none=True)
        loss.backward()
        if self.grad_clip is not None:
            nn.utils.clip_grad_norm_(self.parameters(), self.grad_clip)
        self._optim.step()
        return loss.detach()

    # --------------------------------------------------------------------- #
    # evaluation
    # --------------------------------------------------------------------- #
    @torch.no_grad()
    def evaluate(self, batch: Dict[str, Any]) -> Tensor:
        self.eval()
        batch = to_device(batch, self.device)
        z = self.encoder(batch["data"])
        head = self._select_head(batch.get("task_id"))
        return torch.sigmoid(head(z))

    # --------------------------------------------------------------------- #
    # Fisher & consolidation
    # --------------------------------------------------------------------- #
    @torch.no_grad()
    def _estimate_fisher(self, dataloader) -> Dict[str, Tensor]:
        """Diagonal Fisher ≈ avg (∂ℓ/∂θ)² over `fisher_n_samples` samples."""
        self.eval()
        fisher: defaultdict[str, Tensor] = defaultdict(
            lambda: torch.zeros((), device=self.device)
        )

        samples_seen = 0
        for batch in dataloader:
            if samples_seen >= self.fisher_n_samples:
                break
            batch = to_device(batch, self.device)
            # (1) forward
            z = self.encoder(batch["data"])
            logits = self._select_head(batch.get("task_id"))(z)
            y = batch["y"].float().view_as(logits)
            loss = F.binary_cross_entropy_with_logits(logits, y)

            # (2) grads
            grads = torch.autograd.grad(
                loss, [p for _, p in _iter_params(self)], retain_graph=False
            )
            for (name, _), g in zip(_iter_params(self), grads):
                fisher[name] += g.pow(2).detach()
            samples_seen += len(y)

        # normalize
        for k in fisher:
            fisher[k] /= max(samples_seen, 1)
        return fisher

    def consolidate(self, dataloader) -> None:
        """Call **after** completing a task to store θ* and Fisher diag."""
        fisher = self._estimate_fisher(islice(dataloader, 0, None))
        params_star = {n: p.detach().clone() for n, p in _iter_params(self)}
        self.prev_task_params.append(params_star)
        self.prev_task_fishers.append(fisher)

    # --------------------------------------------------------------------- #
    # checkpoint util
    # --------------------------------------------------------------------- #
    def save(self, path: str | pathlib.Path) -> None:
        state = {
            "time": datetime.now().isoformat(),
            "model": self.state_dict(),
            "prev_task_params": self.prev_task_params,
            "prev_task_fishers": self.prev_task_fishers,
        }
        torch.save(state, path)

    def load(self, path: str | pathlib.Path) -> None:
        ckpt = torch.load(path, map_location="cpu", weights_only=False)
        self.load_state_dict(ckpt["model"])
        self.prev_task_params = ckpt["prev_task_params"]
        self.prev_task_fishers = ckpt["prev_task_fishers"]
        self.to(self.device)
