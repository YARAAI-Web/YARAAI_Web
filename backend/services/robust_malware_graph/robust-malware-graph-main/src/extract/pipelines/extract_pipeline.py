from __future__ import annotations
"""
src.extract.pipelines.extract_pipeline
======================================

Programmatic interface for the *extract → validate → fix → persist* workflow.

Typical usage
-------------

>>> from pathlib import Path
>>> from src.extract.pipelines.extract_pipeline import ExtractPipeline
>>>
>>> pipe = ExtractPipeline(
...     views=["ast", "cfg", "fcg"],
...     out_dir=Path("data/views"),
...     strict=True,
...     auto_fix=True,
...     workers=8,          # mp.Pool
... )
>>> summary = pipe.run(Path("samples/"))
>>> print(summary.pretty())

Design notes
------------
* **Batch-friendly** : accepts list/iterator/dir of sample paths
* **Stateless Extractor** assumption – one instance per call
* **tqdm** optional; gracefully degrades if missing
* **Return value** : `ExtractionSummary` (counts, per-file errors)
"""



import hashlib
import json
import multiprocessing as mp
import os
from dataclasses import dataclass, field
import inspect
from functools import partial
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

try:
    from tqdm import tqdm  # type: ignore
except ModuleNotFoundError:  # fallback: no-op iterator
    tqdm = lambda x, **_: x  # type: ignore

# --------------------------------------------------------------------------- #
# Project imports
# --------------------------------------------------------------------------- #
from src.common.utils import ensure_dir, get_logger, set_random_seed
from src.extract.validators import clean, check, SanityError
from src.extract.extractors.view_registry import get_extractor, list_views

LOG = get_logger(__name__)


# --------------------------------------------------------------------------- #
# 1. Helper – SHA-256 & JSON saver
# --------------------------------------------------------------------------- #
def _sha256(fp: Path, chunk: int = 8192) -> str:
    h = hashlib.sha256()
    with fp.open("rb") as fh:
        for blk in iter(lambda: fh.read(chunk), b""):
            h.update(blk)
    return h.hexdigest()


def _dump_json(obj: Dict, dst: Path) -> None:
    ensure_dir(dst.parent)
    with dst.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=False)


# --------------------------------------------------------------------------- #
# 2. Result containers
# --------------------------------------------------------------------------- #
@dataclass(slots=True)
class FileReport:
    path: Path
    errors: List[str] = field(default_factory=list)

    def ok(self) -> bool:  # noqa: D401 (simple property)
        return not self.errors


@dataclass(slots=True)
class ExtractionSummary:
    total: int
    ok: int
    failed: int
    reports: List[FileReport] = field(repr=False)

    def pretty(self) -> str:
        bar = "-" * 52
        lines = [bar,
                 f"  total   : {self.total}",
                 f"  success : {self.ok}",
                 f"  failed  : {self.failed}",
                 bar]
        if self.failed:
            lines.append("  Failures:")
            for r in self.reports:
                if r.errors:
                    lines.extend([f"    • {e}" for e in r.errors])
            lines.append(bar)
        return "\n".join(lines)

    # console-friendly repr
    def __repr__(self) -> str:
        return self.pretty()


# --------------------------------------------------------------------------- #
# 3. Core worker (single sample, multiple views)
# --------------------------------------------------------------------------- #
def _process_sample(
    sample: Path,
    view_names: List[str],
    out_dir: Path,
    *,
    strict: bool,
    auto_fix: bool,
    overwrite: bool,
) -> FileReport:
    """Return `FileReport` summarising extraction result for one sample."""
    rep = FileReport(path=sample)
    sha = _sha256(sample)

    for view in view_names:
        extractor_cls = get_extractor(view)
        sig = inspect.signature(extractor_cls)
        if "out_dir" in sig.parameters:
            extractor = extractor_cls(out_dir=out_dir / view)
        else:
            extractor = extractor_cls()            # stateless
        view_tag = f"[{sample.name}/{view}]"

        # --------------------- run extractor ------------------------------ #
        try:
            data_dict = extractor.run(sample)  # MUST return dict
        except Exception as e:  # noqa: BLE001
            msg = f"{view_tag} extractor error → {e}"
            LOG.exception(msg)
            rep.errors.append(msg)
            continue

        # --------------------- validate / fix ----------------------------- #
        try:
            if auto_fix:
                data_dict, _ = clean(view, data_dict, max_iter=3)
            else:
                check(view, data_dict, strict=strict)
        except SanityError as se:
            msg = f"{view_tag} sanity error → {se}"
            LOG.error(msg)
            rep.errors.append(msg)
            continue

        # --------------------- persist ------------------------------------ #
        dst = out_dir / view / f"{sha}.json"
        if dst.exists() and not overwrite:
            LOG.debug("%s exists; skip (overwrite=False)", dst)
            continue
        try:
            _dump_json(data_dict, dst)
        except Exception as e:  # noqa: BLE001
            msg = f"{view_tag} save error → {e}"
            LOG.exception(msg)
            rep.errors.append(msg)

    return rep


