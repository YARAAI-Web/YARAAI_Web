import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

pytest = __import__("pytest")
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
import numpy as np
from torch_geometric.data import Data
from src.cli.pretrain_selfgcl import HeteroGraphDiskDataset


def test_encode_metadata_various_lists(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()
    g = Data(x=torch.randn(2, 1))
    g.num_nodes = 2
    g.num_list = [1, 2, 3]
    g.empty_list = []
    g.str_list = ["a", "b"]
    g.dict_list = [{"k": 1}, {"k": 2}]
    g.mixed_list = [1, "a"]
    g.tensor_attr = torch.tensor([4, 5])
    g.numpy_attr = np.array([6, 7])
    g.text = "foo"
    torch.save(g, graph_dir / "a.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    data = ds[0]
    meta = data.meta
    assert torch.equal(data.num_list, torch.tensor([1, 2, 3]))
    assert hasattr(data, "str_list_id")
    assert "empty_list" not in data.__dict__
    assert torch.equal(data.tensor_attr, torch.tensor([4, 5]))
    assert torch.equal(data.numpy_attr, torch.tensor([6, 7]))
    assert "tensor_attr" not in meta
    assert "numpy_attr" not in meta
    assert meta["text"] == "foo"
    assert meta["empty_list"] == json.dumps([])
    assert meta["dict_list"] == json.dumps([{"k": 1}, {"k": 2}])
    assert meta["mixed_list"] == json.dumps([1, "a"])


def test_encode_metadata_complex_object(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()
    g = Data(x=torch.randn(1, 1))
    g.num_nodes = 1
    g.complex_list = [complex(1, 2)]
    torch.save(g, graph_dir / "a.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    data = ds[0]
    meta = data.meta
    assert meta["complex_list"] == repr([complex(1, 2)])


def test_encode_metadata_tensor_numpy(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()
    g = Data(x=torch.randn(1, 1))
    g.num_nodes = 1
    g.tensor_attr = torch.tensor([1, 2, 3])
    g.numpy_attr = np.array([4, 5, 6])
    torch.save(g, graph_dir / "a.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    data = ds[0]
    meta = data.meta
    assert torch.equal(data.tensor_attr, torch.tensor([1, 2, 3]))
    assert torch.equal(data.numpy_attr, torch.tensor([4, 5, 6]))
    assert "tensor_attr" not in meta
    assert "numpy_attr" not in meta


def test_encode_metadata_addr_str_list_success(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()
    g = Data(x=torch.randn(3, 1))
    g.num_nodes = 3
    g.addr = ["0x1", "2", "0x3"]
    torch.save(g, graph_dir / "a.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    data = ds[0]
    meta = data.meta
    assert torch.equal(data.addr, torch.tensor([1, 2, 3], dtype=torch.long))
    assert "addr" not in meta
    assert not hasattr(data, "addr_id")


def test_encode_metadata_addr_str_list_fallback(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()
    g = Data(x=torch.randn(2, 1))
    g.num_nodes = 2
    g.addr = ["0x1", "bogus"]
    torch.save(g, graph_dir / "a.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    data = ds[0]
    meta = data.meta
    assert meta["addr"] == ["0x1", "bogus"]
    assert hasattr(data, "addr_id")
