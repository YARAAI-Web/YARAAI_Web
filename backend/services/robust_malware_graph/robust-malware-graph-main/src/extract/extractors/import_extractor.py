from __future__ import annotations

"""ImportExtractor
==================

Recover the **Import Table** (a.k.a. Dynamic Symbol Table) of a PE or ELF
binary and output a *stable, compact JSON* file with the following layout::

    {
        "binary_sha256": "...",      # input file hash for provenance
        "format": "PE" | "ELF",
        "imports": [                  # sorted by DLL / shared‑obj then symbol name
            {
                "lib": "KERNEL32.dll",  # library / SONAME
                "symbol": "CreateFileW",# imported symbol name (or ordinal)
                "iat_addr": 4198400,      # RVA/VADDR of the IAT/PLT entry
                "bind": "WEAK" | "GLOBAL" | "UNSPECIFIED"
            },
            ...
        ]
    }

The extractor follows the same *pluggable backend* design used by
:pyfile:`ast_extractor.py` and :pyfile:`cfg_extractor.py`.  By default it relies
on **angr** (which internally uses *cle* + *lief*) for binary loading, but
switches to plain *lief* if angr is not available.  Caching, timeout handling,
and multiprocessing hooks are also supported via the shared
:class:`~src.extract.base.ExtractorBase` mixin.
"""

from dataclasses import dataclass
import hashlib
import json
import logging
import multiprocessing as mp
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Literal
# Import the shared extractor interface
from ..base import ExtractorBase

try:
    import angr  # type: ignore
except ImportError:  # pragma: no cover
    angr = None  # noqa: N816 – keep sentinel lowercase

try:
    import lief  # type: ignore
except ImportError:  # pragma: no cover
    lief = None  # noqa: N816 – keep sentinel lowercase

# ---------------------------------------------------------------------------
# ImportExtractor implementation
# ---------------------------------------------------------------------------

@dataclass(kw_only=True, slots=True)
class ImportRecord:
    lib: str
    symbol: str
    iat_addr: int | None = None  # may be None for ELF w/o PLT relocation
    bind: Literal["GLOBAL", "WEAK", "UNSPECIFIED"] = "UNSPECIFIED"

    def to_json(self) -> Dict[str, Any]:
        return {
            "lib": self.lib,
            "symbol": self.symbol,
            "iat_addr": self.iat_addr,
            "bind": self.bind,
        }


