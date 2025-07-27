"""
robust-malware-graph – Common Utilities
=======================================
This module centralises *light‑weight* helper functions that are shared across
multiple sub‑packages (``src.augment``, ``src.graphs``, ``src.models`` …).  The
focus is on **reproducibility**, **ergonomics** and **zero heavy dependencies** –
*only* the Python standard‑library plus *NumPy / PyTorch / tqdm* are required.
New helpers should be (1) widely re‑usable and (2) completely side‑effect free
unless the function name explicitly signals otherwise (e.g. ``ensure_dir``).

Key Features
------------
* ``set_random_seed`` – consistent RNG seeding for *random*, *NumPy*, *torch*.
* ``get_logger``      – colourised singleton logger with lazy instantiation.
* ``ensure_dir``      – mkdir -p wrapper that returns the *Path* object.
* ``timer``           – context‑manager for quick wall‑time measurements.
* ``tqdm_wrap``       – safe import wrapper: returns *tqdm* if available else
                       the original iterable (graceful degradation).
* ``human_bytes``     – convert raw byte counts to **GiB, MiB, KiB** strings.
* ``MemoryUsageFilter`` – add RAM/VRAM info to logger output.
* ``flatten_dict``    – flatten nested mapping into ``"a.b.c"`` dotted keys.
* ``get_device``      – auto‑detect *CUDA/MPS* → *torch.device* helper.
* ``to_numpy`` / ``to_tensor`` – zero‑copy conversions where possible.

These utilities are referenced throughout the code‑base – for example in
``src/augment/utils.py`` (seed fixing) fileciteturn0file0 and
``src/graphs/utils.py`` (logging / tqdm helpers) fileciteturn0file1.
"""
from __future__ import annotations

import contextlib
import hashlib
import logging
import os
import random
import sys
import time

import psutil
from pathlib import Path
from types import TracebackType
from typing import Any, Dict, Generator, Iterable, Iterator, Mapping, MutableMapping, Optional, Tuple, Type, TypeVar, Union

import numpy as np

try:
    import torch
except ImportError as _e:  # pragma: no cover – torch is optional in some envs
    torch = None  # type: ignore

# ---------------------------------------------------------------------------
# Logger helpers
# ---------------------------------------------------------------------------

_LOGGERS: dict[str, logging.Logger] = {}


class MemoryUsageFilter(logging.Filter):
    """Attach RAM and VRAM usage information to log records."""

    def filter(self, record: logging.LogRecord) -> bool:  # noqa: D401
        try:
            process = psutil.Process(os.getpid())
            record.ram = human_bytes(process.memory_info().rss)
        except Exception:
            record.ram = "n/a"

        if torch is not None and torch.cuda.is_available():
            try:
                record.vram = human_bytes(int(torch.cuda.memory_allocated()))
            except Exception:
                record.vram = "n/a"
        else:
            record.vram = "n/a"
        if "RAM" not in record.getMessage():
            record.msg = (
                f"RAM {record.ram} | VRAM {record.vram} | {record.getMessage()}"
            )
            record.args = None
        return True


