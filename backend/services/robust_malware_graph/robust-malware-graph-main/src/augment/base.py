"""
공통 인터페이스 및 편의 베이스클래스
=========================================

* AugmentBase   – 단일 증강 연산(op)용 Protocol
* ViewGenerator – 여러 op를 묶어 g' 또는 (g₁, g₂)를 만드는 Protocol
* SimpleAug     – name/hyperparams 자동 제공 ABC
* DualViewBase  – 2-view 생성기 기본 골격

그래프 타입은 PyTorch-Geometric `Data | HeteroData`,  NetworkX Graph,
또는 사용자 커스텀 클래스를 모두 허용합니다.
"""

from __future__ import annotations

import abc
from typing import Any, Dict, Generic, Protocol, TypeVar, runtime_checkable

# ──────────────────────────────────────────────────────────────
# 1. 제네릭 그래프 타입
# ──────────────────────────────────────────────────────────────
GraphT = TypeVar("GraphT")  # torch_geometric.data.Data 등


# ──────────────────────────────────────────────────────────────
# 2. 인터페이스 프로토콜
# ──────────────────────────────────────────────────────────────
@runtime_checkable
class AugmentBase(Protocol, Generic[GraphT]):
    """그래프 객체를 받아 **동일 유형**의 그래프를 반환해야 한다."""

    def __call__(self, g: GraphT) -> GraphT: ...

    @property
    def name(self) -> str:  # noqa: D401
        """읽기 전용 이름 (로깅·checkpoint 식별)."""

    def hyperparams(self) -> Dict[str, Any]:
        """재현성 목적으로 모든 하이퍼파라미터를 dict 로 반환."""


@runtime_checkable
class ViewGenerator(Protocol, Generic[GraphT]):
    """원본 그래프 → 1 or 2 개 증강 그래프를 생성."""

    def __call__(self, g: GraphT): ...  # noqa: D401,E701


# ──────────────────────────────────────────────────────────────
# 3. 편의 베이스 클래스
# ──────────────────────────────────────────────────────────────
class SimpleAug(abc.ABC, Generic[GraphT]):
    """
    AugmentBase 구현을 간소화하기 위한 ABC.

    * 생성자 인자를 그대로 인스턴스 변수로 저장
    * `name` 속성은 클래스명, `hyperparams()`는 public 속성 자동 수집
    """

    def __init__(self, **kwargs: Any):
        for k, v in kwargs.items():
            setattr(self, k, v)

    # --- AugmentBase 호환 메서드 -----------------------------
    @property
    def name(self) -> str:  # noqa: D401
        return self.__class__.__name__

    def hyperparams(self) -> Dict[str, Any]:  # noqa: D401
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    @abc.abstractmethod
    def __call__(self, g: GraphT) -> GraphT:
        """자식 클래스에서 증강 로직 구현."""


class DualViewBase(abc.ABC, Generic[GraphT]):
    """
    (g₁, g₂) 두 뷰를 반환하는 View Generator 기본 골격.

    * `ops_a`, `ops_b` : AugmentBase 리스트
    * 자식 클래스에서는 “op 호출 순서·규칙”만 정의하면 됨
    """

    def __init__(
        self,
        ops_a: list[AugmentBase[GraphT]],
        ops_b: list[AugmentBase[GraphT]],
    ):
        self.ops_a = ops_a
        self.ops_b = ops_b

    # --- ViewGenerator 호환 메서드 ---------------------------
    def __call__(self, g: GraphT):
        g1 = self._apply_ops(g, self.ops_a)
        g2 = self._apply_ops(g, self.ops_b)
        return g1, g2

    # --- 내부 헬퍼 -------------------------------------------
    @staticmethod
    def _apply_ops(g: GraphT, ops: list[AugmentBase[GraphT]]) -> GraphT:
        g_aug = g
        for op in ops:
            g_aug = op(g_aug)
        return g_aug


# ──────────────────────────────────────────────────────────────
# 4. public export
# ──────────────────────────────────────────────────────────────
__all__ = [
    "GraphT",
    "AugmentBase",
    "ViewGenerator",
    "SimpleAug",
    "DualViewBase",
]
