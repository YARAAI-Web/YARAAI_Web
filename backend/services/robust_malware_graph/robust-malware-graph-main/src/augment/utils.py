"""
src.augment.utils (PyG 버전)
===========================

* set_global_seed   – Python · NumPy · Torch · **PyG** RNG 동기화
* flatten_dict      – 중첩 dict → 'a.b.c': value 평탄화
* load_yaml         – 안전한 YAML 로더
* resolve_path      – 상대/사용자 경로를 절대 Path 로 변환
"""

from __future__ import annotations

import os
import random
import sys
from pathlib import Path
from typing import Any, Dict
import warnings

import numpy as np
import yaml

# ──────────────────────────────────────────────────────────────
# 0. 라이브러리 존재 여부 체크
# ──────────────────────────────────────────────────────────────
try:
    import torch

    _HAS_TORCH = True
except ImportError:  # pragma: no cover
    _HAS_TORCH = False

try:
    from torch_geometric.seed import seed_everything as pyg_seed  # PyG ≥2.3
except ImportError:  # pragma: no cover
    pyg_seed = None  # PyG 미설치 or 구버전


# ──────────────────────────────────────────────────────────────
# 1. 시드 고정
# ──────────────────────────────────────────────────────────────
def set_global_seed(seed: int | None = None) -> int:
    """
    모든 RNG 시드를 **하나의 값**으로 통일합니다.

    Parameters
    ----------
    seed : int | None
        고정할 시드 값. None 이면 난수로 생성하여 사용합니다.

    Returns
    -------
    int
        실제로 설정된 시드 값
    """
    if seed is None:
        seed = random.SystemRandom().randint(0, 2**32 - 1)

    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    if _HAS_TORCH:
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        # CuDNN 결정론적 동작
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

    # PyG 전용 시드 (가능한 경우)
    if pyg_seed is not None:
        pyg_seed(seed)

    return seed


# ──────────────────────────────────────────────────────────────
# 2. 딕셔너리 유틸
# ──────────────────────────────────────────────────────────────
def flatten_dict(
    d: Dict[str, Any],
    parent_key: str = "",
    sep: str = ".",
) -> Dict[str, Any]:
    """
    중첩 dict → 단일 레벨 dict ('a.b': value).

    Examples
    --------
    >>> flatten_dict({"a": {"b": 1, "c": 2}})
    {'a.b': 1, 'a.c': 2}
    """
    items: Dict[str, Any] = {}
    for k, v in d.items():
        key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, key, sep=sep))
        else:
            items[key] = v
    return items


# ──────────────────────────────────────────────────────────────
# 3. 안전한 파일·YAML 로딩
# ──────────────────────────────────────────────────────────────
def resolve_path(path: str | os.PathLike) -> Path:
    """'~/foo/bar' → 절대경로(Path)."""
    return Path(path).expanduser().resolve()


def load_yaml(path: str | os.PathLike) -> Any:
    """YAML 파일을 Python 객체로 읽어옵니다 (SafeLoader)."""
    with resolve_path(path).open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ──────────────────────────────────────────────────────────────
# 4. import 경로 헬퍼
# ──────────────────────────────────────────────────────────────
def add_project_root_to_sys_path(levels_up: int = 1) -> None:
    """
    현재 파일 기준 `levels_up` 단계 위 디렉터리를 `sys.path` 에 추가합니다.
    외부 위치에서 스크립트를 실행할 때 상대 import 오류를 방지합니다.
    """
    root = Path(__file__).resolve().parents[levels_up]
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))


# ---------------------------------------------------------------------------
# 5. Mask helper
# ---------------------------------------------------------------------------
def ensure_target_node(mask: "torch.Tensor", target_idx: int | None) -> "torch.Tensor":
    """Ensure ``mask[target_idx]`` is ``True`` if index is valid.

    Parameters
    ----------
    mask : torch.Tensor
        Boolean node keep mask of shape ``[num_nodes]``.
    target_idx : int | None
        Local index of the node to *preserve* (``None`` ⇒ no-op). For
        ``HeteroData`` this is the index within the target node type.

    Returns
    -------
    torch.Tensor
        ``mask`` with ``target_idx`` forced to ``True`` when possible.
    """
    if target_idx is None:
        return mask
    if mask.dtype is not torch.bool:
        raise TypeError("mask must be a boolean tensor")
    if not (0 <= target_idx < mask.size(0)):
        warnings.warn(
            f"target_idx {target_idx} out of range for mask of size {mask.size(0)}",
            RuntimeWarning,
        )
        return mask
    mask[target_idx] = True
    return mask


# ──────────────────────────────────────────────────────────────
# 5. public export
# ──────────────────────────────────────────────────────────────
__all__ = [
    "set_global_seed",
    "flatten_dict",
    "load_yaml",
    "resolve_path",
    "add_project_root_to_sys_path",
    "ensure_target_node",
]
