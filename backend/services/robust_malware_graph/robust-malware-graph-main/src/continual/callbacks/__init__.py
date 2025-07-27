"""Callback utilities for continual-learning experiments.

src.continual.callbacks
=======================

콜백 모듈 집합.

노출 항목
---------
BaseCallback         : 콜백 인터페이스 (logger.py 내부 정의)
StdoutLogger         : 콘솔 ANSI 로거
TensorBoardLogger    : TensorBoard SummaryWriter 래퍼
WandBLogger          : Weights & Biases 로거
EarlyStopping        : 개선 정지 콜백
ModelCheckpoint      : 주기·베스트 모델 체크포인트
CallbackManager      : 콜백 리스트를 일괄 호출하는 헬퍼
"""

from __future__ import annotations

from typing import Iterable, List

# 개별 서브모듈에서 가져오기
from .logger import BaseCallback, StdoutLogger, TensorBoardLogger, WandBLogger
from .earlystop import EarlyStopping
from .checkpoint import ModelCheckpoint

__all__ = [
    "BaseCallback",
    "StdoutLogger",
    "TensorBoardLogger",
    "WandBLogger",
    "EarlyStopping",
    "ModelCheckpoint",
    "CallbackManager",
]


class CallbackManager:
    """
    여러 콜백을 묶어 **학습 엔진 → CallbackManager** 단일 객체 형태로 사용.

    Examples
    --------
    >>> cbs = CallbackManager(
    ...     StdoutLogger(print_freq=50),
    ...     TensorBoardLogger("./runs"),
    ...     EarlyStopping(monitor="val_loss", mode="min", patience=5),
    ...     ModelCheckpoint(out_dir="ckpts", monitor="val_loss", mode="min"),
    ... )
    >>> cbs.on_train_start()
    >>> for epoch in range(epochs):
    ...     cbs.on_epoch_start(epoch=epoch)
    ...     for step, batch in enumerate(stream):
    ...         loss = learner.training_step(batch)
    ...         cbs.on_step_end(step=step, loss=loss)
    ...     cbs.on_epoch_end(epoch=epoch, val_loss=val_loss)
    ...     if any(getattr(cb, "should_stop", False) for cb in cbs):
    ...         break
    >>> cbs.on_train_end()
    """

    def __init__(self, *callbacks: BaseCallback | Iterable[BaseCallback]):
        # 가변 인자 혹은 iterable 인자를 모두 평탄화
        self.callbacks: List[BaseCallback] = []
        for cb in callbacks:
            if isinstance(cb, Iterable):
                self.callbacks.extend(cb)  # type: ignore[arg-type]
            else:
                self.callbacks.append(cb)

    # ----------------- 브로드캐스팅 헬퍼 ----------------- #
    def _call(self, name: str, **kwargs):
        for cb in self.callbacks:
            hook = getattr(cb, name, None)
            if callable(hook):
                hook(**kwargs)

    # --------------- 공개 Hook 메서드 ---------------- #
    def on_train_start(self, **kwargs):  # noqa: D401
        self._call("on_train_start", **kwargs)

    def on_epoch_start(self, **kwargs):
        self._call("on_epoch_start", **kwargs)

    def on_step_end(self, **kwargs):
        self._call("on_step_end", **kwargs)

    def on_epoch_end(self, **kwargs):
        self._call("on_epoch_end", **kwargs)

    def on_train_end(self, **kwargs):
        self._call("on_train_end", **kwargs)

    # ------------------------------------------------ #
    def __iter__(self):
        return iter(self.callbacks)

    def __repr__(self) -> str:  # noqa: D401
        names = ", ".join(cb.__class__.__name__ for cb in self.callbacks)
        return f"{self.__class__.__name__}([{names}])"
