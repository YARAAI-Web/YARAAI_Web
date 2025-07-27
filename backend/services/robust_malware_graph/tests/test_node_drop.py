import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")
pytest.importorskip("numpy")

import torch
import numpy as np
from torch_geometric.data import Data, HeteroData

from src.augment.ops.drop_node import NodeDrop


def test_node_drop_updates_num_nodes():
    num_nodes = 10
    g = Data(
        x=torch.randn(num_nodes, 2),
        edge_index=torch.stack(
            [torch.arange(num_nodes - 1), torch.arange(1, num_nodes)],
            dim=0,
        ),
        num_nodes=num_nodes,
    )

    aug = NodeDrop(keep_prob=0.5, seed=42)
    result = aug(g)

    rng = np.random.RandomState(42)
    mask_np = rng.rand(num_nodes) < 0.5
    if not mask_np.any():
        mask_np[rng.randint(0, num_nodes)] = True
    expected = int(mask_np.sum())

    assert result.num_nodes == expected
    assert result.num_nodes == result.x.size(0)


def test_node_drop_filters_invalid_edges_data():
    g = Data(
        x=torch.randn(3, 1),
        edge_index=torch.tensor([[0, 1, 2], [1, 4, -1]]),
        edge_attr=torch.tensor([10, 20, 30]),
        num_nodes=3,
    )

    aug = NodeDrop(keep_prob=1.0)
    out = aug(g)

    assert out.edge_index.size(1) == 1
    assert torch.equal(out.edge_index, torch.tensor([[0], [1]]))
    assert torch.equal(out.edge_attr, torch.tensor([10]))


def test_node_drop_filters_invalid_edges_hetero():
    g = HeteroData()
    g["a"].x = torch.randn(2, 1)
    g["a"].num_nodes = 2
    g["b"].x = torch.randn(1, 1)
    g["b"].num_nodes = 1
    g[("a", "to", "b")].edge_index = torch.tensor([[0, 1], [0, 5]])
    g[("b", "to", "a")].edge_index = torch.tensor([[0], [-1]])

    aug = NodeDrop(keep_prob=1.0)
    out = aug(g)

    assert torch.equal(out[("a", "to", "b")].edge_index, torch.tensor([[0], [0]]))
    assert out[("b", "to", "a")].edge_index.numel() == 0


def test_node_drop_ignores_invalid_references():
    g = Data(
        x=torch.randn(2, 1),
        edge_index=torch.tensor([[0, 2], [1, 0]]),
        edge_attr=torch.tensor([5, 7]),
        num_nodes=2,
    )

    aug = NodeDrop(keep_prob=1.0)
    out = aug(g)

    assert torch.equal(out.edge_index, torch.tensor([[0], [1]]))
    assert torch.equal(out.edge_attr, torch.tensor([5]))


def test_node_drop_handles_out_of_range_indices():
    g = Data(
        x=torch.randn(4, 1),
        edge_index=torch.tensor([[0, 4, 2], [1, 3, 3]]),
        edge_attr=torch.tensor([11, 22, 33]),
        num_nodes=4,
    )

    aug = NodeDrop(keep_prob=1.0)
    out = aug(g)

    assert torch.equal(out.edge_index, torch.tensor([[0, 2], [1, 3]]))
    assert torch.equal(out.edge_attr, torch.tensor([11, 33]))
    assert out.edge_index.max().item() < 4
