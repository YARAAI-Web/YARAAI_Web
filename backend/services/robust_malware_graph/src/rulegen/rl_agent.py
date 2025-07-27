#  ───────────────────────────────────────────────────────────────
#  robust-malware-graph / src / rulegen / rl_agent.py
#  ───────────────────────────────────────────────────────────────
"""
PPORuleAgent
============

• 목적
    - `rl_env.RuleGenEnv`에 대해 **PPO‑Clip** 알고리즘으로
      토큰‑수준 YARA/CAPA 룰 생성 정책을 학습한다.

• 특징
    ─────────────────────────────────────────────────────────────
    1. ***의존성 최소화***
       Stable‑Baselines3 대신 **pure‑PyTorch** 구현
       (torch≥2.1, gymnasium≥0.29, numpy).

    2. ***시퀀스 관측 처리***
       관측값(obs)은 길이 `max_len`의 토큰 ID 배열.
       ‑ 전체 시퀀스를 GRU에 통과시켜 마지막 hidden state를
         상태 표현으로 사용한다.

    3. ***정책 네트워크***
       `Embedding` → `LayerNorm` → `GRU`(1 layer, hidden=256) →
       (a) **Policy head** (logits), (b) **Value head** (V(s)).

    4. ***학습 루프***
       ‑ Rollout n_steps 수집 → GAE(λ) ADV 계산 →
         미니배치 다중 epoch으로 **clip objective** 업데이트.
       ‑ `entropy_coef`, `vf_coef` 등 하이퍼파라미터 configurable.

    5. ***저장·재시작***
       `save(path)` / `load(path)` 제공. policy state_dict만 저장하므로
       가볍고 호환성 ↑.

    6. ***로깅***
       프로젝트 전역 `common.logger` 존재 시 활용,
       없으면 Python 기본 `logging`.

    7. ***스모크 테스트***
       `python -m rulegen.rl_agent --smoke_test` 한 줄로
       3 000 스텝 학습을 돌려 reward가 + 증가하는지 확인 가능.
"""

from __future__ import annotations

import argparse
import logging
import math
from pathlib import Path
from typing import Dict, List, Tuple, Sequence, Optional

import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


from common.utils import set_random_seed, tqdm_wrap

# ───────────────────────────── 내부 모듈
try:
    from common.logger import get_logger  # type: ignore
except ModuleNotFoundError:

    def get_logger(name: str):
        logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
        return logging.getLogger(name)

try:
    from transformers import GPT2LMHeadModel, BitsAndBytesConfig
except ModuleNotFoundError:
    GPT2LMHeadModel = None
    BitsAndBytesConfig = None  # type: ignore


from .rl_env import RuleGenEnv
# NOTE: lora utilities live under the project `src` package. When
# running the CLI with `PYTHONPATH=src` or after installing the
# package, they are available as ``src.models``. Importing from the
# top-level ``models`` package would fail because that directory is
# reserved for checkpoints and does not contain code.
from src.models.lora_utils import apply_lora_gpt2
from lr_scheduler import build_warm_cosine

_LOG = get_logger(__name__)


