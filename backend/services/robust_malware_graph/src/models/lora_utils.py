from __future__ import annotations

from typing import Any, Dict

try:
    from peft import LoraConfig, get_peft_model
except Exception:  # pragma: no cover - peft optional
    LoraConfig = None
    def get_peft_model(model, config):  # type: ignore
        raise ImportError("peft is required for LoRA")


def apply_lora_gpt2(model, cfg: Dict[str, Any]):
    """Apply LoRA adapters to a GPT2 model using PEFT.

    Parameters
    ----------
    model : transformers.PreTrainedModel
        GPT2 model instance.
    cfg : dict
        Configuration dictionary with keys `r`, `alpha`, `dropout` and
        optional `target_modules`.
    """
    if LoraConfig is None:
        raise ImportError("peft is required for LoRA")
    lora_cfg = LoraConfig(
        r=cfg.get("r", 8),
        lora_alpha=cfg.get("alpha", 16),
        lora_dropout=cfg.get("dropout", 0.1),
        target_modules=cfg.get("target_modules", ["c_attn"]),
    )
    return get_peft_model(model, lora_cfg)