class ImportExtractor(ExtractorBase):
    """Concrete extractor for import table."""

    #: File extension → format name mapping (angr uses *cle* loader names)
    _FORMAT_MAP: Dict[str, str] = {"pe": "PE", "elf": "ELF"}

    def __init__(self, *, timeout: int | None = 120, cache_dir: str | Path | None = None, backend: Literal["angr", "lief", "auto"] = "auto") -> None:  # noqa: D401,E501
        # ExtractorBase no longer supports a timeout parameter
        super().__init__(cache_dir=cache_dir)
        self.timeout = timeout
        self.backend = self._resolve_backend(backend)
        self.name = "ImportExtractor"
        self.logger = logging.getLogger(self.name)

    # ---------------------------------------------------------------------
    # Public API (the actual logic is delegated to _extract)
    # ---------------------------------------------------------------------

    def _extract(self, binary: Path, **_: Any) -> Dict[str, Any]:  # noqa: D401
        start = time.perf_counter()
        self.logger.debug("Loading binary %s with backend=%s", binary, self.backend)

        if self.backend == "angr":
            result = self._extract_with_angr(binary)
        else:
            result = self._extract_with_lief(binary)

        elapsed = time.perf_counter() - start
        self.logger.debug("Finished import extraction in %.02f s", elapsed)
        return result

    def extract(self, binary_path: Path, *, force: bool = False) -> Path:
        """Extract imports and cache the JSON result."""
        binary_path = Path(binary_path)
        cache_path = self._cache_path_for(binary_path)

        if cache_path.exists() and not force:
            return cache_path

        cache_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with mp.Pool(1) as pool:
                async_res = pool.apply_async(self._extract, (binary_path,))
                data = async_res.get(self.timeout)
        except TimeoutError:
            self.logger.warning("Timeout extracting imports from %s", binary_path)
            data = {
                "error": "timeout",
                "binary_sha256": self._sha256(binary_path),
                "backend": self.backend,
            }
        else:
            data["backend"] = self.backend

        self._serialise(data, cache_path)
        return cache_path

    def run(self, sample_path: Path) -> Dict[str, Any]:
        """Return the parsed JSON dictionary for *sample_path*."""
        json_path = self.extract(sample_path)
        return self._deserialise(json_path)

    # ------------------------------------------------------------------
    # Backend‑specific extraction helpers
    # ------------------------------------------------------------------

    def _extract_with_angr(self, binary: Path) -> Dict[str, Any]:
        if angr is None:
            raise RuntimeError("angr is not installed; cannot use angr backend")

        p = angr.Project(str(binary), auto_load_libs=False)  # lazy; avoids heavy deps

        imports: List[ImportRecord] = []
        for obj in p.loader.all_objects:
            for sym in obj.imports:
                imports.append(
                    ImportRecord(
                        lib=obj.provides if obj.provides else obj.binary.basename,
                        symbol=sym.name or f"ordinal_{sym.ordinal}",
                        iat_addr=sym.rebased_addr if hasattr(sym, "rebased_addr") else None,
                        bind="UNSPECIFIED",
                    )
                )

        j = self._normalise_output(binary, imports, format_=p.loader.main_object.execstack)
        return j

    def _extract_with_lief(self, binary: Path) -> Dict[str, Any]:
        if lief is None:
            raise RuntimeError("lief is not installed; cannot use lief backend")

        bin_obj = lief.parse(str(binary))
        if bin_obj is None:
            raise RuntimeError("lief failed to parse binary")

        imports: List[ImportRecord] = []
        if bin_obj.format == lief.EXE_FORMATS.PE:
            for dll in bin_obj.imports:
                for entry in dll.entries:
                    imports.append(
                        ImportRecord(
                            lib=dll.name,
                            symbol=entry.name or f"ordinal_{entry.ordinal}",
                            iat_addr=entry.iat_address if entry.iat_address != 0 else None,
                            bind="UNSPECIFIED",
                        )
                    )
        elif bin_obj.format == lief.EXE_FORMATS.ELF:
            for sym in bin_obj.imported_functions:
                imports.append(
                    ImportRecord(
                        lib=sym.library or "UNKNOWN",
                        symbol=sym.name,
                        iat_addr=None,
                        bind="WEAK" if sym.binding == lief.ELF.SYMBOL_BINDINGS.WEAK else "GLOBAL",
                    )
                )
        else:
            raise NotImplementedError(f"Unsupported binary format: {bin_obj.format}")

        fmt = "PE" if bin_obj.format == lief.EXE_FORMATS.PE else "ELF"
        j = self._normalise_output(binary, imports, format_=fmt)
        return j

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _sha256(path: Path, chunk: int = 65536) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            while (blk := f.read(chunk)):
                h.update(blk)
        return h.hexdigest()

    def _normalise_output(self, binary: Path, imports: List[ImportRecord], *, format_: str) -> Dict[str, Any]:
        imports.sort(key=lambda r: (r.lib.lower(), r.symbol.lower()))
        return {
            "binary_sha256": self._sha256(binary),
            "format": format_.upper(),
            "imports": [rec.to_json() for rec in imports],
        }

    # ------------------------------------------------------------------
    # Backend selection logic
    # ------------------------------------------------------------------

    @staticmethod
    def _resolve_backend(backend: Literal["angr", "lief", "auto"]) -> Literal["angr", "lief"]:
        if backend == "auto":
            if angr is not None:
                return "angr"
            if lief is not None:
                return "lief"
            raise RuntimeError("Neither angr nor lief backends are available")
        if backend == "angr":
            if angr is None:
                raise RuntimeError("Backend 'angr' requested but angr not installed")
            return "angr"
        if backend == "lief":
            if lief is None:
                raise RuntimeError("Backend 'lief' requested but lief not installed")
            return "lief"
        raise ValueError(f"Unknown backend: {backend}")


# ---------------------------------------------------------------------------
# Convenience function for single‑shot extraction (bypasses ExtractorBase.run)
# ---------------------------------------------------------------------------

def extract_imports(
    binary_path: str | os.PathLike[str],
    *,
    out_dir: str | Path | None = None,
    timeout: int | None = 120,
    backend: Literal["angr", "lief", "auto"] = "auto",
    overwrite: bool = False,
) -> Path:
    """Helper for scripts / CLI wrappers"""

    extractor = ImportExtractor(timeout=timeout, backend=backend)
    return extractor.run(binary_path, out_dir, overwrite=overwrite)


# ---------------------------------------------------------------------------
# CLI entry point (python -m ...)
# ---------------------------------------------------------------------------

if __name__ == "__main__":  # pragma: no cover – manual usage only
    import argparse

    parser = argparse.ArgumentParser(description="Extract import table from PE/ELF binary")
    parser.add_argument("binary", type=Path)
    parser.add_argument("--out", type=Path, default=None, help="Output directory (defaults to alongside binary)")
    parser.add_argument("--backend", choices=["auto", "angr", "lief"], default="auto")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    out_path = extract_imports(
        args.binary,
        out_dir=args.out,
        backend=args.backend,  # type: ignore[arg-type]
        timeout=args.timeout,
        overwrite=args.overwrite,
    )
    print(f"[+] Import JSON written to {out_path}")
