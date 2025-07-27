"""
src.continual.callbacks.logger
==============================

Callback utilities for Continual / Online Learning loops.

• BaseCallback      : on_{train,epoch,step}_* 훅 정의
• StdoutLogger      : 콘솔(ANSI) 출력, 주기별 평균·EMA
• TensorBoardLogger : torch.utils.tensorboard.SummaryWriter
• WandBLogger       : Weights & Biases 경량 래퍼

Learner 또는 Engine 루프 예시
----------------------------
>>> logger_cb = StdoutLogger(print_freq=100)
>>> tb_cb     = TensorBoardLogger("./runs")
>>> for epoch in range(epochs):
...     logger_cb.on_epoch_start(epoch=epoch)
...     for step, batch in enumerate(stream):
...         loss = learner.training_step(batch)
...         logger_cb.on_step_end(step=step, loss=loss)
...         tb_cb.on_step_end(step=step, loss=loss)
...     logger_cb.on_epoch_end(epoch=epoch)
...     tb_cb.on_epoch_end(epoch=epoch)
>>> logger_cb.on_train_end()
>>> tb_cb.on_train_end()
"""

from __future__ import annotations

import os
import time
from abc import ABC, abstractmethod
from typing import Any, Dict

import torch

from ..utils import AverageMeter, get_logger, is_rank_zero

__all__ = [
    "BaseCallback",
    "StdoutLogger",
    "TensorBoardLogger",
    "WandBLogger",
]

# --------------------------------------------------------------------------- #
# 1. 공통 인터페이스
# --------------------------------------------------------------------------- #
class BaseCallback(ABC):
    """학습 루프 단계별 훅을 가지는 추상 클래스."""

    # 필요 훅만 오버라이드하면 됨 (pass → no-op)
    def on_train_start(self, **kwargs): ...
    def on_epoch_start(self, **kwargs): ...
    def on_step_end(self, **kwargs): ...
    def on_epoch_end(self, **kwargs): ...
    def on_train_end(self, **kwargs): ...

    @abstractmethod
    def __repr__(self) -> str: ...


# --------------------------------------------------------------------------- #
# 2. 표준 콘솔 로거
# --------------------------------------------------------------------------- #
class StdoutLogger(BaseCallback):
    """
    주기적으로 콘솔에 평균/EMA 메트릭을 출력하는 로거.

    Parameters
    ----------
    print_freq : int
        출력 간격(step 단위, 1 이상).
    ema_alpha : float | None
        0<alpha<1이면 EMA 계수 사용, None이면 단순 평균만.
    """

    def __init__(self, print_freq: int = 100, *, ema_alpha: float | None = 0.9):
        self.print_freq = max(1, print_freq)
        self.ema_alpha = ema_alpha
        self.meters: Dict[str, AverageMeter] = {}
        self.epoch_start_time: float = 0.0
        self.logger = get_logger("stdout")

    # 내부: 메트릭 누적
    def _update(self, **metrics: float):
        for k, v in metrics.items():
            if k not in self.meters:
                self.meters[k] = AverageMeter(alpha=self.ema_alpha)
            self.meters[k].update(float(v))

    # ------------------- Hook 구현 ------------------- #
    def on_train_start(self, **kwargs):
        if is_rank_zero():
            self.logger.info("Training started.")

    def on_epoch_start(self, *, epoch: int, **kwargs):
        self.epoch_start_time = time.time()
        for m in self.meters.values():
            m.reset()
        if is_rank_zero():
            self.logger.info(f"Epoch {epoch} started.")

    def on_step_end(self, *, step: int, **metrics):
        self._update(**metrics)
        if is_rank_zero() and (step + 1) % self.print_freq == 0:
            msg = f"[step {step+1}] " + ", ".join(
                f"{k}: {m.avg:.4f}" for k, m in self.meters.items()
            )
            self.logger.info(msg)

    def on_epoch_end(self, *, epoch: int, **kwargs):
        if not is_rank_zero():
            return
        dur = time.time() - self.epoch_start_time
        msg = f"Epoch {epoch} finished in {dur:.1f}s | " + ", ".join(
            f"{k}: {m.avg:.4f}" for k, m in self.meters.items()
        )
        self.logger.info(msg)

    def on_train_end(self, **kwargs):
        if is_rank_zero():
            self.logger.info("Training finished.")

    def __repr__(self) -> str:  # noqa: D401
        return f"{self.__class__.__name__}(print_freq={self.print_freq})"


# --------------------------------------------------------------------------- #
# 3. TensorBoard 로거 (선택 의존성)
# --------------------------------------------------------------------------- #
class TensorBoardLogger(BaseCallback):
    """
    torch.utils.tensorboard.SummaryWriter 기반 스칼라 로거.

    모든 훅은 **step or epoch** 키워드 인자가 필요합니다.
    """

    def __init__(self, log_dir: str = "./runs", flush_secs: int = 30):
        from torch.utils.tensorboard import SummaryWriter  # 지연 import

        # DDP 중복 방지: rank>0 은 하위 폴더로 분리
        if not is_rank_zero():
            log_dir = os.path.join(log_dir, f"rank{torch.distributed.get_rank()}")
        self.writer = SummaryWriter(log_dir, flush_secs=flush_secs)
        self.t0 = time.time()

    def on_step_end(self, *, step: int, **metrics):
        for k, v in metrics.items():
            self.writer.add_scalar(k, float(v), global_step=step)

    def on_epoch_end(self, *, epoch: int, **metrics):
        self.writer.add_scalar("time/epoch", time.time() - self.t0, global_step=epoch)
        for k, v in metrics.items():
            self.writer.add_scalar(f"epoch/{k}", float(v), global_step=epoch)

    def on_train_end(self, **kwargs):
        self.writer.close()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(log_dir={self.writer.log_dir})"


# --------------------------------------------------------------------------- #
# 4. Weights & Biases 로거 (선택 의존성)
# --------------------------------------------------------------------------- #
class WandBLogger(BaseCallback):
    """
    Weights & Biases 스칼라 로거.

    환경변수 WANDB_MODE=dryrun 으로 오프라인 기록 가능.
    """

    def __init__(self, project: str = "robust-malware-graph", name: str | None = None):
        import wandb

        self.wandb = wandb
        if is_rank_zero():
            self.run = wandb.init(project=project, name=name, reinit=True)
        else:
            self.run = None

    def on_step_end(self, *, step: int, **metrics):
        if self.run is not None:
            self.wandb.log(metrics, step=step)

    def on_epoch_end(self, *, epoch: int, **metrics):
        if self.run is not None:
            self.wandb.log({f"epoch/{k}": v for k, v in metrics.items()}, step=epoch)

    def on_train_end(self, **kwargs):
        if self.run is not None:
            self.run.finish()

    def __repr__(self) -> str:
        proj = self.run.project if self.run is not None else "-"
        return f"{self.__class__.__name__}(project={proj})"
