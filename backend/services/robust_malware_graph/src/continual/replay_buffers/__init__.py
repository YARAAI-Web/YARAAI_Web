# --------------------------------------------------------------------------- #
# src/continual/replay_buffers/__init__.py
# --------------------------------------------------------------------------- #
"""
continual.replay_buffers
========================
다양한 리플레이 버퍼 전략(Reservoir, Ring, Tag-Exp …)을 한곳에 모은 서브패키지.

빠른 사용 – Factory
-------------------
>>> from continual.replay_buffers import get_replay_buffer
>>> buf = get_replay_buffer("reservoir", capacity=10_000, seed=123)

* ``name`` 인자는 대·소문자 무시하며, ``"-"`` / ``"_"`` 표기도 동등 처리됩니다.
"""

from __future__ import annotations

from typing import Dict, Type

from .base import BaseReplayBuffer, FifoBuffer, collate_graph_samples
from .reservoir import ReservoirBuffer
from .ring import RingBuffer
from .tagexp import TagExpBuffer

__all__ = [
    # core API
    "BaseReplayBuffer",
    "collate_graph_samples",
    # concrete buffers
    "FifoBuffer",
    "ReservoirBuffer",
    "RingBuffer",
    "TagExpBuffer",
    # factory helper
    "get_replay_buffer",
]

# --------------------------------------------------------------------------- #
# Internal mapping : str → BufferClass
# --------------------------------------------------------------------------- #
_BUFFERS: Dict[str, Type[BaseReplayBuffer]] = {
    # canonical
    "fifo": FifoBuffer,
    "reservoir": ReservoirBuffer,
    "ring": RingBuffer,
    "tagexp": TagExpBuffer,
    # aliases
    "tag_exp": TagExpBuffer,
    "tag-exp": TagExpBuffer,
}

# --------------------------------------------------------------------------- #
# Public factory
# --------------------------------------------------------------------------- #
def get_replay_buffer(name: str, /, **kwargs) -> BaseReplayBuffer:
    """
    이름 기반 버퍼 인스턴스 생성 헬퍼.

    Parameters
    ----------
    name : {"fifo", "reservoir", "ring", "tagexp", …}
        대/소문자 구분 없음. ``tag-exp``·``tag_exp`` 모두 허용.
    **kwargs
        해당 버퍼 클래스 생성자에 그대로 전달.

    Returns
    -------
    BaseReplayBuffer
        초기화된 버퍼 객체.

    Raises
    ------
    ValueError
        지원하지 않는 이름인 경우.
    """
    key = name.lower().replace("-", "").replace("_", "")
    if key not in _BUFFERS:
        raise ValueError(
            f"Unknown replay buffer '{name}'. "
            f"Available: {sorted(set(_BUFFERS.keys()))}"
        )
    return _BUFFERS[key](**kwargs)
