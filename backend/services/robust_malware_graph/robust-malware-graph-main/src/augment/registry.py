# src/augment/registry.py
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, List

from . import build_op, build_view

__all__ = ["build", "AugmentBuilderError"]


class AugmentBuilderError(RuntimeError):
    """Raised when a configuration dictionary cannot be resolved into an augmentation."""


# --------------------------------------------------------------------------- #
# internal helpers
# --------------------------------------------------------------------------- #
def _build_op_from_cfg(cfg: Mapping[str, Any]):
    """Single-operator factory with basic validation."""
    if "name" not in cfg:  # defensive check
        raise AugmentBuilderError("Operator config must contain a 'name' field.")
    cfg = dict(cfg)               # shallow copy to avoid side-effects
    name = cfg.pop("name")
    return build_op(name, **cfg)


def _parse_ops(key: str, cfg_list: List[Mapping[str, Any]] | None) -> List[Any]:
    """Convert a list of operator-config dicts into operator instances."""
    if not cfg_list:
        return []
    if not isinstance(cfg_list, list):
        raise AugmentBuilderError(f"Expected '{key}' to be a list, got {type(cfg_list).__name__}")
    return [_build_op_from_cfg(c) for c in cfg_list]


# --------------------------------------------------------------------------- #
# public entrypoint
# --------------------------------------------------------------------------- #
def build(cfg: Mapping[str, Any]):
    """
    Instantiate an augmentation operator *or* a two-view generator from ``cfg``.

    Examples
    --------
    >>> build({"type": "drop_node", "p": 0.3})
    >>> build({
    ...     "view": "standard_pair",
    ...     "ops_a": [{"name": "drop_node", "p": 0.2}],
    ...     "ops_b": [{"name": "attr_mask", "p": 0.1, "cols": ["opcode"]}],
    ...     "prob": 0.5
    ... })
    >>> build({  # RandomPair: op_pool + k
    ...     "view": "random_pair",
    ...     "op_pool": [
    ...         {"name": "drop_edge", "p": 0.1},
    ...         {"name": "attr_mask", "p": 0.2}
    ...     ],
    ...     "k": 2
    ... })
    """
    if not isinstance(cfg, Mapping):
        raise AugmentBuilderError("cfg must be a mapping (dict-like) object")

    # ── (A) 단일 증강 연산 ----------------------------------------------------
    if "type" in cfg:
        op_cfg = dict(cfg)
        name = op_cfg.pop("type")
        return build_op(name, **op_cfg)

    # ── (B) 두-뷰 생성기 ------------------------------------------------------
    if "view" in cfg:
        view_cfg = dict(cfg)          # shallow copy

        view_name = view_cfg.pop("view")

        # 명시적 per-view 목록
        ops_a = _parse_ops("ops_a", view_cfg.pop("ops_a", []))
        ops_b = _parse_ops("ops_b", view_cfg.pop("ops_b", []))

        # RandomPair 등에서 op_pool 한 번에 주는 것도 지원
        if not ops_a and not ops_b and "op_pool" in view_cfg:
            pool_cfg = view_cfg.pop("op_pool")
            if not isinstance(pool_cfg, list):
                raise AugmentBuilderError("'op_pool' must be a list of operator configs")
            op_pool = [_build_op_from_cfg(c) for c in pool_cfg]
            return build_view(view_name, op_pool=op_pool, **view_cfg)

        return build_view(view_name, ops_a=ops_a, ops_b=ops_b, **view_cfg)

    # ── (C) 오류 처리 ---------------------------------------------------------
    raise AugmentBuilderError("Config must contain either 'type' or 'view' key.")
