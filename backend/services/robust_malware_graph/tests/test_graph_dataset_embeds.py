import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.graphs.dataset.graph_dataset import GraphDataset
from src.graphs.features.cache import save_tensor


def _setup(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)
    g = HeteroData()
    g["token"].num_nodes = 2
    torch.save(g, graph_dir / "sample.pt")
    feat = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    save_tensor("sample", feat, tmp_path / "embeds")
    return feat


def test_dataset_loads_embeds(tmp_path):
    feat = _setup(tmp_path)
    ds = GraphDataset(tmp_path, split="train", label_file=None)
    g, _, _ = ds[0]
    assert torch.allclose(g["token"].x, feat)


def test_dataset_disable_embeds(tmp_path):
    _setup(tmp_path)
    ds = GraphDataset(tmp_path, split="train", label_file=None, load_embeds=False)
    g, _, _ = ds[0]
    assert not hasattr(g["token"], "x")


def test_dataset_loads_embeds_mmap(tmp_path, monkeypatch):
    feat = _setup(tmp_path)

    called = {}

    def fake_load_tensor(name, dir_, *, mmap=True):
        called['mmap'] = mmap
        return feat

    monkeypatch.setattr(
        "src.graphs.dataset.graph_dataset.load_tensor", fake_load_tensor
    )

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    g, _, _ = ds[0]
    assert torch.allclose(g["token"].x, feat)
    # Embedding tensors should be loaded using memory mapping by default
    assert called.get('mmap') is True
