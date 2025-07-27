#!/usr/bin/env python3
"""
src.extract.pipelines.cli
=========================

Command-line driver for the *extract → validate → fix* pipeline.

::

    $ python -m src.extract.pipelines.cli \
        samples/malware.exe \
        --views ast cfg fcg syscall imports \
        --out-dir data/views \
        --fix --workers 8

Features
--------
* **Multiprocessing** for batch extraction (`--workers N`)
* **Per-view validators** (`--strict / --no-strict`)
* **Heuristic auto-fixer** (`--fix`)
* **Pretty progress bar** when `tqdm` is available
"""
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing as mp
import os
import sys
from functools import partial
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

try:
    from tqdm import tqdm
except ImportError:  # graceful fallback
    tqdm = lambda x, **_: x  # type: ignore

# --------------------------------------------------------------------------- #
# Project imports
# --------------------------------------------------------------------------- #
from src.common.utils import ensure_dir, get_logger, set_random_seed
from src.extract.validators import clean, check, FixReport, SanityError
from src.extract.extractors.view_registry import get_extractor, list_views  # view registry helpers

LOG = get_logger(__name__)


# --------------------------------------------------------------------------- #
# Helper utils
# --------------------------------------------------------------------------- #
def _sha256_of_file(path: Path, chunksize: int = 8192) -> str:
    """Return *lowercase* SHA-256 hex string of file contents."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(chunksize), b""):
            h.update(chunk)
    return h.hexdigest()


def _save_json(obj: Dict, dst: Path) -> None:
    ensure_dir(dst.parent)
    with dst.open("w", encoding="utf-8") as fout:
        json.dump(obj, fout, indent=2, sort_keys=False, ensure_ascii=False)


# --------------------------------------------------------------------------- #
# Core worker
# --------------------------------------------------------------------------- #
def _process_one(
    sample_path: Path,
    view_names: List[str],
    out_dir: Path,
    *,
    strict: bool,
    auto_fix: bool,
) -> Tuple[Path, List[str]]:
    """
    Extract *view_names* from *sample_path* and save JSON(s) to *out_dir*.

    Returns
    -------
    (sample_path, errors)  – `errors` empty list if all succeeded.
    """
    errors: List[str] = []
    sha = _sha256_of_file(sample_path)
    for v in view_names:
        extractor_cls = get_extractor(v)
        extractor = extractor_cls()  # each extractor should be stateless/light
        try:
            view_dict = extractor.run(sample_path)  # ← MUST return Python dict
        except Exception as e:  # noqa: BLE001
            msg = f"[{sample_path.name}/{v}] extractor error → {e}"
            LOG.exception(msg)
            errors.append(msg)
            continue

        try:
            if auto_fix:
                view_dict, report = clean(v, view_dict, max_iter=3)
                if report.status == "fixed":
                    LOG.debug("[%s/%s] auto-fixed:\n%s", sample_path.name, v, report.pretty())
            else:
                check(v, view_dict, strict=strict)
        except SanityError as se:
            msg = f"[{sample_path.name}/{v}] sanity error → {se}"
            LOG.error(msg)
            errors.append(msg)
            continue

        # persistence path: <out_dir>/<view>/<sha>.json
        dst = out_dir / v / f"{sha}.json"
        try:
            _save_json(view_dict, dst)
        except Exception as e:  # noqa: BLE001
            msg = f"[{sample_path.name}/{v}] save error → {e}"
            LOG.exception(msg)
            errors.append(msg)

    return sample_path, errors


# --------------------------------------------------------------------------- #
# Argument parser
# --------------------------------------------------------------------------- #
def _parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="extract-pipeline",
        description="PE/ELF → multi-view JSON extractor with validation/fixer.",
    )
    parser.add_argument("inputs", nargs="+", type=Path,
                        help="input file(s) or directory(ies) to recurse")
    parser.add_argument(
        "--views",
        nargs="+",
        default=list(list_views()),
        choices=list(list_views()),
        help=f"which view(s) to extract (default: all {list(list_views())})",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("data/views"),
        help="output root directory (default: data/views)",
    )
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 4,
                        help="parallel extractor workers (default: CPU count)")
    parser.add_argument("--fix", action="store_true",
                        help="run heuristic auto-fixer on sanity violations")
    parser.add_argument("--no-strict", dest="strict", action="store_false",
                        help="lenient sanity check (collect warnings)")
    parser.set_defaults(strict=True)
    parser.add_argument("--seed", type=int, default=42, help="global RNG seed")
    return parser.parse_args(argv)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main(argv: Iterable[str] | None = None) -> None:
    args = _parse_args(argv)
    set_random_seed(args.seed)
    LOG.info("views   : %s", args.views)
    LOG.info("out-dir : %s", args.out_dir.resolve())
    LOG.info("workers : %d", args.workers)
    LOG.info("strict? : %s  | auto-fix? : %s", args.strict, args.fix)

    # gather sample paths
    paths: List[Path] = []
    for p in args.inputs:
        if p.is_dir():
            paths.extend(p.rglob("*"))  # include nested
        else:
            paths.append(p)
    # filter only files
    paths = [p for p in paths if p.is_file()]
    if not paths:
        LOG.error("no input files found – abort")
        sys.exit(2)
    LOG.info("total   : %d sample(s)", len(paths))

    worker_fn = partial(
        _process_one,
        view_names=args.views,
        out_dir=args.out_dir,
        strict=args.strict,
        auto_fix=args.fix,
    )

    n_err = 0
    with mp.Pool(args.workers) as pool:
        for _, errs in tqdm(pool.imap_unordered(worker_fn, paths), total=len(paths)):
            n_err += len(errs)
            for e in errs:
                LOG.warning("%s", e)

    LOG.info("finished: %d sample(s), %d error(s)", len(paths), n_err)
    if n_err:
        LOG.warning("pipeline completed with errors (see log)")
        sys.exit(1)


if __name__ == "__main__":
    main()
