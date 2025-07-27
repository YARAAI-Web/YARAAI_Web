"""
src.extract.pipelines
=====================

Convenience exports + thin CLI hand-off.

Quick start
-----------

>>> from src.extract.pipelines import run_pipeline
>>> run_pipeline(["samples/a.exe", "samples/b.exe"], auto_fix=True)

Command-line
------------

$ python -m src.extract.pipelines --help
(= 내부적으로 ``src.extract.pipelines.cli.main`` 실행)
"""
from __future__ import annotations

import sys
from typing import Iterable, List

from .extract_pipeline import (
    ExtractPipeline,
    ExtractionSummary,
    run_pipeline,
)

# --------------------------------------------------------------------------- #
# Public re-exports
# --------------------------------------------------------------------------- #
__all__: List[str] = [
    "ExtractPipeline",
    "ExtractionSummary",
    "run_pipeline",
    "main",
]

# --------------------------------------------------------------------------- #
# CLI delegation
# --------------------------------------------------------------------------- #
def main(argv: Iterable[str] | None = None) -> None:
    """
    Thin wrapper that forwards to :pyfunc:`src.extract.pipelines.cli.main`.

    This makes the package runnable via::

        python -m src.extract.pipelines  --help
    """
    from .cli import main as _cli_main

    _cli_main(argv)


# When executed as ``python -m src.extract.pipelines`` ---------------------- #
if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
