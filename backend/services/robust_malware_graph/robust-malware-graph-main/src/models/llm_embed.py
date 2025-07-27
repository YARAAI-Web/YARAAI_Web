# SPDX‑License‑Identifier: MIT
"""llm_embed.py
============================================
Code‑LLM Node Feature Extractor
--------------------------------
`CodeLLMNodeFeat` wraps a HuggingFace *code* language model (e.g.
`microsoft/codebert‑base`, `codellama‑7b‑hf`) and converts per‑node token
sequences into fixed‑size **embeddings** that downstream GNNs can directly
consume (dim = model.hidden_size, default 768).

Key Points
~~~~~~~~~~
* **Pooling**: "cls" | "mean" | "max" over token axis.
* **Fine‑tuning**  optional – by default the LM is *frozen* for speed/VRAM.
* **Masked‑Node CE** helper (`mlm_loss`) enables BERT‑style pre‑text training.
* **Batch API** matches torch‑geometric graphs: accepts flattened tensors
  `(∑_B N, L≤64)` with optional `attention_mask`.

Example
-------
```python
from src.models.llm_embed import CodeLLMNodeFeat
node_feat = CodeLLMNodeFeat("microsoft/codebert‑base", pooling="mean")

# token_ids: LongTensor [(∑N) × L]
emb = node_feat(token_ids, attn_mask)            # -> float32 [(∑N) × 768]
```
"""
from __future__ import annotations

from typing import Literal, Tuple, Dict, Any, Optional
from pathlib import Path

import torch
from torch import nn
from transformers import (
    AutoConfig,
    AutoModel,
    AutoModelForMaskedLM,
    PreTrainedModel,
)

from src.common.utils import get_logger, tqdm_wrap

__all__ = ["CodeLLMNodeFeat", "embed_corpus"]

LOGGER = get_logger(__name__)

Pooling = Literal["cls", "mean", "max"]


