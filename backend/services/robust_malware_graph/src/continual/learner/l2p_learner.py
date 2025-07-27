# ---------------------------------------------------------------------------
# src/continual/learner/l2p_learner.py
# ---------------------------------------------------------------------------
"""Graph-aware **Learning-to-Prompt (L2P)** learner.

핵심 아이디어
-------------
1. **Frozen GNN** 백본 (ex. RGCNEncoder)으로부터 그래프 임베딩 `z ∈ ℝ^{B×D}` 획득. :contentReference[oaicite:0]{index=0}
2. 쿼리 `q = Proj(z)` 와 프롬프트 키 간 코사인 유사도 → top-k 소프트 Attention.
3. 가중 합·평균으로 얻은 `p_vec` 을 `z` 와 **additive fusion**: `ẑ = z + p_vec`.
4. Task-specific or shared **head**(s) 가 로짓 출력.
5. **EMA Prompt Pool** + 옵션 **cosine LR schedule** 로 온라인 스트림에서도 안정적.

전체 학습 파이프라인이 **torch_geometric** 그래프 배치(`Batch`)만 주입되면 돌아가도록 설계했습니다.
"""
from __future__ import annotations

import math
import pathlib
from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, List, Mapping, Optional

import torch
import torch.nn.functional as F
from torch import Tensor, nn
from torch.optim.lr_scheduler import CosineAnnealingWarmRestarts
from torch_geometric.data import Batch

from src.continual.learner.adapters import to_device
from src.continual.utils import Timer, set_random_seed   # 공통 헬퍼


# ---------------------------------------------------------------------------
# Prompt Pool
# ---------------------------------------------------------------------------
class PromptPool(nn.Module):
    """Learnable prompt vectors **and** keys (with optional EMA shadow copy)."""

    def __init__(
        self,
        num_prompts: int,
        prompt_len: int,
        dim: int,
        key_dim: Optional[int] = None,
        temperature: float = 0.07,
        ema_decay: Optional[float] = 0.999,
    ) -> None:
        super().__init__()
        key_dim = key_dim or dim
        self.prompt_len = prompt_len
        self.temperature = temperature
        self.ema_decay = ema_decay

        # N×L×D prompts / N×K keys
        self.prompts = nn.Parameter(torch.empty(num_prompts, prompt_len, dim))
        self.keys = nn.Parameter(torch.empty(num_prompts, key_dim))
        self.reset_parameters()

        if ema_decay is not None:
            self.register_buffer("prompts_m", self.prompts.data.clone())
            self.register_buffer("keys_m", self.keys.data.clone())

    # --------------------------------------------------------------------- #
    def reset_parameters(self) -> None:
        nn.init.kaiming_uniform_(self.prompts, a=math.sqrt(5))
        nn.init.kaiming_uniform_(self.keys, a=math.sqrt(5))

    # --------------------------------------------------------------------- #
    # EMA helpers
    # --------------------------------------------------------------------- #
    @torch.no_grad()
    def _momentum_update(self) -> None:
        if self.ema_decay is None:
            return
        for live, ema in ((self.prompts, self.prompts_m), (self.keys, self.keys_m)):
            ema.lerp_(live.data, 1.0 - self.ema_decay)

    def _params(self, use_ema: bool) -> tuple[Tensor, Tensor]:
        if use_ema and self.ema_decay is not None:
            return self.prompts_m, self.keys_m
        return self.prompts, self.keys

    # --------------------------------------------------------------------- #
    # forward
    # --------------------------------------------------------------------- #
    def forward(
        self,
        query: Tensor,             # (B, key_dim)
        top_k: int = 4,
        use_ema: bool = False,
    ) -> Tensor:                   # (B, prompt_len, dim)
        prompts, keys = self._params(use_ema)
        sim: Tensor = F.cosine_similarity(
            query.unsqueeze(1), keys.unsqueeze(0), dim=-1
        )                           # (B, N)

        # soft top-k selection
        top_sim, top_idx = sim.topk(top_k, dim=-1)          # (B, k)
        w = F.softmax(top_sim / self.temperature, dim=-1)   # (B, k)

        chosen = prompts[top_idx]                           # (B, k, L, D)
        w = w.unsqueeze(-1).unsqueeze(-1)                   # (B, k, 1, 1)
        agg = (chosen * w).sum(1)                           # (B, L, D)
        return agg                                          # keep seq dim


