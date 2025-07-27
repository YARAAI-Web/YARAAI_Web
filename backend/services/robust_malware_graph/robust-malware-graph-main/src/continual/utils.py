"""
src.continual.utils
===================

공통 유틸리티 – 실시간 · 온라인 Continual Learning 모듈 전역에서 재사용.

Functions
---------
set_random_seed      : NumPy / PyTorch / Python RNG 고정
get_logger           : 싱글턴 Logger (ANSI 색 지원)
ensure_dir           : `mkdir -p` 동작
tqdm_wrap            : tqdm 없을 때 no-op 래퍼
timer                : with 문 기반 성능 계측
AverageMeter         : 지수·단순 이동평균 지원 메트릭 트래커
batch_to_device      : (nested) Tensor/Dict/List → GPU/CPU 이동
is_rank_zero         : DDP 환경에서 메인 프로세스 여부 판별
"""

from __future__ import annotations

import logging
import os
import random
import sys
from contextlib import contextmanager
from pathlib import Path
from time import perf_counter
from typing import Any, Iterable, Iterator, Mapping, MutableMapping, Sequence

import numpy as np
import torch

# --------------------------------------------------------------------------- #
# 1. 시드 고정
# --------------------------------------------------------------------------- #
def set_random_seed(seed: int = 42, *, deterministic: bool = False) -> None:
    """
    모든 주요 RNG(py, np, torch)의 시드를 고정한다.

    Parameters
    ----------
    seed : int
        사용할 시드 값.
    deterministic : bool, optional
        True면 PyTorch 연산을 완전 결정론적으로 강제(cudnn.benchmark=False 등).
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    if deterministic:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True


# --------------------------------------------------------------------------- #
# 2. Logger – 싱글턴 패턴
# --------------------------------------------------------------------------- #
_LOGGERS: dict[str, logging.Logger] = {}

def get_logger(name: str = "continual") -> logging.Logger:
    """
    ANSI 색상 포맷을 포함한 스트림 Logger를 반환한다.
    (같은 이름이면 동일 인스턴스 재사용)

    Examples
    --------
    >>> logger = get_logger(__name__)
    >>> logger.info("Start online learning…")
    """
    if name in _LOGGERS:
        return _LOGGERS[name]

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO if is_rank_zero() else logging.WARNING)

    # 중복 핸들러 방지
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "[%(asctime)s] \x1b[1m%(levelname)s\x1b[0m "
            "\x1b[34m%(name)s\x1b[0m: %(message)s",
            datefmt="%H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    _LOGGERS[name] = logger
    return logger


# --------------------------------------------------------------------------- #
# 3. 편의 함수
# --------------------------------------------------------------------------- #
def ensure_dir(path: os.PathLike | str) -> Path:
    """`mkdir -p` 동작을 수행하고 Path 객체를 반환."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def is_rank_zero() -> bool:
    """DDP/TPU 등 분산 환경에서 '주 프로세스'인지 확인."""
    return (not torch.distributed.is_available()) or (
        not torch.distributed.is_initialized()
    ) or (torch.distributed.get_rank() == 0)


# --------------------------------------------------------------------------- #
# 4. tqdm 래퍼 – tqdm 미설치 시 graceful fallback
# --------------------------------------------------------------------------- #
def tqdm_wrap(iterable: Iterable[Any], *args, **kwargs) -> Iterable[Any]:
    """
    tqdm이 import 불가능하면 원본 iterable 그대로 반환.

    Returns
    -------
    Iterable
        tqdm.tqdm(…) 혹은 그대로 iterable
    """
    try:
        from tqdm.auto import tqdm  # type: ignore
        return tqdm(iterable, *args, **kwargs)
    except ModuleNotFoundError:
        return iterable


# --------------------------------------------------------------------------- #
# 5. 성능 계측 타이머
# --------------------------------------------------------------------------- #
@contextmanager
def timer(name: str = "block", logger: logging.Logger | None = None):
    """
    with 블록의 wall-time(sec)을 측정하여 로그로 남긴다.

    Examples
    --------
    >>> with timer("supcon-step"):
    ...     learner.train_step(batch)
    """
    _logger = logger or get_logger("timer")
    start = perf_counter()
    yield
    dur = perf_counter() - start
    _logger.info(f"{name} took {dur:.3f}s")


# --------------------------------------------------------------------------- #
# 6. Metric Tracker
# --------------------------------------------------------------------------- #
class AverageMeter:
    """
    단순/지수 이동평균 둘 다 지원하는 메트릭 누적기.

    Attributes
    ----------
    value : float
        최근 업데이트 값.
    avg : float
        누적 평균(단순 or EMA).
    """

    def __init__(self, alpha: float | None = None):
        """
        Parameters
        ----------
        alpha : float, optional
            0<alpha<1이면 EMA 계수, None이면 단순 평균.
        """
        self.alpha = alpha
        self.reset()

    def reset(self) -> None:
        self.count = 0
        self.sum = 0.0
        self.avg = 0.0
        self.value = 0.0

    def update(self, val: float, n: int = 1) -> None:
        self.value = float(val)
        if self.alpha is None:
            self.count += n
            self.sum += val * n
            self.avg = self.sum / self.count
        else:
            # EMA
            self.avg = self.alpha * val + (1 - self.alpha) * self.avg


# --------------------------------------------------------------------------- #
# 7. 배치 디바이스 이동
# --------------------------------------------------------------------------- #
def batch_to_device(batch: Any, device: torch.device | str) -> Any:
    """
    (Tensor, Dict[str,Tensor], List, Tuple …) 재귀 이동.

    Examples
    --------
    >>> batch = {"g": graph, "y": torch.tensor([1])}
    >>> batch = batch_to_device(batch, "cuda")
    """
    if torch.is_tensor(batch):
        return batch.to(device)

    if isinstance(batch, Mapping):
        return {k: batch_to_device(v, device) for k, v in batch.items()}

    if isinstance(batch, (tuple, list)):
        return type(batch)(batch_to_device(obj, device) for obj in batch)

    # DGL / PyG Graph 등 .to() 지원 객체
    if hasattr(batch, "to"):
        try:
            return batch.to(device)
        except Exception:  # pragma: no cover
            pass

    return batch  # 그대로 반환


# --------------------------------------------------------------------------- #
# 8. 모듈 import 시 기본 초기화
# --------------------------------------------------------------------------- #
# (CLI 진입 시 자동으로 재현성을 보장)
if int(os.getenv("CL_SEED_AUTO_INIT", "1")):
    set_random_seed(42)
