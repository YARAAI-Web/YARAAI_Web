"""
src.continual.callbacks.earlystop
=================================

EarlyStopping Callback
----------------------
지정 메트릭이 n epoch 연속으로 개선되지 않으면 학습 중단 신호를 주는 헬퍼.

사용 예시
~~~~~~~~
>>> earlystop = EarlyStopping(monitor="val_loss", mode="min", patience=5)
>>> for epoch in range(epochs):
...     # … training loop …
...     earlystop.on_epoch_end(epoch=epoch, val_loss=val_loss, val_acc=val_acc)
...     if earlystop.should_stop:
...         print(f"Stopped @ {epoch=}")
...         break
>>> best_state_dict = earlystop.best_state_dict  # 필요 시 가중치 복구
"""

from __future__ import annotations

import math
from typing import Any, Dict, Optional

import torch

from ..utils import get_logger, is_rank_zero
from .logger import BaseCallback  # 같은 패키지 내부

__all__ = ["EarlyStopping"]


class EarlyStopping(BaseCallback):
    """
    Parameters
    ----------
    monitor : str
        감시할 메트릭 이름 (kwargs 에 동일 키로 전달돼야 함).
    mode : {'min', 'max'}
        'min' → 더 작아질 때 개선, 'max' → 더 커질 때 개선.
    patience : int
        개선이 없는 epoch 연속 횟수 초과 시 중단.
    min_delta : float
        개선으로 인정하기 위한 최소 변화폭 (절댓값).
    restore_best_state : bool
        True면 최고 성능 시점의 model.state_dict() 저장.
    """

    def __init__(
        self,
        monitor: str = "val_loss",
        mode: str = "min",
        patience: int = 10,
        *,
        min_delta: float = 0.0,
        restore_best_state: bool = True,
    ):
        assert mode in {"min", "max"}
        self.monitor = monitor
        self.mode = mode
        self.patience = patience
        self.min_delta = min_delta
        self.restore_best_state = restore_best_state

        self.best_value: float = math.inf if mode == "min" else -math.inf
        self.best_epoch: int = -1
        self.num_bad_epochs: int = 0
        self.should_stop: bool = False
        self.best_state_dict: Optional[Dict[str, Any]] = None

        self.logger = get_logger("earlystop")

    # ------------------- Hook ------------------- #
    def on_epoch_end(self, *, epoch: int, **metrics):
        if self.monitor not in metrics:
            if is_rank_zero():
                self.logger.warning(
                    f"EarlyStopping: '{self.monitor}' not provided in metrics."
                )
            return

        current = float(metrics[self.monitor])
        improved = (
            (self.mode == "min" and current < self.best_value - self.min_delta)
            or (self.mode == "max" and current > self.best_value + self.min_delta)
        )

        if improved:
            self.best_value = current
            self.best_epoch = epoch
            self.num_bad_epochs = 0
            if self.restore_best_state:
                # Learner(model=...) 쪽에서 self.model attribute를 넘겨줄 수도,
                # 외부에서 직접 earlystop.save_state(model) 호출할 수도 있음.
                model = metrics.get("model")
                if isinstance(model, torch.nn.Module):
                    self.best_state_dict = {
                        k: v.detach().cpu().clone() for k, v in model.state_dict().items()
                    }
        else:
            self.num_bad_epochs += 1
            if self.num_bad_epochs >= self.patience:
                self.should_stop = True
                if is_rank_zero():
                    self.logger.info(
                        f"Early stopping triggered @ epoch {epoch} "
                        f"(best {self.monitor}: {self.best_value:.4f} @ {self.best_epoch})"
                    )

    # -------------------------------------------------- #
    # 선택: 외부에서 명시적으로 가중치 저장하도록 도와주는 메서드
    # -------------------------------------------------- #
    def save_state(self, model: torch.nn.Module) -> None:
        """현재 모델 state_dict를 deep-copy하여 저장."""
        self.best_state_dict = {
            k: v.detach().cpu().clone() for k, v in model.state_dict().items()
        }

    def __repr__(self) -> str:  # noqa: D401
        return (
            f"{self.__class__.__name__}(monitor='{self.monitor}', mode='{self.mode}', "
            f"patience={self.patience}, min_delta={self.min_delta})"
        )
