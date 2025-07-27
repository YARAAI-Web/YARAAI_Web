from __future__ import annotations

"""src.extract.base
================================
Abstract base class that unifies common logic across all *view* extractors in
:py_mod:`src.extract`.  Sub‑classes only need to implement two things:

*   A class attribute ``VIEW`` that uniquely identifies the view (e.g. ``"ast"``
    or ``"cfg"``).  This value is used to auto‑register the extractor and to
    determine the default on‑disk cache location ``data/views/<VIEW>/``.
*   The :pymeth:`~ExtractorBase.extract` method that receives a path to the input
    binary and **returns a Python object** representing the extracted data.  The
    base‑class takes care of serialisation, deserialisation, and cache hits.

All remaining boiler‑plate—CLI wiring, multiprocessing, logging, SHA256‑based
cache naming, and basic error handling—is handled here so that each concrete
extractor remains minimal.

❗ **Design choices**
--------------------
* **Registration via ``__init_subclass__``** — import side‑effects automatically
  populate :pyattr:`ExtractorBase.registry` so that factory code can do
  ``ExtractorBase.registry[view]``.
* **Content‑addressable caching** — cache file name is ``<sha256>.<fmt>`` where
  *sha256* is computed over the input file *contents* (not just the file name),
  guaranteeing immunity against path aliasing.
* **Progress‑bar & multiprocessing friendly** — :pymeth:`ExtractorBase.run_dir`
  parallelises extraction over multiple files with *tqdm* progress reporting.
* **Pluggable (I/O) formats** — subclasses can override
  :pymeth:`ExtractorBase.serialise` / :pymeth:`ExtractorBase.deserialise` to
  switch between JSON, pickle, msgpack, Parquet, etc.
"""

from abc import ABC, abstractmethod
import argparse
import hashlib
import json
import multiprocessing as mp
import pickle
import signal
import sys
from functools import partial
from pathlib import Path
from typing import Any, ClassVar, Dict, Iterable, List, Sequence

# --------------------------------------------------------------------------- #
# Optional project‑wide utilities (do *not* introduce hard deps in base class)
# --------------------------------------------------------------------------- #
try:
    from src.common.utils import ensure_dir, get_logger, tqdm_wrap  # type: ignore
except ModuleNotFoundError:  # Fallbacks for unit tests / minimal installs
    import logging
    from contextlib import contextmanager

    def ensure_dir(p: Path | str) -> Path:  # noqa: D401
        """Create *p* with parents if needed and return as :class:`Path`."""
        p = Path(p)
        p.mkdir(parents=True, exist_ok=True)
        return p

    def get_logger(name: str = "ExtractorBase") -> logging.Logger:  # noqa: D401
        logging.basicConfig(
            level=logging.INFO, format="[%(asctime)s] %(levelname)s %(name)s: %(message)s"
        )
        return logging.getLogger(name)

    @contextmanager
    def tqdm_wrap(iterable: Iterable[Any], *_, **__):  # noqa: D401
        yield iterable

# --------------------------------------------------------------------------- #
# Base class
# --------------------------------------------------------------------------- #


