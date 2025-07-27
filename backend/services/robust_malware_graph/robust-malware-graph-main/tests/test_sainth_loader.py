import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.graphs.builders.graph_sampler import sainth_loader_hetero


def build_small_graph():
    g = HeteroData()
    g["n"].x = torch.randn(4, 3)
    g["n"].num_nodes = 4
    ei = torch.tensor([[0, 1, 2], [1, 2, 3]], dtype=torch.long)
    g[("n", "rel", "n")].edge_index = ei
    return g


def test_sainth_loader_hetero_yields_graphs():
    g = build_small_graph()
    loader = sainth_loader_hetero(g, num_steps=1)
    sub = next(iter(loader))
    assert isinstance(sub, HeteroData)
    assert sub.num_nodes > 0
    assert sub.node_types == g.node_types
    assert sub.edge_types == g.edge_types
