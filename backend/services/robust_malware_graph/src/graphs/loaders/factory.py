"""
src.graphs.loaders.factory
==========================

문자열 키 하나로 GraphLoader 인스턴스를 얻기 위한 편의 레이어.

주요 기능
--------
1. 내부 *_loader.py 모듈 자동 import
2. 외부 패키지 플러그인(entry_points) 자동 로드
3. available()  : 현재 등록된 로더 키 목록
4. get_loader() : 로더 인스턴스 반환

Entry-point 예시(pyproject.toml)
--------------------------------
[project.entry-points."robust_malware_graph.loaders"]
pe_loader = "my_pkg.pe_loader:PELoader"
"""

from __future__ import annotations

import importlib
import pkgutil
from importlib.metadata import entry_points
from pathlib import Path
from typing import List

from . import base as _base
from .base import GraphLoaderBase

# --------------------------------------------------------------------------- #
# 1) 내부 *_loader.py 모듈 자동 import
# --------------------------------------------------------------------------- #
def _import_builtin_loaders() -> None:
    """패키지 내부에서 *_loader.py 파일을 찾아 import → 레지스트리 등록."""
    pkg_path = Path(__file__).resolve().parent            # .../loaders
    pkg_name = __package__                                # 'src.graphs.loaders'

    for module_info in pkgutil.iter_modules([str(pkg_path)]):
        name = module_info.name
        if (
            name.startswith("_") or                       # _private.py 제외
            name in {"base", "factory"} or                # 현재/베이스 모듈 제외
            not name.endswith("_loader")                  # 패턴 미일치
        ):
            continue
        importlib.import_module(f"{pkg_name}.{name}")

_import_builtin_loaders()

# --------------------------------------------------------------------------- #
# 2) 외부 플러그인(importlib.metadata entry_points)
# --------------------------------------------------------------------------- #
def _import_plugin_loaders() -> None:
    """entry_points(group='robust_malware_graph.loaders') 로 등록된 로더 import."""
    try:
        eps = entry_points(group="robust_malware_graph.loaders")
    except TypeError:  # Python<3.10 호환
        eps = entry_points().get("robust_malware_graph.loaders", ())

    for ep in eps:
        ep.load()  # 클래스 반환 → @register_loader 데코레이터로 자동 등록

_import_plugin_loaders()

# --------------------------------------------------------------------------- #
# 3) public API
# --------------------------------------------------------------------------- #
def available() -> List[str]:
    """현재 등록된 로더 키를 알파벳순으로 반환."""
    return sorted(_base._LOADER_REGISTRY.keys())


def get_loader(name: str, **kwargs) -> GraphLoaderBase:
    """
    Parameters
    ----------
    name : str
        로더 키(예: 'ast', 'cfg', 'fcg', …).
    **kwargs
        로더 클래스 생성자 인자(cache_dir, force_reload 등).

    Returns
    -------
    GraphLoaderBase
        요청된 로더 인스턴스.
    """
    return _base.get_loader(name, **kwargs)  # type: ignore[return-value]


__all__ = ["available", "get_loader"]
