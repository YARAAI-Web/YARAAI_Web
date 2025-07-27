from pathlib import Path

# ensure submodules like rulegen.feature_miner resolve even if the repo root shadows site-packages
_src_pkg = Path(__file__).resolve().parents[1] / "src" / "rulegen"
if _src_pkg.exists() and str(_src_pkg) not in __path__:
    __path__.append(str(_src_pkg))

import src.rulegen
from src.rulegen import *  # re-export

__all__ = src.rulegen.__all__
