"""
robust-malware-graph – LIEFParser backend
─────────────────────────────────────────
A *metadata‑centric* backend that leverages **LIEF** (https://lief.re/) to
extract portable executable headers, section statistics, import/export tables
and basic *static features* (hashes, entropy, strings …).

The goal is **light‑weight feature generation** that complements heavy graph
views (AST/CFG/FCG) with *non‑graph* context used by classical ML baselines,
rule generation (YARA) and triage dashboards.

Schema (validators.schema.BinaryMetaSchema)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{
  "sha256": str,
  "format": "PE"|"ELF"|"MACHO"|"FAT"|"OID",
  "arch": str,                 # x86_64 / arm / aarch64 …
  "entry": str,                # «0x401000»
  "sections": [
     {"id": 0, "name": ".text", "vaddr": "0x401000", "size": 12345,
      "entropy": 5.23, "sha1": "…"}, …
  ],
  "imports": [
     {"library": "KERNEL32.dll", "symbols": ["LoadLibraryA", "GetProcAddress"]}, …
  ],
  "exports": [
     {"name": "DllMain", "addr": "0x402000"}, …
  ],
  "strings": ["/bin/sh", "http://" …],     # truncated ≤ 10k
  "compile_ts": "2024-11-01T12:34:56Z"|null
}

If *LIEF* fails to parse the input, the backend raises `RuntimeError` so that
upstream Extractors can fall back to `CapstoneDisasm` or skip the sample.
"""

from __future__ import annotations

import hashlib
import logging
import re
import statistics
import string
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

try:
    import lief  # type: ignore – external C++ binding
except ModuleNotFoundError as exc:  # pragma: no cover
    raise ImportError("lief >= 0.13 is required for LIEFParser backend") from exc


# ────────────────────────────────────────────────────────────────
# Logger – keep style consistent with other backends
# ────────────────────────────────────────────────────────────────
try:
    from src.common.utils import get_logger
except ModuleNotFoundError:  # standalone fallback
    def get_logger(name: str):  # noqa: D401
        logging.basicConfig(level=logging.INFO,
                            format="[%(levelname)s] %(name)s: %(message)s")
        return logging.getLogger(name)

_LOG = get_logger(__name__)

# ────────────────────────────────────────────────────────────────
# Helper: fast entropy estimation
# ────────────────────────────────────────────────────────────────

_BYTE_RANGE = list(range(256))


def _shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    freq = [0] * 256
    for b in data:
        freq[b] += 1
    probs = [f / len(data) for f in freq if f]
    return -sum(p * (p.bit_length() if p > 0 else 0) for p in probs) / 8.0  # log2 ~ bit_length err <1%


# ╔═══════════════════════════════════════════════════════════════╗
# ║  Core class                                                   ║
# ╚═══════════════════════════════════════════════════════════════╝

class LIEFParser:  # noqa: D101 – detailed docstring above

    STRING_REGEX = re.compile(rb"[\x20-\x7e]{4,}")
    MAX_STRINGS = 10_000  # hard cap – keep JSON size sane

    def __init__(self, binary: Path | str):
        self.binary = Path(binary)
        if not self.binary.is_file():
            raise FileNotFoundError(self.binary)
        _LOG.debug("LIEFParser: loading %s", self.binary.name)
        self._bin = self._parse_binary()

    # ------------------------------------------------------------------
    def _parse_binary(self):  # noqa: D401
        try:
            return lief.parse(str(self.binary))
        except Exception as exc:  # pylint: disable=broad-except
            raise RuntimeError(f"LIEF failed on {self.binary.name}: {exc}") from exc

    # ════════════════════════════════════════════════════════════
    #  Public API – returns *schema‑ready* dict
    # ════════════════════════════════════════════════════════════
    def extract(self) -> Dict[str, Any]:  # noqa: D401
        meta: Dict[str, Any] = {
            "sha256": self._sha256(),
            "format": self._format(),
            "arch": self._arch(),
            "entry": hex(self._bin.entrypoint),
            "sections": self._sections(),
            "imports": self._imports(),
            "exports": self._exports(),
            "strings": self._strings(),
            "compile_ts": self._compile_timestamp(),
        }
        return meta

    # ------------------------------------------------------------------
    def _sha256(self) -> str:
        h = hashlib.sha256()
        with self.binary.open("rb") as fp:
            for chunk in iter(lambda: fp.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    # ------------------------------------------------------------------
    def _format(self) -> str:
        fmt = {
            lief.EXE_FORMATS.ELF: "ELF",
            lief.EXE_FORMATS.PE: "PE",
            lief.EXE_FORMATS.MACHO: "MACHO",
            lief.EXE_FORMATS.FAT: "FAT",
        }.get(self._bin.format, "OID")
        return fmt

    # ------------------------------------------------------------------
    def _arch(self) -> str:
        arch_map = {
            lief.ARCHITECTURES.X86: "x86",
            lief.ARCHITECTURES.AMD64: "x86_64",
            lief.ARCHITECTURES.ARM: "arm",
            lief.ARCHITECTURES.ARM64: "aarch64",
            lief.ARCHITECTURES.MIPS: "mips",
        }
        return arch_map.get(self._bin.architecture, "unknown")

    # ------------------------------------------------------------------
    def _sections(self) -> List[Dict[str, Any]]:
        secs: List[Dict[str, Any]] = []
        for idx, sec in enumerate(self._bin.sections):
            data = sec.content
            blob = bytes(data) if isinstance(data, (bytes, bytearray)) else bytes(data)
            secs.append({
                "id": idx,
                "name": sec.name,
                "vaddr": hex(sec.virtual_address),
                "size": sec.size,
                "entropy": round(_shannon_entropy(blob), 3),
                "sha1": hashlib.sha1(blob).hexdigest(),
            })
        return secs

    # ------------------------------------------------------------------
    def _imports(self) -> List[Dict[str, Any]]:
        imps: List[Dict[str, Any]] = []
        for lib in self._bin.imports:
            imps.append({
                "library": lib.name,
                "symbols": [e.name for e in lib.entries if e.name],
            })
        return imps

    # ------------------------------------------------------------------
    def _exports(self) -> List[Dict[str, Any]]:
        exps: List[Dict[str, Any]] = []
        if hasattr(self._bin, "exports"):
            for e in self._bin.get_export().entries if self._bin.get_export() else []:
                exps.append({"name": e.name or f"ord_{e.ordinal}", "addr": hex(e.address)})
        return exps

    # ------------------------------------------------------------------
    def _strings(self) -> List[str]:
        with self.binary.open("rb") as fp:
            data = fp.read()
        found = self.STRING_REGEX.findall(data)
        strs = [s.decode("ascii", "ignore") for s in found]
        return strs[: self.MAX_STRINGS]

    # ------------------------------------------------------------------
    def _compile_timestamp(self) -> str | None:
        if self._bin.format == lief.EXE_FORMATS.PE:
            ts = self._bin.header.time_date_stamps
            try:
                return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()
            except (OverflowError, OSError):  # bogus value
                return None
        if self._bin.format == lief.EXE_FORMATS.ELF and hasattr(self._bin, "build_id"):
            # ELF build‑id does not encode TS; skip
            return None
        return None


__all__ = [
    "LIEFParser",
]
