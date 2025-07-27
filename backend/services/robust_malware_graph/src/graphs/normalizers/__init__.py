"""
src.graphs.normalizers
======================

공개 API
-------
>>> from graphs.normalizers import get_normalizer, available
>>> print(available())                 # ['ast', 'cfg', 'fcg', 'syscall', ...]
>>> ast_norm = get_normalizer('ast').normalize(raw_ast)

 • get_normalizer(name, **kw) → NormalizerBase 인스턴스
 • available()                  → 등록된 노멀라이저 키 목록
 • register_normalizer(key)     → 데코레이터 (외부 플러그인 확장용)

노멀라이저 자동 탐색/등록은 `base.py` 내부 레지스트리가 처리합니다.
"""

from __future__ import annotations

from typing import List, TYPE_CHECKING

# 내부 구현에서 가져온 심벌 re-export
from .base import get_normalizer, register_normalizer
from .base import _NORMALIZER_REG as _REG  # 내부 딕셔너리

def available() -> List[str]:
    """현재 등록된 노멀라이저 키를 알파벳 순으로 반환."""
    return sorted(_REG.keys())

__all__: List[str] = ["get_normalizer", "register_normalizer", "available"]

# 선택: 패키지 버전 문자열 노출 (있을 때만)
try:
    from importlib.metadata import version as _ver
    __version__ = _ver("robust-malware-graph")
except Exception:                           # pragma: no cover
    __version__: str = "0.0.0"

from . import ast_norm, cfg_norm, fcg_norm, syscall_norm  # register built-ins

# IDE / 타입체커용 스타틱 임포트 힌트
if TYPE_CHECKING:                           # pragma: no cover
    from . import ast_norm                  # noqa: F401
    from . import cfg_norm                  # noqa: F401
    from . import fcg_norm                  # noqa: F401
    from . import syscall_norm              # noqa: F401
