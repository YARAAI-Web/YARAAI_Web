"""
src.extract.validators.schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pydantic-based schema definitions + runtime validator for every
view produced by the extractor layer (AST / CFG / FCG / SysCall / Import).

>>> from src.extract.validators.schema import validate_view
>>> validate_view("cfg", json.loads(open("cfg.json").read()))
"""
from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Type

from pydantic import BaseModel, Field, root_validator, validator


# --------------------------------------------------------------------------- #
# 1. Common helpers
# --------------------------------------------------------------------------- #
class ViewName(str, Enum):
    ast = "ast"
    cfg = "cfg"
    fcg = "fcg"
    syscall = "syscall"
    imports = "imports"


class _BaseViewModel(BaseModel):
    """Shared pydantic config: forbid extras & enable orm."""
    class Config:
        extra = "forbid"
        orm_mode = True


# --------------------------------------------------------------------------- #
# 2. AST – function/statement abstract-syntax tree
# --------------------------------------------------------------------------- #
class ASTNode(_BaseViewModel):
    id: int
    type: str
    tokens: List[str] = Field(default_factory=list)
    parent: Optional[int] = None  # root → None

class ASTMetadata(_BaseViewModel):
    sha256: str
    backend: str
    num_nodes: int
    build_time: Optional[str] = None


class ASTView(_BaseViewModel):
    metadata: ASTMetadata
    nodes: List[ASTNode]

    # --- sanity helpers ---------------------------------------------------- #
    @validator("nodes")
    def _unique_ids(cls, nodes):
        ids = [n.id for n in nodes]
        if len(ids) != len(set(ids)):
            raise ValueError("AST: duplicated node id detected")
        return nodes


# --------------------------------------------------------------------------- #
# 3. CFG – basic-block control-flow graph
# --------------------------------------------------------------------------- #
class CFGNode(_BaseViewModel):
    id: int
    addr: int
    size: int

class CFGEdge(_BaseViewModel):
    src: int
    dst: int
    kind: str = "uncond"  # {uncond,true,false,call,ret,…}

class CFGView(_BaseViewModel):
    nodes: List[CFGNode]
    edges: List[CFGEdge]

    @root_validator
    def _edge_reference_check(cls, values):
        node_ids = {n.id for n in values["nodes"]}
        for e in values["edges"]:
            if e.src not in node_ids or e.dst not in node_ids:
                raise ValueError(f"CFG: edge {e} references missing node")
        return values


# --------------------------------------------------------------------------- #
# 4. FCG – function-call graph
# --------------------------------------------------------------------------- #
class FCGNode(_BaseViewModel):
    id: int
    name: str
    is_lib: bool = False

class FCGEdge(_BaseViewModel):
    caller: int
    callee: int

class FCGView(_BaseViewModel):
    nodes: List[FCGNode]
    edges: List[FCGEdge]

    @root_validator
    def _edge_reference_check(cls, values):
        node_ids = {n.id for n in values["nodes"]}
        for e in values["edges"]:
            if e.caller not in node_ids or e.callee not in node_ids:
                raise ValueError(f"FCG: edge {e} references missing node")
        return values


# --------------------------------------------------------------------------- #
# 5. SysCall trace – linear list
# --------------------------------------------------------------------------- #
class SysCallItem(_BaseViewModel):
    idx: int
    name: str
    args: List[str] = Field(default_factory=list)

class SysCallView(_BaseViewModel):
    calls: List[SysCallItem]

    @validator("calls")
    def _idx_sequential(cls, calls):
        expected = list(range(len(calls)))
        got = [c.idx for c in calls]
        if got != expected:
            raise ValueError("SysCall: indices must be 0…n-1 in order")
        return calls


# --------------------------------------------------------------------------- #
# 6. Import table – DLL → [func,…]
# --------------------------------------------------------------------------- #
class ImportView(_BaseViewModel):
    __root__: Dict[str, List[str]]

    # ensure inner list contains only strings
    @validator("__root__", each_item=True)
    def _func_names_are_str(cls, funcs):
        if not all(isinstance(f, str) for f in funcs):
            raise TypeError("imports.json: every function name must be str")
        return funcs


# --------------------------------------------------------------------------- #
# 7. Public registry + validation helper
# --------------------------------------------------------------------------- #
_SCHEMA_REGISTRY: Dict[ViewName, Type[_BaseViewModel]] = {
    ViewName.ast: ASTView,
    ViewName.cfg: CFGView,
    ViewName.fcg: FCGView,
    ViewName.syscall: SysCallView,
    ViewName.imports: ImportView,
}

def validate_view(view: str | ViewName, data: Any) -> _BaseViewModel:
    """
    Validate *data* against the pydantic schema for *view*.

    Parameters
    ----------
    view : {"ast","cfg","fcg","syscall","imports"}
        Name of the extractor view.
    data : Any
        Parsed JSON/dict to validate.

    Returns
    -------
    pydantic.BaseModel
        The validated (and possibly coerced) model instance.

    Raises
    ------
    KeyError
        If *view* is unknown.
    pydantic.ValidationError
        If *data* does not conform to the schema.
    """
    try:
        model = _SCHEMA_REGISTRY[ViewName(view)]
    except KeyError as e:
        raise KeyError(f"unknown view '{view}'") from e
    return model.parse_obj(data)


__all__ = [
    "ViewName",
    "validate_view",
    # schema classes (exported mainly for typing)
    "ASTMetadata",
    "ASTView",
    "CFGView",
    "FCGView",
    "SysCallView",
    "ImportView",
]
