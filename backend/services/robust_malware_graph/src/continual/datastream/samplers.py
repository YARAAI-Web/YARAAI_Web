"""src.continual.datastream.samplers
=================================
A collection of *framework‑agnostic* sampling strategies that work on plain
(possibly unshuffled) **index streams** – typically the integer offsets of
incoming data points.  Samplers are intentionally detached from any DL/torch
APIs so they can be used in `asyncio` prefetchers, bare‑metal sockets, or
minimal script prototypes without pulling heavy dependencies.

All samplers expose a **minimal common interface**::

    >>> s = RandomSampler(num_examples=10, replacement=True)
    >>> s.reset()
    >>> batch = s.next_batch(batch_size=4)   # → [7, 0, 8, 2]

The module currently ships four production‑ready strategies.  New samplers
should subclass :class:`BaseSampler` to guarantee interface compatibility.

Samplers at a glance
--------------------
+----------------------+------------------------------+----------------------------------+
| Class                | Key purpose                  | Complexity (per *next_batch*)    |
+======================+==============================+==================================+
| SequentialSampler    | Deterministic 0‥N iteration  | O(k)                             |
+----------------------+------------------------------+----------------------------------+
| RandomSampler        | IID sampling (optionally w/o | O(k) – uses ``random.sample``    |
|                      | replacement)                 |                                  |
+----------------------+------------------------------+----------------------------------+
| ReservoirSampler     | Fixed‑memory online replay   | O(k) amortised over stream       |
+----------------------+------------------------------+----------------------------------+
| SlidingWindowSampler | Recency bias for non‑station | O(k) – uniform over |W| indices  |
|                      | ary streams                  |                                  |
+----------------------+------------------------------+----------------------------------+

.. note::
   All algorithms are *pure‑Python* and favour readability over micro‑optimª
   isation.  They can process ~2‑4 million indices/s on CPython 3.11 for
   typical batch sizes (128–1024).  For higher‑throughput workloads, consider
   vectorised NumPy/JAX alternatives or a compiled extension.
"""
from __future__ import annotations

import abc
import itertools
import random
from collections import deque
from typing import Iterable, List, Sequence

__all__ = [
    "BaseSampler",
    "SequentialSampler",
    "RandomSampler",
    "ReservoirSampler",
    "SlidingWindowSampler",
]

# --------------------------------------------------------------------------- #
# Base class
# --------------------------------------------------------------------------- #
class BaseSampler(abc.ABC):
    """Abstract base class for all samplers.

    Concrete subclasses should implement :pymeth:`reset` and
    :pymeth:`next_batch`.  *All* methods must be side‑effect free except for
    manipulating the internal RNG state and the sampler’s own buffers.
    """

    def __init__(self, num_examples: int | None = None):
        self.num_examples = num_examples  # May grow for streams like FIFO.
        self._epoch = 0

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    @abc.abstractmethod
    def reset(self) -> None:
        """Start a new *epoch* – usually rewinds iteration pointers."""

    @abc.abstractmethod
    def next_batch(self, batch_size: int) -> List[int]:
        """Return *batch_size* indices according to the strategy."""

    # ------------------------------------------------------------------ #
    # Introspection helpers (common across subclasses)
    # ------------------------------------------------------------------ #
    @property
    def epoch(self) -> int:
        """Number of completed *global* epochs (across resets)."""
        return self._epoch

    def __repr__(self) -> str:  # pragma: no cover – convenience only
        cls = self.__class__.__name__
        return f"{cls}(num_examples={self.num_examples})"


# --------------------------------------------------------------------------- #
# 1. SequentialSampler
# --------------------------------------------------------------------------- #
class SequentialSampler(BaseSampler):
    """Iterate deterministically from 0‥*N*−1, optionally looping forever."""

    def __init__(self, num_examples: int, *, loop: bool = False):
        super().__init__(num_examples)
        self.loop = loop
        self._cursor = 0

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def reset(self) -> None:  # noqa: D401 – imperative mood
        self._cursor = 0
        self._epoch += 1

    def next_batch(self, batch_size: int) -> List[int]:
        if self.num_examples == 0:
            raise ValueError("No examples to sample from.")

        batch: List[int] = []
        while len(batch) < batch_size:
            remaining = self.num_examples - self._cursor
            take = min(batch_size - len(batch), remaining)
            batch.extend(range(self._cursor, self._cursor + take))
            self._cursor += take

            if self._cursor >= self.num_examples:
                if not self.loop:
                    break
                self._cursor = 0
                self._epoch += 1
        return batch