# --------------------------------------------------------------------------- #
# 4. Public pipeline class
# --------------------------------------------------------------------------- #
class ExtractPipeline:
    """
    End-to-end extractor / validator pipeline exposed as a reusable class.
    """

    # --------------------------------------------------------------------- #
    def __init__(
        self,
        *,
        views: List[str] | None = None,
        out_dir: Path | None = None,
        cache_dir: Path | None = None,
        auto_fix: bool = False,
        strict: bool = True,
        workers: int | None = None,
        seed: int = 42,
        overwrite: bool = False,
    ) -> None:
        if cache_dir is not None and out_dir is None:
            out_dir = cache_dir  # 과거 이름 지원
        self.out_dir = out_dir or Path("data/views")
        self.overwrite = overwrite
        self.views = views or list(list_views())
        self.strict = strict
        self.auto_fix = auto_fix
        self.workers = workers or (os.cpu_count() or 4)
        self.seed = seed

        set_random_seed(seed)  # for deterministic extractors (if any)
        LOG.debug("ExtractPipeline init: %s", self.__dict__)

    # --------------------------------------------------------------------- #
    def _gather_inputs(self, inputs: Iterable[Path | str]) -> List[Path]:
        paths: List[Path] = []
        for p in inputs:
            p = Path(p)
            if p.is_dir():
                paths.extend(pp for pp in p.rglob("*") if pp.is_file())
            elif p.is_file():
                paths.append(p)
        return paths

    # --------------------------------------------------------------------- #
    def run(self, *inputs: Path | str | Iterable[Path | str]) -> ExtractionSummary:
        """
        Execute pipeline on given *inputs* (files or directories).

        Returns
        -------
        ExtractionSummary
        """
        # flatten variadic inputs
        merged: List[Path | str] = []
        for arg in inputs:
            if isinstance(arg, (list, tuple, set)):
                merged.extend(arg)
            else:
                merged.append(arg)

        samples = self._gather_inputs(merged)
        if not samples:
            raise FileNotFoundError("No input files found.")

        LOG.info("pipeline starting – samples: %d, views: %s", len(samples), self.views)

        worker_fn = partial(
            _process_sample,
            view_names=self.views,
            out_dir=self.out_dir,
            strict=self.strict,
            auto_fix=self.auto_fix,
            overwrite=self.overwrite,
        )

        # --- parallel map with tqdm -------------------------------------- #
        reports: List[FileReport]
        if self.workers == 1:
            reports = [worker_fn(p) for p in tqdm(samples)]
        else:
            with mp.Pool(self.workers) as pool:
                reports = list(
                    tqdm(pool.imap_unordered(worker_fn, samples), total=len(samples))
                )

        # --- summarise ---------------------------------------------------- #
        total = len(reports)
        ok = sum(1 for r in reports if r.ok())
        failed = total - ok
        summary = ExtractionSummary(total=total, ok=ok, failed=failed, reports=reports)

        LOG.info("pipeline done – success: %d / %d", ok, total)
        if failed:
            LOG.warning("pipeline finished with %d failure(s)", failed)

        return summary


# --------------------------------------------------------------------------- #
# 5. Convenience functional wrapper
# --------------------------------------------------------------------------- #
def run_pipeline(
    inputs: Iterable[Path | str],
    **kwargs,
) -> ExtractionSummary:
    """
    Shorthand for one-off execution without instantiating `ExtractPipeline`.

    Example
    -------
    >>> from src.extract.pipelines.extract_pipeline import run_pipeline
    >>> run_pipeline(["samples/a.exe", "samples/b.exe"], auto_fix=True)
    """
    pipe = ExtractPipeline(**kwargs)
    return pipe.run(*inputs)


__all__ = [
    "ExtractPipeline",
    "ExtractionSummary",
    "run_pipeline",
]
