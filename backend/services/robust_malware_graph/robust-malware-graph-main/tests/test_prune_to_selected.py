import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.explain.utils.prune import prune_to_selected


def build_graph():
    g = HeteroData()
    g["n"].x = torch.zeros(3, 1)
    g["n"].num_nodes = 3
    g[("n", "r", "n")].edge_index = torch.tensor([[0, 1, 0], [1, 2, 2]], dtype=torch.long)
    return g


def test_prune_to_selected_keeps_nodes():
    g = build_graph()
    out = prune_to_selected(g, [0, 2])
    assert out["n"].num_nodes == 2
    assert out[("n", "r", "n")].edge_index.tolist() == [[0], [1]]
