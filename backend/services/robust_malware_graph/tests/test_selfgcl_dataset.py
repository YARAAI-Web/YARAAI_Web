import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
import torch.serialization as torch_serial
from torch_geometric.data import HeteroData
from torch_geometric.loader import DataLoader

if not hasattr(torch_serial, "add_safe_globals"):

    def add_safe_globals(objs):
        pass

    torch_serial.add_safe_globals = add_safe_globals

from src.cli.pretrain_selfgcl import HeteroGraphDiskDataset, validate_dataset
from src.graphs.features.cache import save_tensor


def test_hetero_disk_dataset_meta(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()
    g = HeteroData()
    g["token"].x = torch.randn(2, 1)
    g["token"].text = ["hello", "world"]
    g["token"].num_nodes = 2
    torch.save(g, graph_dir / "a.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    loader = DataLoader(ds, batch_size=1)
    batch = next(iter(loader))
    store = batch[0]["token"] if isinstance(batch, list) else batch["token"]
    assert store.meta["text"] == [["hello", "world"]]
    assert hasattr(store, "text_id")
    assert torch.all(store.text_id.eq(torch.tensor([1, 2], dtype=torch.long)))


def test_hetero_disk_dataset_meta_batch(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()
    g1 = HeteroData()
    g1["token"].x = torch.randn(1, 1)
    g1["token"].text = ["foo"]
    g1["token"].num_nodes = 1
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["token"].x = torch.randn(2, 1)
    g2["token"].text = ["bar", "baz"]
    g2["token"].num_nodes = 2
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    loader = DataLoader(ds, batch_size=2)
    batch = next(iter(loader))
    store = batch["token"] if not isinstance(batch, list) else batch[0]["token"]
    assert store.meta["text"] == [["foo"], ["bar", "baz"]]


def test_hetero_disk_dataset_token_addr(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = HeteroData()
    g1["token"].x = torch.randn(1, 1)
    g1["token"].addr = [1234]
    g1["token"].num_nodes = 1
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["token"].x = torch.randn(2, 1)
    g2["token"].addr = [4321, 8765]
    g2["token"].num_nodes = 2
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)

    store0 = ds[0]["token"]
    store1 = ds[1]["token"]
    assert torch.all(store0.addr.eq(torch.tensor([1234])))
    assert torch.all(store1.addr.eq(torch.tensor([4321, 8765])))

    loader = DataLoader(ds, batch_size=2)
    batch = next(iter(loader))
    store = batch["token"] if not isinstance(batch, list) else batch[0]["token"]
    assert torch.all(store.addr.eq(torch.tensor([1234, 4321, 8765])))


def test_extra_attr_moved_to_meta(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = HeteroData()
    g1["token"].x = torch.randn(1, 1)
    g1["token"].foo = [4321]
    g1["token"].num_nodes = 1
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["token"].x = torch.randn(2, 1)
    g2["token"].num_nodes = 2
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    loader = DataLoader(ds, batch_size=2)
    batch = next(iter(loader))
    store = batch["token"] if not isinstance(batch, list) else batch[0]["token"]
    assert not hasattr(store, "foo")
    assert store.meta["foo"] == ["[4321]", None]


def test_hetero_disk_dataset_syscall_addr(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = HeteroData()
    g1["syscall"].x = torch.randn(1, 1)
    g1["syscall"].addr = [1111]
    g1["syscall"].num_nodes = 1
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["syscall"].x = torch.randn(2, 1)
    g2["syscall"].addr = [2222, 3333]
    g2["syscall"].num_nodes = 2
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)

    sc0 = ds[0]["syscall"]
    sc1 = ds[1]["syscall"]
    assert torch.all(sc0.addr.eq(torch.tensor([1111])))
    assert torch.all(sc1.addr.eq(torch.tensor([2222, 3333])))

    loader = DataLoader(ds, batch_size=2)
    batch = next(iter(loader))
    store = batch["syscall"] if not isinstance(batch, list) else batch[0]["syscall"]
    assert torch.all(store.addr.eq(torch.tensor([1111, 2222, 3333])))


def test_fill_missing_attributes(tmp_path, monkeypatch, caplog):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = HeteroData()
    g1["token"].x = torch.randn(1, 1)
    g1["token"].addr = [1]
    g1["token"].num_nodes = 1
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["token"].x = torch.randn(2, 1)
    g2["token"].num_nodes = 2
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    with caplog.at_level("WARNING"):
        ds = HeteroGraphDiskDataset(graph_dir)
    assert any("Filled missing attribute" in rec.message for rec in caplog.records)

    loader = DataLoader(ds, batch_size=2)
    batch = next(iter(loader))
    store = batch["token"] if not isinstance(batch, list) else batch[0]["token"]
    assert torch.all(store.addr.eq(torch.tensor([1, 0, 0], dtype=torch.long)))


def test_hex_addr_conversion(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = HeteroData()
    g1["token"].x = torch.randn(1, 1)
    g1["token"].addr = "0x10"
    g1["token"].num_nodes = 1
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["token"].x = torch.randn(1, 1)
    g2["token"].addr = "0x20"
    g2["token"].num_nodes = 1
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)

    st0 = ds[0]["token"]
    st1 = ds[1]["token"]
    assert torch.all(st0.addr.eq(torch.tensor([16], dtype=torch.long)))
    assert torch.all(st1.addr.eq(torch.tensor([32], dtype=torch.long)))

    loader = DataLoader(ds, batch_size=2)
    batch = next(iter(loader))
    store = batch["token"] if not isinstance(batch, list) else batch[0]["token"]
    assert torch.all(store.addr.eq(torch.tensor([16, 32], dtype=torch.long)))


def test_schema_addr_default(tmp_path, monkeypatch):
    """Ensure 'addr' is added when defined in schema but missing in data."""
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = HeteroData()
    g1["token"].x = torch.randn(1, 1)
    g1["token"].num_nodes = 1
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["token"].x = torch.randn(2, 1)
    g2["token"].num_nodes = 2
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    loader = DataLoader(ds, batch_size=2)
    batch = next(iter(loader))
    store = batch["token"] if not isinstance(batch, list) else batch[0]["token"]
    assert torch.all(store.addr.eq(torch.zeros(3, dtype=torch.long)))


def test_metadata_file_saved(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = HeteroData()
    g1["n"].x = torch.randn(1, 1)
    g1["n"].num_nodes = 1
    g1[("n", "r0", "n")].edge_index = torch.tensor([[0], [0]])
    g1[("n", "r0", "n")].edge_type = torch.tensor([0], dtype=torch.long)
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["n"].x = torch.randn(1, 1)
    g2["n"].num_nodes = 1
    g2[("n", "r1", "n")].edge_index = torch.tensor([[0], [0]])
    g2[("n", "r1", "n")].edge_type = torch.tensor([1], dtype=torch.long)
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)
    meta_path = graph_dir / "processed" / "metadata.pkl"

    assert meta_path.is_file()
    assert ds.metadata == torch.load(meta_path)
    assert ds.metadata == (("n",), (("n", "r0", "n"), ("n", "r1", "n")))
    assert torch.all(ds[0][("n", "r0", "n")].edge_type.eq(0))
    assert torch.all(ds[1][("n", "r1", "n")].edge_type.eq(1))


def test_validate_dataset_relation_index(tmp_path, monkeypatch, caplog):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = HeteroData()
    g1["n"].x = torch.randn(1, 1)
    g1["n"].num_nodes = 1
    g1[("n", "r0", "n")].edge_index = torch.tensor([[0], [0]])
    g1[("n", "r0", "n")].edge_type = torch.tensor([0], dtype=torch.long)
    torch.save(g1, graph_dir / "a.pt")

    g2 = HeteroData()
    g2["n"].x = torch.randn(1, 1)
    g2["n"].num_nodes = 1
    g2[("n", "r0", "n")].edge_index = torch.tensor([[0], [0]])
    g2[("n", "r0", "n")].edge_type = torch.tensor([5], dtype=torch.long)
    torch.save(g2, graph_dir / "b.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(graph_dir)

    with caplog.at_level("ERROR"):
        ok = validate_dataset(ds)
    assert not ok
    assert any("reprocess" in rec.message.lower() for rec in caplog.records)


def test_load_embeds(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g = HeteroData()
    g["token"].num_nodes = 2
    torch.save(g, graph_dir / "a.pt")

    feat = torch.randn(2, 3)
    save_tensor("a", feat, tmp_path / "embeds")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(
        graph_dir, load_embeds=True, embed_dir=tmp_path / "embeds"
    )
    data = ds[0]
    assert torch.allclose(data["token"].x, feat)


def test_disable_embeds(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g = HeteroData()
    g["token"].num_nodes = 1
    torch.save(g, graph_dir / "a.pt")

    feat = torch.randn(1, 2)
    save_tensor("a", feat, tmp_path / "embeds")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    ds = HeteroGraphDiskDataset(
        graph_dir, load_embeds=False, embed_dir=tmp_path / "embeds"
    )
    data = ds[0]
    assert not hasattr(data["token"], "x")


def test_load_embeds_mmap(tmp_path, monkeypatch):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g = HeteroData()
    g["token"].num_nodes = 2
    torch.save(g, graph_dir / "a.pt")

    feat = torch.randn(2, 3)
    save_tensor("a", feat, tmp_path / "embeds")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    called = {}

    def fake_load_tensor(name, dir_, *, mmap=True):
        called['mmap'] = mmap
        return feat

    monkeypatch.setattr("src.cli.pretrain_selfgcl.load_tensor", fake_load_tensor)

    ds = HeteroGraphDiskDataset(
        graph_dir, load_embeds=True, embed_dir=tmp_path / "embeds"
    )
    data = ds[0]
    assert torch.allclose(data["token"].x, feat)
    # ``load_tensor`` should default to memory mapping
    assert called.get('mmap') is True


def test_empty_api_num_nodes(tmp_path, monkeypatch, caplog):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g = HeteroData()
    g["bb"].x = torch.randn(1, 1)
    g["bb"].num_nodes = 1
    _ = g["api"]  # empty store without num_nodes
    torch.save(g, graph_dir / "a.pt")

    vocab_path = tmp_path / "vocab.json"
    monkeypatch.setattr(HeteroGraphDiskDataset, "VOCAB_PATH", vocab_path)

    with caplog.at_level("WARNING"):
        ds = HeteroGraphDiskDataset(graph_dir)
    assert not any("Filled missing attribute" in rec.message for rec in caplog.records)

    api_store = ds[0]["api"]
    assert api_store.num_nodes == 0
