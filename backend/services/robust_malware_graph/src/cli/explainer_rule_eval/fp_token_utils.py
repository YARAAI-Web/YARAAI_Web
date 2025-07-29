from __future__ import annotations

import json
import os
import sys
import pickle
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import numpy as np

from filelock import FileLock

from src.common.utils import get_logger

LOGGER = get_logger(__name__)

__all__ = [
    "TokenCache",
    "_load_fp_exclude",
    "_save_fp_exclude",
    "estimate_token_cache_size",
    "_load_token_index",
    "_cache_version_info",
    "_load_clean_cache",
    "_save_clean_cache",
    "tokens_to_bitvec",
    "_FP_EXCLUDE_COUNTS",
    "_FP_EXCLUDE_SET",
]


_GLOBAL_TOKEN_INDEX: dict[str, int] = {}
_GLOBAL_INDEX_TOKENS: list[str] = []


def tokens_to_bitvec(
    tokens: Iterable[str],
    idx_map: dict[str, int] | None = None,
    rev: list[str] | None = None,
) -> np.ndarray:
    """Return a numpy bit vector for ``tokens`` using ``idx_map``."""
    if idx_map is None:
        idx_map = _GLOBAL_TOKEN_INDEX
    if rev is None:
        rev = _GLOBAL_INDEX_TOKENS
    arr = np.zeros(len(rev), dtype=bool)
    for tok in tokens:
        tok_l = str(tok).lower()
        idx = idx_map.get(tok_l)
        if idx is None:
            idx = len(rev)
            idx_map[tok_l] = idx
            rev.append(tok_l)
            arr = np.pad(arr, (0, 1))
        arr[idx] = True
    return arr


@dataclass
class TokenCache:
    """Store clean sample tokens and token index."""

    tokens: dict[Path, np.ndarray] = field(default_factory=dict)
    index: dict[str, set[Path]] = field(default_factory=lambda: defaultdict(set))
    token_index: dict[str, int] = field(default_factory=lambda: _GLOBAL_TOKEN_INDEX)
    index_tokens: list[str] = field(default_factory=lambda: _GLOBAL_INDEX_TOKENS)

    def _grow_vectors(self) -> None:
        size = len(self.index_tokens)
        for p, vec in list(self.tokens.items()):
            if vec.size < size:
                self.tokens[p] = np.pad(vec, (0, size - vec.size))

    def add(self, path: Path, tokens: set[str]) -> None:
        """Add ``tokens`` for ``path`` updating the index."""
        prev = len(self.index_tokens)
        vec = tokens_to_bitvec(tokens, self.token_index, self.index_tokens)
        if len(self.index_tokens) > prev:
            self._grow_vectors()
        self.tokens[path] = vec
        for t in tokens:
            self.index.setdefault(t, set()).add(path)


# Persistent false positive exclude tokens
_FP_EXCLUDE_COUNTS: Counter[str] = Counter()
_FP_EXCLUDE_SET: set[str] = set()
_FP_EXCLUDE_PATH: Path | None = None


def _load_fp_exclude(path: Path) -> Counter[str]:
    """Load persistent FP exclude tokens from ``path``."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return Counter({str(k).lower(): int(v) for k, v in data.items()})
        if isinstance(data, list):
            return Counter({str(t).lower(): 1 for t in data})
    except FileNotFoundError:
        return Counter()
    except Exception as exc:  # noqa: BLE001
        LOGGER.warning("Failed to read %s: %s", path, exc)
    return Counter()


def _save_fp_exclude(path: Path, tokens: Mapping[str, int]) -> None:
    """Persist FP exclude ``tokens`` and counts to ``path``."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        lock_path = path.with_suffix(path.suffix + ".lock")
        with FileLock(str(lock_path)):
            merged = _load_fp_exclude(path)
            for k, v in tokens.items():
                merged[k.lower()] += int(v)
            data = {k: int(v) for k, v in sorted(merged.items(), key=lambda x: (-x[1], x[0]))}
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        LOGGER.warning("Failed to write %s: %s", path, exc)


def estimate_token_cache_size(cache: Mapping[Path, np.ndarray] | TokenCache) -> int:
    """Roughly estimate total memory usage of a token cache."""
    if isinstance(cache, TokenCache):
        values = cache.tokens.values()
    else:
        values = cache.values()
    total = 0
    for token_set in values:
        if isinstance(token_set, np.ndarray):
            total += int(token_set.nbytes)
        else:
            total += sys.getsizeof(token_set)
            for tok in token_set:
                total += sys.getsizeof(tok)
    return total


_CACHE_VERSION = 2


def _load_token_index(path: str | Path) -> dict[str, set[Path]]:
    """Load token index from JSON file."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {k: {Path(p) for p in v} for k, v in data.items()}


def _cache_version_info(paths: Sequence[Path]) -> dict[str, float]:
    return {
        str(p.with_suffix(".json")): os.path.getmtime(p.with_suffix(".json")) if p.with_suffix(".json").is_file() else -1
        for p in paths
    }


def _load_clean_cache(path: Path) -> tuple[TokenCache, dict[str, float]] | None:
    try:
        with path.open("rb") as f:
            data = pickle.load(f)
        if data.get("cache_version") != _CACHE_VERSION:
            return None
        idx_map = {str(k): int(v) for k, v in data.get("token_bit_index", {}).items()}
        rev = [None] * len(idx_map)
        for k, i in idx_map.items():
            if i < len(rev):
                rev[i] = k
        clean_cache = {
            Path(p): np.array(t, dtype=bool)
            for p, t in data.get("clean_token_cache", {}).items()
        }
        index = {k: {Path(p) for p in v} for k, v in data.get("token_index", {}).items()}
        version = data.get("version_info", {})
        tc = TokenCache(clean_cache, defaultdict(set, index), idx_map, rev)
        return tc, version
    except Exception:
        return None


def _save_clean_cache(path: Path, cache: TokenCache, version: Mapping[str, float]) -> None:
    try:
        with path.open("wb") as f:
            pickle.dump(
                {
                    "cache_version": _CACHE_VERSION,
                    "clean_token_cache": {str(p): vec.astype(int).tolist() for p, vec in cache.tokens.items()},
                    "token_index": {k: [str(p) for p in v] for k, v in cache.index.items()},
                    "token_bit_index": cache.token_index,
                    "version_info": dict(version),
                },
                f,
            )
    except Exception as exc:  # noqa: BLE001
        LOGGER.warning("Failed to save clean cache %s: %s", path, exc)
