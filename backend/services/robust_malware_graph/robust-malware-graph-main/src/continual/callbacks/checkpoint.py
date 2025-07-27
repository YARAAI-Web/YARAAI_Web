"""
src.continual.callbacks.checkpoint
==================================

ModelCheckpoint
---------------
• save_freq      : N epoch/step 간격 저장 (mode='epoch' | 'step')
• monitor        : 개선 여부를 판단할 메트릭 키
• mode           : 'min' or 'max' (val_loss↓, val_acc↑ 등)
• save_best      : True면 best.ckpt 별도 관리
• top_k          : 최근 K개만 유지 (None=무한)
• atomic_write   : 임시 파일 → rename 방식으로 중단에도 안전

사용 예시
~~~~~~~~
>>> ckpt = ModelCheckpoint(
...     out_dir="checkpoints", monitor="val_loss", mode="min",
...     save_freq=1, save_best=True, top_k=5
... )
>>> for epoch in range(epochs):
...     # … training loop …
...     ckpt.on_epoch_end(
...         epoch=epoch,
...         model=model,
...         optimizer=optimizer,
...         scheduler=scheduler,
...         val_loss=val_loss, val_acc=val_acc
...     )
...     if ckpt.should_resume:
...         model.load_state_dict(ckpt.best_state_dict)
"""

from __future__ import annotations

import os
import shutil
import tempfile
from collections import deque
from pathlib import Path
from typing import Any, Dict, Literal, Optional

import torch

from ..utils import ensure_dir, get_logger, is_rank_zero
from .logger import BaseCallback

__all__ = ["ModelCheckpoint"]


class ModelCheckpoint(BaseCallback):
    """
    Parameters
    ----------
    out_dir : str | os.PathLike
        체크포인트 저장 디렉터리.
    monitor : str, default='val_loss'
        개선 여부를 판단할 메트릭 키.
    mode : {'min','max'}, default='min'
        작은/큰 값이 좋음을 결정.
    save_freq : int, default=1
        저장 간격 (mode='epoch'일 때 epoch 단위, 'step'일 때 step 단위).
    freq_mode : {'epoch','step'}, default='epoch'
        간격 기준.
    save_best : bool, default=True
        True면 best.ckpt 갱신.
    top_k : int | None, default=None
        None이면 무제한, else 최근 K개만 유지.
    atomic_write : bool, default=True
        임시 파일로 저장 후 rename → 장애 대비.
    """

    def __init__(
        self,
        out_dir: str | os.PathLike = "./checkpoints",
        *,
        monitor: str = "val_loss",
        mode: Literal["min", "max"] = "min",
        save_freq: int = 1,
        freq_mode: Literal["epoch", "step"] = "epoch",
        save_best: bool = True,
        top_k: Optional[int] = None,
        atomic_write: bool = True,
    ):
        assert mode in {"min", "max"}
        assert freq_mode in {"epoch", "step"}
        self.out_dir = ensure_dir(out_dir)
        self.monitor = monitor
        self.mode = mode
        self.save_freq = max(1, save_freq)
        self.freq_mode = freq_mode
        self.save_best = save_best
        self.top_k = top_k
        self.atomic_write = atomic_write

        self._better = (lambda a, b: a < b) if mode == "min" else (lambda a, b: a > b)
        self.best_value: float = float("inf") if mode == "min" else float("-inf")
        self.best_state_dict: Optional[Dict[str, Any]] = None
        self.saved_paths: deque[str] = deque(maxlen=top_k or 0)  # 0이면 무제한
        self.logger = get_logger("checkpoint")

    # ------------------------- 내부 유틸 ------------------------- #
    def _format_name(self, index: int, suffix: str = ".ckpt") -> str:
        return f"{self.freq_mode}_{index:05d}{suffix}"

    def _atomic_save(self, obj: Dict[str, Any], path: Path) -> None:
        if not self.atomic_write:
            torch.save(obj, path)
            return
        with tempfile.NamedTemporaryFile(delete=False, dir=path.parent) as tmp:
            torch.save(obj, tmp.name)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp.name, path)  # atomic on POSIX

    def _enqueue_path(self, path: str) -> None:
        if self.top_k is None:
            return
        if len(self.saved_paths) == self.saved_paths.maxlen:
            old = self.saved_paths.popleft()
            if os.path.exists(old):
                try:
                    os.remove(old)
                except OSError:
                    self.logger.warning(f"Could not remove old checkpoint {old}")
        self.saved_paths.append(path)

    # ------------------- Hook 구현 ------------------- #
    def on_step_end(self, *, step: int, **kwargs):
        if self.freq_mode != "step" or (step + 1) % self.save_freq:
            return
        self._save(index=step, **kwargs)

    def on_epoch_end(self, *, epoch: int, **kwargs):
        if self.freq_mode != "epoch" or (epoch + 1) % self.save_freq:
            return
        self._save(index=epoch, **kwargs)

    # ----------------------- Save Core ----------------------- #
    def _save(self, *, index: int, **kwargs):
        if not is_rank_zero():
            return

        # Required arguments
        model: torch.nn.Module = kwargs["model"]
        optimizer: torch.optim.Optimizer | None = kwargs.get("optimizer")
        scheduler: Any | None = kwargs.get("scheduler")
        metrics: Dict[str, float] = {
            k: float(v) for k, v in kwargs.items() if isinstance(v, (int, float))
        }

        # Assemble checkpoint dict
        ckpt: Dict[str, Any] = {
            "index": index,
            "freq_mode": self.freq_mode,
            "model_state": model.state_dict(),
            "optimizer_state": optimizer.state_dict() if optimizer else None,
            "scheduler_state": scheduler.state_dict() if scheduler and hasattr(scheduler, "state_dict") else None,
            "metrics": metrics,
        }

        # Standard filename
        fname = self._format_name(index)
        fpath = self.out_dir / fname
        self._atomic_save(ckpt, fpath)
        self._enqueue_path(str(fpath))
        self.logger.info(f"Saved checkpoint: {fpath}")

        # Best checkpoint logic
        if self.save_best and self.monitor in metrics:
            current = metrics[self.monitor]
            if self._better(current, self.best_value):
                self.best_value = current
                self.best_state_dict = {
                    k: v.detach().cpu().clone() for k, v in model.state_dict().items()
                }
                best_path = self.out_dir / "best.ckpt"
                self._atomic_save(ckpt, best_path)
                self.logger.info(
                    f"New best ({self.monitor}={current:.4f}) → {best_path}"
                )

    # ------------------- Convenience ------------------- #
    def __repr__(self) -> str:  # noqa: D401
        return (
            f"{self.__class__.__name__}(out_dir='{self.out_dir}', "
            f"monitor='{self.monitor}', mode='{self.mode}', "
            f"save_freq={self.save_freq}, freq_mode='{self.freq_mode}', "
            f"top_k={self.top_k})"
        )
