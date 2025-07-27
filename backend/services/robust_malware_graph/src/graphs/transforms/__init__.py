"""
src.graphs.transforms
=====================

공개 API
--------
>>> from graphs.transforms import (
...     GraphAugmentTransform,  # 증강 파이프라인 래퍼
...     GraphPruner,           # 중요도 기반 노드·엣지 프루닝
...     AttributeScaler,       # 표준화 / 정규화 / 양자화
...     available,             # 지원 변환 목록 조회
... )

새로운 변환을 추가하려면
-----------------------
1. `src/graphs/transforms/` 하위에 모듈을 추가하고
2. 아래 `_TRANSFORMS` 딕셔너리에 키/클래스를 등록하면 됩니다.
"""

from __future__ import annotations

from typing import Dict, List, TYPE_CHECKING, Type

# 개별 모듈에서 필요한 클래스 가져오기
from .augment_bridge import GraphAugmentTransform
from .pruner import GraphPruner
from .attrib_scaler import AttributeScaler

# 내부 레지스트리  ────────────────────────────────────────────────
_TRANSFORMS: Dict[str, Type] = {
    "augment": GraphAugmentTransform,
    "pruner": GraphPruner,
    "scaler": AttributeScaler,
}

# 헬퍼 함수  ──────────────────────────────────────────────────────
def available() -> List[str]:
    """현재 등록된 변환 키를 알파벳순으로 반환합니다."""
    return sorted(_TRANSFORMS.keys())

def get(name: str, **kwargs):
    """
    문자열 키로 변환 인스턴스를 생성합니다.

    Examples
    --------
    >>> scaler = get("scaler", mode="minmax")
    """
    try:
        cls = _TRANSFORMS[name]
    except KeyError as e:
        raise ValueError(f"Unknown transform '{name}'. "
                         f"Use one of: {', '.join(available())}") from e
    return cls(**kwargs)  # type: ignore[return-value]

# re-export 목록  ────────────────────────────────────────────────
__all__: List[str] = [
    "GraphAugmentTransform",
    "GraphPruner",
    "AttributeScaler",
    "available",
    "get",
]

# IDE / 타입체커용 힌트  ─────────────────────────────────────────
if TYPE_CHECKING:          # pragma: no cover
    from . import augment_bridge  # noqa: F401
    from . import pruner          # noqa: F401
    from . import attrib_scaler   # noqa: F401
