from __future__ import annotations

from torch.optim import Optimizer
from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR, LRScheduler


def build_warm_cosine(
    optimizer: Optimizer,
    warmup_steps: int,
    total_steps: int,
) -> LRScheduler:
    """Return scheduler with linear warm-up followed by cosine annealing."""
    warmup_steps = int(warmup_steps)
    total_steps = int(total_steps)
    cosine = CosineAnnealingLR(optimizer, T_max=max(1, total_steps - warmup_steps))
    if warmup_steps > 0:
        linear = LinearLR(
            optimizer,
            start_factor=1e-6,
            end_factor=1.0,
            total_iters=warmup_steps,
        )
        scheduler = SequentialLR(
            optimizer,
            schedulers=[linear, cosine],
            milestones=[warmup_steps],
        )
    else:
        scheduler = cosine
    return scheduler