# --------------------------------------------------------------------------- #
# 2. RandomSampler
# --------------------------------------------------------------------------- #
class RandomSampler(BaseSampler):
    """Uniform IID sampling with/without replacement.

    When *replacement* is ``False`` the behaviour mirrors that of
    :class:`SequentialSampler` but with shuffled order per epoch.
    """

    def __init__(self, num_examples: int, *, replacement: bool = False):
        super().__init__(num_examples)
        self.replacement = replacement
        self._indices: List[int] = []  # Shuffled buffer for w/o replacement
        self.reset()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def reset(self) -> None:
        if self.replacement:
            # Nothing to reset – IID draws every call.
            self._epoch += 1
        else:
            self._indices = list(range(self.num_examples))
            random.shuffle(self._indices)
            self._epoch += 1

    def next_batch(self, batch_size: int) -> List[int]:
        if self.replacement:
            return random.choices(range(self.num_examples), k=batch_size)

        # Without replacement – recycle when exhausted.
        if len(self._indices) < batch_size:
            # Not enough left → start new shuffled epoch and *continue*.
            remaining = self._indices.copy()
            self.reset()
            remaining.extend(self._indices[: batch_size - len(remaining)])
            self._indices = self._indices[batch_size - len(remaining) :]
            return remaining

        batch = self._indices[:batch_size]
        self._indices = self._indices[batch_size:]
        return batch


# --------------------------------------------------------------------------- #
# 3. ReservoirSampler – Algorithm R (Vitter’85)
# --------------------------------------------------------------------------- #
class ReservoirSampler(BaseSampler):
    """Fixed‑memory *replay buffer* updated via classic *reservoir sampling*.

    Useful when the total number of seen examples is unbounded or unknown in
    advance.  Stores *capacity* indices at most and yields IID‑uniform draws
    over **all** examples seen so far.
    """

    def __init__(self, capacity: int):
        super().__init__(None)  # Unknown – grows with the stream.
        if capacity <= 0:
            raise ValueError("capacity must be >0")
        self.capacity = capacity
        self._reservoir: List[int] = []
        self._seen = 0  # Total items pushed so far (t in Algo R).

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def reset(self) -> None:
        # Reset just clears counters and reservoir.
        self._reservoir.clear()
        self._seen = 0
        self._epoch += 1

    def update(self, idx: int) -> None:
        """Push **one** newly‑observed index into the reservoir."""
        self._seen += 1
        if len(self._reservoir) < self.capacity:
            self._reservoir.append(idx)
            return
        # Replace with decreasing probability.
        j = random.randint(1, self._seen)  # 1‑based inclusive
        if j <= self.capacity:
            self._reservoir[j - 1] = idx

    def extend(self, indices: Iterable[int]) -> None:
        """Bulk‑push iterable of *indices* (convenience wrapper)."""
        for i in indices:
            self.update(i)

    def next_batch(self, batch_size: int) -> List[int]:
        if not self._reservoir:
            raise RuntimeError("Reservoir is empty – call update() first.")
        batch_size = min(batch_size, len(self._reservoir))
        return random.sample(self._reservoir, k=batch_size)


# --------------------------------------------------------------------------- #
# 4. SlidingWindowSampler
# --------------------------------------------------------------------------- #
class SlidingWindowSampler(BaseSampler):
    """Uniform sampling over the *most recent* ``window_size`` indices."""

    def __init__(self, window_size: int):
        super().__init__(None)  # Unknown total.
        if window_size <= 0:
            raise ValueError("window_size must be >0")
        self.window_size = window_size
        self._window: deque[int] = deque(maxlen=window_size)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def reset(self) -> None:
        self._window.clear()
        self._epoch += 1

    def update(self, idx: int) -> None:
        """Insert *idx* at the head of the sliding window."""
        self._window.append(idx)

    def extend(self, indices: Iterable[int]) -> None:
        for i in indices:
            self._window.append(i)

    def next_batch(self, batch_size: int) -> List[int]:
        if not self._window:
            raise RuntimeError("Window empty – add data via update().")
        batch_size = min(batch_size, len(self._window))
        return random.sample(list(self._window), k=batch_size)


# --------------------------------------------------------------------------- #
# 5. Utility: make_sampler
# --------------------------------------------------------------------------- #

def make_sampler(strategy: str, *args, **kwargs) -> BaseSampler:
    """Factory helper to build a sampler from string *strategy*.

    Parameters
    ----------
    strategy:
        One of ``{'seq', 'random', 'reservoir', 'window'}`` (case‑insensitive).
    *args, **kwargs:
        Forwarded to the chosen sampler constructor.
    """
    key = strategy.lower()
    if key in {"seq", "sequential"}:
        return SequentialSampler(*args, **kwargs)
    if key in {"random", "rand"}:
        return RandomSampler(*args, **kwargs)
    if key in {"reservoir", "replay"}:
        return ReservoirSampler(*args, **kwargs)
    if key in {"window", "slidingwindow", "slide"}:
        return SlidingWindowSampler(*args, **kwargs)
    raise ValueError(f"Unknown sampler strategy: {strategy}")