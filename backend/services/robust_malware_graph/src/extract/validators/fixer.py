"""
src.extract.validators.fixer
============================

Heuristic *auto-fixer* for extractor views (AST / CFG / …).

>>> from src.extract.validators.fixer import fix_view
>>> fixed, report = fix_view("cfg", cfg_json_dict)
>>> print(report.pretty())
-------------------- Fix-Report --------------------
view       : cfg
status     : fixed (7 patch(es))
patches
  1. + removed 2 duplicated edge(s)
  2. + normalized negative addr → abs(...)
  3. + clamped size<=0 to 1  (3 node(s))
  4. + pruned 5 unreachable basic-block(s)
---------------------------------------------------
"""
from __future__ import annotations

import itertools
from collections import defaultdict
from typing import Any, Callable, Dict, List, Tuple

from pydantic import BaseModel, ValidationError

from .schema import (
    ASTNode,
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
from .sanity_checks import sanity_check, SanityError, WarningList

# --------------------------------------------------------------------------- #
# 1. Fix-report util
# --------------------------------------------------------------------------- #
class FixReport:
    __slots__ = ("view", "patches", "status")

    def __init__(self, view: str):
        self.view = view
        self.patches: List[str] = []
        self.status: str = "unchanged"

    def add(self, msg: str) -> None:
        self.patches.append(f"+ {msg}")
        self.status = "fixed"

    # pretty-printer
    def pretty(self) -> str:
        bar = "-" * 52
        body = "\n".join(self.patches) or "(no change)"
        return (
            f"{bar}\n"
            f"view       : {self.view}\n"
            f"status     : {self.status}\n"
            f"patches\n  {body}\n"
            f"{bar}"
        )

    # representation inside notebook / REPL
    def __repr__(self) -> str:
        return self.pretty()


# --------------------------------------------------------------------------- #
# 2-A. AST fixer
# --------------------------------------------------------------------------- #
def _fix_ast(model: ASTView, rpt: FixReport) -> ASTView:
    # 1. unique id – rename duplicates
    ids = [n.id for n in model.nodes]
    dup_map: Dict[int, List[int]] = {}
    for idx, nid in enumerate(ids):
        dup_map.setdefault(nid, []).append(idx)
    next_id = max(ids) + 1 if ids else 0
    for dup_idxs in dup_map.values():
        if len(dup_idxs) > 1:
            for i in dup_idxs[1:]:
                model.nodes[i].id = next_id
                rpt.add(f"renamed duplicated node id {ids[i]} → {next_id}")
                next_id += 1

    # 2. ensure exactly one root
    roots = [n for n in model.nodes if n.parent is None]
    if len(roots) == 0:
        # pick node with smallest id as root
        cand = min(model.nodes, key=lambda n: n.id)
        cand.parent = None
        rpt.add(f"no root detected → set node {cand.id} as root")
    elif len(roots) > 1:
        keeper = roots[0]
        for extra in roots[1:]:
            extra.parent = keeper.id
        rpt.add(f"{len(roots)-1} extra root(s) re-parented to {keeper.id}")

    # 3. remove parent refs to nonexistent ids
    valid_ids = {n.id for n in model.nodes}
    for n in model.nodes:
        if n.parent is not None and n.parent not in valid_ids:
            rpt.add(f"node {n.id} parent {n.parent} missing → unset")
            n.parent = None

    # 4. break simple cycles (tortoise-hare) by detaching offender
    parent = {n.id: n.parent for n in model.nodes if n.parent is not None}

    def _cycle_nodes() -> List[int]:
        cyc = []
        for nid in parent:
            tort, hare = nid, nid
            while True:
                tort = parent.get(tort)
                hare = parent.get(parent.get(hare))
                if tort is None or hare is None:
                    break
                if tort == hare:
                    cyc.append(nid)
                    break
        return cyc

    cyc_nodes = _cycle_nodes()
    for nid in cyc_nodes:
        node = next(n for n in model.nodes if n.id == nid)
        node.parent = None
        rpt.add(f"cycle detected – detached node {nid}")

    return model


# --------------------------------------------------------------------------- #
# 2-B. CFG fixer
# --------------------------------------------------------------------------- #
def _fix_cfg(model: CFGView, rpt: FixReport) -> CFGView:
    # 1. deduplicate edges
    before = len(model.edges)
    uniq_edges = {(e.src, e.dst, e.kind) for e in model.edges}
    if len(uniq_edges) < before:
        rpt.add(f"removed {before - len(uniq_edges)} duplicated edge(s)")
    model.edges = [CFGEdge(src=s, dst=d, kind=k) for s, d, k in uniq_edges]

    # 2. normalize addr ≥ 0
    neg = [n.id for n in model.nodes if n.addr < 0]
    if neg:
        for n in model.nodes:
            if n.addr < 0:
                n.addr = abs(n.addr)
        rpt.add(f"normalized negative addr → abs(...)")

    # 3. enforce size > 0
    bad = [n.id for n in model.nodes if n.size <= 0]
    if bad:
        for n in model.nodes:
            if n.size <= 0:
                n.size = 1
        rpt.add(f"clamped size<=0 to 1  ({len(bad)} node(s))")

    # 4. prune unreachable blocks
    if model.nodes:
        entry = min(model.nodes, key=lambda n: n.addr).id
        out_edges = defaultdict(list)
        for e in model.edges:
            out_edges[e.src].append(e.dst)
        reachable = set()
        stack = [entry]
        while stack:
            cur = stack.pop()
            if cur in reachable:
                continue
            reachable.add(cur)
            stack.extend(out_edges.get(cur, []))
        unreachable = {n.id for n in model.nodes} - reachable
        if unreachable:
            model.nodes = [n for n in model.nodes if n.id in reachable]
            model.edges = [e for e in model.edges if e.src in reachable and e.dst in reachable]
            rpt.add(f"pruned {len(unreachable)} unreachable basic-block(s)")
    return model


# --------------------------------------------------------------------------- #
# 2-C. FCG fixer
# --------------------------------------------------------------------------- #
def _fix_fcg(model: FCGView, rpt: FixReport) -> FCGView:
    # 1. rename duplicate function names
    name_count = defaultdict(int)
    for n in model.nodes:
        cnt = name_count[n.name]
        if cnt:
            new_name = f"{n.name}#{cnt}"
            rpt.add(f"duplicate func name '{n.name}' → '{new_name}'")
            n.name = new_name
        name_count[n.name] += 1

    # 2. lib caller → mark callee lib as well (heuristic)
    lib_set = {n.id for n in model.nodes if n.is_lib}
    id2node = {n.id: n for n in model.nodes}
    fix = 0
    for e in model.edges:
        if e.caller in lib_set and e.callee not in lib_set:
            id2node[e.callee].is_lib = True
            lib_set.add(e.callee)
            fix += 1
    if fix:
        rpt.add(f"propagated lib flag to {fix} callee(s)")
    return model


# --------------------------------------------------------------------------- #
# 2-D. SysCall fixer
# --------------------------------------------------------------------------- #
def _fix_syscall(model: SysCallView, rpt: FixReport) -> SysCallView:
    # 1. re-index sequentially
    for i, call in enumerate(model.calls):
        if call.idx != i:
            rpt.add("re-indexed syscall sequence")
            for j, c in enumerate(model.calls):
                c.idx = j
            break
    return model


# --------------------------------------------------------------------------- #
# 2-E. Import fixer
# --------------------------------------------------------------------------- #
def _fix_imports(model: ImportView, rpt: FixReport) -> ImportView:
    # remove empty DLL entries
    empties = [dll for dll, funcs in model.__root__.items() if not funcs]
    if empties:
        for dll in empties:
            del model.__root__[dll]
        rpt.add(f"removed {len(empties)} empty DLL import(s)")
    return model


# view → fixer registry
_FIX_REGISTRY: Dict[ViewName, Callable[[BaseModel, FixReport], BaseModel]] = {
    ViewName.ast: _fix_ast,
    ViewName.cfg: _fix_cfg,
    ViewName.fcg: _fix_fcg,
    ViewName.syscall: _fix_syscall,
    ViewName.imports: _fix_imports,
}


# --------------------------------------------------------------------------- #
# 3. Public entrypoint
# --------------------------------------------------------------------------- #
def fix_view(
    view: str | ViewName,
    data: Any,
    *,
    max_iter: int = 3,
) -> Tuple[Dict[str, Any], FixReport]:
    """
    Attempt to *auto-fix* structural + sanity issues.

    Parameters
    ----------
    view : {"ast","cfg","fcg","syscall","imports"}
    data : Any
        Raw dict (typically `json.load` result).
    max_iter : int, default 3
        Re-apply fixer until `sanity_check` passes or iteration limit.

    Returns
    -------
    fixed_data : dict
        Heuristically repaired JSON (guaranteed to pass sanity_check).
    report : FixReport
        Human-readable patch summary.

    Raises
    ------
    RuntimeError
        If unable to fix within *max_iter* iterations.
    """
    vname = ViewName(view)
    rpt = FixReport(vname)
    attempt = 0
    model = validate_view(vname, data)  # may raise ValidationError
    fixer = _FIX_REGISTRY[vname]

    while attempt < max_iter:
        try:
            # sanity OK? – we're done
            sanity_check(vname, model.dict(), strict=True)
            return model.dict(), rpt
        except SanityError:
            # perform one round of fixes
            model = fixer(model, rpt)
            attempt += 1

    raise RuntimeError(f"[fixer] unable to auto-fix view '{view}' after {max_iter} iteration(s)")


__all__ = ["fix_view", "FixReport"]
