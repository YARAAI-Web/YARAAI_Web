"""Incremental running mean and variance utility."""
from __future__ import annotations

import math


class RunningStats:
    """Compute running mean and variance.

    Uses Welford's online algorithm for numerical stability.
    """

    def __init__(self) -> None:
        self.n = 0
        self._mean = 0.0
        self._m2 = 0.0

    def update(self, x: float) -> None:
        """Update statistics with a new value ``x``."""
        self.n += 1
        delta = x - self._mean
        self._mean += delta / self.n
        delta2 = x - self._mean
        self._m2 += delta * delta2

    @property
    def mean(self) -> float:
        """Return the current mean (0 if no samples)."""
        return self._mean if self.n else 0.0

    @property
    def var(self) -> float:
        """Return the current variance (0 if fewer than 2 samples)."""
        return self._m2 / self.n if self.n else 0.0

    @property
    def std(self) -> float:
        """Return the current standard deviation."""
        return math.sqrt(self.var)
