import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData, Batch
from torch.utils.data import DataLoader

from src.graphs.dataset.graph_dataset import GraphDataset


def test_collate_sanitizes_list_attrs(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g1 = HeteroData()
    g1["n"].x = torch.randn(1, 1)
    g1["n"].foo = [1, 2]
    g1["n"].bar = ["a", "b"]
    g1["n"].name = "sample1"
    g1["n"].num_nodes = 1

    g2 = HeteroData()
    g2["n"].x = torch.randn(1, 1)
    g2["n"].foo = [3]
    g2["n"].bar = ["c"]
    g2["n"].name = "sample2"
    g2["n"].num_nodes = 1

    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    loader = DataLoader(ds, batch_size=2, collate_fn=GraphDataset.collate_fn)
    batch = next(iter(loader))

    assert isinstance(batch["graph"], Batch)
    assert torch.is_tensor(batch["graph"]["n"].foo)
    assert hasattr(batch["graph"]["n"], "meta")
    assert "bar" in batch["graph"]["n"].meta
    assert "name" in batch["graph"]["n"].meta


def test_dataset_filters_invalid_edges_data(tmp_path):
    from torch_geometric.data import Data

    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = Data(
        x=torch.randn(3, 1),
        edge_index=torch.tensor([[0, 1, 2], [1, 4, -1]]),
        edge_attr=torch.tensor([10, 20, 30]),
        num_nodes=3,
    )

    torch.save(g, graph_dir / "a.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    loaded, _, _ = ds[0]

    assert torch.equal(loaded.edge_index, torch.tensor([[0], [1]]))
    assert torch.equal(loaded.edge_attr, torch.tensor([10]))


def test_dataset_filters_invalid_edges_hetero(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = HeteroData()
    g["a"].x = torch.randn(2, 1)
    g["a"].num_nodes = 2
    g["b"].x = torch.randn(1, 1)
    g["b"].num_nodes = 1
    g[("a", "to", "b")].edge_index = torch.tensor([[0, 1], [0, 5]])
    g[("b", "to", "a")].edge_index = torch.tensor([[0], [-1]])

    torch.save(g, graph_dir / "s.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    loaded, _, _ = ds[0]

    assert torch.equal(loaded[("a", "to", "b")].edge_index, torch.tensor([[0], [0]]))
    assert loaded[("b", "to", "a")].edge_index.numel() == 0


def test_transform_sanitizes_edges_data(tmp_path):
    from torch_geometric.data import Data

    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = Data(x=torch.randn(2, 1), edge_index=torch.tensor([[0], [1]]), num_nodes=2)
    torch.save(g, graph_dir / "a.pt")

    def corrupt(graph: Data):
        graph.edge_index = torch.tensor([[2], [3]])
        return graph

    ds = GraphDataset(tmp_path, split="train", label_file=None, transform=corrupt)
    loaded, _, _ = ds[0]

    assert loaded.edge_index.numel() == 0


def test_transform_sanitizes_edges_hetero(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = HeteroData()
    g["a"].x = torch.randn(2, 1)
    g["a"].num_nodes = 2
    g["b"].x = torch.randn(1, 1)
    g["b"].num_nodes = 1
    g[("a", "to", "b")].edge_index = torch.tensor([[0], [0]])

    torch.save(g, graph_dir / "s.pt")

    def corrupt(graph: HeteroData):
        graph[("a", "to", "b")].edge_index = torch.tensor([[1], [2]])
        return graph

    ds = GraphDataset(tmp_path, split="train", label_file=None, transform=corrupt)
    loaded, _, _ = ds[0]

    assert loaded[("a", "to", "b")].edge_index.numel() == 0
