import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import Data

from src.graphs.dataset.graph_dataset import GraphDataset


def test_ensure_x_trim_pad(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = Data(feat=torch.randn(3, 2))
    g.num_nodes = 2
    torch.save(g, graph_dir / "a.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    import warnings
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        loaded, _, _ = ds[0]

    assert loaded.x.size(0) == 2
    assert record
    msg = str(record[0].message)
    assert "Data" in msg or "data" in msg


def test_ensure_x_pad_missing(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g = Data(x=torch.randn(1, 2))
    g.num_nodes = 3
    torch.save(g, graph_dir / "a.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    loaded, _, _ = ds[0]

    assert loaded.x.size(0) == 3
    assert torch.allclose(loaded.x[:1], g.x)
    assert torch.all(loaded.x[1:].eq(0))
