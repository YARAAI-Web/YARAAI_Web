from __future__ import annotations

import math
from typing import Tuple

import torch
import torch.nn as nn


class AttnPolicy(nn.Module):
    """Simple attention-based actor-critic for token sequences."""

    def __init__(
        self,
        vocab_size: int,
        embed_dim: int = 128,
        hidden_size: int = 256,
        num_heads: int = 4,
        gru_layers: int = 1,
        *,
        use_hint: bool = False,
        hint_size: int | None = None,
        pad_id: int = 0,
    ) -> None:
        super().__init__()
        self.use_hint = use_hint
        self.hint_size = hint_size
        self.pad_id = pad_id
        self.embed = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_id)
        self.attn = nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)
        self.gru = nn.GRU(
            input_size=embed_dim * (2 if use_hint else 1),
            hidden_size=hidden_size,
            num_layers=gru_layers,
            batch_first=True,
        )
        self.hint_proj: nn.Module | None = None
        if self.use_hint and self.hint_size is not None:
            self.hint_proj = nn.Linear(hint_size, embed_dim)
        self.in_drop = nn.Dropout(0.1)
        self.out_drop = nn.Dropout(0.1)
        self.pi_head = nn.Linear(hidden_size, vocab_size)
        self.v_head = nn.Linear(hidden_size, 1)

        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.orthogonal_(m.weight, gain=math.sqrt(2))
                nn.init.zeros_(m.bias)
        nn.init.orthogonal_(self.pi_head.weight, gain=0.01)

    def forward(
        self, obs: torch.Tensor, hint: torch.Tensor | None = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        mask = obs != self.pad_id
        if mask.ndim == 1:
            mask = mask.unsqueeze(0)
        x = self.embed(obs)
        x = self.in_drop(x)
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
                    hint_input = hint if hint.ndim > 1 else hint.unsqueeze(0)
                    hint_input = hint_input.to(x.dtype)
                hint_vec = self.hint_proj(hint_input)
            hint_seq = hint_vec.unsqueeze(1).expand(-1, x.size(1), -1)
            x = torch.cat([x, hint_seq], dim=2)
        attn_out, _ = self.attn(x, x, x, key_padding_mask=~mask)
        lengths = mask.sum(dim=1).clamp(min=1)
        packed = nn.utils.rnn.pack_padded_sequence(
            attn_out, lengths.cpu(), batch_first=True, enforce_sorted=False
        )
        _, h_n = self.gru(packed)
        h = h_n[-1]
        h = self.out_drop(h)
        logits = self.pi_head(h)
        value = self.v_head(h).squeeze(-1)
        return logits, value
