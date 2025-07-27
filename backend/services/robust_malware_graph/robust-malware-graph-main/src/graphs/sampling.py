"""
Utility functions for memory-efficient subgraph sampling on heterogeneous graphs.
"""

from typing import Dict, List, Union
import torch
from torch_geometric.loader import NeighborLoader
from torch_geometric.data import HeteroData

__all__ = ["sample_subgraph"]

def _build_num_neighbors(
    data: HeteroData,
    num_neighbors: Union[int, List[int]]
) -> Dict[str, List[int]]:
    """
    Build {edge_type: [num_neighbors]*num_layers} dict required by NeighborLoader.
    """
    if isinstance(num_neighbors, int):
        num_neighbors = [num_neighbors]
    return {etype: list(num_neighbors) for etype in data.edge_types}

def sample_subgraph(
    data: HeteroData,
    target_node_type: str,
    *,
    batch_size: int = 1024,
    num_neighbors: Union[int, List[int]] = 15,
    num_hops: int = 2,
    device: Union[str, torch.device] = "cpu",
) -> HeteroData:
    """
    Draw a single heterogeneous subgraph mini-batch and move it to *device*.
    Returns
    -------
    HeteroData  –  subgraph with .batch vectors set for every node type.
    """
    loader = NeighborLoader(
        data,
        input_nodes=(target_node_type, torch.arange(data[target_node_type].num_nodes)),
        batch_size=batch_size,
        num_neighbors=_build_num_neighbors(data, [num_neighbors] * num_hops),
        shuffle=True,
    )
    # Return the first mini-batch
    subgraph = next(iter(loader))
    subgraph = subgraph.to(device)

    # Ensure batch vector exists
    for nt in subgraph.node_types:
        if "batch" not in subgraph[nt]:
            subgraph[nt].batch = torch.zeros(
                subgraph[nt].num_nodes, dtype=torch.long, device=device
            )
    return subgraph
