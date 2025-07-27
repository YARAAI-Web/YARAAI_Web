# ---------------------------------------------------------------------------
# src/continual/learner/rehearsal_learner.py
# ---------------------------------------------------------------------------
"""Experience-Replay(ER) learner for malware-graph continual learning.

* backbone  : fine-tuned ⭕  (encoder를 계속 업데이트)
* replay    : current mini-batch + memory 샘플 `β × |B|`
* memory    : ReservoirSamplingBuffer (task 불문, 균일 확률로 치환)

정형 입력(keys in batch dict)
----------------------------
* data    : torch_geometric.data.Batch  – 그래프
* y       : Tensor[float]               – label(s)  (B, 1) or (B,)
* task_id : int | None                  – optional (for head bank)

Typical usage
-------------
>>> learner = RehearsalLearner(encoder, head,
...                            mem_capacity=10_000, replay_ratio=1.0)
>>> for batch in stream:
...     loss = learner.observe(batch)
>>> preds = learner.evaluate(test_batch)
"""
from __future__ import annotations

import math
import pathlib
from collections import defaultdict
from datetime import datetime
from random import randrange, random
from typing import Any, Dict, List, Mapping, Optional, Tuple

import torch
import torch.nn.functional as F
from torch import Tensor, nn
from torch_geometric.data import Batch, Data

from src.continual.learner.adapters import to_device
from src.continual.utils import set_random_seed


# --------------------------------------------------------------------------- #
# Memory Buffer – Reservoir sampling
# --------------------------------------------------------------------------- #
class ReservoirSamplingBuffer:
    """Task-agnostic replay buffer with **uniform reservoir sampling**."""

    def __init__(self, capacity: int, seed: int = 42) -> None:
        self.capacity = capacity
        self._data: List[Data] = []          # pyG Data objects (graphs)
        self._labels: List[Tensor] = []      # corresponding labels  (1-D tensor)
        self._task_ids: List[Optional[int]] = []
        set_random_seed(seed)
        self._seen = 0                       # total items seen

    # --------------------------------------------------------------------- #
    def __len__(self) -> int:  # noqa: D401
        return len(self._data)

    # --------------------------------------------------------------------- #
    def add(
        self,
        graphs: List[Data],
        labels: Tensor,
        task_ids: Optional[Tensor] = None,
    ) -> None:
        """Add a mini-batch to buffer (reservoir-sample each instance)."""
        labels = labels.view(-1)  # flatten
        if task_ids is not None:
            task_ids = task_ids.view(-1)
        for i, g in enumerate(graphs):
            y_i = labels[i].detach().cpu()
            t_i = int(task_ids[i]) if task_ids is not None else None
            self._add_single(g.detach().cpu(), y_i, t_i)

    def _add_single(self, g: Data, y: Tensor, task_id: Optional[int]) -> None:
        n = self._seen
        self._seen += 1
        if len(self) < self.capacity:
            self._data.append(g)
            self._labels.append(y)
            self._task_ids.append(task_id)
        else:
            j = randrange(n + 1)  # 0…n
            if j < self.capacity:
                self._data[j] = g
                self._labels[j] = y
                self._task_ids[j] = task_id

    # --------------------------------------------------------------------- #
    def sample(self, k: int, device: torch.device) -> Optional[Dict[str, Any]]:
        """Return a replay mini-batch dict or **None** if buffer empty."""
        if k == 0 or len(self) == 0:
            return None
        k = min(k, len(self))
        idx = torch.randperm(len(self))[:k].tolist()
        data_list = [self._data[i] for i in idx]
        y = torch.stack([self._labels[i] for i in idx]).to(device)
        task = (
            torch.tensor([self._task_ids[i] for i in idx], dtype=torch.long).to(device)
            if any(t is not None for t in self._task_ids)
            else None
        )
        batch = {
            "data": Batch.from_data_list(data_list).to(device),
            "y": y,
        }
        if task is not None:
            batch["task_id"] = task
        return batch


