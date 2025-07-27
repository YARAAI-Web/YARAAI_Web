"""
src.graphs.normalizers.base
===========================

⟦NormalizerBase⟧
-----------------
• Raw(또는 View Loader가 반환한) 그래프를
  ▸ **스키마 호환** 노드·엣지 타입
  ▸ **속성 화이트리스트**(schema.NODE_ATTRS) 필터링
  ▸ **속성 dtype/shape** 일관화
  로 정규화한다.

주요 기능
--------
1. register_normalizer(name)  : decorator (글로벌 레지스트리)
2. get_normalizer(name, ...)  : factory
3. NormalizerBase.normalize() : 공통 pre/post → _normalize_graph() 구현만 하면 OK
4. strict mode                : 스키마 불일치 시 예외/경고 선택
"""

from __future__ import annotations

import abc
import logging
from typing import Dict, List, Optional, Sequence, Type, Union, overload

import torch
from torch_geometric.data import Data, HeteroData

from ..utils import get_logger
from .schema import (  # noqa: WPS347 (relative import ok)
    EDGE_REL_ID,
    NODE_ATTRS,
    NODE_TYPE_ID,
    EdgeRel,
    NodeType,
)

# ────────────────────────────────────────────────────────────────────────────
# 레지스트리 & 데코레이터
# ────────────────────────────────────────────────────────────────────────────
_NORMALIZER_REG: Dict[str, Type["NormalizerBase"]] = {}


def register_normalizer(name: str):
    """`@register_normalizer("cfg")` 로 등록."""
    def _wrap(cls: Type["NormalizerBase"]):
        if name in _NORMALIZER_REG:
            raise KeyError(f"Normalizer '{name}' already registered")
        _NORMALIZER_REG[name] = cls
        cls.NORM_NAME = name
        return cls
    return _wrap


def get_normalizer(name: str, **kwargs) -> "NormalizerBase":
    try:
        cls = _NORMALIZER_REG[name]
    except KeyError as e:
        raise ValueError(f"Unknown normalizer '{name}'") from e
    return cls(**kwargs)  # type: ignore[return-value]


# ────────────────────────────────────────────────────────────────────────────
# 타입 별칭
# ────────────────────────────────────────────────────────────────────────────
GraphT = Union[Data, HeteroData]

# ────────────────────────────────────────────────────────────────────────────
# Base Class
# ────────────────────────────────────────────────────────────────────────────
class NormalizerBase(abc.ABC):
    """
    Abstract base for all view‐specific graph normalizers.

    Parameters
    ----------
    strict : bool, default True
        True  → 스키마 불일치(미정의 타입/속성) 시 ValueError
        False → 경고만 출력하고 best-effort 정규화
    """

    NORM_NAME: str = "base"

    def __init__(self, *, strict: bool = True, log_level: int = logging.INFO) -> None:
        self.strict = strict
        self.log = get_logger(f"norm.{self.NORM_NAME}", log_level)

    # ────────────────────────────────────────────────────────────────────
    # 공용 진입점
    # ────────────────────────────────────────────────────────────────────
    def normalize(self, g: GraphT, **kwargs) -> GraphT:
        """
        GraphT → GraphT (in‐place 가능).

        1) 하위 클래스 _normalize_graph() 호출
        2) 공통 후처리: 스키마 검증 / attribute 필터
        """
        g = self._normalize_graph(g, **kwargs)

        # 2-1) 노드 타입/속성 검증
        self._validate_node_attrs(g)

        # 2-2) (선택) edge_type sanity
        self._validate_edge_types(g)

        return g

    # ────────────────────────────────────────────────────────────────────
    # 서브클래스 필수 구현
    # ────────────────────────────────────────────────────────────────────
    @abc.abstractmethod
    def _normalize_graph(self, g: GraphT, **kwargs) -> GraphT:  # noqa: N802
        """뷰별 로직: 타입 이름 매핑·속성 보강 등을 수행."""
        raise NotImplementedError

    # ────────────────────────────────────────────────────────────────────
    # 내부 유틸
    # ────────────────────────────────────────────────────────────────────
    def _validate_node_attrs(self, g: GraphT) -> None:
        """
        • 허용되지 않은 속성 → 제거(strict=False) 또는 ValueError(strict=True)
        • dtype 미일치 시 torch.*Tensor 로 강제 캐스팅 (strict=True에서 오류)
        """
        for ntype, attrs in g.node_items():
            if ntype not in NODE_ATTRS:
                self._handle_error(f"Unknown node type '{ntype}'", ntype)
                continue

            allowed = set(NODE_ATTRS[NodeType(ntype)])
            to_drop: List[str] = []
            for k, v in attrs.items():
                if k not in allowed:
                    self._handle_error(f"{ntype}: drop attr '{k}' (not in schema)", ntype)
                    to_drop.append(k)
                elif isinstance(v, torch.Tensor):
                    continue
                elif isinstance(v, str):
                    # string attributes (e.g. function name) remain as-is
                    continue
                elif isinstance(v, Sequence) and all(isinstance(x, str) for x in v):
                    # ensure list type for sequences of strings
                    attrs[k] = list(v)
                else:  # list/np.ndarray etc. → torch
                    try:
                        attrs[k] = torch.as_tensor(v)
                    except Exception as e:  # pragma: no cover
                        self._handle_error(f"{ntype}.{k}: tensor cast fail {e}", ntype)

            for k in to_drop:
                attrs.pop(k, None)

    def _validate_edge_types(self, g: GraphT) -> None:
        if isinstance(g, HeteroData):
            for (src, rel, dst), store in g.edge_items():
                if rel not in EDGE_REL_ID:
                    self._handle_error(f"Unknown edge rel '{rel}'", rel)
                if "edge_type" not in store:
                    # edge_type 없으면 자동 설정
                    store["edge_type"] = torch.full(
                        (store["edge_index"].shape[1],),
                        EDGE_REL_ID.get(rel, -1),
                        dtype=torch.long,
                    )

    # error / warning switch
    def _handle_error(self, msg: str, ctx: str) -> None:  # noqa: D401
        if self.strict:
            raise ValueError(f"[{self.NORM_NAME}] {msg}")
        self.log.warning(msg, extra={"ctx": ctx})
