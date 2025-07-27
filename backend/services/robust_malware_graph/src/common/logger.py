# Lightweight logging utilities used across the project.
"""
src/common/logger.py
~~~~~~~~~~~~~~~~~~~~
프로젝트 전반에서 사용할 수 있는 가벼운 로거 헬퍼입니다.
콘솔 로그에 ANSI 색상 코드를 적용하며 파일 핸들러를 간단히 추가할 수 있습니다.

사용 예
-------
>>> from src.common.logger import get_logger
>>> log = get_logger(__name__, level="INFO", log_file="logs/run.log")
>>> log.info("ready!")
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Optional

__all__ = ["get_logger", "COLOR_MAP"]

# --------------------------------------------------------------------------- #
# 1. ANSI 색상 코드 (간단 매핑)
# --------------------------------------------------------------------------- #
RESET = "\x1b[0m"
COLOR_MAP: dict[int, str] = {
    logging.DEBUG:    "\x1b[38;21m",  # bright gray
    logging.INFO:     "\x1b[32;21m",  # green
    logging.WARNING:  "\x1b[33;21m",  # yellow
    logging.ERROR:    "\x1b[31;21m",  # red
    logging.CRITICAL: "\x1b[31;1m",   # bold red
}


class _ColorFormatter(logging.Formatter):
    """`levelname` 필드에만 색을 입히는 Formatter."""

    def __init__(self, fmt: str, datefmt: str | None = None, use_color: bool = True):
        super().__init__(fmt, datefmt)
        self._use_color = use_color

    def format(self, record: logging.LogRecord) -> str:
        if self._use_color and record.levelno in COLOR_MAP:
            record.levelname = f"{COLOR_MAP[record.levelno]}{record.levelname}{RESET}"
        return super().format(record)


# 싱글턴 캐시 – 동일 name에 대해 중복 handler 붙는 것 방지
_LOGGER_CACHE: dict[str, logging.Logger] = {}


# --------------------------------------------------------------------------- #
# 2. Handler 빌더
# --------------------------------------------------------------------------- #
def _build_stream_handler(level: int, use_color: bool) -> logging.Handler:
    fmt = "%(asctime)s | %(levelname)-9s | %(name)s:%(lineno)d | %(message)s"
    datefmt = "%H:%M:%S"
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(_ColorFormatter(fmt, datefmt, use_color))
    return handler


def _build_file_handler(level: int, filepath: Path) -> logging.Handler:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    fmt = "%(asctime)s | %(levelname)-9s | %(name)s:%(lineno)d | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    handler = logging.FileHandler(filepath, mode="a", encoding="utf-8")
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(fmt, datefmt))
    return handler


# --------------------------------------------------------------------------- #
# 3. Public helper
# --------------------------------------------------------------------------- #
def get_logger(
    name: str | None = None,
    *,
    level: int | str = logging.INFO,
    log_file: str | os.PathLike | None = None,
    color: bool = True,
    rank: int | None = None,
    force_reconfig: bool = False,
) -> logging.Logger:
    """
    Parameters
    ----------
    name
        Logger name (`None` ⇒ root logger).
    level
        최소 출력 레벨 (int 또는 "INFO"/"DEBUG" 형태 문자열).
    log_file
        경로 지정 시 같은 레벨로 파일 핸들러도 추가.
    color
        콘솔(levelname) 색상 사용 여부.
    rank
        DDP 등 멀티 프로세스 환경용. `rank>0`이면 콘솔 출력 생략.
    force_reconfig
        True면 기존 핸들러를 모두 제거하고 재구성.
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    cache_key = name or "root"
    if not force_reconfig and cache_key in _LOGGER_CACHE:
        return _LOGGER_CACHE[cache_key]

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # root 중복 출력 방지

    if force_reconfig:
        logger.handlers.clear()

    # rank>0 (GPU worker) → 콘솔 핸들러 건너뛰기
    if rank in (None, 0):
        logger.addHandler(_build_stream_handler(level, use_color=color))

    if log_file:
        logger.addHandler(_build_file_handler(level, Path(log_file)))

    _LOGGER_CACHE[cache_key] = logger
    return logger
