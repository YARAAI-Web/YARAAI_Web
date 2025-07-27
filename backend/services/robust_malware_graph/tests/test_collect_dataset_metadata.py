import importlib
import sys
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.models.gnn.encoder import RGCNEncoder
from src.graphs.dataset.graph_dataset import GraphDataset, collect_dataset_metadata


def _make_graph(path: Path, rels: list[str]) -> None:
    g = HeteroData()
    g["n"].x = torch.randn(2, 4)
    g["n"].num_nodes = 2
    for r in rels:
        ei = torch.tensor([[0, 1], [1, 0]])
        g[("n", r, "n")].edge_index = ei
        idx = int(r[1:]) if r.startswith("r") else 0
        g[("n", r, "n")].edge_type = torch.full(
            (ei.size(1),), idx, dtype=torch.long
        )
    torch.save(g, path)


def _make_invalid_graph(path: Path, invalid_idx: int) -> None:
    g = HeteroData()
    g["n"].x = torch.randn(2, 4)
    g["n"].num_nodes = 2
    ei = torch.tensor([[0, 1], [1, 0]])
    g[("n", "r0", "n")].edge_index = ei
    g[("n", "r0", "n")].edge_type = torch.full((ei.size(1),), invalid_idx, dtype=torch.long)
    torch.save(g, path)


def test_extra_edge_types(tmp_path, caplog):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_graph(gdir / "a.pt", ["r0"])
        _make_graph(gdir / "b.pt", ["r0", "r1"])
        (data_root / split / "labels.csv").write_text("sha256,label\na,0\nb,1\n")

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    ckpt_path = tmp_path / "enc.pt"
    torch.save({"model": enc.state_dict()}, ckpt_path)

    argv = [
        "train_res_gcl",
        "--encoder-checkpoint",
        str(ckpt_path),
        "--splits-dir",
        str(data_root),
        "--epochs",
        "1",
        "--batch-size",
        "1",
        "--device",
        "cpu",
        "--output",
        str(tmp_path / "model.pt"),
    ]

    mod = importlib.import_module("src.cli.train_res_gcl")
    caplog.set_level("INFO")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert any("Epoch 1" in rec.message for rec in caplog.records)


def test_collect_metadata_preserves_order(tmp_path):
    gdir = tmp_path / "train" / "graphs"
    gdir.mkdir(parents=True)

    g1 = HeteroData()
    g1["n1"].x = torch.randn(1, 1)
    g1["n1"].num_nodes = 1
    g1["n2"].x = torch.randn(1, 1)
    g1["n2"].num_nodes = 1
    g1[("n1", "r1", "n2")].edge_index = torch.tensor([[0], [0]])
    torch.save(g1, gdir / "a.pt")

    g2 = HeteroData()
    g2["n1"].x = torch.randn(1, 1)
    g2["n1"].num_nodes = 1
    g2["n3"].x = torch.randn(1, 1)
    g2["n3"].num_nodes = 1
    g2[("n1", "r2", "n3")].edge_index = torch.tensor([[0], [0]])
    g2[("n3", "r3", "n1")].edge_index = torch.tensor([[0], [0]])
    torch.save(g2, gdir / "b.pt")

    (tmp_path / "train" / "labels.csv").write_text("sha256,label\na,0\nb,1\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)
    metadata, _, _, _ = collect_dataset_metadata(ds)
    node_types, edge_types = metadata

    from src.graphs.normalizers.schema import EDGE_TYPES

    assert node_types == ["n1", "n2", "n3"]
    assert edge_types == list(EDGE_TYPES)


def test_collect_metadata_empty_edge_type(tmp_path):
    gdir = tmp_path / "train" / "graphs"
    gdir.mkdir(parents=True)

    g = HeteroData()
    g["n"].x = torch.randn(1, 1)
    g["n"].num_nodes = 1
    g[("n", "r0", "n")].edge_index = torch.empty(2, 0, dtype=torch.long)
    g[("n", "r0", "n")].edge_type = torch.empty(0, dtype=torch.long)
    torch.save(g, gdir / "a.pt")

    (tmp_path / "train" / "labels.csv").write_text("sha256,label\na,0\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)
    metadata, _, _, _ = collect_dataset_metadata(ds)

    from src.graphs.normalizers.schema import EDGE_TYPES

    assert metadata[0] == ["n"]
    assert metadata[1][: len(EDGE_TYPES)] == list(EDGE_TYPES)
    assert len(metadata[1]) >= len(EDGE_TYPES)


def test_val_extra_relation(tmp_path, caplog):
    data_root = tmp_path / "data"

    train_gdir = data_root / "train" / "graphs"
    train_gdir.mkdir(parents=True)
    _make_graph(train_gdir / "a.pt", ["r0"])
    (data_root / "train" / "labels.csv").write_text("sha256,label\na,0\n")

    val_gdir = data_root / "val" / "graphs"
    val_gdir.mkdir(parents=True)
    _make_graph(val_gdir / "b.pt", ["r1"])
    (data_root / "val" / "labels.csv").write_text("sha256,label\nb,0\n")

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    ckpt_path = tmp_path / "enc.pt"
    torch.save({"model": enc.state_dict()}, ckpt_path)

    argv = [
        "train_res_gcl",
        "--encoder-checkpoint",
        str(ckpt_path),
        "--splits-dir",
        str(data_root),
        "--epochs",
        "1",
        "--batch-size",
        "1",
        "--device",
        "cpu",
        "--output",
        str(tmp_path / "model.pt"),
    ]

    mod = importlib.import_module("src.cli.train_res_gcl")
    caplog.set_level("INFO")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert any("Epoch 1" in rec.message for rec in caplog.records)


def test_collect_metadata_invalid_edge_type_detail(tmp_path):
    gdir = tmp_path / "train" / "graphs"
    gdir.mkdir(parents=True)

    from src.graphs.normalizers import schema

    _make_invalid_graph(gdir / "a.pt", len(schema.EDGE_REL_ID))

    (tmp_path / "train" / "labels.csv").write_text("sha256,label\na,0\n")

    ds = GraphDataset(tmp_path, split="train", require_labels=True)

    with pytest.raises(ValueError, match="a.pt"):
        collect_dataset_metadata(ds, strict=True)

