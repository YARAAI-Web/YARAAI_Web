"""src.continual.datastream.utils
=================================
Reusable helper utilities for *stream‑style* continual‑learning dataloaders.
All functions in this module are **framework‑agnostic** – they do not depend
on any learner/replay implementation so that they can be imported freely by
samplers, learners, or evaluation loops.

Key features
------------
* ``set_random_seed`` : Wrapper around :pyfunc:`common.utils.set_random_seed`.
* ``bucket_by``       : Group arbitrary items by a user‑provided key function.
* ``round_robin``     : Fair, class‑balanced merging of multiple iterators.
* ``batcher``         : Lightweight graph‑aware mini‑batch iterator.
* ``dgl_to_pyg``      : Best‑effort conversion from a **DGLGraph** to a
                        :pyclass:`torch_geometric.data.Data` object so that
                        online pipelines can seamlessly move between the two
                        popular graph libraries.

Notes
-----
* While the wider project still uses DGL internally for heterogeneous
  processing, **torch_geometric** is required by downstream augmentation and
  continual‑learning experiments.  The ``dgl_to_pyg`` helper therefore acts as
  an *escape hatch* without pulling in a hard dependency on either library at
  import‑time – conversion is attempted only when the corresponding packages
  are available.
* All public helpers are listed in ``__all__`` so that ``from ... import *``
  remains tidy.
"""
from __future__ import annotations

import itertools
import random
from collections import defaultdict
from typing import Any, Callable, Dict, Generator, Iterable, Iterator, List, Sequence, Tuple, TypeVar

import numpy as np
import torch

# Optional dependencies -------------------------------------------------------
try:
    import dgl  # type: ignore
except ImportError:  # pragma: no cover – runtime optional
    dgl = None  # noqa: N816 – keep lower‑case alias for sanity

try:
    from torch_geometric.data import Batch as PygBatch  # type: ignore
    from torch_geometric.data import Data as PygData  # type: ignore
except ImportError:  # pragma: no cover – runtime optional
    PygBatch = None  # type: ignore  # noqa: N816
    PygData = None  # type: ignore  # noqa: N816

# --------------------------------------------------------------------------- #
# Public API
# --------------------------------------------------------------------------- #
__all__ = [
    "set_random_seed",
    "bucket_by",
    "round_robin",
    "batcher",
    "dgl_to_pyg",
]

T = TypeVar("T")
K = TypeVar("K")

# --------------------------------------------------------------------------- #
# 1. Reproducibility helper
# --------------------------------------------------------------------------- #

def set_random_seed(seed: int = 42, *, deterministic: bool = False) -> None:
    """Seed Python, NumPy and PyTorch RNGs in a single call.

    Parameters
    ----------
    seed : int, default=42
        Master seed to use across libraries.
    deterministic : bool, default=False
        If *True*, additionally configure CuDNN/CUDA for fully deterministic
        execution.  This can have a performance impact.
    """
    import importlib

    # Defer to the common project‑wide utility if it exists; fallback otherwise.
    try:
        common_utils = importlib.import_module("src.common.utils")
        if hasattr(common_utils, "set_random_seed"):
            common_utils.set_random_seed(seed, deterministic=deterministic)  # type: ignore[attr-defined]
            return
    except ModuleNotFoundError:
        pass  # continue with local implementation

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    if deterministic:
        torch.backends.cudnn.deterministic = True  # type: ignore[attr-defined]
        torch.backends.cudnn.benchmark = False  # type: ignore[attr-defined]

# --------------------------------------------------------------------------- #
# 2. Data bucketing & fair interleaving
# --------------------------------------------------------------------------- #

def bucket_by(iterable: Iterable[T], key_fn: Callable[[T], K]) -> Dict[K, List[T]]:
    """Group *iterable* items into buckets w.r.t. ``key_fn``.

    Examples
    --------
    >>> bucket_by(["cat", "dog", "car"], str.isalpha)
    {True: ["cat", "dog"], False: ["car"]}
    """
    buckets: Dict[K, List[T]] = defaultdict(list)
    for item in iterable:
        buckets[key_fn(item)].append(item)
    return buckets


