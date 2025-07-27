"""Light-weight helpers for :class:`torch_geometric.data.HeteroData`."""
from __future__ import annotations

from fnmatch import fnmatch
from typing import Iterable, Tuple

import torch
from torch_geometric.data import HeteroData

EdgeType = Tuple[str, str, str]


def get_edge_store(
    g: HeteroData, etype: EdgeType
) -> Tuple[torch.Tensor, HeteroData, torch.Tensor]:
    """Return ``(edge_index, store, edge_id)`` for ``etype``.

    If the edge store already defines ``edge_id`` it is returned. Otherwise a
    global index is constructed by summing ``num_edges`` of preceding edge
    types in ``g.edge_types``.
    """
    store = g[etype]
    edge_index = store.edge_index

    if "edge_id" in store:
        global_idx = store.edge_id
    else:
        offset = 0
        for key in g.edge_types:
            if key == etype:
                break
            offset += g[key].edge_index.size(1)
        global_idx = torch.arange(
            offset,
            offset + edge_index.size(1),
            dtype=torch.long,
            device=edge_index.device,
        )
    return edge_index, store, global_idx


def edge_mask_to_global(
    mask_local: torch.Tensor, global_idx: torch.Tensor, num_total: int
) -> torch.Tensor:
    """Expand a local edge mask into a graph-level tensor."""
    out = torch.zeros(num_total, dtype=mask_local.dtype, device=mask_local.device)
    out[global_idx] = mask_local
    return out


def iter_edge_types(g: HeteroData, view: str | None = None) -> Iterable[EdgeType]:
    """Yield edge types whose relation matches ``view`` (supports ``fnmatch``)."""

    if view is None:
        yield from g.edge_types
        return

    for key in g.edge_types:
        if fnmatch(key[1], view):
            yield key


def ensure_edgeaware_selector(selector, g: HeteroData) -> None:
    """Ensure ``selector`` has initialized parameters for ``g``.

    If ``g`` is a :class:`~torch_geometric.data.HeteroData` graph and the
    selector declares an ``initialized`` attribute evaluating to ``False``, the
    selector's private ``_init_params`` method is invoked.  This mirrors the
    lazy initialisation performed inside the selector's forward pass but allows
    callers to guarantee the parameters exist *before* any forward operation.
    """

    if isinstance(g, HeteroData) and not getattr(selector, "initialized", True):
        # ``_init_params`` is an internal helper on ``GumbelMaskSelector``.  It
        # creates per-edge-type parameters based on the provided graph.
        selector._init_params(g)


def drop_unselected_nodes(data: HeteroData, node_idx, view: str | None) -> HeteroData:
    """Return subgraph retaining only ``node_idx`` for edge types matching ``view``.

    Parameters
    ----------
    data : HeteroData
        Input heterogeneous graph.
    node_idx : Sequence[int] | Mapping[str, Sequence[int]]
        Nodes to keep. When a mapping is provided the keys correspond to
        node types.
    view : str | None
        Edge relation pattern (fnmatch) identifying node types.  ``None``
        targets all edge types.
    """
    from collections.abc import Mapping, Sequence
    from src.graphs.transforms import GraphPruner

    selected: dict[str, torch.Tensor] = {}

    if isinstance(node_idx, Mapping):
        for ntype in data.node_types:
            device = getattr(data[ntype], "device", None)
            if device is None:
                for val in data[ntype].values():
                    if isinstance(val, torch.Tensor):
                        device = val.device
                        break
            if device is None:
                device = torch.device("cpu")
            idx = torch.as_tensor(
                node_idx.get(ntype, []), dtype=torch.long, device=device
            )
            mask = torch.zeros(
                data[ntype].num_nodes, dtype=torch.float, device=device
            )
            if idx.numel() > 0:
                mask[idx] = 1.0
            selected[ntype] = mask
    else:
        # infer node type from view edge types
        types = {et[0] for et in iter_edge_types(data, view)} | {
            et[2] for et in iter_edge_types(data, view)
        }
        if len(types) != 1:
            raise ValueError("Ambiguous node types; provide mapping per type")
        ntype = next(iter(types))
        device = getattr(data[ntype], "device", None)
        if device is None:
            for val in data[ntype].values():
                if isinstance(val, torch.Tensor):
                    device = val.device
                    break
        if device is None:
            device = torch.device("cpu")
        mask = torch.zeros(
            data[ntype].num_nodes, dtype=torch.float, device=device
        )
        idx = torch.as_tensor(node_idx, dtype=torch.long, device=device)
        if idx.numel() > 0:
            mask[idx] = 1.0
        selected = {ntype: mask}
        for other in data.node_types:
            if other != ntype:
                selected.setdefault(
                    other,
                    torch.zeros(
                        data[other].num_nodes,
                        dtype=torch.float,
                        device=getattr(
                            data[other],
                            "device",
                            next(
                                (
                                    v.device
                                    for v in data[other].values()
                                    if isinstance(v, torch.Tensor)
                                ),
                                torch.device("cpu"),
                            ),
                        ),
                    ),
                )

    pruner = GraphPruner(selected, thresh=0.5)
    out = pruner.apply(data)

    if not isinstance(out, HeteroData):
        builder = HeteroGraphBuilder()
        builder.add_view(out, view)
        out = builder.build()
    return out


def filter_view(graph: HeteroData, view: str | None) -> HeteroData:
    """Remove edges not matching ``view`` and drop disconnected node types.

    ``None`` keeps all edge types.
    """

    keep = set(iter_edge_types(graph, view))

    # remove unrelated edge stores
    for et in list(graph.edge_types):
        if et not in keep:
            del graph[et]

    # gather node types still used by remaining edges
    connected: set[str] = set()
    for et in keep:
        connected.add(et[0])
        connected.add(et[2])

    for ntype in list(graph.node_types):
        if ntype not in connected:
            del graph[ntype]

    return graph