class CodeLLMNodeFeat(nn.Module):
    """Node‑level feature extractor using a pretrained *code* LM.

    Parameters
    ----------
    model_name : str, default "microsoft/codebert‑base"
        HuggingFace model id / local path.
    max_length : int, default 64
        Truncation length for sequences.
    pooling : {"cls", "mean", "max"}, default "cls"
        How to pool the per‑token hidden states into a single vector.
    fine_tune : bool, default False
        If **False**, all LM parameters are *frozen* (no grad).
    masked_lm : bool, default False
        If **True**, loads `AutoModelForMaskedLM` instead of plain `AutoModel`
        and enables the :pymeth:`mlm_loss` method.
    dtype : torch.dtype, default torch.float32
        Output datatype.  *NOTE* transformers models internally run fp32/bf16.
    """

    def __init__(
        self,
        model_name: str = "microsoft/codebert-base",
        *,
        max_length: int = 64,
        pooling: Pooling = "cls",
        fine_tune: bool = False,
        masked_lm: bool = False,
        dtype: torch.dtype = torch.float32,
    ) -> None:
        super().__init__()

        self.config = AutoConfig.from_pretrained(model_name)
        self.max_length = max_length
        self.pooling: Pooling = pooling
        self.dtype = dtype
        self.masked_lm = masked_lm

        if masked_lm:
            self.model: PreTrainedModel = AutoModelForMaskedLM.from_pretrained(model_name)
        else:
            self.model = AutoModel.from_pretrained(model_name)

        if not fine_tune:
            for p in self.model.parameters():
                p.requires_grad_(False)

        self.hidden_size: int = self.config.hidden_size

    # ------------------------------------------------------------------ #
    # Utility ‑ pooling ops
    # ------------------------------------------------------------------ #
    def _pool(self, hidden: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """Pool token states → node vector.

        * hidden: (B, L, H)
        * mask  : (B, L) or None
        """
        if self.pooling == "cls":
            return hidden[:, 0]  # (B, H)
        elif self.pooling == "mean":
            if mask is None:
                return hidden.mean(dim=1)
            mask = mask.unsqueeze(-1)  # (B, L, 1)
            sums = (hidden * mask).sum(dim=1)
            counts = mask.sum(dim=1).clamp_min(1e-6)
            return sums / counts
        elif self.pooling == "max":
            if mask is None:
                return hidden.max(dim=1).values
            hidden = hidden.masked_fill(~mask.unsqueeze(-1).bool(), float("-inf"))
            return hidden.max(dim=1).values
        else:  # pragma: no cover
            raise ValueError(f"Unknown pooling: {self.pooling}")

    # ------------------------------------------------------------------ #
    # Forward
    # ------------------------------------------------------------------ #
    @torch.no_grad()
    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Encode node token sequences → embeddings.

        Parameters
        ----------
        input_ids : LongTensor[(∑N) × L]
        attention_mask : Bool/Long Tensor, optional
        """
        if input_ids.ndim != 2:
            raise ValueError("input_ids must have shape (batch, seq_len)")
        if input_ids.size(1) > self.max_length:
            input_ids = input_ids[:, : self.max_length]
            if attention_mask is not None:
                attention_mask = attention_mask[:, : self.max_length]

        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_hidden_states=False,
            return_dict=True,
        )
        last_hidden = outputs.last_hidden_state  # (B, L, H)
        emb = self._pool(last_hidden, attention_mask).to(self.dtype)
        return emb  # (B, H)

    # ------------------------------------------------------------------ #
    # Masked‑LM Node Pre‑text Loss
    # ------------------------------------------------------------------ #
    def mlm_loss(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        labels: torch.Tensor,
        reduction: str = "mean",
    ) -> torch.Tensor:
        """Compute Masked‑Language‑Model loss over node tokens.

        **Requires** `masked_lm=True` at init.
        Labels must use `‑100` for non‑masked positions as in HF.
        """
        if not self.masked_lm:
            raise RuntimeError("mlm_loss is available only when masked_lm=True")

        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels,
            return_dict=True,
        )
        loss = outputs.loss  # already reduced (mean) by HF
        if reduction == "sum":
            loss = loss * input_ids.size(0)
        elif reduction == "none":
            pass  # leave per‑item loss – HF returns scalar, so replicate
        return loss

    # ------------------------------------------------------------------ #
    # Utility: freeze / unfreeze
    # ------------------------------------------------------------------ #
    def freeze(self) -> None:
        for p in self.model.parameters():
            p.requires_grad_(False)

    def unfreeze(self) -> None:
        for p in self.model.parameters():
            p.requires_grad_(True)

    # ------------------------------------------------------------------ #
    # State dict helpers – only save small subset when frozen
    # ------------------------------------------------------------------ #
    def state_dict(self, *args: Any, **kwargs: Any):  # type: ignore[override]
        if all(not p.requires_grad for p in self.model.parameters()):
            # Skip LM weights if fully frozen → huge disk space saving
            base = {
                "config": self.config.to_dict(),
                "pooling": self.pooling,
                "dtype": str(self.dtype),
                "masked_lm": self.masked_lm,
            }
            return base
        return super().state_dict(*args, **kwargs)

    def load_state_dict(self, state_dict: Dict[str, Any], *args: Any, **kwargs: Any):  # type: ignore[override]
        # If minimal checkpoint – re‑init model from config
        if "config" in state_dict:
            cfg = AutoConfig.from_dict(state_dict["config"])
            if self.masked_lm:
                self.model = AutoModelForMaskedLM.from_config(cfg)
            else:
                self.model = AutoModel.from_config(cfg)
            self.pooling = state_dict["pooling"]
            self.dtype = getattr(torch, state_dict["dtype"], torch.float32)
            return  # nothing else to load
        super().load_state_dict(state_dict, *args, **kwargs)


def embed_corpus(
    encoder: CodeLLMNodeFeat,
    *,
    hetero_dir: Path,
    out_dir: Path,
    batch_size: int = 32,
    overwrite: bool = False,
) -> tuple[int, int]:
    """Encode all ``token`` nodes under ``hetero_dir`` and cache embeddings.

    Parameters
    ----------
    encoder : CodeLLMNodeFeat
        Initialized model. Device is inferred from encoder parameters.
    hetero_dir : Path
        Directory containing ``*.pt`` hetero graphs.
    out_dir : Path
        Output directory for cached features (``name.ftr``).
    batch_size : int, default 32
        Mini-batch size for encoding.
    overwrite : bool, default False
        Replace existing feature files.

    Returns
    -------
    tuple[int, int]
        Number of processed and skipped graphs.
    """

    import torch

    from src.graphs.features.cache import save_tensor

    hetero_dir = Path(hetero_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    processed = 0
    skipped = 0

    try:
        device = next(encoder.parameters()).device
    except StopIteration:  # encoder with no parameters
        device = torch.device("cpu")

    pt_files = list(hetero_dir.glob("*.pt"))
    if not pt_files:
        raise RuntimeError(f"No hetero graphs found in {hetero_dir}")

    for fp in tqdm_wrap(pt_files, desc="[embed]", unit="graph"):
        out_name = fp.stem
        out_path = out_dir / f"{out_name}.ftr"
        if out_path.exists() and not overwrite:
            continue

        g = torch.load(fp, weights_only=False)
        if "token" not in g.node_types:
            skipped += 1
            continue

        store = g["token"]
        none_idx: list[int] = []

        if "input_ids" in store:
            input_ids = store["input_ids"]
            attn_mask = store.get("attention_mask")
        else:
            texts = store.get("text") or store.get("kind_str")
            if texts is None:
                skipped += 1
                continue
            if isinstance(texts, str):
                texts = [texts]
            else:
                try:
                    texts = list(texts)
                except TypeError:
                    texts = [texts]

            clean_texts = []
            for idx, t in enumerate(texts):
                if t is None:
                    none_idx.append(idx)
                    clean_texts.append("")
                else:
                    clean_texts.append(str(t))
            texts = clean_texts

            from transformers import AutoTokenizer

            try:
                tok = AutoTokenizer.from_pretrained(encoder.config._name_or_path)
            except Exception as exc:  # pragma: no cover - tokenizer optional
                raise RuntimeError("Tokenizer required for text embeddings") from exc

            try:
                enc = tok(
                    texts,
                    padding=True,
                    truncation=True,
                    max_length=encoder.max_length,
                    return_tensors="pt",
                )
            except Exception as exc:
                raise RuntimeError(f"Tokenization failed for {out_name}: {exc}") from exc

            input_ids = enc["input_ids"]
            attn_mask = enc["attention_mask"]

        embeddings: list[torch.Tensor] = []
        ranges = range(0, input_ids.size(0), batch_size)
        for start in ranges:
            batch_ids = input_ids[start : start + batch_size].to(device)
            if attn_mask is not None:
                batch_mask = attn_mask[start : start + batch_size].to(device)
            else:
                batch_mask = None
            emb = encoder(batch_ids, batch_mask).cpu()
            embeddings.append(emb)

        feat = torch.cat(embeddings, dim=0)
        if none_idx:
            feat[none_idx] = 0
        save_tensor(out_name, feat, out_dir, overwrite=overwrite)
        processed += 1

    LOGGER.info(
        "embed_corpus completed: processed=%d skipped=%d", processed, skipped
    )
    if processed == 0:
        raise RuntimeError("No graphs contained token nodes")
    return processed, skipped
