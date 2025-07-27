# --------------------------------------------------------------------------- #
# src/continual/__init__.py
# --------------------------------------------------------------------------- #
"""
continual
=========
온라인‧증분 학습 파이프라인을 구성하는 모듈 묶음.

Quick-start
-----------
>>> import continual as ct
>>> ct.set_random_seed(42)
>>> buf = ct.get_replay_buffer("reservoir", capacity=10_000)
>>> stream = ct.GraphStream(...)            # 실제 스트림 구현체
>>> learner = ct.L2PLearner(buffer=buf, ...)  # 예시

노출 심볼
---------
* **Utilities**   : ``set_random_seed``, ``get_logger``
* **ReplayBuffer**: ``get_replay_buffer`` + 각 버퍼 클래스
* **DataStream**  : ``GraphStream`` (샘플 스트림 인터페이스)
* **Learners**    : ``SupConLearner``, ``L2PLearner``, ``EWCLearner`` …
* **Evaluation**  : ``metrics`` 서브모듈
* **Version**     : ``__version__``  (PEP 440)
"""

from __future__ import annotations

from .learner import SupConLearner, EWCLearner, L2PLearner

# --------------------------------------------------------------------------- #
# Version (PEP 440) – pkg metadata 있으면 읽고, 없으면 '0.0.0'
# --------------------------------------------------------------------------- #
try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover – <3.8 fallback
    from importlib_metadata import version, PackageNotFoundError  # type: ignore

try:
    __version__: str = version("robust-malware-graph")
except PackageNotFoundError:  # 개발 단계 / editable 설치 X
    __version__ = "0.0.0"

# --------------------------------------------------------------------------- #
# Core utilities – lightweight, 즉시 import
# --------------------------------------------------------------------------- #
from .utils import set_random_seed, get_logger  # noqa: E402

# --------------------------------------------------------------------------- #
# Replay buffers – 경량, 즉시 import
# --------------------------------------------------------------------------- #
from .replay_buffers import (  # noqa: E402
    BaseReplayBuffer,
    FifoBuffer,
    ReservoirBuffer,
    RingBuffer,
    TagExpBuffer,
    get_replay_buffer,
)

# --------------------------------------------------------------------------- #
# Lazy sub-package 노출
# --------------------------------------------------------------------------- #
# learner / datastream / evaluation 등은 의존성이 무겁거나,
# PyTorch-CUDA context 초기화 등을 포함할 수 있으므로 **지연 로딩**한다.
import importlib
import sys
from types import ModuleType
from typing import Any


def __getattr__(name: str) -> Any:  # noqa: D401
    """
    서브패키지를 *필요할 때* 가져오는 lazy import 디스패처.

    지원 이름
    ----------
    * Learners   : ``SupConLearner``, ``L2PLearner``, ``EWCLearner`` …
    * DataStream : ``GraphStream``, ``StreamSampler`` …
    * Evaluation : ``metrics`` 모듈
    * Callbacks  : ``EarlyStop``, ``LoggerCallback`` …
    """
    _lazy_submodules = {
        # subpackage → attr list (or None = export submodule itself)
        "learner": None,
        "datastream": None,
        "evaluation": None,
        "callbacks": None,
        "cli": None,
    }

    # -------- 1) 모듈 요청 -------- #
    if name in _lazy_submodules:
        module = importlib.import_module(f".{name}", __name__)
        sys.modules[f"{__name__}.{name}"] = module
        return module

    # -------- 2) 심볼 요청 -------- #
    for subpkg, attrs in _lazy_submodules.items():
        module_path = f"{__name__}.{subpkg}"
        try:
            module: ModuleType = sys.modules.get(module_path) or importlib.import_module(
                f".{subpkg}", __name__
            )
        except ModuleNotFoundError:  # pragma: no cover
            continue

        if attrs is None:  # 모든 공개 심볼 허용
            if hasattr(module, name):
                return getattr(module, name)
        else:  # 제한된 attr만 허용
            if name in attrs:
                return getattr(module, name)

    # 요청한 이름을 찾지 못한 경우
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# --------------------------------------------------------------------------- #
# Public re-exports
# --------------------------------------------------------------------------- #
__all__ = [
    "__version__",
    # utils
    "set_random_seed",
    "get_logger",
    # replay buffer
    "BaseReplayBuffer",
    "FifoBuffer",
    "ReservoirBuffer",
    "RingBuffer",
    "TagExpBuffer",
    "get_replay_buffer",
    # lazy-loaded(문서화 목적) – 실제 접근 시 __getattr__에서 import
    "GraphStream",
    "SupConLearner",
    "L2PLearner",
    "EWCLearner",
    "metrics",
]
