from __future__ import annotations

"""view_registry.py
====================

Central *registry* that maps **view identifiers** (``"ast"``, ``"cfg"``, …)
used across the data‑collection pipeline to their concrete *Extractor* classes.
The indirection keeps orchestration code agnostic of heavy dependencies
(``angr``, ``lief``, …) by *lazy‑loading* each extractor only when it is first
requested.

Example
-------
>>> from src.extract.view_registry import get_extractor
>>> CFGExtractor = get_extractor("cfg")
>>> output_path = CFGExtractor(root_dir="/tmp/out").extract("sample.exe")

The call returns an **un‑instantiated class** so that callers can pass custom
init kwargs.

Design goals
------------
* **Lazy import**  – avoid importing heavyweight analysis back‑ends unless the
  view is actually needed.
* **Extensibility** – external plugins / research prototypes can register new
  views at runtime via :pyfunc:`register_view`.
* **Thread‑safety** – registration and look‑ups are protected by a standard
  `threading.Lock`.

Public API
~~~~~~~~~~
* :pyfunc:`get_extractor(id)`   → `type[BaseExtractor]`
* :pyfunc:`register_view(id, cls | (module_path, class_name))`
* :pyfunc:`list_views()`        → `list[str]`

If you need to override / alias an existing id, simply call
``register_view(id, NewExtractor, force=True)``.
"""

from importlib import import_module
from threading import Lock
from types import ModuleType
from typing import Any, Dict, List, Mapping, MutableMapping, Sequence, Tuple, Type, Union, overload

# --------------------------------------------------------------------------- #
# Type helpers
# --------------------------------------------------------------------------- #
ExtractorRef = Union[
    "type[BaseExtractor]",                 # direct class object
    Tuple[str, str],                        # ("pkg.module", "ClassName")
]

try:
    from src.extract.base import BaseExtractor  # local import for typing only
except Exception:  # pragma: no cover – circular during bootstrap
    class BaseExtractor:  # type: ignore  # noqa: D101
        pass

# --------------------------------------------------------------------------- #
# Internal state
# --------------------------------------------------------------------------- #
_LOCK = Lock()
_REGISTRY: MutableMapping[str, ExtractorRef] = {
    "ast": ("src.extract.extractors.ast_extractor", "ASTExtractor"),
    "cfg": ("src.extract.extractors.cfg_extractor", "CFGExtractor"),
    "fcg": ("src.extract.extractors.fcg_extractor", "FCGExtractor"),
    "imports": ("src.extract.extractors.import_extractor", "ImportExtractor"),
    "syscall": ("src.extract.extractors.syscall_extractor", "SysCallExtractor"),
}
_CACHE: Dict[str, Type[BaseExtractor]] = {}

# --------------------------------------------------------------------------- #
# Exceptions
# --------------------------------------------------------------------------- #
class ViewRegistrationError(RuntimeError):
    """Raised when registration fails due to duplicate ids or bad targets."""

# --------------------------------------------------------------------------- #
# Public API
# --------------------------------------------------------------------------- #

def list_views() -> List[str]:
    """Return all currently registered view identifiers (sorted)."""
    with _LOCK:
        return sorted(_REGISTRY)


def get_extractor(view_id: str) -> Type[BaseExtractor]:
    """Return the *Extractor class* associated with *view_id*.

    Parameters
    ----------
    view_id : str
        Key such as ``"ast"`` or ``"cfg"``.

    Raises
    ------
    KeyError
        If the id is unknown.
    ViewRegistrationError
        If the referenced class cannot be imported / located.
    """
    with _LOCK:
        if view_id in _CACHE:
            return _CACHE[view_id]
        if view_id not in _REGISTRY:
            raise KeyError(f"Unknown view id: {view_id!r}")
        target = _REGISTRY[view_id]

    # Resolve lazy reference outside the lock – heavy import may take time.
    if isinstance(target, tuple):
        module_path, cls_name = target
        try:
            module: ModuleType = import_module(module_path)
            extractor_cls: Type[BaseExtractor] = getattr(module, cls_name)  # type: ignore[arg-type]
        except Exception as exc:  # pragma: no cover
            raise ViewRegistrationError(
                f"Failed to import extractor for view '{view_id}': {module_path}.{cls_name}") from exc
    else:
        extractor_cls = target  # type: ignore[assignment]

    with _LOCK:
        _CACHE[view_id] = extractor_cls
    return extractor_cls


def register_view(
    view_id: str,
    extractor: ExtractorRef,
    *,
    force: bool = False,
) -> None:
    """Register / override a view‐id → Extractor mapping.

    Parameters
    ----------
    view_id : str
        Identifier such as ``"cfg"``.
    extractor : ExtractorRef
        Either the *class* itself or a tuple ``("module.path", "ClassName")``.
    force : bool, default ``False``
        If *False*, attempting to overwrite an existing id raises
        :class:`ViewRegistrationError`.
    """
    if not isinstance(view_id, str):
        raise TypeError("view_id must be a string")
    if not (callable(extractor) or (
        isinstance(extractor, tuple) and len(extractor) == 2 and all(isinstance(s, str) for s in extractor)
    )):
        raise TypeError("extractor must be a class or ('module', 'ClassName') tuple")

    with _LOCK:
        if view_id in _REGISTRY:
            if not force and _REGISTRY[view_id] != extractor:
                raise ViewRegistrationError(
                    f"View id '{view_id}' already registered – use force=True to override."
                )
            if _REGISTRY.get(view_id) == extractor:
                return  # idempotent re-registration
        _REGISTRY[view_id] = extractor
        _CACHE.pop(view_id, None)  # force lazy re-import on next get
