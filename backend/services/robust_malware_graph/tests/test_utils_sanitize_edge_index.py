import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import Data, HeteroData

from src.graphs.utils import sanitize_edge_index


def test_sanitize_edge_index_data():
    g = Data(
        edge_index=torch.tensor([[0, 1, 2], [1, 3, -1]]),
        edge_attr=torch.tensor([10, 20, 30]),
    )
    sanitize_edge_index(g, src_nodes=2, dst_nodes=2)
    assert torch.equal(g.edge_index, torch.tensor([[0], [1]]))
    assert torch.equal(g.edge_attr, torch.tensor([10]))


def test_sanitize_edge_index_hetero():
    g = HeteroData()
    g["a"].num_nodes = 2
    g["b"].num_nodes = 1
    g[("a", "to", "b")].edge_index = torch.tensor([[0, 1], [0, 5]])

    sanitize_edge_index(g[("a", "to", "b")], src_nodes=g["a"].num_nodes, dst_nodes=g["b"].num_nodes)

    assert torch.equal(g[("a", "to", "b")].edge_index, torch.tensor([[0], [0]]))