# --------------------------------------------------------------------------- #
# Rehearsal Learner
# --------------------------------------------------------------------------- #
class RehearsalLearner(nn.Module):
    """Experience-Replay continual learner."""

    def __init__(
        self,
        *,
        encoder: nn.Module,
        head: nn.Module | Mapping[int, nn.Module],
        mem_capacity: int = 10_000,
        replay_ratio: float = 1.0,            # β, e.g. 1.0 ⇒ |B_replay| ≈ |B_curr|
        lr: float = 3e-4,
        weight_decay: float = 1e-4,
        grad_clip: Optional[float] = 1.0,
        device: str | torch.device = "cuda",
        seed: int = 42,
    ) -> None:
        super().__init__()
        set_random_seed(seed)
        self.device = torch.device(device)

        # ---------------- modules ---------------- #
        self.encoder = encoder
        if isinstance(head, Mapping):
            self.head_bank = nn.ModuleDict({str(t): h for t, h in head.items()})
            self._shared_head = None
        else:
            self.head_bank = nn.ModuleDict()
            self._shared_head = head

        # ---------------- buffer ----------------- #
        self.buffer = ReservoirSamplingBuffer(mem_capacity, seed)

        self.replay_ratio = replay_ratio

        # ---------------- optim ------------------ #
        self.grad_clip = grad_clip
        self._optim = torch.optim.AdamW(
            [p for p in self.parameters() if p.requires_grad],
            lr=lr,
            weight_decay=weight_decay,
        )

        # move to device
        self.to(self.device)

    # --------------------------------------------------------------------- #
    # helpers
    # --------------------------------------------------------------------- #
    def _select_head(self, task_id: Optional[int]) -> nn.Module:
        if self._shared_head is not None:
            return self._shared_head
        if task_id is None:
            raise ValueError("task_id required when using per-task heads.")
        return self.head_bank[str(int(task_id))]

    # --------------------------------------------------------------------- #
    # main training step
    # --------------------------------------------------------------------- #
    def observe(self, batch: Dict[str, Any]) -> Tensor:
        """One training step with replay; returns total loss (detached)."""
        self.train()
        batch = to_device(batch, self.device)

        # ---------------- replay mix ---------------- #
        B_curr = batch["y"].shape[0]
        replay_k = int(math.ceil(self.replay_ratio * B_curr))
        replay_batch = self.buffer.sample(replay_k, self.device)
        if replay_batch is not None:
            mix_batch = {
                "data": Batch.from_data_list(
                    batch["data"].to_data_list() + replay_batch["data"].to_data_list()
                ).to(self.device),
                "y": torch.cat([batch["y"], replay_batch["y"]], 0),
            }
            if "task_id" in batch or (replay_batch and "task_id" in replay_batch):
                mix_batch["task_id"] = torch.cat(
                    [
                        batch.get("task_id", torch.full((B_curr,), -1, device=self.device)),
                        replay_batch.get(
                            "task_id",
                            torch.full((replay_k,), -1, device=self.device),
                        ),
                    ],
                    0,
                )
        else:
            mix_batch = batch

        # ---------------- forward ------------------- #
        z = self.encoder(mix_batch["data"])             # (B_total, D)
        head = self._select_head(mix_batch.get("task_id"))
        logits = head(z)
        y = mix_batch["y"].float().view_as(logits)
        loss = F.binary_cross_entropy_with_logits(logits, y)

        # ---------------- backward ------------------ #
        self._optim.zero_grad(set_to_none=True)
        loss.backward()
        if self.grad_clip is not None:
            nn.utils.clip_grad_norm_(self.parameters(), self.grad_clip)
        self._optim.step()

        # ---------------- buffer update ------------- #
        self.buffer.add(
            batch["data"].to_data_list(),
            batch["y"].detach().cpu(),
            task_ids=batch.get("task_id", None).detach().cpu()
            if "task_id" in batch
            else None,
        )
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
    # checkpoint util
    # --------------------------------------------------------------------- #
    def save(self, path: str | pathlib.Path) -> None:
        """Save model weights **and** replay buffer (graphs/labels)."""
        path = pathlib.Path(path)
        state = {
            "time": datetime.now().isoformat(),
            "model": self.state_dict(),
            "buffer_data": self.buffer._data,
            "buffer_labels": self.buffer._labels,
            "buffer_task_ids": self.buffer._task_ids,
            "buffer_seen": self.buffer._seen,
        }
        torch.save(state, path)

    def load(self, path: str | pathlib.Path) -> None:
        """Restore learner + buffer."""
        ckpt = torch.load(path, map_location="cpu", weights_only=False)
        self.load_state_dict(ckpt["model"])
        self.buffer._data = ckpt["buffer_data"]
        self.buffer._labels = ckpt["buffer_labels"]
        self.buffer._task_ids = ckpt["buffer_task_ids"]
        self.buffer._seen = ckpt["buffer_seen"]
        self.to(self.device)
