from __future__ import annotations

"""src.extract.constants
=======================
Centralised constants, including directory layout and view identifiers,
used by the *extract* sub‑package.  Keeping them in a single module avoids
accidental duplication and circular imports.
"""

import os
from pathlib import Path

# --------------------------------------------------------------------------- #
# Filesystem layout
# --------------------------------------------------------------------------- #

# Project root → <repo>/src/extract/constants.py  ⇒ three parents up is repo
_PROJECT_ROOT = Path(__file__).resolve().parents[2]

#: Default data directory (can be overridden via ``$BM_DATA_DIR``)
DEFAULT_DATA_DIR: Path = Path(os.getenv("BM_DATA_DIR", _PROJECT_ROOT / "data"))

#: Content‑addressable view cache root, e.g. ``data/views/ast/``
DEFAULT_VIEWS_DIR: Path = DEFAULT_DATA_DIR / "views"

#: Directory where multi‑view heterographs (Parquet) are stored
DEFAULT_HETERO_DIR: Path = DEFAULT_DATA_DIR / "hetero"

#: Numpy‑compressed embedding cache
DEFAULT_EMBEDS_DIR: Path = DEFAULT_DATA_DIR / "embeds"

# --------------------------------------------------------------------------- #
# View identifiers
# --------------------------------------------------------------------------- #
#: Canonical names for each graph view
VIEW_AST: str = "ast"
VIEW_CFG: str = "cfg"
VIEW_FCG: str = "fcg"
VIEW_SYSCALL: str = "syscall"

#: Set of all recognised views
ALL_VIEWS: set[str] = {VIEW_AST, VIEW_CFG, VIEW_FCG, VIEW_SYSCALL}

# -- Backwards‑compat aliases (pre‑refactor names) -------------------------- #
DEFAULT_AST_VIEW: str = VIEW_AST
DEFAULT_CFG_VIEW: str = VIEW_CFG
DEFAULT_FCG_VIEW: str = VIEW_FCG
DEFAULT_SYSCALL_VIEW: str = VIEW_SYSCALL

# --------------------------------------------------------------------------- #
# Serialisation formats
# --------------------------------------------------------------------------- #

JSON_FMT = "json"
PKL_FMT = "pkl"
SUPPORTED_FMTS: set[str] = {JSON_FMT, PKL_FMT}

# --------------------------------------------------------------------------- #
# Misc magic numbers
# --------------------------------------------------------------------------- #

#: Chunk size for streaming file I/O (1 MiB)
HASH_CHUNK_SIZE: int = 1 << 20

#: Default timeout for external CLI tools (seconds)
CMD_TIMEOUT: int = 120

#: Supported single‑level archive extensions recognised by
#: :pyfunc:`src.extract.utils.extract_archive`
ARCHIVE_SUFFIXES: tuple[str, ...] = (
    ".zip",
    ".tar",
    ".tar.gz",
    ".tgz",
    ".tar.xz",
    ".txz",
    ".tar.bz2",
    ".tbz2",
    ".gz",  # *single file* gzip
)

__all__: list[str] = [
    # Path constants
    "DEFAULT_DATA_DIR",
    "DEFAULT_VIEWS_DIR",
    "DEFAULT_HETERO_DIR",
    "DEFAULT_EMBEDS_DIR",
    # View constants
    "VIEW_AST",
    "VIEW_CFG",
    "VIEW_FCG",
    "VIEW_SYSCALL",
    "ALL_VIEWS",
    # Back‑compat
    "DEFAULT_AST_VIEW",
    "DEFAULT_CFG_VIEW",
    "DEFAULT_FCG_VIEW",
    "DEFAULT_SYSCALL_VIEW",
    # Serialisation
    "JSON_FMT",
    "PKL_FMT",
    "SUPPORTED_FMTS",
    # Misc
    "HASH_CHUNK_SIZE",
    "CMD_TIMEOUT",
    "ARCHIVE_SUFFIXES",
]