class ExtractorBase(ABC):
    """Base‑class for all *view* extractors.

    Parameters
    ----------
    cache_dir:
        Directory where extracted artefacts are stored.  Defaults to
        ``data/views/<VIEW>/`` relative to the project root.
    force:
        Re‑run extraction even if a cache entry already exists.
    fmt:
        Output serialisation format.  Currently ``"json"`` and ``"pkl"`` are
        built‑in.
    """

    #: concrete subclasses must override with unique identifier
    VIEW: ClassVar[str] = ""

    #: global registry populated via ``__init_subclass__``
    registry: ClassVar[Dict[str, "type[ExtractorBase]"]]
    registry = {}

    # --------------------------------------------------------------------- #
    # Registration magic & constructor
    # --------------------------------------------------------------------- #

    def __init_subclass__(cls, **kwargs):  # noqa: D401
        super().__init_subclass__(**kwargs)
        if not getattr(cls, "VIEW", None):  # pragma: no cover
            return  # abstract helper / mix‑in => skip registration
        if cls.VIEW in ExtractorBase.registry:
            raise ValueError(f"Duplicate extractor view id: {cls.VIEW!r}")
        ExtractorBase.registry[cls.VIEW] = cls  # type: ignore[arg‑type]

    def __init__(
        self,
        cache_dir: str | Path | None = None,
        *,
        force: bool = False,
        fmt: str = "json",
        verbose: bool = False,
    ) -> None:
        self.view = self.VIEW or self.__class__.__name__.lower()
        root_cache = Path(cache_dir) if cache_dir else Path("data") / "views" / self.view
        self.cache_dir = ensure_dir(root_cache)
        self.force = force
        self.fmt = fmt
        self.log = get_logger(self.__class__.__name__)
        if verbose:
            self.log.setLevel("DEBUG")

    # ------------------------------------------------------------------ #
    # Public user‑facing API
    # ------------------------------------------------------------------ #

    def __call__(self, target: str | Path) -> Path:
        """Extract *target* and return the *cache file path*.

        *target* can be a single binary or an archive.  Sub‑classes decide how
        to treat the input.
        """
        target = Path(target)
        cache_path = self._cache_path_for(target)
        if cache_path.exists() and not self.force:
            self.log.debug("Cache hit → %s", cache_path)
            return cache_path

        self.log.info("[%s] extracting %s", self.view, target)
        data = self.extract(target)
        self._serialise(data, cache_path)
        return cache_path

    # ------------------------------------------------------------------ #
    # Overridable hooks
    # ------------------------------------------------------------------ #

    @abstractmethod
    def extract(self, binary_path: Path) -> Any:  # noqa: D401
        """Concrete extractors implement this.  *Must* be side‑effect free."""

    # ------------------------------------------------------------------ #
    # (De)Serialisation helpers
    # ------------------------------------------------------------------ #

    def _serialise(self, data: Any, dest: Path) -> None:  # noqa: D401
        dest.parent.mkdir(parents=True, exist_ok=True)
        if self.fmt == "json":
            dest.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        elif self.fmt in {"pkl", "pickle"}:
            with dest.open("wb") as fp:
                pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            raise ValueError(f"Unsupported format: {self.fmt}")

    def _deserialise(self, src: Path) -> Any:  # noqa: D401
        if self.fmt == "json":
            return json.loads(src.read_text())
        if self.fmt in {"pkl", "pickle"}:
            with src.open("rb") as fp:
                return pickle.load(fp)
        raise ValueError(f"Unsupported format: {self.fmt}")

    # ------------------------------------------------------------------ #
    # Cache helpers
    # ------------------------------------------------------------------ #

    def _cache_path_for(self, binary_path: Path) -> Path:  # noqa: D401
        sha256 = self._sha256(binary_path)
        return self.cache_dir / f"{sha256}.{self.fmt}"

    @staticmethod
    def _sha256(p: Path, chunk_size: int = 1 << 20) -> str:  # noqa: D401
        h = hashlib.sha256()
        with p.open("rb") as fp:
            while chunk := fp.read(chunk_size):
                h.update(chunk)
        return h.hexdigest()

    # ------------------------------------------------------------------ #
    # Batch utilities (multiprocessing‑safe)
    # ------------------------------------------------------------------ #

    def run_dir(
        self, input_dir: str | Path, *, pattern: str = "**/*", n_jobs: int = 1
    ) -> List[Path]:
        """Extract every file matching *pattern* under *input_dir*.

        Returns the list of cache paths (in arbitrary order).
        """
        files = [p for p in Path(input_dir).rglob(pattern) if p.is_file()]
        self.log.info("%d candidates → %s extractor", len(files), self.view)

        if n_jobs <= 1:
            with tqdm_wrap(files, desc=f"{self.view}:extract", unit="file") as it:
                return [self(f) for f in it]

        # Handle CTRL‑C gracefully in child processes
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        with mp.Pool(processes=n_jobs) as pool:
            worker = partial(_worker_call, cls=self.__class__, cfg=self._cfg())
            try:
                with tqdm_wrap(pool.imap_unordered(worker, files), total=len(files), desc=f"{self.view}:mp") as it:
                    return list(it)
            finally:
                pool.terminate()

    # ------------------------------------------------------------------ #
    # CLI facade
    # ------------------------------------------------------------------ #

    @classmethod
    def main(cls) -> None:  # noqa: D401
        """CLI entry‑point: ``python -m src.extract.base <args>``."""
        parser = argparse.ArgumentParser(description="Generic extractor runner")
        parser.add_argument("input", help="File or directory to extract")
        parser.add_argument("--view", required=True, choices=cls.registry.keys())
        parser.add_argument("--cache-dir", default=None, help="Override cache dir")
        parser.add_argument("--force", action="store_true", help="Ignore existing cache")
        parser.add_argument("--fmt", default="json", help="Output format (json|pkl)")
        parser.add_argument("--workers", "-j", type=int, default=1, help="#processes")
        parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
        args = parser.parse_args()

        extractor_cls = cls.registry[args.view]
        extractor: "ExtractorBase" = extractor_cls(
            cache_dir=args.cache_dir,
            force=args.force,
            fmt=args.fmt,
            verbose=args.verbose,
        )

        in_path = Path(args.input)
        if in_path.is_dir():
            extractor.run_dir(in_path, n_jobs=args.workers)
        elif in_path.is_file():
            extractor(in_path)
        else:
            parser.error(f"Input path not found: {in_path}")

    # ------------------------------------------------------------------ #
    # Support utilities
    # ------------------------------------------------------------------ #

    def _cfg(self) -> Dict[str, Any]:  # noqa: D401
        """Return kwargs necessary to re‑instantiate *self* in a child process."""
        return dict(cache_dir=self.cache_dir, force=self.force, fmt=self.fmt)


# --------------------------------------------------------------------------- #
# Multiprocessing helper (top‑level for picklability)
# --------------------------------------------------------------------------- #

def _worker_call(path: str | Path, *, cls: "type[ExtractorBase]", cfg: Dict[str, Any]) -> Path:  # noqa: D401
    """Entry‑point for :pyclass:`multiprocessing.Pool` workers."""
    inst: ExtractorBase = cls(**cfg)  # Re‑create extractor in forked process
    return inst(Path(path))


# --------------------------------------------------------------------------- #
# Boiler‑plate
# --------------------------------------------------------------------------- #

if __name__ == "__main__":  # pragma: no cover
    ExtractorBase.main()

__all__ = ["ExtractorBase"]
