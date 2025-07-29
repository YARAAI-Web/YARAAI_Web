from __future__ import annotations

from typing import Mapping, Any, Sequence

import torch
import torch.nn.functional as F

from src.cli.categorical_optimizer import CategoricalOptimizer, PopulationOptimizer


__all__ = [
    "_optimizer_loss",
    "_optimizer_step",
    "CategoricalOptimizer",
    "PopulationOptimizer",
]


def _optimizer_loss(
    trial: Mapping[str, Any] | Sequence[Mapping[str, Any]],
    opt: CategoricalOptimizer,
    fp_ratio_benign: float = 0.0,
    beta: float | None = None,
) -> torch.Tensor:
    """Return differentiable loss for optimizer step."""
    from collections.abc import Sequence as _Seq

    if isinstance(trial, _Seq) and trial and not isinstance(trial, Mapping):
        fp_ratio_benign = float(
            sum(t.get("fp_ratio_benign", fp_ratio_benign) for t in trial) / len(trial)
        )
        fp_avg = sum(float(t.get("false_positive", False)) for t in trial) / len(trial)
        tp_avg = sum(float(t.get("detected", False)) for t in trial) / len(trial)
        base = trial[0]
        trial = {
            "false_positive": fp_avg,
            "detected": tp_avg,
            "condition_type": base.get("condition_type", "any"),
            "combine_mode": base.get("combine_mode", "or"),
        }

    fp = torch.tensor(float(trial.get("false_positive", False)), device=opt.condition_type_logits.device)
    tp = torch.tensor(float(trial.get("detected", False)), device=opt.condition_type_logits.device)

    cond_prob = F.gumbel_softmax(opt.condition_type_logits, tau=1.0, hard=False)
    comb_prob = F.gumbel_softmax(opt.combine_mode_logits, tau=1.0, hard=False)

    cond_indicator = torch.tensor(
        [trial.get("condition_type", "any") == c for c in opt.CONDITION_TYPES],
        dtype=torch.float32,
        device=opt.condition_type_logits.device,
    )
    comb_indicator = torch.tensor(
        [trial.get("combine_mode", "or") == c for c in opt.COMBINE_MODES],
        dtype=torch.float32,
        device=opt.condition_type_logits.device,
    )
    bool_probs = torch.sigmoid(
        torch.stack(
            [
                opt.dynamic_k_logit,
                opt.auto_relax_logit,
                opt.adjust_group_percentage_logit,
                opt.group_min_ratio_logit,
                opt.combine_min_ratio_logit,
                opt.freq_threshold_logit,
                opt.group_min_count_logit,
            ]
        )
    )

    mix = bool_probs.mean()
    fp_weight = 1.0 + float(fp_ratio_benign)
    if beta is None:
        beta = getattr(opt, "beta", 0.5)
    fp_val = fp * torch.sum(cond_prob * cond_indicator) * mix
    tp_val = tp * torch.sum(comb_prob * comb_indicator) * mix
    loss = fp_weight * fp_val + float(beta) * (1.0 - tp_val)
    return loss


def _optimizer_step(
    trial: Mapping[str, Any],
    optimizer: CategoricalOptimizer | PopulationOptimizer | None,
    param_update=None,
) -> tuple[float, str, float, float | int, int | None] | None:
    """Update optimizer with ``trial`` and return new parameters."""

    if optimizer is None:
        return None

    if isinstance(optimizer, PopulationOptimizer):
        optimizer.step([trial])
        params = optimizer.optimizers[0].discrete_params()
    else:
        loss = _optimizer_loss(trial, optimizer, trial.get("fp_ratio_benign", 0.0))
        optimizer.step(loss)
        params = optimizer.discrete_params()

    if param_update:
        param_update(params)

    return (
        params["combine_min_ratio"],
        params["combine_mode"],
        params["group_min_ratio"],
        params.get("freq_threshold", 0.0),
        params.get("group_min_count"),
    )
