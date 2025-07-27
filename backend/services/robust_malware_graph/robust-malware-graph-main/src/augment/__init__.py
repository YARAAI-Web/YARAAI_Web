"""
src.augment
===========

기능
-----
1. 증강 연산(ops)·뷰(view) 클래스 **전역 레지스트리**
2. `@register_op`, `@register_view` 데코레이터로 자동 등록
3. 하위 패키지(ops / domain / view_generators) **동적 임포트**
4. YAML 한 장으로 파이프라인 재현 `build_from_yaml`

예시
-----
from augment import build_from_yaml
view_gen = build_from_yaml("cfgs/aug.yaml")
g1, g2 = view_gen(pyg_graph)
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
import warnings
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, List, Protocol, Type, TypeVar, Union

import yaml

# ──────────────────────────────────────────────────────────────
# 0. 공통 타입
# ──────────────────────────────────────────────────────────────
GraphT = TypeVar("GraphT")  # torch_geometric.data.Data | HeteroData | etc.


# ──────────────────────────────────────────────────────────────
# 1. 인터페이스 프로토콜
# ──────────────────────────────────────────────────────────────
class AugmentBase(Protocol[GraphT]):
    """단일 증강 연산(op)의 최소 인터페이스."""

    def __call__(self, g: GraphT) -> GraphT: ...

    @property
    def name(self) -> str: ...

    def hyperparams(self) -> Dict[str, Any]: ...


class ViewGenerator(Protocol[GraphT]):
    """여러 op를 묶어 (g₁, g₂) 또는 g' 를 반환."""

    def __call__(self, g: GraphT) -> Union[GraphT, tuple[GraphT, GraphT]]: ...


T_Aug = TypeVar("T_Aug", bound=AugmentBase)
T_View = TypeVar("T_View", bound=ViewGenerator)

# ──────────────────────────────────────────────────────────────
# 2. 전역 레지스트리 & 데코레이터
# ──────────────────────────────────────────────────────────────
OPS_REGISTRY: Dict[str, Type[AugmentBase]] = {}
VIEW_REGISTRY: Dict[str, Type[ViewGenerator]] = {}


def register_op(cls: Type[T_Aug]) -> Type[T_Aug]:
    """`augment.ops.*` 또는 `augment.domain.*` 클래스 등록용."""
    if not inspect.isclass(cls):
        raise TypeError("@register_op 는 클래스에만 사용할 수 있습니다.")
    OPS_REGISTRY[cls.__name__] = cls
    return cls


def register_view(cls: Type[T_View]) -> Type[T_View]:
    """`augment.view_generators.*` 클래스 등록용."""
    if not inspect.isclass(cls):
        raise TypeError("@register_view 는 클래스에만 사용할 수 있습니다.")
    VIEW_REGISTRY[cls.__name__] = cls
    return cls


# ──────────────────────────────────────────────────────────────
# 3. 하위 패키지 자동 임포트
# ──────────────────────────────────────────────────────────────
def _safe_import(name: str) -> ModuleType | None:
    try:
        return importlib.import_module(name)
    except ImportError as exc:
        warnings.warn(f"[augment] 모듈 '{name}' import 실패: {exc}", RuntimeWarning)
        return None


def _walk_and_import(pkg_name: str) -> None:
    """패키지 내부 모든 서브모듈 import → 데코레이터가 레지스트리 채움."""
    pkg = _safe_import(pkg_name)
    if pkg is None or not hasattr(pkg, "__path__"):
        return

    for mod in pkgutil.walk_packages(pkg.__path__, prefix=f"{pkg_name}."):
        _safe_import(mod.name)


for _sub in ("ops", "domain", "view_generators"):
    _walk_and_import(f"{__name__}.{_sub}")

# ──────────────────────────────────────────────────────────────
# 4. 빌더 유틸
# ──────────────────────────────────────────────────────────────
def build_op(name: str, **kwargs) -> AugmentBase:
    """레지스트리에서 증강 연산 인스턴스 생성."""
    if name not in OPS_REGISTRY:
        raise KeyError(f"[augment] Op '{name}' 이(가) 레지스트리에 없습니다.")
    return OPS_REGISTRY[name](**kwargs)  # type: ignore[call-arg]


def build_view(name: str, **kwargs) -> ViewGenerator:
    """레지스트리에서 뷰 생성기 인스턴스 생성."""
    if name not in VIEW_REGISTRY:
        raise KeyError(f"[augment] View '{name}' 이(가) 레지스트리에 없습니다.")
    return VIEW_REGISTRY[name](**kwargs)  # type: ignore[call-arg]


def _instantiate_ops(lst_cfg: List[Dict[str, Any]]) -> List[AugmentBase]:
    """YAML 리스트(dict) → op 객체 리스트."""
    insts: List[AugmentBase] = []
    for cfg in lst_cfg:
        cfg = dict(cfg)               # shallow copy
        op_name = cfg.pop("name")
        insts.append(build_op(op_name, **cfg))
    return insts


def build_from_yaml(path: str | Path) -> ViewGenerator:
    """
    YAML → ViewGenerator 복원.

    YAML 형식
    ----------
    view: StandardPair
    ops_a:
      - {name: NodeDrop, keep_prob: 0.2}
    ops_b:
      - {name: EdgeDrop, keep_prob: 0.2}
    """
    with Path(path).expanduser().open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    if not isinstance(cfg, dict):
        raise ValueError("YAML 구조가 dict 형태여야 합니다.")

    ops_a = _instantiate_ops(cfg.get("ops_a", []))
    ops_b = _instantiate_ops(cfg.get("ops_b", []))

    view_name: str = cfg["view"]
    other_kwargs = {k: v for k, v in cfg.items() if k not in {"view", "ops_a", "ops_b"}}

    return build_view(view_name, ops_a=ops_a, ops_b=ops_b, **other_kwargs)


# 하위 모듈에서 사용할 통합 빌더(registry) 노출
from . import registry  # noqa: E402


# ──────────────────────────────────────────────────────────────
# 5. 공개 API
# ──────────────────────────────────────────────────────────────
__all__ = [
    # 인터페이스
    "AugmentBase",
    "ViewGenerator",
    # 레지스트리·데코레이터
    "OPS_REGISTRY",
    "VIEW_REGISTRY",
    "register_op",
    "register_view",
    # 빌더
    "build_op",
    "build_view",
    "build_from_yaml",
    "registry",
]
