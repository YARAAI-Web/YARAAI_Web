# ---------------------------------------------------------------------------
# src/continual/learner/adapters.py
# ---------------------------------------------------------------------------
"""Utility helpers that are reused across different *online* continual learning
learners (SupCon, Rehearsal, EWC, L2P …).

The functions in this module are intentionally **framework-agnostic** (plain
PyTorch + torch_geometric) so that learners can mix-and-match them without
pulling additional heavy dependencies.

Key conventions
---------------
* Every *sample* coming from a ``GraphStream`` is a dict with at least
  ``data`` (``torch_geometric.data.Data`` **or** ``torch_geometric.data.HeteroData``)
  and ``y`` (torch.Tensor).  Additional keys (``task_id``, ``meta`` …) are kept
  untouched and propagated when collating.
* Learners call :func:`to_device` before the forward pass so that every nested
  tensor ends up on the correct CUDA device.
* SupCon / contrastive learners often need *two* augmented views of the same
  graph in the batch.  When ``batch`` already contains a ``views`` key we
  concatenate the views along the batch dimension so that a single forward pass
  produces 2× embeddings (B, 2, D).
"""
from __future__ import annotations

import copy
from typing import Any, Dict, List, Sequence

import torch
from torch_geometric.data import Batch, Data, HeteroData

__all__ = [
    "collate_graphs",
    "to_device",
    "freeze_except",
]

def _collate_pyG_graphs(graphs: Sequence[Data | HeteroData]) -> Batch:
    """Collate a list of PyG ``Data``/**HeteroData** into a single ``Batch``.

    Unlike the vanilla ``torch_geometric.data.Batch.from_data_list`` this helper
    keeps ``type`` information so that encoders expecting ``HeteroData`` still
    work after batching.
    """
    if all(isinstance(g, HeteroData) for g in graphs):
        return Batch.from_data_list(graphs, follow_batch=[])
    if all(isinstance(g, Data) for g in graphs):
        return Batch.from_data_list(graphs)  # type: ignore[arg-type]
    raise TypeError("Mixing Data and HeteroData is not supported.")

