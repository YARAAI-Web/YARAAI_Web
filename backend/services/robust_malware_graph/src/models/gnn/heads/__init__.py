# src/models/gnn/heads/__init__.py
"""
Heads package initializer.

‣ 기능
│  • 단일 전역 registry(`HEAD_REGISTRY`)에 헤드 클래스를 등록/조회
│  • 하위 모듈을 import 하여 side-effect 로 registry 채움
│  • 편의 함수: `register_head`, `get_head`, `available_heads`

예시
----
from src.models.gnn.heads import get_head

head = get_head("multi_class_mlp", num_classes=5, in_dim=256)
"""

from __future__ import annotations

import importlib
import pkgutil
from typing import Callable, Dict, List, Type

import torch.nn as nn


# --------------------------------------------------------------------------- #
# Registry
# --------------------------------------------------------------------------- #

HEAD_REGISTRY: Dict[str, Type[nn.Module]] = {}


def register_head(name: str) -> Callable[[Type[nn.Module]], Type[nn.Module]]:
    """
    Decorator 방식 등록:

    @register_head("binary")
    class BinaryHead(nn.Module):
        ...
    """

    def _register(cls: Type[nn.Module]) -> Type[nn.Module]:
        key = name.lower()
        if key in HEAD_REGISTRY:
            raise KeyError(f"Head '{key}' already registered.")
        if not issubclass(cls, nn.Module):
            raise TypeError("Only subclasses of torch.nn.Module can be registered.")
        HEAD_REGISTRY[key] = cls
        return cls

    return _register


def get_head(name: str, *args, **kwargs) -> nn.Module:
    """
    인스턴스 생성 헬퍼.

    Example
    -------
    head = get_head("multi_label_mlp", num_classes=6, in_dim=256)
    """
    key = name.lower()
    if key not in HEAD_REGISTRY:
        raise KeyError(
            f"Head '{key}' is not registered. "
            f"Available: {', '.join(sorted(HEAD_REGISTRY)) or 'None'}"
        )
    return HEAD_REGISTRY[key](*args, **kwargs)


def available_heads() -> List[str]:
    """현재 등록된 헤드 이름 목록 반환."""
    return sorted(HEAD_REGISTRY)


# --------------------------------------------------------------------------- #
# Auto-import submodules so their classes get registered via decorator/side-effect
# --------------------------------------------------------------------------- #

_current_pkg = __name__
for module_info in pkgutil.walk_packages(__path__, prefix=f"{_current_pkg}."):
    # 하위 패키지(ex: tests)는 건너뜀
    if module_info.ispkg:
        continue
    # importlib.import_module 로 side-effect import
    importlib.import_module(module_info.name)

# --------------------------------------------------------------------------- #
# 명시적 export
# --------------------------------------------------------------------------- #

__all__ = [
    "HEAD_REGISTRY",
    "register_head",
    "get_head",
    "available_heads",
]