# ---------------------------------------------------------------------------
# L2P Learner
# ---------------------------------------------------------------------------
class L2PLearner(nn.Module):
    """Prompt-based learner for **online continual malware graph classification**."""

    # ------------------------------- #
    # constructor
    # ------------------------------- #
    def __init__(
        self,
        *,
        encoder: nn.Module,
        head: nn.Module | Mapping[int, nn.Module],
        dim: int = 256,
        key_dim: Optional[int] = None,
        num_prompts: int = 40,
        prompt_len: int = 5,
        top_k: int = 4,
        temperature: float = 0.07,
        ema_decay: Optional[float] = 0.999,
        lr: float = 3e-4,
        weight_decay: float = 1e-4,
        grad_clip: Optional[float] = 1.0,
        scheduler_t0: int = 500,
        device: str | torch.device = "cuda",
        seed: int = 42,
    ) -> None:
        super().__init__()
        set_random_seed(seed)
        self.device = torch.device(device)
        self.grad_clip = grad_clip
        self.top_k = top_k

        # ---------------- backbone (frozen) ---------------- #
        self.encoder = encoder.eval()
        for p in self.encoder.parameters():
            p.requires_grad = False

        # ---------------- prompt pool ---------------- #
        key_dim = key_dim or dim
        self.query_proj = (
            nn.Linear(dim, key_dim, bias=False) if key_dim != dim else nn.Identity()
        )
        self.prompt_pool = PromptPool(
            num_prompts, prompt_len, dim, key_dim, temperature, ema_decay
        )

        # ---------------- head(s) ---------------- #
        if isinstance(head, Mapping):
            # task-id → head dict
            self.head_bank = nn.ModuleDict(
                {str(t): h for t, h in head.items()}
            )
            self._shared_head = None
        else:
            self.head_bank = nn.ModuleDict()
            self._shared_head = head

        # ---------------- optim & sched ---------------- #
        self._optim = torch.optim.AdamW(
            list(self.prompt_pool.parameters())
            + list(self.query_proj.parameters())
            + list(self.head_bank.parameters())
            + ([] if self._shared_head is None else list(self._shared_head.parameters())),
            lr=lr,
            weight_decay=weight_decay,
        )
        self._sched = CosineAnnealingWarmRestarts(self._optim, T_0=scheduler_t0)

        # move to device
        self.to(self.device)

    # --------------------------------------------------------------------- #
    # low-level helpers
    # --------------------------------------------------------------------- #
    @torch.no_grad()
    def encode(self, graphs: Batch) -> Tensor:
        return self.encoder(graphs)

    def _prompt_vec(self, z: Tensor, ema: bool = False) -> Tensor:
        q = F.normalize(self.query_proj(z), dim=-1)        # (B, K)
        pv = self.prompt_pool(q, self.top_k, use_ema=ema)  # (B, L, D)
        return pv.mean(1)                                  # (B, D)

    def _select_head(self, task_id: Optional[int]) -> nn.Module:
        if self._shared_head is not None:
            return self._shared_head
        if task_id is None:
            raise ValueError("Task id must be provided when using task-specific heads.")
        return self.head_bank[str(int(task_id))]

    # --------------------------------------------------------------------- #
    # public API
    # --------------------------------------------------------------------- #
    def observe(self, batch: Dict[str, Any]) -> Tensor:
        """1-step online update. **Returns loss (detached).**"""
        batch = to_device(batch, self.device)
        self.train()

        z = self.encode(batch["data"])            # (B,D)
        p = self._prompt_vec(z)                   # (B,D)
        z_hat = z + p

        head = self._select_head(batch.get("task_id", None))
        logits = head(z_hat)

        y = batch["y"].float()
        if y.ndim == 1:
            y = y.unsqueeze(1)
        loss = F.binary_cross_entropy_with_logits(logits, y)

        self._optim.zero_grad(set_to_none=True)
        loss.backward()
        if self.grad_clip is not None:
            torch.nn.utils.clip_grad_norm_(
                self.parameters(), max_norm=self.grad_clip
            )
        self._optim.step()
        self._sched.step()
        with torch.no_grad():
            self.prompt_pool._momentum_update()

        return loss.detach()

    @torch.no_grad()
    def evaluate(
        self,
        batch: Dict[str, Any],
        *,
        ema_prompts: bool = True,
    ) -> Tensor:
        """Return sigmoid probs **without** gradient."""
        self.eval()
        batch = to_device(batch, self.device)

        z = self.encode(batch["data"])
        p = self._prompt_vec(z, ema_prompts)
        z_hat = z + p

        head = self._select_head(batch.get("task_id", None))
        return torch.sigmoid(head(z_hat))

    # --------------------------------------------------------------------- #
    # checkpoint util
    # --------------------------------------------------------------------- #
    def save(self, path: str | pathlib.Path) -> None:
        path = pathlib.Path(path)
        state = {
            "time": datetime.now().isoformat(),
            "prompt_pool": self.prompt_pool.state_dict(),
            "query_proj": self.query_proj.state_dict(),
            "head_bank": self.head_bank.state_dict(),
            "_shared_head": None
            if self._shared_head is None
            else self._shared_head.state_dict(),
        }
        torch.save(state, path)

    def load(self, path: str | pathlib.Path) -> None:
        path = pathlib.Path(path)
        state = torch.load(path, map_location="cpu", weights_only=False)
        self.prompt_pool.load_state_dict(state["prompt_pool"])
        self.query_proj.load_state_dict(state["query_proj"])
        self.head_bank.load_state_dict(state["head_bank"])
        if self._shared_head is not None and state["_shared_head"] is not None:
            self._shared_head.load_state_dict(state["_shared_head"])

    # --------------------------------------------------------------------- #
    # stats / debug
    # --------------------------------------------------------------------- #
    @torch.no_grad()
    def prompt_usage_hist(self, dataloader) -> Dict[int, int]:
        """Return histogram of prompt indices chosen over dataloader."""
        self.eval()
        hist: defaultdict[int, int] = defaultdict(int)
        for batch in dataloader:
            batch = to_device(batch, self.device)
            z = self.encode(batch["data"])
            q = F.normalize(self.query_proj(z), dim=-1)
            _, keys = self.prompt_pool._params(use_ema=True)
            sim = F.cosine_similarity(q.unsqueeze(1), keys.unsqueeze(0), dim=-1)
            top_idx: Tensor = sim.topk(self.top_k, dim=-1).indices  # (B,k)
            for idx in top_idx.flatten().tolist():
                hist[int(idx)] += 1
        return dict(hist)
