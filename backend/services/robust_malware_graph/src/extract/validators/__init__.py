"""
src.extract.validators
======================

High-level facade around three sub-modules:

1. ``schema``        – Pydantic 구조(필드) 검증
2. ``sanity_checks`` – 도메인 특화 논리 검증
3. ``fixer``         – 경미한 오류 자동 패치

빠르게 활용하고 싶다면 아래 세 가지 헬퍼가 전부입니다.

>>> from src.extract.validators import validate, check, clean
>>> model = validate("cfg", cfg_json_dict)          # 구조 검증
>>> check("cfg", cfg_json_dict)                     # 구조 + 논리 검증
>>> fixed, report = clean("cfg", cfg_json_dict)     # 검증 + 자동수정
"""

from __future__ import annotations

from typing import Any, Dict, Tuple

from .schema import (  # re-export public schema API
    ASTView,
    CFGView,
    FCGView,
    ImportView,
    SysCallView,
    ViewName,
    validate_view,
)
from .sanity_checks import SanityError, sanity_check
from .fixer import FixReport, fix_view

# --------------------------------------------------------------------------- #
# Facade helpers
# --------------------------------------------------------------------------- #
def validate(view: str | ViewName, data: Any):
    """
    **Structure-only** 검증 (``schema.validate_view`` alias).

    Returns
    -------
    pydantic model instance (e.g., ``CFGView``)
    """
    return validate_view(view, data)


def check(view: str | ViewName, data: Any, *, strict: bool = True):
    """
    Structure + Sanity 검증.

    Parameters
    ----------
    strict : bool, default True
        • True  → 위반 시 ``SanityError`` 즉시 발생
        • False → 경고 리스트(List[str]) 반환
    """
    return sanity_check(view, data, strict=strict)


def clean(
    view: str | ViewName,
    data: Any,
    *,
    max_iter: int = 3,
) -> Tuple[Dict[str, Any], FixReport]:
    """
    ``validate`` + ``fix_view`` + ``sanity_check``를 연속 수행하여
    *가능한 한* 문제를 자동으로 고칩니다.

    Returns
    -------
    fixed_data : dict
        패치 후 JSON-serialisable 딕셔너리.
    report : FixReport
        패치 상세 내역.

    Raises
    ------
    RuntimeError
        ``max_iter`` 반복 내에도 고치지 못한 치명적 손상.
    """
    return fix_view(view, data, max_iter=max_iter)


# --------------------------------------------------------------------------- #
# Public re-exports
# --------------------------------------------------------------------------- #
__all__ = [
    # facade
    "validate",
    "check",
    "clean",
    # schema API
    "ViewName",
    "ASTView",
    "CFGView",
    "FCGView",
    "SysCallView",
    "ImportView",
    "validate_view",
    # sanity API
    "SanityError",
    "sanity_check",
    # fixer API
    "FixReport",
    "fix_view",
]
