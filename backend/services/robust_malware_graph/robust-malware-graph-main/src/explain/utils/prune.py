"""Subgraph pruning helpers."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Dict

import torch
from torch_geometric.data import HeteroData

from src.graphs.transforms import GraphPruner


def prune_to_selected(graph: HeteroData, selected_nodes) -> HeteroData:
    """Return a subgraph containing only ``selected_nodes``.

    Parameters
    ----------
    graph : HeteroData
        Input heterogeneous graph.
    selected_nodes : Sequence[int] | Mapping[str, Sequence[int]]
        Nodes to keep. When a mapping is provided, keys should be node types.
        Node types not present in the mapping are pruned entirely.
    """
    scores: Dict[str, torch.Tensor] = {}

    if isinstance(selected_nodes, Mapping):
        for ntype in graph.node_types:
            N = graph[ntype].num_nodes
            idx = torch.as_tensor(selected_nodes.get(ntype, []), dtype=torch.long)
            mask = torch.zeros(N, dtype=torch.float)
            if idx.numel() > 0:
                mask[idx] = 1.0
            scores[ntype] = mask
    else:
        # assume single node type or apply to the first node type
        ntype = graph.node_types[0]
        idx = torch.as_tensor(selected_nodes, dtype=torch.long)
        mask = torch.zeros(graph[ntype].num_nodes, dtype=torch.float)
        if idx.numel() > 0:
            mask[idx] = 1.0
        scores = {ntype: mask}
        for other in graph.node_types[1:]:
            scores[other] = torch.zeros(graph[other].num_nodes, dtype=torch.float)

    pruner = GraphPruner(scores, thresh=0.5)
    return pruner.apply(graph)
