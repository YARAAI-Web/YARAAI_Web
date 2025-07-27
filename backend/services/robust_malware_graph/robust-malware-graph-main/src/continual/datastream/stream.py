"""src.continual.datastream.stream
==================================
A *framework‑agnostic* iterable that turns an **arbitrary sequence** of
examples ( e.g. graphs, tensors, file‑paths …) into an infinite (or finite)
stream of mini‑batches – the basic *input primitive* for online / continual
learning loops in *robust‑malware‑graph*.

This module deliberately does **not** depend on PyTorch, DGL, or
Torch‑Geometric so that it can be shared by CPU‑only utilities (e.g. rule
generation agents) and GPU trainers alike.  The actual tensor / graph
assembly is delegated to a user‑supplied ``collate_fn``.

Typical usage::

    >>> from src.continual.datastream.stream import DataStream
    >>> from torch.utils.data import Dataset
    >>> ds = CustomGraphDataset(path)
    >>> stream = DataStream(ds, batch_size=64, shuffle=True)
    >>> for batch_idx, batch in enumerate(stream):
    ...     train_step(batch)
    ...     if batch_idx == 1_000:            # break after some steps
    ...         break


Design Goals
------------
* **Minimal** public API (``__iter__`` / ``__next__``).  No side effects.
* **Composable** – works with any object implementing ``__len__`` and
  ``__getitem__``.
* **Deterministic** shuffling via ``seed``; independent *NumPy* RNG so that
  global random state is not polluted.
* **Infinite** or finite iteration depending on the *``repeat``* flag.
* **Online‑append** – new samples can be appended mid‑epoch via
  :pyfunc:`add_samples` without interrupting iteration.
* **Lightweight** – zero threading, zero locks.  One Python file.


Limitations
-----------
* Single‑process iteration only; for multi‑worker prefetch use an external
  DataLoader (PyTorch) or multiprocessing.Queue wrapper.
* Does **not** call ``Dataset.__getitem__`` concurrently – each sample is
  fetched in the main thread.
* ``drop_last`` is applied *per epoch* (not per infinite loop).

"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterator, List, Sequence
import itertools
import numpy as np

__all__ = [
    "Batch",
    "DataStream",
]


@dataclass
class Batch:  # pragma: no cover – convenience container
    """Typed wrapper around a mini‑batch.

    Attributes
    ----------
    data : Any
        User‑defined structure produced by ``collate_fn`` – often a tuple
        ``(graphs, labels, meta)`` or a *torch_geometric.data.Batch*.
    idx  : List[int]
        Indices of the underlying samples.  Useful for replay buffers,
        debugging or mapping predictions back to original files.
    epoch : int
        0‑based epoch counter – increments each full pass through the
        (shuffled) dataset.
    step : int
        Global batch counter across *all* epochs.
    """

    data: Any
    idx: List[int]
    epoch: int
    step: int


class DataStream(Iterator[Batch]):
    """Streaming mini‑batch iterator with optional infinite looping.

    Parameters
    ----------
    dataset : Sequence[Any]
        *Either* an object implementing ``__len__``+``__getitem__`` *or* a
        simple list.  Samples can be of any type – they are passed verbatim
        to ``collate_fn``.
    batch_size : int, default ``32``
        Number of samples per :pyclass:`Batch`.
    shuffle : bool, default ``False``
        Whether to reshuffle indices **at the beginning of every epoch**.
    drop_last : bool, default ``False``
        If *True*, the last incomplete batch of each epoch is skipped.
    repeat : bool | int, default ``True``
        * ``True``  – **infinite** loop (repeat forever).
        * ``False`` – single finite pass.
        * ``int``   – repeat exactly *n* epochs then stop.
    collate_fn : Callable[[List[Any]], Any] | None, default ``None``
        Function that merges **a list of raw samples** into a single object
        suitable for the learner.  When ``None`` the list itself is
        returned unchanged.
    seed : int, default ``42``
        RNG seed used *only* for shuffling this stream – ensures reproducible
        ordering regardless of global NumPy / Python RNG.

    Notes
    -----
    *Iteration state* (epoch cursor, RNG) is **local** to this iterator –
    calling ``iter(stream)`` will *reset* the state.  This means one should
    not create multiple concurrent iterators from the same DataStream
    instance unless that is the desired behaviour.
    """

    def __init__(
        self,
        dataset: Sequence[Any],
        batch_size: int = 32,
        *,
        shuffle: bool = False,
        drop_last: bool = False,
        repeat: bool | int = True,
        collate_fn: Callable[[List[Any]], Any] | None = None,
        seed: int = 42,
    ) -> None:
        if batch_size <= 0:
            raise ValueError("batch_size must be positive")
        if not isinstance(dataset, Sequence):
            raise TypeError("dataset must implement __len__ & __getitem__")

        self.dataset: Sequence[Any] = dataset
        self.batch_size = int(batch_size)
        self.shuffle = bool(shuffle)
        self.drop_last = bool(drop_last)
        self.repeat = repeat  # could be bool or int (epochs)
        self._collate = collate_fn or (lambda batch: batch)

        # independent RNG – no interference with global numpy.random.
        self._rng = np.random.RandomState(seed)

        # stateful cursors
        self._epoch = 0
        self._step = 0
        self._epoch_counter = 0  # how many *completed* epochs so far

        # Cache total length for performance.
        self._n_samples = len(dataset)
        if self._n_samples == 0:
            raise ValueError("Empty dataset")

        self._epoch_indices: List[int] = list(range(self._n_samples))
        if self.shuffle:
            self._rng.shuffle(self._epoch_indices)
        self._pos_in_epoch = 0  # pointer within current shuffled indices

    # --------------------------------------------------------------------- #
    # Iterator interface
    # --------------------------------------------------------------------- #
    def __iter__(self) -> "DataStream":
        # Creating a *new* iterator resets the cursor but maintains RNG
        self._epoch = 0
        self._epoch_counter = 0
        self._step = 0
        self._reset_epoch(shuffle=self.shuffle)
        return self

    def __next__(self) -> Batch:
        if self._should_stop():
            raise StopIteration

        # Compute slice of indices for the next batch
        start, end = self._pos_in_epoch, self._pos_in_epoch + self.batch_size
        idx_slice = self._epoch_indices[start:end]

        # If not enough samples left for a full batch
        if len(idx_slice) < self.batch_size:
            if self.drop_last:
                # Move to next epoch and recompute indices
                self._advance_epoch()
                return self.__next__()
            else:
                # Return smaller final batch then advance epoch afterwards
                self._advance_epoch()
        else:
            # Advance position within epoch cursor
            self._pos_in_epoch += self.batch_size
            if self._pos_in_epoch >= self._n_samples:
                self._advance_epoch()

        # Fetch raw samples and collate
        raw_samples = [self.dataset[i] for i in idx_slice]
        batch_data = self._collate(raw_samples)

        batch = Batch(
            data=batch_data,
            idx=list(idx_slice),
            epoch=self._epoch_counter,
            step=self._step,
        )
        self._step += 1
        return batch

    # ------------------------------------------------------------------ #
    # Public helpers
    # ------------------------------------------------------------------ #
    def add_samples(self, new_samples: Sequence[Any]) -> None:
        """Append *new_samples* to the underlying dataset *in‑place*.

        This is a **shallow** operation – the original *dataset* must be a
        mutable sequence such as ``list`` for this to be meaningful.  If the
        dataset is an immutable wrapper (e.g. *torch.utils.data.Dataset*),
        the caller is responsible for ensuring that ``__len__`` and
        ``__getitem__`` reflect the new size.
        """
        if not new_samples:
            return
        # Assumes dataset is list‑like and supports .extend()
        if hasattr(self.dataset, "extend"):
            self.dataset.extend(new_samples)  # type: ignore[arg-type]
        else:
            raise TypeError(
                "Underlying dataset does not support in‑place extension"
            )
        self._n_samples = len(self.dataset)
        # Recompute indices for *NEXT* epoch – current epoch stays intact
        self._epoch_indices.extend(range(self._n_samples - len(new_samples), self._n_samples))

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #
    def _reset_epoch(self, *, shuffle: bool) -> None:
        self._epoch_indices = list(range(self._n_samples))
        if shuffle:
            self._rng.shuffle(self._epoch_indices)
        self._pos_in_epoch = 0

    def _advance_epoch(self) -> None:
        """Finish current epoch and prepare the next one."""
        self._epoch_counter += 1
        # Handle finite repeat counts
        if isinstance(self.repeat, int) and self._epoch_counter >= self.repeat:
            # Mark as finished so that _should_stop() triggers StopIteration
            self._repeat_done = True  # type: ignore[attr-defined]
            return
        # Prepare indices for next epoch
        self._reset_epoch(shuffle=self.shuffle)

    def _should_stop(self) -> bool:
        # Determine if we have exhausted epochs
        if self.repeat is True:
            return False  # infinite
        if self.repeat is False:
            return self._epoch_counter >= 1 and self._pos_in_epoch == 0
        if isinstance(self.repeat, int):
            # self._repeat_done set in _advance_epoch() once limit reached
            return getattr(self, "_repeat_done", False)
        raise RuntimeError("Invalid repeat flag state")

    # -------------------------------------------------------------- #
    # Convenience getters
    # -------------------------------------------------------------- #
    @property
    def epoch(self) -> int:
        """0‑based index of the *current* epoch (starts at 0)."""
        return self._epoch_counter

    @property
    def step(self) -> int:
        """Number of batches yielded so far (global across epochs)."""
        return self._step

    # ------------------------------------------------------------------ #
    # Representation helpers – for debugging
    # ------------------------------------------------------------------ #
    def __repr__(self) -> str:  # pragma: no cover – cosmetic only
        return (
            f"{self.__class__.__name__}(n_samples={self._n_samples}, batch={self.batch_size}, "
            f"shuffle={self.shuffle}, repeat={self.repeat}, step={self._step}, epoch={self._epoch_counter})"
        ).replace("\n", "")
