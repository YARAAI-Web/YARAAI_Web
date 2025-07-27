from __future__ import annotations

"""src.extract.utils
====================
Light-weight helper functions used across *view* extractors.
These utilities are intentionally dependency-free (\*standard library only\*) so
that they work in minimal environments such as read-only Docker images used for
static analysis.

Functions
---------
sha256_file
    Streaming SHA-256 hash (memory-efficient).
is_pe / is_elf / is_macho
    Magic-number based format probes.
detect_binary_kind
    One-shot wrapper that returns ``"pe"``, ``"elf"``, ``"macho"`` or
    ``"unknown"``.
extract_archive
    Single-level decompression for common archive formats (``.zip``, ``.tar.*``
    and ``.gz`` singletons).  Returns the extracted member paths.
run_cmd
    Simple *subprocess* wrapper with timeout and logging.
find_binaries_in_dir
    Recursively walk a directory and yield regular files that *look* like
    native binaries (based on :pyfunc:`detect_binary_kind`).
"""

from pathlib import Path
from subprocess import CalledProcessError, CompletedProcess, run
from typing import Iterable, List, Sequence
import hashlib
import logging
import shutil
import tarfile
import tempfile
import zipfile
import gzip
import os

try:
    from src.common.utils import get_logger  # type: ignore
except ModuleNotFoundError:  # Fallback when running in isolation / unit tests
    import logging

    def get_logger(name: str = "extract.utils") -> logging.Logger:  # noqa: D401
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] %(levelname)s %(name)s: %(message)s",
        )
        return logging.getLogger(name)

log = get_logger("extract.utils")

# --------------------------------------------------------------------------- #
# 1. Cryptographic hash
# --------------------------------------------------------------------------- #

def sha256_file(path: str | Path, *, chunk_size: int = 1 << 20) -> str:  # noqa: D401
    """Return hexadecimal SHA-256 of *path* without loading file into memory."""
    h = hashlib.sha256()
    with Path(path).open("rb") as fp:
        while chunk := fp.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


# --------------------------------------------------------------------------- #
# 2. File-format probes (magic numbers — cheap and cheerful)
# --------------------------------------------------------------------------- #

_PE_MAGIC = b"MZ"
_ELF_MAGIC = b"\x7fELF"
_MACHO_MAGICS = {
    b"\xfe\xed\xfa\xce",  # MH_MAGIC   (32-bit, little-endian)
    b"\xce\xfa\xed\xfe",  # MH_CIGAM   (32-bit, big-endian)
    b"\xfe\xed\xfa\xcf",  # MH_MAGIC_64
    b"\xcf\xfa\xed\xfe",  # MH_CIGAM_64
}


def _read_prefix(path: Path, n: int = 4) -> bytes:
    with path.open("rb") as fp:
        return fp.read(n)


def is_pe(path: str | Path) -> bool:  # noqa: D401
    """Return *True* iff file starts with PE/COFF magic (``MZ``)."""
    return _read_prefix(Path(path), 2) == _PE_MAGIC


def is_elf(path: str | Path) -> bool:  # noqa: D401
    """Return *True* iff file starts with ``0x7F 45 4C 46`` (ELF)."""
    return _read_prefix(Path(path), 4) == _ELF_MAGIC


def is_macho(path: str | Path) -> bool:  # noqa: D401
    """Return *True* iff file header matches one of Mach-O magic values."""
    return _read_prefix(Path(path), 4) in _MACHO_MAGICS


def detect_binary_kind(path: str | Path) -> str:  # noqa: D401
    """Cheap heuristic → ``'pe' | 'elf' | 'macho' | 'unknown'``."""
    p = Path(path)
    if p.is_file():
        if is_pe(p):
            return "pe"
        if is_elf(p):
            return "elf"
        if is_macho(p):
            return "macho"
    return "unknown"


# --------------------------------------------------------------------------- #
# 3. Archive extraction (single-level)
# --------------------------------------------------------------------------- #

_ALLOWED_TAR_COMPS = ("gz", "xz", "bz2")


def extract_archive(archive: str | Path, dest_dir: str | Path | None = None) -> List[Path]:  # noqa: D401
    """Extract *archive* into *dest_dir* (temp if *None*).

    Only handles *single-level* archives.  Nested archives are returned as is.
    Returns a list of extracted *Path*s.  Caller is responsible for clean-up if
    *dest_dir* was *None*.
    """
    archive = Path(archive)
    dest_dir = Path(dest_dir) if dest_dir else Path(tempfile.mkdtemp(prefix="ext_"))
    extracted: List[Path] = []

    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(dest_dir)
            extracted.extend(Path(dest_dir / m) for m in zf.namelist())
        return extracted

    if tarfile.is_tarfile(archive):
        with tarfile.open(archive) as tf:
            tf.extractall(dest_dir)
            extracted.extend(Path(dest_dir / m) for m in tf.getnames())
        return extracted

    if archive.suffix == ".gz" and not archive.name.endswith(
        (".tar.gz", ".tgz")
    ):  # plain .gz (single member)
        target = dest_dir / archive.stem
        with gzip.open(archive, "rb") as src, target.open("wb") as dst:
            shutil.copyfileobj(src, dst)
        extracted.append(target)
        return extracted

    raise ValueError(f"Unsupported archive format: {archive}")


# --------------------------------------------------------------------------- #
# 4. Subprocess helper
# --------------------------------------------------------------------------- #

def run_cmd(
    cmd: Sequence[str] | str,
    *,
    timeout: int | float | None = 120,
    check: bool = True,
    capture_output: bool = True,
    text: bool = True,
    cwd: str | Path | None = None,
    env: dict[str, str] | None = None,
) -> CompletedProcess:  # noqa: D401
    """Wrapper around :pyfunc:`subprocess.run` with sane defaults & logging."""
    log.debug("$ %s", cmd)
    try:
        result = run(
            cmd,
            timeout=timeout,
            check=check,
            capture_output=capture_output,
            text=text,
            cwd=cwd,
            env=env,
        )
    except CalledProcessError as exc:
        log.error("Command failed (code=%s): %s", exc.returncode, exc.cmd)
        if exc.stdout:
            log.error("stdout: %s", exc.stdout[:500])
        if exc.stderr:
            log.error("stderr: %s", exc.stderr[:500])
        raise
    except Exception:  # pragma: no cover — generic fall-back
        log.exception("Unhandled error while running command: %s", cmd)
        raise
    return result


# --------------------------------------------------------------------------- #
# 5. Directory walkers
# --------------------------------------------------------------------------- #

_BINARY_EXT_HINTS = {
    ".exe",
    ".dll",
    ".sys",
    ".so",
    ".dylib",
    ".bin",
    ".o",
    ".ko",
}


def find_binaries_in_dir(
    root: str | Path,
    *,
    follow_links: bool = False,
    recurse: bool = True,
) -> Iterable[Path]:  # noqa: D401
    """Yield files that *look* like native binaries under *root*.

    Uses two heuristics: file-extension hint OR magic-number probe.
    """
    root = Path(root)
    walker = root.rglob("*") if recurse else root.glob("*")
    for p in walker:
        try:
            if not p.is_file():
                continue
            if p.suffix.lower() in _BINARY_EXT_HINTS or detect_binary_kind(p) != "unknown":
                yield p
        except OSError:  # permission issues etc.
            log.debug("Skip unreadable file: %s", p)


__all__ = [
    "sha256_file",
    "is_pe",
    "is_elf",
    "is_macho",
    "detect_binary_kind",
    "extract_archive",
    "run_cmd",
    "find_binaries_in_dir",
]