# ╔══════════════════════════════════════════════════════════════╗
# ║                     Policy 네트워크 정의                     ║
# ╚══════════════════════════════════════════════════════════════╝
class GRUPolicy(nn.Module):
    """
    Token‑sequence 관측용 간단 GRU Actor‑Critic.
    """

    def __init__(
        self,
        vocab_size: int,
        embed_dim: int = 128,
        hidden_size: int = 256,
        gru_layers: int = 1,
        use_hint: bool = False,
        hint_size: int | None = None,
        pad_id: int = 0,
    ):
        super().__init__()
        self.pad_id = pad_id
        self.embed = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_id)
        self.ln = nn.LayerNorm(embed_dim)
        self.use_hint = use_hint
        self.hint_size = hint_size
        self.hint_proj: nn.Module | None = None
        if self.use_hint and self.hint_size is not None:
            # If hint_size is provided, expect a vector input of that size
            # Map it to the embedding dimension via a learnable projection
            self.hint_proj = nn.Linear(hint_size, embed_dim)
        self.gru = nn.GRU(
            input_size=embed_dim * (2 if use_hint else 1),
            hidden_size=hidden_size,
            num_layers=gru_layers,
            batch_first=True,
        )
        self.pi_head = nn.Linear(hidden_size, vocab_size)
        self.v_head = nn.Linear(hidden_size, 1)
        self.aux_head = nn.Linear(hidden_size, 2)

        # Orthogonal init (Amodei et al. 2016 style)
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.orthogonal_(m.weight, gain=math.sqrt(2))
                nn.init.zeros_(m.bias)
        nn.init.orthogonal_(self.pi_head.weight, gain=0.01)

    def encode(
        self,
        obs: torch.Tensor,
        hint: torch.Tensor | None = None,
    ) -> torch.Tensor:
        """Return final hidden state for a batch of token sequences."""
        self.gru.flatten_parameters()
        mask = obs != self.pad_id
        if mask.ndim == 1:
            mask = mask.unsqueeze(0)
            obs = obs.unsqueeze(0)
            if hint is not None and hint.ndim == 1:
                hint = hint.unsqueeze(0)
        x = self.embed(obs)
        x = self.ln(x)
        lengths = mask.sum(dim=1).clamp(min=1)

        if self.use_hint:
            if self.hint_size is None:
                if hint is None:
                    hint_vec = torch.zeros(x.size(0), x.size(2), device=x.device, dtype=x.dtype)
                else:
                    hint_vec = self.embed(hint.long()).mean(dim=1)
            else:
                if hint is None:
                    hint_input = torch.zeros((x.size(0), self.hint_size), device=x.device, dtype=x.dtype)
                else:
                    hint_input = hint.unsqueeze(0) if hint.ndim == 1 else hint
                    hint_input = hint_input.to(x.dtype)
                hint_vec = self.hint_proj(hint_input)

            hint_seq = hint_vec.unsqueeze(1).expand(-1, x.size(1), -1)
            x = torch.cat([x, hint_seq], dim=2).contiguous()

        x_packed = nn.utils.rnn.pack_padded_sequence(
            x, lengths.cpu(), batch_first=True, enforce_sorted=False
        )
        _, h_n = self.gru(x_packed)
        h = h_n[-1]
        return h

    def forward(
        self,
        obs: torch.Tensor,
        hint: torch.Tensor | None = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Parameters
        ----------
        obs : LongTensor  (B, L)  token IDs padded

        Returns
        -------
        logits : (B, vocab_size)
        value  : (B, 1)
        """
        h = self.encode(obs, hint)
        logits = self.pi_head(h)
        value = self.v_head(h).squeeze(-1)
        return logits, value


class GPTPolicy(nn.Module):
    """GPT‑based policy network."""

    def __init__(
        self,
        env: RuleGenEnv,
        policy_net: str = "gpt2",
        *,
        checkpoint_layers: bool = False,
        load_4bit: bool = False,
        load_8bit: bool = False,
    ):
        super().__init__()
        self.env = env

        qconfig = None
        if load_4bit or load_8bit:
            if BitsAndBytesConfig is None:
                raise RuntimeError("bitsandbytes is required for quantized loading")
            qconfig = BitsAndBytesConfig(load_in_4bit=load_4bit, load_in_8bit=load_8bit)

        self.gpt = GPT2LMHeadModel.from_pretrained(policy_net, quantization_config=qconfig)
        if checkpoint_layers and hasattr(self.gpt, "gradient_checkpointing_enable"):
            self.gpt.gradient_checkpointing_enable()
        self.gpt.resize_token_embeddings(len(self.env.tokenizer))
        self.value_head = nn.Linear(self.gpt.config.hidden_size, 1)
        self.hint_size = None

    def forward(self, obs: torch.Tensor, hint: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        # hint is not used by the GPT policy, but is kept for API compatibility
        outputs = self.gpt(input_ids=obs, output_hidden_states=True)
        logits = outputs.logits
        value = self.value_head(outputs.hidden_states[-1])
        return logits[:, -1, :], value[:, -1]


class GPTCritic(nn.Module):
    """GPT‑based critic network."""

    def __init__(self, policy: GPTPolicy):
        super().__init__()
        self.gpt = policy.gpt  # Share the same GPT model
        self.value_head = nn.Linear(self.gpt.config.hidden_size, 1)

    def forward(self, obs: torch.Tensor) -> torch.Tensor:
        outputs = self.gpt(input_ids=obs, output_hidden_states=True)
        value = self.value_head(outputs.hidden_states[-1])
        return value[:, -1]


# ╔══════════════════════════════════════════════════════════════╗
# ║                         PPO Agent                           ║
# ╚══════════════════════════════════════════════════════════════╝
class PPORuleAgent:
    """
    Pure‑PyTorch PPO‑Clip 구현.
    """

    def __init__(
        self,
        env: gym.Env,
        *,
        policy_net: str = "gru",
        gamma: float = 0.99,
        gae_lambda: float = 0.9,
        clip_eps: float = 0.1,
        lr: float = 1e-4,
        schedule_type: str | None = None,
        total_updates: int | None = None,
        vf_coef: float = 0.5,
        entropy_coef: float = 0.05,
        entropy_coef_final: float = 0.01,
        entropy_coef_steps: int | None = None,
        max_grad_norm: float = 0.5,
        n_steps: int = 1024,
        n_epochs: int = 4,
        batch_size: int = 256,
        minibatch_size: int = 64,
        accum_steps: int = 1,
        device: str | torch.device = "cuda" if torch.cuda.is_available() else "cpu",
        use_hint: bool = False,
        use_amp: bool = False,
        checkpoint_layers: bool = False,
        load_4bit: bool = False,
        load_8bit: bool = False,
        lora_cfg: dict | None = None,
        seed: int = 2024,
        constraint_thresh: float = 0.5,
        lagrange_lr: float = 0.05,
        init_lagrange_multiplier: float = 1.0,
    ):
        set_random_seed(seed)
        self.env = env
        self.gamma = gamma
        self.gae_lambda = gae_lambda
        self.clip_eps = clip_eps
        self.vf_coef = vf_coef
        self.entropy_coef = entropy_coef
        self.entropy_coef_init = entropy_coef
        self.entropy_coef_final = entropy_coef_final
        self.entropy_coef_steps = (
            int(entropy_coef_steps) if entropy_coef_steps is not None else None
        )
        self.max_grad_norm = max_grad_norm
        self.n_steps = n_steps
        self.n_epochs = n_epochs
        self.batch_size = batch_size
        self.minibatch_size = minibatch_size
        self.accum_steps = max(1, accum_steps)

        self.device = torch.device(device)
        self.use_hint = use_hint
        self.use_amp = use_amp
        self.scaler = torch.amp.GradScaler("cuda", enabled=self.use_amp)
        self.checkpoint_layers = checkpoint_layers
        self.load_4bit = load_4bit
        self.load_8bit = load_8bit
        self.lora_cfg = lora_cfg

        self.constraint_thresh = constraint_thresh
        self.lagrange_lr = lagrange_lr
        self.lagrange_multiplier = init_lagrange_multiplier

        self.policy_net = policy_net

        if policy_net.lower() == "gru":
            self.policy = GRUPolicy(
                vocab_size=env.action_space.n,
                embed_dim=128,
                hidden_size=256,
                use_hint=use_hint,
                pad_id=env.token2id[env.PAD],
            ).to(self.device)
            # --------------------------------------------------------------
            # Optional: initialise embeddings from classifier encoder
            enc = getattr(env, "classifier", None)
            meta = getattr(getattr(enc, "encoder", None), "meta_embed", None)
            if meta is not None:
                attr_vocab = getattr(enc.encoder, "attr_vocab", None)
                if isinstance(attr_vocab, dict):
                    src_dim = meta.weight.size(1)
                    dst_dim = self.policy.embed.weight.size(1)
                    for tok, tid in env.token2id.items():
                        aid = attr_vocab.get(tok)
                        if aid is None:
                            continue
                        vec = meta.weight[aid].detach()
                        if src_dim == dst_dim:
                            new_vec = vec
                        elif src_dim < dst_dim:
                            new_vec = torch.zeros(dst_dim, device=vec.device, dtype=vec.dtype)
                            new_vec[:src_dim] = vec
                        else:  # src_dim > dst_dim
                            proj_w = torch.empty(dst_dim, src_dim, device=vec.device, dtype=vec.dtype)
                            nn.init.xavier_uniform_(proj_w)
                            new_vec = torch.matmul(proj_w, vec)
                        with torch.no_grad():
                            self.policy.embed.weight[tid] = new_vec
            self.policy.gru.flatten_parameters()
        elif policy_net.lower() == "attn":
            from models.attn_policy import AttnPolicy

            self.policy = AttnPolicy(
                vocab_size=env.action_space.n,
                embed_dim=128,
                hidden_size=256,
                use_hint=use_hint,
                pad_id=env.token2id[env.PAD],
            ).to(self.device)
        else:
            _LOG.info("Using GPT policy: %s", policy_net)
            self.policy = GPTPolicy(
                env,
                policy_net=policy_net,
                checkpoint_layers=self.checkpoint_layers,
                load_4bit=self.load_4bit,
                load_8bit=self.load_8bit,
            ).to(self.device)
            if self.lora_cfg is not None:
                try:
                    self.policy.gpt = apply_lora_gpt2(self.policy.gpt, self.lora_cfg)
                except Exception as exc:  # pragma: no cover - optional dep
                    _LOG.error("Failed to apply LoRA: %s", exc)
            self.critic = GPTCritic(self.policy).to(self.device)

        self.optimizer = torch.optim.Adam(self.policy.parameters(), lr=lr)

        self.scheduler: torch.optim.lr_scheduler.LRScheduler | None = None
        if schedule_type:
            if total_updates is None:
                raise ValueError("total_updates must be provided when using a scheduler")
            if schedule_type == "linear":
                lr_lambda = lambda step: 1 - min(step, total_updates) / float(total_updates)
                self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lr_lambda)
            elif schedule_type == "cosine":
                self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                    self.optimizer, T_max=total_updates
                )
            elif schedule_type == "warmcos":
                self.scheduler = build_warm_cosine(
                    self.optimizer,
                    warmup_steps=5000,
                    total_steps=total_updates,
                )
            else:
                raise ValueError(f"Unknown schedule_type '{schedule_type}'")

        # rollout storage
        self.reset_rollout_buffers()

        # flag for dynamic max_len updates
        self._max_len_updated = False

    # ──────────────────────────────── rollout helpers ───────────
    def reset_rollout_buffers(self):
        self.obs_buf: List[np.ndarray] = []
        self.act_buf: List[np.ndarray] = []
        self.logp_buf: List[np.ndarray] = []
        self.rew_buf: List[float] = []
        self.done_buf: List[bool] = []
        self.val_buf: List[float] = []
        if self.use_hint:
            self.hint_buf: List[np.ndarray] = []
        self.f1_buf: List[float] = []
        self.f1_dummy_buf: List[float] = []

    def pretrain(
        self,
        dataset: Sequence[Tuple[Sequence[int], int]],
        *,
        epochs: int = 1,
        batch_size: int = 64,
        lr: float | None = None,
    ) -> None:
        """Warm-start the policy on a labeled rule dataset."""
        pad_id = self.env.token2id.get(self.env.PAD, 0)

        def collate(batch: Sequence[Tuple[Sequence[int], int]]):
            seqs, labels = zip(*batch)
            seq_t = [torch.tensor(s, dtype=torch.long) for s in seqs]
            obs = nn.utils.rnn.pad_sequence(seq_t, batch_first=True, padding_value=pad_id)
            lbl = torch.tensor(labels, dtype=torch.long)
            return obs, lbl

        loader = torch.utils.data.DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=True,
            collate_fn=collate,
        )

        opt = torch.optim.Adam(self.policy.parameters(), lr=lr or self.optimizer.param_groups[0]["lr"])
        loss_fn = nn.CrossEntropyLoss()
        self.policy.train()
        for _ in range(epochs):
            for obs, lbl in loader:
                obs = obs.to(self.device)
                lbl = lbl.to(self.device)
                h = self.policy.encode(obs)
                logits = self.policy.aux_head(h)
                loss = loss_fn(logits, lbl)
                opt.zero_grad()
                loss.backward()
                opt.step()

    @torch.no_grad()
    def select_action(
        self,
        obs: np.ndarray,
        hint_obs: np.ndarray | None = None,
    ) -> Tuple[int, float, float]:
        """
        Returns
        -------
        action, log_prob, value
        """
        obs_t = torch.from_numpy(obs).long().unsqueeze(0).to(self.device)
        if hint_obs is not None:
            hint_t = torch.from_numpy(hint_obs).unsqueeze(0).to(self.device)
            if self.policy.hint_size is None:
                hint_t = hint_t.long()
            else:
                hint_t = hint_t.to(torch.float32)
        else:
            hint_t = None
        logits, value = self.policy(obs_t, hint_t)
        mask = self.env.get_action_mask()
        logits = logits + torch.where(
            torch.from_numpy(mask).to(self.device) > 0,
            0.0,
            -1e9,
        )
        dist = torch.distributions.Categorical(logits=logits)
        action = dist.sample()
        log_prob = dist.log_prob(action)
        return (
            int(action.item()),
            float(log_prob.item()),
            float(value.item()),
        )

    # ─────────────────────────────── main training loop ─────────
    def train(
        self,
        total_timesteps: int,
        log_interval: int = 10_000,
        save_path: str | Path | None = None,
        *,
        pretrain_dataset: Sequence[Tuple[Sequence[int], int]] | None = None,
        pretrain_epochs: int = 1,
        phase_schedule: dict | None = None,
        auto_adjust: dict | None = None,
    ) -> List[Tuple[int, float]]:
        """Run the main PPO loop.

        Returns
        -------
        List of ``(step, avg_return)`` logged at each ``log_interval``.

        Parameters
        ----------
        auto_adjust : optional mapping
            If provided, automatically adjust reward weights when the average
            ``f1_dummy`` from the recent rollout falls below ``threshold``.
        """
        obs, info = self.env.reset()
        hint = info.get("hint")
        global_step = 0
        pbar = tqdm_wrap(range(total_timesteps), desc="train", unit="step")
        episode_returns: List[float] = []
        interval_returns: List[float] = []
        avg_history: List[Tuple[int, float]] = []
        ep_return = 0.0

        threshold = None
        delta_dummy = 0.0
        delta_clean = 0.0
        if auto_adjust:
            threshold = float(auto_adjust.get("threshold", 0.0))
            delta_dummy = float(auto_adjust.get("delta_f1_dummy", 0.0))
            delta_clean = float(auto_adjust.get("delta_f1_clean", 0.0))

        switch_step = None
        phase2 = {}
        if phase_schedule:
            switch_step = int(phase_schedule.get("switch_step", total_timesteps))
            phase1 = phase_schedule.get("phase1", {})
            phase2 = phase_schedule.get("phase2", {})
            if "reward_weights" in phase1:
                self.env.reward_weights = dict(phase1["reward_weights"])
            if "fp_penalty_start" in phase1:
                self.env.fp_penalty_start = float(phase1["fp_penalty_start"])
            if "fp_penalty_end" in phase1:
                self.env.fp_penalty_end = float(phase1["fp_penalty_end"])
            _LOG.info(
                "Phase 1: weights=%s fp_penalty=[%.3f, %.3f]",
                self.env.reward_weights,
                self.env.fp_penalty_start,
                self.env.fp_penalty_end,
            )
        switched = False

        if pretrain_dataset is not None and pretrain_epochs > 0:
            _LOG.info(
                "Warm-starting policy on %d samples for %d epochs",
                len(pretrain_dataset),
                pretrain_epochs,
            )
            self.pretrain(pretrain_dataset, epochs=pretrain_epochs)

        for _ in pbar:
            action, logp, value = self.select_action(obs, hint)
            next_obs, reward, done, trunc, info = self.env.step(action)

            self.obs_buf.append(obs)
            self.act_buf.append(action)
            self.logp_buf.append(logp)
            self.val_buf.append(value)
            self.rew_buf.append(reward)
            self.done_buf.append(done or trunc)
            metrics = info.get("metrics", {}) if isinstance(info, dict) else {}
            self.f1_buf.append(float(metrics.get("f1_clean", 0.0)))
            self.f1_dummy_buf.append(float(metrics.get("f1_dummy", 0.0)))
            if self.use_hint:
                if hint is not None:
                    self.hint_buf.append(hint)
                else:
                    if self.policy.hint_size is not None:
                        self.hint_buf.append(np.zeros(self.policy.hint_size, dtype=np.float32))
                    else:
                        self.hint_buf.append(np.zeros_like(obs))

            ep_return += reward
            obs = next_obs
            global_step += 1
            if switch_step is not None and not switched and global_step >= switch_step:
                if "reward_weights" in phase2:
                    self.env.reward_weights = dict(phase2["reward_weights"])
                if "fp_penalty_start" in phase2:
                    self.env.fp_penalty_start = float(phase2["fp_penalty_start"])
                if "fp_penalty_end" in phase2:
                    self.env.fp_penalty_end = float(phase2["fp_penalty_end"])
                switched = True
                _LOG.info(
                    "Switched to phase 2 at step %d: weights=%s fp_penalty=[%.3f, %.3f]",
                    global_step,
                    self.env.reward_weights,
                    self.env.fp_penalty_start,
                    self.env.fp_penalty_end,
                )
            if hasattr(pbar, "update"):
                pbar.update(1)

            # ── max_len schedule ─────────────────────────────
            delay_active = (
                self.env.total_steps < getattr(self.env, "rule_len_penalty_delay", 0)
            )
            if delay_active:
                if not getattr(self.env, "_delay_active", False):
                    self.env._delay_active = True
                    self.env.max_len = 50
            elif getattr(self.env, "_delay_active", False):
                self.env._delay_active = False
                self.env.max_len = getattr(self.env, "_orig_max_len", self.env.max_len)

            # ── entropy coefficient schedule
            progress_limit = (
                self.entropy_coef_steps
                if self.entropy_coef_steps is not None
                else total_timesteps
            )
            progress_ratio = min(global_step, progress_limit) / float(progress_limit)
            self.entropy_coef = self.entropy_coef_init + (
                self.entropy_coef_final - self.entropy_coef_init
            ) * progress_ratio
            if (
                not self._max_len_updated
                and not getattr(self.env, "_delay_active", False)
                and global_step >= 50_000
                and self.env.max_len < 128
            ):
                old_len = self.env.max_len
                self.env.max_len = 128
                self._max_len_updated = True
                _LOG.info(
                    "Increased env.max_len from %d to %d at %.2f%% of training",
                    old_len,
                    self.env.max_len,
                    progress_ratio * 100,
                )

            if done or trunc:
                episode_returns.append(ep_return)
                interval_returns.append(ep_return)
                ep_return = 0.0
                obs, info = self.env.reset()
                hint = info.get("hint")

            if global_step % self.n_steps == 0:
                # ── PPO Update
                avg_f1_dummy = float(np.mean(self.f1_dummy_buf)) if self.f1_dummy_buf else 0.0
                self._update()
                if threshold is not None and avg_f1_dummy < threshold:
                    new_dummy = self.env.reward_weights.get("f1_dummy", 0.0) + delta_dummy
                    new_clean = self.env.reward_weights.get("f1_clean", 0.0) + delta_clean
                    self.env.update_reward_weights(f1_dummy=new_dummy, f1_clean=new_clean)
                    _LOG.info(
                        "Auto-adjust reward weights to %s (avg_f1_dummy=%.4f < %.4f)",
                        self.env.reward_weights,
                        avg_f1_dummy,
                        threshold,
                    )

                if global_step % log_interval == 0:
                    avg_ret = float(np.mean(interval_returns)) if interval_returns else 0.0
                    avg_history.append((global_step, avg_ret))
                    _LOG.info(
                        "[PPO] step:%d | avg_ep_return: %.4f | buffer:%d | f1_dummy: %.4f | weights:%s",
                        global_step,
                        avg_ret,
                        len(self.obs_buf),
                        avg_f1_dummy,
                        self.env.reward_weights,
                    )
                    interval_returns.clear()
                    if save_path:
                        self.save(save_path)

        if hasattr(pbar, "close"):
            pbar.close()

        return avg_history

    # ─────────────────────────── PPO optimisation steps ─────────
    def _update(self):
        # 1) Convert rollout buffers to pinned CPU tensors
        obs_cpu = torch.from_numpy(np.stack(self.obs_buf)).long().pin_memory()
        act_cpu = torch.tensor(self.act_buf, dtype=torch.long).pin_memory()
        old_logp_cpu = torch.tensor(self.logp_buf, dtype=torch.float32).pin_memory()
        vals_cpu = torch.tensor(self.val_buf, dtype=torch.float32).pin_memory()
        rews_cpu = torch.tensor(self.rew_buf, dtype=torch.float32).pin_memory()
        dones_cpu = torch.tensor(self.done_buf, dtype=torch.float32).pin_memory()
        hints_cpu = None
        if self.use_hint:
            hint_arr = np.stack(self.hint_buf)
            hints_cpu = torch.from_numpy(hint_arr)
            if self.policy.hint_size is None:
                hints_cpu = hints_cpu.long()
            else:
                hints_cpu = hints_cpu.to(torch.float32)
            hints_cpu = hints_cpu.pin_memory()

        # ── value of the final observation for bootstrapping
        next_value_final = 0.0
        if not self.done_buf[-1]:
            last_obs = obs_cpu[-1].unsqueeze(0).to(self.device, non_blocking=True)
            last_hint = (
                hints_cpu[-1].unsqueeze(0).to(self.device, non_blocking=True)
                if hints_cpu is not None
                else None
            )
            with torch.no_grad():
                _, next_val = self.policy(last_obs, last_hint)
            next_value_final = float(next_val.item())

        # 2) Compute GAE / returns on CPU
        advs = torch.zeros_like(rews_cpu)
        lastgaelam = 0.0
        next_value = 0.0
        for t in reversed(range(len(rews_cpu))):
            if t == len(rews_cpu) - 1:
                next_non_terminal = 1.0 - dones_cpu[-1]
                next_value = next_value_final
            else:
                next_non_terminal = 1.0 - dones_cpu[t + 1]
                next_value = vals_cpu[t + 1]
            delta = rews_cpu[t] + self.gamma * next_value * next_non_terminal - vals_cpu[t]
            lastgaelam = delta + self.gamma * self.gae_lambda * next_non_terminal * lastgaelam
            advs[t] = lastgaelam
        returns = advs + vals_cpu
        advs = (advs - advs.mean()) / (advs.std(unbiased=False) + 1e-8)
        returns = returns.pin_memory()
        advs = advs.pin_memory()

        # --- constraint violation using f1_clean statistics
        finished_idxs = [i for i, d in enumerate(self.done_buf) if d]
        if finished_idxs:
            avg_f1 = float(np.mean([self.f1_buf[i] for i in finished_idxs]))
            violation = self.constraint_thresh - avg_f1
        else:
            avg_f1 = 0.0
            violation = 0.0

        # 3) Epoch loop
        n_samples = obs_cpu.shape[0]
        idxs = np.arange(n_samples)
        self.optimizer.zero_grad()
        mb_count = 0
        for epoch in range(self.n_epochs):
            np.random.shuffle(idxs)
            for start in range(0, n_samples, self.minibatch_size):
                mb_idx = idxs[start : start + self.minibatch_size]
                mb_obs = obs_cpu[mb_idx].to(self.device, non_blocking=True)
                mb_act = act_cpu[mb_idx].to(self.device, non_blocking=True)
                mb_old_logp = old_logp_cpu[mb_idx].to(self.device, non_blocking=True)
                mb_returns = returns[mb_idx].to(self.device, non_blocking=True)
                mb_advs = advs[mb_idx].to(self.device, non_blocking=True)
                mb_hint = (
                    hints_cpu[mb_idx].to(self.device, non_blocking=True)
                    if hints_cpu is not None
                    else None
                )

                with torch.amp.autocast("cuda", enabled=self.use_amp):
                    logits, values = self.policy(mb_obs, mb_hint)
                    masks = []
                    pad_id = self.env.token2id[self.env.PAD]
                    for row in mb_obs.cpu().numpy():
                        toks = [int(t) for t in row if int(t) != pad_id]
                        masks.append(self.env.get_action_mask(tokens=toks))
                    mask_t = torch.from_numpy(np.stack(masks)).to(self.device)
                    logits = logits + torch.where(mask_t > 0, 0.0, -1e9)
                    dist = torch.distributions.Categorical(logits=logits)
                    new_logp = dist.log_prob(mb_act)
                    entropy = dist.entropy().mean()

                    ratio = (new_logp - mb_old_logp).exp()
                    pg_loss1 = ratio * mb_advs
                    pg_loss2 = torch.clamp(ratio, 1 - self.clip_eps, 1 + self.clip_eps) * mb_advs
                    pg_loss = -torch.min(pg_loss1, pg_loss2).mean()

                    mb_vals = vals_cpu[mb_idx].to(self.device, non_blocking=True)
                    value_clip = mb_vals + (values - mb_vals).clamp(-self.clip_eps, self.clip_eps)
                    v_loss1 = (values - mb_returns).pow(2)
                    v_loss2 = (value_clip - mb_returns).pow(2)
                    value_loss = 0.5 * torch.max(v_loss1, v_loss2).mean()

                    constraint_penalty = self.lagrange_multiplier * violation
                    loss = (
                        pg_loss
                        + self.vf_coef * value_loss
                        - self.entropy_coef * entropy
                        + constraint_penalty
                    )

                if self.use_amp:
                    self.scaler.scale(loss / self.accum_steps).backward()
                else:
                    (loss / self.accum_steps).backward()
                mb_count += 1
                is_last_mb = (
                    epoch == self.n_epochs - 1
                    and start + self.minibatch_size >= n_samples
                )
                if mb_count % self.accum_steps == 0 or is_last_mb:
                    if self.use_amp:
                        self.scaler.unscale_(self.optimizer)
                        nn.utils.clip_grad_norm_(self.policy.parameters(), self.max_grad_norm)
                        self.scaler.step(self.optimizer)
                        self.scaler.update()
                    else:
                        nn.utils.clip_grad_norm_(self.policy.parameters(), self.max_grad_norm)
                        self.optimizer.step()

                    if self.scheduler is not None:
                        self.scheduler.step()
                    self.optimizer.zero_grad()

        # update lagrange multiplier using constraint violation
        self.lagrange_multiplier = max(
            0.0, self.lagrange_multiplier + self.lagrange_lr * violation
        )

        self.reset_rollout_buffers()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    # ──────────────────────────────── save / load ───────────────
    def save(self, path: str | Path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(self.policy.state_dict(), path)
        _LOG.info("Saved PPO policy → %s", path)

    def load(self, path: str | Path):
        self.policy.load_state_dict(
            torch.load(path, map_location=self.device, weights_only=False)
        )
        if hasattr(self.policy, "gru"):
            self.policy.gru.flatten_parameters()
        _LOG.info("Loaded PPO policy ← %s", path)

    @torch.no_grad()
    def sample_rules(
        self,
        n: int = 1,
        *,
        temperature: float = 1.0,
        max_len: int | None = None,
    ) -> List[List[str]]:
        """Sample ``n`` rule token sequences from the policy.

        Parameters
        ----------
        n : number of rules to generate
        temperature : sampling temperature for the policy logits
        max_len : optional max token length (defaults to env max_len)
        """

        was_training = self.policy.training
        self.policy.eval()
        max_len = max_len or self.env.max_len
        rules: List[List[str]] = []

        for _ in range(n):
            obs, info = self.env.reset()
            hint = info.get("hint")
            toks: List[int] = []
            done = False
            steps = 0

            while not done and steps < max_len:
                obs_t = torch.from_numpy(obs).long().unsqueeze(0).to(self.device)
                hint_t = None
                if hint is not None:
                    hint_t = torch.from_numpy(hint).unsqueeze(0).to(self.device)
                    if self.policy.hint_size is None:
                        hint_t = hint_t.long()
                    else:
                        hint_t = hint_t.to(torch.float32)

                logits, _ = self.policy(obs_t, hint_t)
                if temperature != 1.0:
                    logits = logits / float(temperature)
                dist = torch.distributions.Categorical(logits=logits)
                action = int(dist.sample().item())

                toks.append(action)
                obs, _, done, trunc, _ = self.env.step(action)
                if trunc or action == self.env.token2id[self.env.END]:
                    done = True
                steps += 1

            rule_tokens = [
                self.env.id2token[t]
                for t in toks
                if t not in {self.env.token2id[self.env.END], self.env.token2id[self.env.PAD]}
            ]
            rules.append(rule_tokens)

        if was_training:
            self.policy.train()
        return rules


# ╔══════════════════════════════════════════════════════════════╗
# ║                          CLI Entry                          ║
# ╚══════════════════════════════════════════════════════════════╝
def _cli():
    """
    간단 smoke‑test:
        python -m rulegen.rl_agent --smoke_test
    실제 학습:
        python -m rulegen.rl_agent --timesteps 100000 --save ppo_rule.pt
    """
    parser = argparse.ArgumentParser(description="PPORuleAgent trainer")
    parser.add_argument("--timesteps", type=int, default=3_000)
    parser.add_argument("--save", type=str, default=None)
    parser.add_argument("--smoke_test", action="store_true")
    parser.add_argument("--accum-steps", type=int, default=1)
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Optional YAML config with auto_adjust settings",
    )
    args = parser.parse_args()

    auto_adjust = None
    if args.config:
        try:
            import yaml  # type: ignore

            with open(args.config, "r", encoding="utf-8") as f:
                cfg = yaml.safe_load(f)
            if isinstance(cfg, dict):
                auto_adjust = cfg.get("auto_adjust")
        except Exception:
            _LOG.warning("Failed to load config: %s", args.config, exc_info=True)

    env = RuleGenEnv(
        rule_type="yara",
        dataset_dir="data/splits",  # 필요시 수정
        max_len=64,
    )

    agent = PPORuleAgent(
        env,
        n_steps=512,
        minibatch_size=128,
        accum_steps=args.accum_steps,
        seed=2024,
    )

    if args.smoke_test:
        _LOG.info("Running smoke‑test (%d timesteps) …", args.timesteps)
    agent.train(
        total_timesteps=args.timesteps,
        save_path=args.save,
        auto_adjust=auto_adjust,
    )

    if args.save:
        agent.save(args.save)


if __name__ == "__main__":
    _cli()
