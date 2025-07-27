"""
src.graphs.features.cache
=========================

📦 FeatureCache
---------------
┌─ disk  : Feather / Parquet 파일(압축 가능, columnar I/O → 빠른 슬라이스)
└─ memory: functools.lru_cache 로 최대 N개 핫 캐시

지원 함수
---------
• save_tensor(name, tensor, dir, *, fmt='feather', overwrite=False)
• load_tensor(name, dir, *, fmt='feather', mmap=True) -> torch.Tensor
• clear_memory_cache()
• FeatureCache  (Class) – 위 함수를 래핑한 상태ful 매니저

전제
----
1) `name` 은 그래프 SHA-256 또는 임의 식별자(str)
2) Tensor dtype 은 float32 / float16 / int64 / bool 등 Arrow 호환 타입
3) Torch Tensor ↔ NumPy ↔ Arrow zero-copy 를 최대한 활용 (mmap=True 권장)
"""

from __future__ import annotations

import functools
import os
from pathlib import Path
from typing import Literal, Optional

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import pyarrow.parquet as pq
import torch

from ..utils import ensure_dir, get_logger

# ────────────────────────────────────────────────────────────────────────────
# 공용 설정
# ────────────────────────────────────────────────────────────────────────────
_DEFAULT_FMT = Literal["feather", "parquet"]
_LOG = get_logger("features.cache")


# ────────────────────────────────────────────────────────────────────────────
# 디스크 I/O 헬퍼
# ────────────────────────────────────────────────────────────────────────────
def _tensor_to_table(t: torch.Tensor) -> pa.Table:
    """Torch Tensor → Arrow Table (zero-copy NumPy view)."""
    arr = t.detach().cpu().contiguous().numpy()
    return pa.Table.from_pandas(pd.DataFrame(arr), preserve_index=False)


def _table_to_tensor(tbl: pa.Table, dtype: torch.dtype) -> torch.Tensor:
    """Arrow Table → Torch Tensor (zero-copy NumPy view)."""
    arr = tbl.to_pandas(split_blocks=True, self_destruct=True).to_numpy()
    return torch.as_tensor(arr, dtype=dtype)


def _path(dir_: Path, name: str, fmt: _DEFAULT_FMT) -> Path:
    ext = "ftr" if fmt == "feather" else "parquet"
    return dir_ / f"{name}.{ext}"


# ────────────────────────────────────────────────────────────────────────────
# public functions
# ────────────────────────────────────────────────────────────────────────────
def save_tensor(
    name: str,
    tensor: torch.Tensor,
    cache_dir: Path,
    *,
    fmt: _DEFAULT_FMT = "feather",
    overwrite: bool = False,
    compression: Optional[str] = "zstd",
) -> Path:
    """
    Tensor → Feather/Parquet 파일 저장.

    Parameters
    ----------
    name : str
        그래프 식별자(sha256 등). 확장자는 자동 부여.
    tensor : torch.Tensor
    cache_dir : Path
    fmt : {'feather','parquet'}
    overwrite : bool
    compression : str | None
    """
    ensure_dir(cache_dir)
    p = _path(cache_dir, name, fmt)
    if p.exists() and not overwrite:
        _LOG.debug("skip save '%s' (exists)", p.name)
        return p

    tbl = _tensor_to_table(tensor)
    if fmt == "feather":
        feather.write_feather(tbl, p, compression=compression)
    else:  # parquet
        pq.write_table(tbl, p, compression=compression)

    _LOG.debug("saved feat %s (%.2f MB)", p.name, p.stat().st_size / 2**20)
    return p


@functools.lru_cache(maxsize=16)
def _load_table_cached(path: str, fmt: _DEFAULT_FMT, mmap: bool) -> pa.Table:
    p = Path(path)
    if fmt == "feather":
        return feather.read_table(p, memory_map=mmap)
    return pq.read_table(p, memory_map=mmap)


def load_tensor(
    name: str,
    cache_dir: Path,
    *,
    fmt: _DEFAULT_FMT = "feather",
    mmap: bool = True,
    dtype: Optional[torch.dtype] = None,
) -> torch.Tensor:
    """
    Feather/Parquet → Torch Tensor (LRU 메모리 캐시 포함).

    Parameters
    ----------
    name : str
    cache_dir : Path
    fmt : {'feather','parquet'}
    mmap : bool, default True
        Arrow memory-map 읽기(useful for large files).
    dtype : torch.dtype | None
        None ⇒ 파일 dtype 유지.
    """
    p = _path(cache_dir, name, fmt)
    if not p.is_file():
        raise FileNotFoundError(p)

    tbl = _load_table_cached(str(p), fmt, mmap)
    t = _table_to_tensor(tbl, dtype or torch.float32)
    _LOG.debug("loaded feat %s (%s)", p.name, t.shape)
    return t


def clear_memory_cache() -> None:
    """LRU 메모리 캐시 비우기."""
    _load_table_cached.cache_clear()
    _LOG.debug("feature memory cache cleared")


# ────────────────────────────────────────────────────────────────────────────
# 상태ful 매니저 클래스 (optional)
# ────────────────────────────────────────────────────────────────────────────
class FeatureCache:
    """
    디렉터리 단위 캐시 매니저.

    Examples
    --------
    >>> cache = FeatureCache(Path('~/.cache/feats').expanduser())
    >>> cache.save("abc123", feats)
    >>> feats = cache.load("abc123")
    """

    def __init__(
        self,
        root: Path,
        *,
        fmt: _DEFAULT_FMT = "feather",
        compression: str | None = "zstd",
        max_mem_items: int = 128,
    ) -> None:
        self.root = Path(root).expanduser()
        self.fmt = fmt
        self.compression = compression
        self._memo: dict[str, torch.Tensor] = {}
        self._max_items = max_mem_items
        ensure_dir(self.root)

    # -------------------------------------------------------------- #
    def save(
        self,
        key: str,
        tensor: torch.Tensor,
        *,
        overwrite: bool = False,
    ) -> Path:
        p = save_tensor(
            key,
            tensor,
            self.root,
            fmt=self.fmt,
            overwrite=overwrite,
            compression=self.compression,
        )
        self._memoize(key, tensor)
        return p

    def load(
        self,
        key: str,
        *,
        mmap: bool = True,
        dtype: Optional[torch.dtype] = None,
    ) -> torch.Tensor:
        # 1) 메모리 캐시 우선
        if key in self._memo:
            return self._memo[key]

        # 2) 디스크
        t = load_tensor(
            key,
            self.root,
            fmt=self.fmt,
            mmap=mmap,
            dtype=dtype,
        )
        self._memoize(key, t)
        return t

    # -------------------------------------------------------------- #
    def _memoize(self, key: str, t: torch.Tensor) -> None:
        if self._max_items <= 0:
            return
        if len(self._memo) >= self._max_items:
            # FIFO pop
            popped = next(iter(self._memo))
            self._memo.pop(popped, None)
        self._memo[key] = t

    def clear(self) -> None:
        """메모리 캐시 비우기."""
        self._memo.clear()
