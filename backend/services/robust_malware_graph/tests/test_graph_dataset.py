import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.graphs.dataset.graph_dataset import GraphDataset


def test_graph_dataset_feat_to_x(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = HeteroData()
    g["node"].feat = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    g["node"].num_nodes = 2

    torch.save(g, graph_dir / "sample.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    loaded, label, sha = ds[0]

    assert label is None
    assert sha == "sample"
    assert "x" in loaded["node"]
    assert torch.all(loaded["node"].x.eq(g["node"].feat))


def test_require_labels_drops_unlabeled(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = HeteroData()
    g["n"].x = torch.tensor([[1.0]])
    g["n"].num_nodes = 1
    torch.save(g, graph_dir / "a.pt")
    torch.save(g, graph_dir / "b.pt")

    labels = tmp_path / "train" / "labels.csv"
    labels.write_text("sha256,label\na,1\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)

    assert len(ds) == 1
    g_loaded, label, sha = ds[0]
    assert label == 1
    assert sha == "a"

    from torch.utils.data import DataLoader

    loader = DataLoader(ds, batch_size=2, collate_fn=GraphDataset.collate_fn)
    batch = next(iter(loader))
    assert batch["label"] is not None
    assert torch.equal(batch["label"], torch.tensor([1]))


def test_collate_pads_feat_dim(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g1 = HeteroData()
    g1["n"].x = torch.randn(1, 2)
    g1["n"].num_nodes = 1
    g2 = HeteroData()
    g2["n"].x = torch.randn(1, 1)
    g2["n"].num_nodes = 1
    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    labels = tmp_path / "train" / "labels.csv"
    labels.write_text("sha256,label\na,0\nb,1\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)
    from torch.utils.data import DataLoader
    loader = DataLoader(ds, batch_size=2, collate_fn=GraphDataset.collate_fn)
    batch = next(iter(loader))

    assert batch["graph"]["n"].x.shape[1] == 2
    assert torch.equal(batch["label"], torch.tensor([0, 1], dtype=torch.long))


def test_collate_sets_missing_num_nodes(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g1 = HeteroData()
    g1["n"].x = torch.randn(2, 1)  # num_nodes inferred from features
    g2 = HeteroData()
    g2["n"].edge_index = torch.tensor([[0, 1], [1, 0]])

    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    labels = tmp_path / "train" / "labels.csv"
    labels.write_text("sha256,label\na,0\nb,1\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)
    from torch.utils.data import DataLoader
    loader = DataLoader(ds, batch_size=2, collate_fn=GraphDataset.collate_fn)

    batch = next(iter(loader))

    # num_nodes should be set for both graphs and sum to 4 in the batch
    assert batch["graph"]["n"].num_nodes == 4


def test_collate_sets_missing_num_nodes_data(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    from torch_geometric.data import Data

    g1 = Data(x=torch.randn(2, 1))
    g2 = Data(edge_index=torch.tensor([[0, 1, 2], [1, 2, 0]]))

    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    labels = tmp_path / "train" / "labels.csv"
    labels.write_text("sha256,label\na,0\nb,1\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)
    from torch.utils.data import DataLoader
    loader = DataLoader(ds, batch_size=2, collate_fn=GraphDataset.collate_fn)

    batch = next(iter(loader))

    assert batch["graph"].num_nodes == 5


def test_collate_handles_mixed_num_nodes_keys(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    from torch_geometric.data import Data

    # g1 relies on inferred num_nodes from features (no key stored)
    g1 = Data(x=torch.randn(2, 1))
    # g2 explicitly stores num_nodes in its mapping
    g2 = Data(edge_index=torch.tensor([[0, 1, 2], [1, 2, 0]]), num_nodes=3)

    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    labels = tmp_path / "train" / "labels.csv"
    labels.write_text("sha256,label\na,0\nb,1\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)
    from torch.utils.data import DataLoader
    loader = DataLoader(ds, batch_size=2, collate_fn=GraphDataset.collate_fn)

    batch = next(iter(loader))

    assert batch["graph"].num_nodes == 5


def test_collate_fills_missing_metadata(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g1 = HeteroData()
    g1["n"].x = torch.randn(1, 1)
    g1["n"].num_nodes = 1
    g1["n"].foo_id = torch.tensor([1])

    g2 = HeteroData()
    g2["n"].x = torch.randn(2, 1)
    g2["n"].num_nodes = 2
    g2["n"].bar_id = torch.tensor([2, 3])

    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    labels = tmp_path / "train" / "labels.csv"
    labels.write_text("sha256,label\na,0\nb,1\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)
    from torch.utils.data import DataLoader
    from functools import partial

    attr_names = {"n": ["foo", "bar"]}
    loader = DataLoader(
        ds,
        batch_size=2,
        collate_fn=partial(GraphDataset.collate_fn, attr_names=attr_names),
    )
    batch = next(iter(loader))

    assert torch.equal(batch["graph"]["n"].foo_id, torch.tensor([1, 0, 0]))
    assert torch.equal(batch["graph"]["n"].bar_id, torch.tensor([0, 2, 3]))


def test_collate_fills_missing_metadata_data(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    from torch_geometric.data import Data

    g1 = Data(x=torch.randn(1, 1), foo_id=torch.tensor([1]), num_nodes=1)
    g2 = Data(x=torch.randn(2, 1), num_nodes=2)

    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    labels = tmp_path / "train" / "labels.csv"
    labels.write_text("sha256,label\na,0\nb,1\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)
    from torch.utils.data import DataLoader
    from functools import partial

    attr_names = {"": ["foo"]}
    loader = DataLoader(
        ds,
        batch_size=2,
        collate_fn=partial(GraphDataset.collate_fn, attr_names=attr_names),
    )

    batch = next(iter(loader))

    assert torch.equal(batch["graph"].foo_id, torch.tensor([1, 0, 0]))


def test_dataset_sets_api_num_nodes(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = HeteroData()
    g["bb"].num_nodes = 1
    g[("bb", "calls", "api")].edge_index = torch.tensor([[0], [0]])
    g["api"].api_name = ["CreateFileA"]

    torch.save(g, graph_dir / "s.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    loaded, _, _ = ds[0]

    assert loaded["api"].num_nodes == 1


def test_collate_pads_edge_attr_dim(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    from torch_geometric.data import Data

    g1 = Data(
        x=torch.tensor([[0.0]]),
        edge_index=torch.tensor([[0], [0]]),
        edge_attr=torch.tensor([[1.0, 2.0]]),
        num_nodes=1,
    )
    g2 = Data(
        x=torch.tensor([[0.0]]),
        edge_index=torch.tensor([[0], [0]]),
        edge_attr=torch.tensor([3.0]),
        num_nodes=1,
    )

    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    from torch.utils.data import DataLoader

    loader = DataLoader(ds, batch_size=2, collate_fn=GraphDataset.collate_fn)
    batch = next(iter(loader))

    assert batch["graph"].edge_attr.shape == (2, 2)
    assert torch.allclose(batch["graph"].edge_attr[0], torch.tensor([1.0, 2.0]))
    assert torch.allclose(batch["graph"].edge_attr[1], torch.tensor([3.0, 0.0]))
