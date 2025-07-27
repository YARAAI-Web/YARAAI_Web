"""src.continual.datastream
================================
Top‑level **package facade** for *online / continual‑learning* data streams in
``robust‑malware‑graph``.  It stitches together the three sub‑modules –
:pyfile:`utils.py`, :pyfile:`samplers.py`, and :pyfile:`stream.py` – and
re‑exports their public symbols behind a concise import surface so that
call‑sites can simply do::

    >>> from src.continual.datastream import Stream, make_sampler
    >>> sampler = make_sampler("random", num_examples=10)
    >>> ds = Stream(data=list(range(10)), sampler=sampler, batch_size=4)
    >>> next(ds)
    [7, 0, 8, 2]

This *facade* stays completely **framework‑agnostic** – it depends only on the
standard library.  Down‑stream packages may, of course, wrap these utilities
into PyTorch `DataLoader`‑like abstractions.
"""
from __future__ import annotations

# Re‑export utilities --------------------------------------------------------
from .utils import set_random_seed

# Re‑export samplers ---------------------------------------------------------
from .samplers import (
    BaseSampler,
    SequentialSampler,
    RandomSampler,
    ReservoirSampler,
    SlidingWindowSampler,
    make_sampler,
)

# Re‑export stream iterable --------------------------------------------------
from .stream import Stream

# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------
__all__: list[str] = [
    # utils
    "set_random_seed",
    # samplers
    "BaseSampler",
    "SequentialSampler",
    "RandomSampler",
    "ReservoirSampler",
    "SlidingWindowSampler",
    "make_sampler",
    # stream
    "Stream",
]

# ---------------------------------------------------------------------------
# Metadata helper (optional)
# ---------------------------------------------------------------------------
__version__: str = "0.1.0"

def __getattr__(name: str):  # pragma: no cover – lazy attr fallback
    """Late‑import fallback for ambience tooling such as Sphinx autodoc.

    This tiny helper prevents *ImportError* when documentation or runtime code
    tries to access sub‑modules (e.g. ``src.continual.datastream.samplers``)
    that are **not** pulled in by the wildcard‑style re‑exports above.
    """
    if name in {"utils", "samplers", "stream"}:
        import importlib

        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
