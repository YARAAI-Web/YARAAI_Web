"""
src.graphs.loaders
==================

패키지 공개 API
---------------
`factory.py` 에 구현된 *편의 함수* 두 가지만 re-export 합니다.

>>> from graphs.loaders import get_loader, available
>>> print(available())         # ['ast', 'cfg', 'fcg', 'syscall', ...]
>>> g = get_loader('ast').load('/path/sample.ast.json')

• get_loader(name, **kw) → GraphLoaderBase 인스턴스
• available()              → 등록된 로더 키 리스트

로더 자동 탐색/플러그인 로딩은 내부적으로 factory 가 처리하므로,
패키지를 import 하는 시점에는 비용이 거의 없습니다.

추가 심벌(GraphLoaderBase, register_loader 등)이 필요하면
`graphs.loaders.base` 모듈을 직접 import 하십시오.
"""

from __future__ import annotations

from typing import List, TYPE_CHECKING

# public façade – 내부 구현은 factory.py
from .factory import available, get_loader

__all__: List[str] = ["get_loader", "available"]

# (선택) 패키지 버전 노출 – 프로젝트 메타데이터가 있을 때만
try:
    from importlib.metadata import version as _ver

    __version__ = _ver("robust-malware-graph")
except Exception:  # pragma: no cover
    __version__ = "0.0.0"

# IDE / 타입체커 힌트용 (런타임 import X)
if TYPE_CHECKING:  # pragma: no cover
    from . import base  # noqa: F401
    from . import ast_loader  # noqa: F401
    from . import cfg_loader  # noqa: F401
    from . import fcg_loader  # noqa: F401
    from . import syscall_loader  # noqa: F401