def collate_graphs(samples: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Custom ``DataLoader`` ``collate_fn`` for a list of samples coming from a
    :class:`~src.continual.datastream.stream.GraphStream`.

    The returned dict has **identical** keys – except that all PyG graphs are
    merged into a single large :class:`torch_geometric.data.Batch` so that the
    downstream learner can feed it to the encoder in one shot.
    """
    batch: Dict[str, Any] = {}
    # 1. Separate graphs and non-graph fields
    graphs: List[Data | HeteroData] = []
    for sample in samples:
        g = sample["data"]
        assert isinstance(g, (Data, HeteroData)), "sample['data'] must be a PyG graph"
        graphs.append(g)
    batch["data"] = _collate_pyG_graphs(graphs)

    # 2. Remaining keys are stacked when possible (Tensor) or copied into list
    for k in samples[0].keys():
        if k == "data":
            continue
        vals = [s[k] for s in samples]
        if torch.is_tensor(vals[0]):
            batch[k] = torch.stack(vals)
        else:
            batch[k] = vals  # keep as Python list (task_id, str …)
    return batch

def to_device(obj: Any, device: torch.device | str) -> Any:  # noqa: ANN401 – recursive
    """Recursively move all tensors inside *obj* to *device*.

    * **torch.Tensor** → ``tensor.to(device, non_blocking=True)``
    * **dict / list / tuple** → recurse element-wise
    * anything else → returned unchanged (int, str …)
    """
    if torch.is_tensor(obj):
        return obj.to(device, non_blocking=True)
    if isinstance(obj, dict):
        return {k: to_device(v, device) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return type(obj)(to_device(v, device) for v in obj)
    return obj

def freeze_except(model: torch.nn.Module, trainable_substrings: Sequence[str] | None = None) -> None:
    """Freeze *all* parameters **except** those whose *name* contains one of the
    provided *trainable_substrings*.

    Examples
    --------
    >>> freeze_except(model, ["prompt_embeddings", "head"])
    """
    for n, p in model.named_parameters():
        p.requires_grad = bool(trainable_substrings and any(s in n for s in trainable_substrings))

# ---------------------------------------------------------------------------
# src/continual/learner/l2p_learner.py
# ---------------------------------------------------------------------------
"""Prompt-based continual learner *à la* **Learning to Prompt (L2P, ECCV ’22)**.

L2P freezes the *backbone* encoder and learns a *pool* of task-agnostic prompt
vectors that are **prepended** to the input representation.  At inference time
only the *top-k* prompts (based on key–query similarity) are selected so that
*each sample* dynamically chooses the most relevant context.

In the malware-graph setting we prepend the prompts to the *graph embedding*
``z ∈ ℝ^{B×D}`` produced by :class:`src.models.gnn.encoder.RGCNEncoder`.  The
prompt vectors are learnable parameters just like in the vision/text versions.
"""
from __future__ import annotations

import math
from typing import Any, Dict

import torch
import torch.nn.functional as F
from torch import nn
from torch_geometric.data import Batch

from .adapters import to_device

__all__ = ["L2PLearner"]

class PromptPool(nn.Module):
    """Simple prompt pool with *N* prompts (length = ``prompt_len``) and *N* keys."""

    def __init__(self, num_prompts: int, prompt_len: int, dim: int, key_dim: int | None = None):
        super().__init__()
        self.prompt_len = prompt_len
        self.dim = dim
        self.num_prompts = num_prompts
        key_dim = key_dim or dim
        # P ∈ ℝ^{N × L × D}
        self.prompts = nn.Parameter(torch.randn(num_prompts, prompt_len, dim) * 0.02)
        # K ∈ ℝ^{N × key_dim}
        self.keys = nn.Parameter(torch.randn(num_prompts, key_dim) * 0.02)
        nn.init.kaiming_uniform_(self.prompts, a=math.sqrt(5))
        nn.init.kaiming_uniform_(self.keys, a=math.sqrt(5))

    def forward(self, query: torch.Tensor, top_k: int) -> torch.Tensor:
        """Return the concatenated prompts ``(B, top_k·L, D)`` for a given query ``(B, key_dim)``."""
        # cosine similarity — we detach query so gradients flow only to prompts & keys
        sim = F.cosine_similarity(query.unsqueeze(1), self.keys.unsqueeze(0), dim=-1)  # (B, N)
        idx = sim.topk(top_k, dim=-1).indices  # (B, k)
        chosen = self.prompts[idx]  # (B, k, L, D)
        return chosen.flatten(1, 2)  # (B, k·L, D)

class L2PLearner(nn.Module):
    """Online continual learner that adapts **only** prompt vectors (frozen backbone)."""

    def __init__(
        self,
        encoder: nn.Module,
        head: nn.Module,
        dim: int = 256,
        num_prompts: int = 30,
        prompt_len: int = 5,
        top_k: int = 3,
        lr: float = 1e-3,
        device: str | torch.device = "cuda",
    ) -> None:
        super().__init__()
        self.encoder = encoder.eval()  # we freeze backbone (no grad)
        for p in self.encoder.parameters():
            p.requires_grad = False

        self.prompt_pool = PromptPool(num_prompts, prompt_len, dim)
        self.head = head  # e.g. BinaryHead / MultiLabelHead
        self.top_k = top_k
        self.device = torch.device(device)

        # Optimizer – only prompt params + head
        self._optimizer = torch.optim.Adam(
            list(self.prompt_pool.parameters()) + list(self.head.parameters()), lr=lr
        )

    @torch.no_grad()
    def encode(self, batched_graph: Batch) -> torch.Tensor:
        """Frozen backbone forward (no grad, saves VRAM)."""
        return self.encoder(batched_graph)

    def _forward_with_prompts(self, z: torch.Tensor) -> torch.Tensor:
        prompt = self.prompt_pool(z.detach(), self.top_k)  # (B, k·L, D)
        prompt_vec = prompt.mean(dim=1)  # (B, D)
        z_aug = z + prompt_vec
        return self.head(z_aug)

    def observe(self, batch: Dict[str, Any]) -> torch.Tensor:  # training step
        batch = to_device(batch, self.device)
        self.train()
        z = self.encode(batch["data"])
        logits = self._forward_with_prompts(z)
        y = batch["y"].float()
        if y.ndim == 1:
            y = y.unsqueeze(1)
        loss = F.binary_cross_entropy_with_logits(logits, y)
        self._optimizer.zero_grad(set_to_none=True)
        loss.backward()
        self._optimizer.step()
        return loss.detach()

    @torch.no_grad()
    def evaluate(self, batch: Dict[str, Any]) -> torch.Tensor:
        self.eval()
        batch = to_device(batch, self.device)
        z = self.encode(batch["data"])
        logits = self._forward_with_prompts(z)
        return torch.sigmoid(logits)

    # ---------------------------------------------------------------------
    # state-dict utils so that Checkpointer can treat learner as 1 module
    # ---------------------------------------------------------------------
    def state_dict(self, *args, **kwargs):  # noqa: D401
        return {
            "prompt_pool": self.prompt_pool.state_dict(*args, **kwargs),
            "head": self.head.state_dict(*args, **kwargs),
        }

    def load_state_dict(self, state_dict: dict, *args, **kwargs):  # noqa: D401
        self.prompt_pool.load_state_dict(state_dict["prompt_pool"], *args, **kwargs)
        self.head.load_state_dict(state_dict["head"], *args, **kwargs)

# ---------------------------------------------------------------------------
# src/continual/learner/supcon_cl.py
# ---------------------------------------------------------------------------
"""Online **Supervised Contrastive Learning (SupCon)** learner for malware graphs.

This learner performs *online* supervised contrastive training with a small
ring-buffer replay memory so that embeddings remain linearly separable across
the ever-growing label space.  It follows the algorithmic template introduced
in *Khosla et al., 2020* but tailored for graph data streams.

Workflow
~~~~~~~~
1. Each incoming *sample* provides **two augmented views** of the same graph in
   ``batch["views"]`` with shape *(2B, …)* — created by the graph augmentation
   pipeline (RandomEdgeDrop, AttrMask …).
2. A frozen *projection head* maps encoder outputs ``z ∈ ℝ^{B×D}`` to
   ``h ∈ ℝ^{B×d_proj}`` where the contrastive loss is computed.
3. The **NT-Xent loss** is extended with label masks so that *only* positives
   sharing the same class contribute.
4. A **ring buffer** of past projected embeddings & labels (size = ``mem_size``)
   is appended to every mini-batch, enabling *replay-augmented* contrast.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Tuple

import torch
import torch.nn.functional as F
from torch import nn
from torch_geometric.data import Batch

from .adapters import to_device

try:
    # Local import (✱ optional – fallback to internal implementation below ✱)
    from src.models.contrast.sup_con import SupContrastHead  # type: ignore
except Exception:  # pragma: no cover – unit tests use minimal fallback

    class SupContrastHead(nn.Module):
        """Minimal NT-Xent loss implementation (label-aware)."""

        def __init__(self, temperature: float = 0.07):
            super().__init__()
            self.temperature = temperature

        def forward(self, h: torch.Tensor, y: torch.Tensor) -> torch.Tensor:  # (2B, d)
            h = F.normalize(h, dim=-1, p=2)
            sim = torch.matmul(h, h.T) / self.temperature  # (2B, 2B)
            # positive mask – exclude self-pairs, keep same-label pairs
            pos_mask = (y.unsqueeze(0) == y.unsqueeze(1)) & (~torch.eye(len(y), dtype=torch.bool, device=y.device))
            neg_mask = ~pos_mask
            log_prob = F.log_softmax(sim * neg_mask.float(), dim=1)
            loss = -(log_prob * pos_mask.float()).sum(1) / pos_mask.sum(1).clamp(min=1)
            return loss.mean()

__all__ += ["SupConLearner"]

class RingBuffer:
    """Reservoir-style replay buffer storing **projected embeddings** & labels."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._embeds: List[torch.Tensor] = []
        self._labels: List[torch.Tensor] = []
        self._n_seen = 0

    def push(self, h: torch.Tensor, y: torch.Tensor) -> None:  # h: (B, d)
        for e, l in zip(h.detach().cpu(), y.detach().cpu()):
            self._n_seen += 1
            if len(self._embeds) < self.capacity:
                self._embeds.append(e)
                self._labels.append(l)
            else:
                idx = random.randrange(self._n_seen)
                if idx < self.capacity:
                    self._embeds[idx] = e
                    self._labels[idx] = l

    def sample(self, k: int) -> Tuple[torch.Tensor, torch.Tensor]:
        if len(self._embeds) == 0:
            return torch.empty(0), torch.empty(0)
        k = min(k, len(self._embeds))
        idx = random.sample(range(len(self._embeds)), k)
        embeds = torch.stack([self._embeds[i] for i in idx], dim=0)
        labels = torch.stack([self._labels[i] for i in idx], dim=0)
        return embeds, labels

class SupConLearner(nn.Module):
    """Supervised Contrastive learner with replay for continual streams."""

    def __init__(
        self,
        encoder: nn.Module,
        dim: int = 256,
        proj_dim: int = 128,
        temperature: float = 0.07,
        mem_size: int = 2048,
        mem_mini_batch: int = 256,
        lr: float = 3e-4,
        device: str | torch.device = "cuda",
    ) -> None:
        super().__init__()
        self.encoder = encoder
        self.proj = nn.Sequential(
            nn.Linear(dim, dim), nn.ReLU(inplace=True), nn.Linear(dim, proj_dim, bias=False)
        )
        self.supcon = SupContrastHead(temperature)

        self.buffer = RingBuffer(mem_size)
        self.mem_mini_batch = mem_mini_batch

        self.device = torch.device(device)
        self._optimizer = torch.optim.Adam(self.parameters(), lr=lr)

    def _project(self, z: torch.Tensor) -> torch.Tensor:
        return self.proj(z)

    def _forward_views(self, graphs: Batch) -> torch.Tensor:  # (2B, d_proj)
        z = self.encoder(graphs)  # (2B, dim)
        return self._project(z)

    def observe(self, batch: Dict[str, Any]) -> torch.Tensor:
        """Perform one SupCon update with replay."""
        batch = to_device(batch, self.device)
        self.train()
        views: Batch = batch["views"]  # (2B, …) already concatenated by collate_fn
        y: torch.Tensor = batch["y"].repeat_interleave(2).to(self.device)  # (2B,)

        h = self._forward_views(views)

        # sample memory & concat
        h_mem, y_mem = self.buffer.sample(self.mem_mini_batch)
        if h_mem.numel():
            h_mem, y_mem = h_mem.to(self.device), y_mem.to(self.device)
            h_all = torch.cat([h_mem, h], dim=0)
            y_all = torch.cat([y_mem, y], dim=0)
        else:
            h_all, y_all = h, y

        loss = self.supcon(h_all, y_all)

        self._optimizer.zero_grad(set_to_none=True)
        loss.backward()
        self._optimizer.step()

        # update buffer with *current* batch (use *projected* embeds)
        with torch.no_grad():
            self.buffer.push(h.detach().cpu(), y.detach().cpu())
        return loss.detach()

    @torch.no_grad()
    def evaluate(self, batch: Dict[str, Any]) -> torch.Tensor:
        """Return *projected* embeddings for external evaluator (k-NN, linear …)."""
        self.eval()
        batch = to_device(batch, self.device)
        views: Batch = batch["views"]
        h = self._forward_views(views)  # (2B, d_proj)
        return h.mean(0)  # cheap trick: average the two views