def round_robin(iterators: Sequence[Iterator[T]]) -> Iterator[T]:
    """Yield items from *iterators* in a class‑balanced round‑robin fashion.

    Exhausted iterators are skipped on‑the‑fly so that the generator terminates
    when all input iterators are consumed.
    """
    iters = list(iterators)
    while iters:
        next_iters = []
        for it in iters:
            try:
                yield next(it)
                next_iters.append(it)
            except StopIteration:
                # iterator exhausted – just drop it
                continue
        iters = next_iters

# --------------------------------------------------------------------------- #
# 3. Mini‑batch creation for graph data
# --------------------------------------------------------------------------- #

def _default_collate(items: Sequence[T]) -> Any:  # pragma: no cover
    """Fallback collate: convert list of torch.Tensors → torch.stack() or return as‑is."""
    if isinstance(items[0], torch.Tensor):
        return torch.stack(items, dim=0)
    return items  # type: ignore[return-value]


def batcher(stream: Iterator[T], *, batch_size: int, collate_fn: Callable[[Sequence[T]], Any] | None = None,
            drop_last: bool = False) -> Iterator[Any]:
    """Yield batched items from a *stream* iterator.

    Parameters
    ----------
    stream : Iterator[T]
        Input infinite/finite item iterator (e.g. ``GraphStream``).
    batch_size : int
        Number of elements per mini‑batch.
    collate_fn : Callable, optional
        Function that converts a *list* of size *batch_size* into a training
        batch (e.g. :pymeth:`torch_geometric.data.Batch.from_data_list`).  When
        *None*, a minimal default is used that simply stacks *torch.Tensor*
        inputs or returns the list unchanged.
    drop_last : bool, default=False
        If *True*, discard the last incomplete batch.
    """
    collate = collate_fn or _default_collate
    bucket: List[T] = []

    for item in stream:
        bucket.append(item)
        if len(bucket) == batch_size:
            yield collate(bucket)
            bucket = []
    if bucket and not drop_last:
        yield collate(bucket)

# --------------------------------------------------------------------------- #
# 4. DGL → PyG best‑effort conversion
# --------------------------------------------------------------------------- #

def dgl_to_pyg(g: "dgl.DGLGraph") -> "PygData":  # type: ignore[valid-type]
    """Convert a **homogeneous** *DGLGraph* to a PyG :class:`Data` object.

    This is primarily intended for *online* scenarios where quick inspection or
    lightweight augmentation is useful.  For *heterogeneous* graphs, users
    should rely on the dedicated builder module ``src.graphs.builders`` instead.

    The function requires both *DGL* and *torch_geometric* to be installed.  If
    either package is missing, a ``RuntimeError`` is raised.
    """
    if dgl is None or PygData is None:
        raise RuntimeError("dgl_to_pyg() requires DGL *and* PyG – install them via pip or conda.")

    if g.is_homogeneous is False:  # type: ignore[attr-defined]
        raise ValueError("dgl_to_pyg currently supports homogeneous graphs only. Use the heterogeneous builder instead.")

    # Extract edge index (2×E) in COO format
    src, dst = g.edges(order="eid")  # type: ignore[attr-defined]
    edge_index = torch.vstack((src, dst))

    data_kwargs: Dict[str, Any] = {
        "edge_index": edge_index,
    }

    # Copy node features ------------------------------------------------------
    for key, value in g.ndata.items():  # type: ignore[attr-defined]
        if torch.is_tensor(value):
            data_kwargs[key] = value

    # Copy edge features ------------------------------------------------------
    for key, value in g.edata.items():  # type: ignore[attr-defined]
        if torch.is_tensor(value):
            data_kwargs[f"edge_{key}"] = value

    return PygData(**data_kwargs)  # type: ignore[valid-type]
