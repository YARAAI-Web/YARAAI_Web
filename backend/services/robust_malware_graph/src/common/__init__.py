"""
src.common package
==================
공통 유틸리티·설정 모듈 모음

외부에서 바로 쓰기 좋은 심볼만 re-export 해 두었으니,
모듈 경로 타이핑을 줄일 때 import * 대신 사용하세요.

Examples
--------
>>> from src.common import get_logger, settings
>>> log = get_logger(__name__)
>>> log.info("device = %s", settings.DEVICE)
"""

from __future__ import annotations

# 기본 로깅 · 설정
from .logger import get_logger, COLOR_MAP          # noqa: F401
try:  # optional heavy dependency
    from .config import settings, update_config        # noqa: F401
except Exception as exc:  # pragma: no cover - allow missing torch
    import logging

    logging.getLogger(__name__).warning("config import failed: %s", exc)

    settings = None  # type: ignore[misc]

    def update_config(*_args: object, **_kwargs: object) -> None:  # type: ignore
        raise RuntimeError("src.common.config unavailable")

# 범용 헬퍼
from .utils import (                               # noqa: F401
    set_random_seed,
    tqdm_wrap,
    ensure_dir,
    timer,
)
from .running_stats import RunningStats  # noqa: F401

__all__: list[str] = [
    # logger.py
    "get_logger",
    "COLOR_MAP",
    # config.py
    "settings",
    "update_config",
    # utils.py
    "set_random_seed",
    "tqdm_wrap",
    "ensure_dir",
    "timer",
    "RunningStats",
]

# --------------------------------------------------------------------------- #
# Package-level logger 초기화 (선택 사항)
# --------------------------------------------------------------------------- #
# 패키지 import 직후에도 로그를 바로 찍을 수 있도록,
# logger를 생성해 두되 출력은 필요할 때 가져다 쓰도록 한다.
_log = get_logger("src.common")
_log.debug("src.common package imported successfully")
