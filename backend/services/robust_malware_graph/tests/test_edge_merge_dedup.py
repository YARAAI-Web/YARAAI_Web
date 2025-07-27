import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.graphs.builders.hetero_builder import HeteroGraphBuilder


def test_edge_merge_dedup_attributes():
    g = HeteroData()
    g["n"].num_nodes = 2
    ei = torch.tensor([[0, 0], [1, 1]])
    g[("n", "r", "n")].edge_index = ei
    g[("n", "r", "n")].edge_type = torch.zeros(ei.size(1), dtype=torch.long)

    builder = HeteroGraphBuilder()
    builder.add_view(g, "v1")

    hetero = builder.build()
    store = hetero[("n", "r", "n")]
    assert store.edge_index.size(1) == store.edge_type.size(0)
    assert store.edge_index.size(1) == 1
