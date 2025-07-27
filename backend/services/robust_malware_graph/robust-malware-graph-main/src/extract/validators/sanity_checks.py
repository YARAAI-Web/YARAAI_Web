"""
src.extract.validators.sanity_checks
====================================

Domain-specific *sanity* rules that go beyond the structural validation
handled in `schema.validate_view`.

Usage
-----

>>> from src.extract.validators.sanity_checks import sanity_check
>>> sanity_check("cfg", cfg_json_dict)       # 예외 없으면 통과
>>> sanity_check("ast", ast_json, strict=False)   # 경고 리스트 반환
"""
from __future__ import annotations

import itertools
from collections import Counter, defaultdict
from typing import Any, List, Sequence

from .schema import (
    ASTView,
    CFGEdge,
    CFGNode,
    CFGView,
    FCGEdge,
    FCGNode,
    FCGView,
    ImportView,
    SysCallItem,
    SysCallView,
    ViewName,
    validate_view,
)


# --------------------------------------------------------------------------- #
# 1. 공통 예외 & helper
# --------------------------------------------------------------------------- #
class SanityError(RuntimeError):
    """Raised when a fatal sanity check fails."""


class WarningList(List[str]):
    """Light wrapper so call-site can distinguish warnings vs. errors."""


def _raise_or_collect(
    condition: bool,
    msg: str,
    *,
    strict: bool,
    warnings: WarningList,
) -> None:
    if condition:
        return
    if strict:
        raise SanityError(msg)
    warnings.append(msg)


# --------------------------------------------------------------------------- #
# 2-A. AST sanity rules
# --------------------------------------------------------------------------- #
def _check_ast(view: ASTView, *, strict: bool, warn: WarningList) -> None:
    # 1. exactly one root (parent == None)
    roots = [n for n in view.nodes if n.parent is None]
    _raise_or_collect(
        len(roots) == 1,
        f"AST: expected exactly 1 root, found {len(roots)}",
        strict=strict,
        warnings=warn,
    )

    # 2. no orphaned parent reference / acyclic
    parent_map = {n.id: n.parent for n in view.nodes if n.parent is not None}
    node_ids = {n.id for n in view.nodes}
    for child_id, parent_id in parent_map.items():
        _raise_or_collect(
            parent_id in node_ids,
            f"AST: node {child_id} refers to missing parent {parent_id}",
            strict=strict,
            warnings=warn,
        )

    # 3. cycle detection (simple tortoise-hare)
    def _has_cycle() -> bool:
        for nid in node_ids:
            tortoise, hare = nid, nid
            while True:
                tortoise = parent_map.get(tortoise)
                hare = parent_map.get(parent_map.get(hare))
                if tortoise is None or hare is None:
                    break
                if tortoise == hare:
                    return True
        return False

    _raise_or_collect(
        not _has_cycle(),
        "AST: parent pointers contain a cycle",
        strict=strict,
        warnings=warn,
    )


# --------------------------------------------------------------------------- #
# 2-B. CFG sanity rules
# --------------------------------------------------------------------------- #
def _check_cfg(view: CFGView, *, strict: bool, warn: WarningList) -> None:
    # helper sets
    node_id_set = {n.id for n in view.nodes}
    edge_pairs = {(e.src, e.dst) for e in view.edges}

    # 1. duplicate edges?
    if len(edge_pairs) < len(view.edges):
        dups = len(view.edges) - len(edge_pairs)
        _raise_or_collect(
            False,
            f"CFG: {dups} duplicated edge(s) detected",
            strict=strict,
            warnings=warn,
        )

    # 2. node addr monotonic ascending?  (heuristic entry = min(addr))
    addrs = [n.addr for n in view.nodes]
    _raise_or_collect(
        all(a >= 0 for a in addrs),
        "CFG: negative address detected",
        strict=strict,
        warnings=warn,
    )

    # 3. node size positive
    bad_sizes = [n.id for n in view.nodes if n.size <= 0]
    _raise_or_collect(
        not bad_sizes,
        f"CFG: non-positive size at node(s) {bad_sizes}",
        strict=strict,
        warnings=warn,
    )

    # 4. connectivity: every node should be reachable from entry (min addr)
    if view.nodes:
        entry = min(view.nodes, key=lambda n: n.addr).id
        out_edges = defaultdict(list)
        for e in view.edges:
            out_edges[e.src].append(e.dst)

        reachable = set()
        stack = [entry]
        while stack:
            cur = stack.pop()
            if cur in reachable:
                continue
            reachable.add(cur)
            stack.extend(out_edges.get(cur, []))

        unreachable = node_id_set - reachable
        _raise_or_collect(
            not unreachable,
            f"CFG: unreachable basic-block(s) {sorted(unreachable)}",
            strict=strict,
            warnings=warn,
        )