def _build_colour_formatter() -> logging.Formatter:
    """Return a minimal colourised *logging.Formatter* (uses ANSI codes)."""
    level_to_colour = {
        logging.DEBUG: "\033[37m",  # white
        logging.INFO: "\033[36m",  # cyan
        logging.WARNING: "\033[33m",  # yellow
        logging.ERROR: "\033[31m",  # red
        logging.CRITICAL: "\033[41m",  # bg‑red
    }

    class _AnsiFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:  # noqa: D401
            colour = level_to_colour.get(record.levelno, "\033[0m")
            reset = "\033[0m"
            prefix = f"{colour}{record.levelname:<8}{reset}"
            msg = super().format(record).replace("-", "-").replace("–", "-")  # CP949 우회
            return f"{prefix} {msg}"

    return _AnsiFormatter(
        "%(asctime)s | %(name)s | RAM %(ram)s | VRAM %(vram)s | %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )


def get_logger(name: str = "robust‑mg", level: int = logging.INFO) -> logging.Logger:  # noqa: D401
    """Return a *singleton* logger with a colour console handler attached."""
    if name in _LOGGERS:
        return _LOGGERS[name]

    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.addFilter(MemoryUsageFilter())
    handler.setFormatter(_build_colour_formatter())
    logger.addHandler(handler)

    _LOGGERS[name] = logger
    return logger


# ---------------------------------------------------------------------------
# Reproducibility helpers
# ---------------------------------------------------------------------------

def set_random_seed(seed: int = 42, *, deterministic: bool = False) -> None:
    """Seed *random*, *NumPy* and *torch* (if available)."""
    random.seed(seed)
    np.random.seed(seed)
    if torch is not None:
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        if deterministic:
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False


# ---------------------------------------------------------------------------
# Filesystem helpers
# ---------------------------------------------------------------------------

def ensure_dir(path: Union[str, Path], *, exist_ok: bool = True) -> Path:
    """Recursively create *path* if it does not exist and return *Path*."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=exist_ok)
    return p


# ---------------------------------------------------------------------------
# Progress‑bar helpers
# ---------------------------------------------------------------------------

T = TypeVar("T")

def tqdm_wrap(iterable: Iterable[T], **kwargs) -> Iterable[T]:  # noqa: D401
    """Wrap *iterable* with *tqdm* if installed; otherwise return unchanged."""
    try:
        from tqdm import tqdm  # local import to avoid hard dependency

        return tqdm(iterable, **kwargs)
    except (ImportError, RuntimeError):
        return iterable


# ---------------------------------------------------------------------------
# Timer context manager
# ---------------------------------------------------------------------------

class timer:  # noqa: D401 – mimic *contextlib.ContextDecorator*
    """Usage: ``with timer("load"): ...`` prints *load: 0.123 s*."""

    def __init__(self, label: str = "", *, logger: Optional[logging.Logger] = None) -> None:
        self.label = label
        self.logger = logger or get_logger()
        self.start: float = 0.0

    def __enter__(self):  # type: ignore[override]
        self.start = time.perf_counter()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> bool:  # noqa: D401
        elapsed = time.perf_counter() - self.start
        self.logger.info(f"{self.label} took {elapsed:.3f} s")
        # propagate exception (if any)
        return False


# ---------------------------------------------------------------------------
# Byte / memory helpers
# ---------------------------------------------------------------------------

def human_bytes(num: int, suffix: str = "B") -> str:  # noqa: D401
    """Convert *num* bytes to readable *KiB/MiB/GiB* representation."""
    for unit in ("", "Ki", "Mi", "Gi", "Ti"):
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Pi{suffix}"


# ---------------------------------------------------------------------------
# Device helpers
# ---------------------------------------------------------------------------

def get_device(prefer: str = "cuda") -> "torch.device":  # type: ignore[name‑defined]
    """Return first available device (CUDA › MPS › CPU)."""
    if torch is None:
        raise RuntimeError("torch is required for get_device()")

    if prefer == "cuda" and torch.cuda.is_available():
        return torch.device("cuda")
    if prefer in {"cuda", "mps"} and hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


# ---------------------------------------------------------------------------
# Numpy / Tensor helpers
# ---------------------------------------------------------------------------

def to_numpy(x: Union["np.ndarray", "torch.Tensor"]) -> np.ndarray:  # type: ignore[name‑defined]
    """Convert *x* to *np.ndarray* (zero‑copy if *torch.Tensor* on CPU)."""
    if torch is not None and isinstance(x, torch.Tensor):
        return x.detach().cpu().numpy()
    if isinstance(x, np.ndarray):
        return x
    raise TypeError(f"Unsupported type: {type(x)}")


def to_tensor(x: Union[np.ndarray, "torch.Tensor"], *, device: Optional["torch.device"] = None, dtype=None):  # type: ignore[name‑defined]
    """Convert *x* to *torch.Tensor* (no copy if already tensor on same device)."""
    if torch is None:
        raise RuntimeError("torch is required for to_tensor()")

    if isinstance(x, torch.Tensor):
        return x.to(device=device, dtype=dtype) if (device or dtype) else x
    if isinstance(x, np.ndarray):
        return torch.as_tensor(x, device=device, dtype=dtype)
    raise TypeError(f"Unsupported type: {type(x)}")


# ---------------------------------------------------------------------------
# Dict helpers
# ---------------------------------------------------------------------------

K = TypeVar("K")
V = TypeVar("V")

def flatten_dict(d: Mapping[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:  # noqa: D401
    """Flatten nested mapping using *dot*‑separated keys.

    >>> flatten_dict({'a': {'b': 1, 'c': 2}})
    {'a.b': 1, 'a.c': 2}
    """
    items: list[Tuple[str, Any]] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, Mapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


# ---------------------------------------------------------------------------
# State dict helpers
# ---------------------------------------------------------------------------

def filter_state_dict(
    model: "torch.nn.Module",
    state: Mapping[str, "torch.Tensor"],
    *,
    logger: Optional[logging.Logger] = None,
) -> Dict[str, "torch.Tensor"]:
    """Return subset of ``state`` compatible with ``model``.

    Parameters
    ----------
    model:
        Target model whose ``state_dict`` provides reference shapes.
    state:
        Checkpoint state dictionary to be filtered.
    logger:
        Optional logger to emit warnings for ignored keys.
    """

    if torch is None:
        raise RuntimeError("filter_state_dict requires PyTorch")

    logger = logger or get_logger(__name__)
    model_state = model.state_dict()
    filtered: Dict[str, torch.Tensor] = {}

    for k, v in state.items():
        target = model_state.get(k)
        if target is None:
            logger.debug("Ignoring checkpoint parameter '%s' not found in model", k)
            continue

        if target.shape != v.shape:
            # special case for RGCNConv relation dimension mismatch
            if (
                k.startswith("convs")
                and k.endswith(".weight")
                and v.dim() == 3
                and target.dim() == 3
                and v.shape[1:] == target.shape[1:]
            ):
                old_rel = v.size(0)
                new_rel = target.size(0)
                copy_rel = min(old_rel, new_rel)
                if copy_rel == 0:
                    logger.warning(
                        "Ignoring checkpoint parameter '%s' with zero relations to copy",
                        k,
                    )
                    continue
                new_weight = target.clone()
                new_weight[:copy_rel] = v[:copy_rel]
                filtered[k] = new_weight
                logger.info("copied %d/%d relations from checkpoint", copy_rel, old_rel)
                continue

            if (
                k.startswith("convs")
                and k.endswith(".comp")
                and v.dim() == 2
                and target.dim() == 2
            ):
                if v.shape[0] == v.shape[1] and target.shape[0] == target.shape[1]:
                    old_rel = v.size(0)
                    new_rel = target.size(0)
                    copy_rel = min(old_rel, new_rel)
                    if copy_rel == 0:
                        logger.warning(
                            "Ignoring checkpoint parameter '%s' with zero relations to copy",
                            k,
                        )
                        continue
                    new_comp = target.clone()
                    new_comp[:copy_rel, :copy_rel] = v[:copy_rel, :copy_rel]
                    filtered[k] = new_comp
                    logger.info(
                        "copied %d/%d relations from checkpoint", copy_rel, old_rel
                    )
                    continue

                old_bases = v.size(0)
                new_bases = target.size(0)
                old_rel = v.size(1)
                new_rel = target.size(1)
                copy_bases = min(old_bases, new_bases)
                copy_rel = min(old_rel, new_rel)
                if copy_bases == 0 or copy_rel == 0:
                    logger.warning(
                        "Ignoring checkpoint parameter '%s' with zero bases/relations to copy",
                        k,
                    )
                    continue
                new_comp = target.clone()
                new_comp[:copy_bases, :copy_rel] = v[:copy_bases, :copy_rel]
                filtered[k] = new_comp
                logger.info(
                    "copied %d/%d bases and %d/%d relations from checkpoint",
                    copy_bases,
                    old_bases,
                    copy_rel,
                    old_rel,
                )
                continue

            logger.warning(
                "Ignoring checkpoint parameter '%s' with shape %s (expected %s)",
                k,
                tuple(v.shape),
                tuple(target.shape),
            )
            continue

        filtered[k] = v

    return filtered


# ---------------------------------------------------------------------------
# Miscellaneous helpers
# ---------------------------------------------------------------------------

def sha256sum(file_path: Union[str, Path], chunk_size: int = 1 << 20) -> str:  # noqa: D401
    """Return SHA‑256 hex digest of the given *file_path*."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


__all__ = [
    "ensure_dir",
    "flatten_dict",
    "get_device",
    "get_logger",
    "human_bytes",
    "MemoryUsageFilter",
    "filter_state_dict",
    "set_random_seed",
    "sha256sum",
    "timer",
    "to_numpy",
    "to_tensor",
    "tqdm_wrap",
]
