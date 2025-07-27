"""
robust-malware-graph – backends package
──────────────────────────────────────
Unifies every *low‑level* analysis engine behind a single import so that
higher‑level Extractors (AST / CFG / FCG / SysCall / BinaryMeta) can pick the
best‑suited backend at runtime without worrying about optional dependencies.

Available backends (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| key        | class              | weight | deps                 |
|------------|--------------------|--------|----------------------|
| ``angr``   | :class:`AngrEngine`| heavy  | angr                 |
| ``ghidra`` | :class:`GhidraBridge` | heavy  | ghidra_bridge + GHIDRA |
| ``r2``     | :class:`Radare2Bridge` | mid    | radare2, r2pipe      |
| ``capstone``| :class:`CapstoneDisasm` | light  | capstone             |
| ``lief``   | :class:`LIEFParser`| light  | lief                 |

Each backend *may* fail to import if its dependency stack is missing.  This
init file catches those ``ImportError``s and only exposes the backends that
loaded successfully via :data:`AVAILABLE`.

Helper functions
----------------
``get_backend(key)``
    Return backend class by key or raise ``KeyError``.

``best_available(order)``
    Iterate through *order* and return the first backend key that is
    available.  Default priority favours *heavy → light* so that high‑fidelity
    analysis is attempted first.
"""

from __future__ import annotations

import importlib
import logging
from typing import Any, Dict, Mapping, Sequence, Type

try:
    from src.common.utils import get_logger
except ModuleNotFoundError:
    import logging as _logging  # noqa: WPS433

    def get_logger(name: str) -> logging.Logger:  # noqa: D401
        _logging.basicConfig(level=_logging.INFO,
                             format="[%(levelname)s] %(name)s: %(message)s")
        return _logging.getLogger(name)

_LOG = get_logger(__name__)

# ────────────────────────────────────────────────────────────────
# Internal registry builder
# ────────────────────────────────────────────────────────────────

_BackendSpec = tuple[str, str]  # (import_path, class_name)

_SPECS: Mapping[str, _BackendSpec] = {
    "angr":    (".angr_engine", "AngrEngine"),
    "ghidra":  (".ghidra_bridge", "GhidraBridge"),
    "r2":      (".radare2_bridge", "Radare2Bridge"),
    "capstone": (".capstone_disasm", "CapstoneDisasm"),
    "lief":    (".lief_parser", "LIEFParser"),
}

AVAILABLE: Dict[str, Type[Any]] = {}

for _key, (_mrel, _cls) in _SPECS.items():
    try:
        _mod = importlib.import_module(_mrel, package=__name__)
        _cls_obj = getattr(_mod, _cls)
        AVAILABLE[_key] = _cls_obj  # type: ignore[assignment]
        _LOG.debug("backend '%s' loaded (module=%s)", _key, _mrel)
    except ImportError as err:
        _LOG.warning("backend '%s' unavailable: %s", _key, err.args[0])
    except Exception as err:  # pylint: disable=broad-except
        _LOG.error("backend '%s' failed to initialise: %s", _key, err)


def get_backend(key: str):  # noqa: D401, ANN001
    """Return backend *class* by registry key.

    Example
    -------
    >>> BE = get_backend("angr")
    >>> be = BE(Path("/bin/ls"))
    """
    try:
        return AVAILABLE[key]
    except KeyError as exc:  # pragma: no cover
        raise KeyError(f"backend '{key}' not available (have: {list(AVAILABLE)})") from exc


def best_available(order: Sequence[str] | None = None) -> str:  # noqa: D401
    """Pick first key in *order* that exists in :data:`AVAILABLE`."""
    if order is None:
        order = ("ghidra", "angr", "r2", "capstone")  # lief is *meta* only
    for key in order:
        if key in AVAILABLE:
            return key
    raise RuntimeError("no usable backend found – install at least one heavy/light engine")


__all__ = [
    "AVAILABLE",
    "get_backend",
    "best_available",
] + [cls.__name__ for cls in AVAILABLE.values()]