# --------------------------------------------------------------------------- #
# 2-C. FCG sanity rules
# --------------------------------------------------------------------------- #
def _check_fcg(view: FCGView, *, strict: bool, warn: WarningList) -> None:
    # 1. duplicate function names (excluding overloading ambiguity)
    name_counts = Counter(n.name for n in view.nodes)
    dups = [name for name, cnt in name_counts.items() if cnt > 1]
    _raise_or_collect(
        not dups,
        f"FCG: duplicate function name(s) {dups}",
        strict=strict,
        warnings=warn,
    )

    # 2. lib-funcs should have no outgoing edges pointing to non-lib callee
    lib_nodes = {n.id for n in view.nodes if n.is_lib}
    for e in view.edges:
        if e.caller in lib_nodes and e.callee not in lib_nodes:
            _raise_or_collect(
                False,
                f"FCG: library function {e.caller} calls non-lib {e.callee}",
                strict=strict,
                warnings=warn,
            )


# --------------------------------------------------------------------------- #
# 2-D. SysCall sanity rules
# --------------------------------------------------------------------------- #
# (opt) minimal whitelist - could be expanded
_ALLOWED_SYSCALLS = {
    "open",
    "read",
    "write",
    "close",
    "execve",
    "mmap",
    "socket",
    "connect",
    "send",
    "recv",
}


def _check_syscall(view: SysCallView, *, strict: bool, warn: WarningList) -> None:
    # 1. duplicate idx impossible, already checked; here we ensure *continuous*
    idxs = [c.idx for c in view.calls]
    missing = set(range(len(idxs))) - set(idxs)
    _raise_or_collect(
        not missing,
        f"SysCall: missing indices {sorted(missing)}",
        strict=strict,
        warnings=warn,
    )

    # 2. unknown syscall names
    unknown = [c.name for c in view.calls if c.name not in _ALLOWED_SYSCALLS]
    if unknown:
        warn_msg = f"SysCall: {len(unknown)} unknown syscall(s): {unknown[:5]}"
        _raise_or_collect(True, warn_msg, strict=strict, warnings=warn)  # warning only


# --------------------------------------------------------------------------- #
# 2-E. Import sanity rules
# --------------------------------------------------------------------------- #
def _check_imports(view: ImportView, *, strict: bool, warn: WarningList) -> None:
    # 1. empty dll?
    empties = [dll for dll, funcs in view.__root__.items() if not funcs]
    _raise_or_collect(
        not empties,
        f"imports.json: {len(empties)} DLL(s) have empty import lists → {empties}",
        strict=strict,
        warnings=warn,
    )

    # 2. dll name casing heuristic (should contain '.dll' or be uppercase)
    bad_case = [
        dll for dll in view.__root__.keys()
        if not (dll.endswith(".dll") or dll.isupper())
    ]
    if bad_case:
        warn_msg = f"imports.json: suspicious DLL casing {bad_case}"
        _raise_or_collect(True, warn_msg, strict=strict, warnings=warn)  # warning only


# --------------------------------------------------------------------------- #
# 3. Registry + entrypoint
# --------------------------------------------------------------------------- #
_CHECK_REGISTRY = {
    ViewName.ast: _check_ast,
    ViewName.cfg: _check_cfg,
    ViewName.fcg: _check_fcg,
    ViewName.syscall: _check_syscall,
    ViewName.imports: _check_imports,
}


def sanity_check(
    view: str | ViewName,
    data: Any,
    *,
    strict: bool = True,
) -> None | WarningList:
    """
    Run *sanity* validation for one extractor view.

    Parameters
    ----------
    view : {"ast","cfg","fcg","syscall","imports"}
        View name.
    data : Any
        Parsed JSON/dict (raw).  Structural validation is run first.
    strict : bool, default True
        • True  → raise SanityError on the *first* fatal issue.
        • False → collect all violations as warnings and return them.

    Returns
    -------
    None | List[str]
        None if everything is fine.  Otherwise, in non-strict mode, a
        `WarningList` of human-readable messages is returned.

    Raises
    ------
    SanityError
        When *strict* is True and a fatal violation is found.
    """
    model = validate_view(view, data)  # structural validity
    checker = _CHECK_REGISTRY[ViewName(view)]
    warnings: WarningList = WarningList()
    checker(model, strict=strict, warn=warnings)
    return None if strict or not warnings else warnings


__all__ = [
    "sanity_check",
    "SanityError",
]
