import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.explain.utils.hetero import drop_unselected_nodes


def build_graph():
    g = HeteroData()
    g["bb"].x = torch.zeros(3, 1)
    g["bb"].num_nodes = 3
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0, 1, 2], [1, 2, 0]])
    return g


def test_drop_nodes():
    g = build_graph()
    out = drop_unselected_nodes(g, [0, 2], "cfg")
    assert out["bb"].num_nodes == 2
    assert out[("bb", "cfg", "bb")].edge_index.tolist() == [[1], [0]]


def test_drop_nodes_none_view():
    g = build_graph()
    out = drop_unselected_nodes(g, [0, 2], None)
    assert out["bb"].num_nodes == 2
    assert out[("bb", "cfg", "bb")].edge_index.tolist() == [[1], [0]]


@pytest.mark.skipif(not torch.cuda.is_available(), reason="CUDA not available")
def test_drop_nodes_cuda():
    g = build_graph().to("cuda")
    out = drop_unselected_nodes(g, [0, 2], "cfg")
    assert out["bb"].num_nodes == 2
    assert out[("bb", "cfg", "bb")].edge_index.device.type == "cuda"
    assert out[("bb", "cfg", "bb")].edge_index.tolist() == [[1], [0]]
