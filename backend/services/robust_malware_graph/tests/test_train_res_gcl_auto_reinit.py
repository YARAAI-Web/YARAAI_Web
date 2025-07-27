import importlib
import sys
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.models.gnn.encoder import RGCNEncoder


def _make_graph(path: Path, feat_dim: int) -> None:
    g = HeteroData()
    g["n"].x = torch.randn(2, feat_dim)
    g["n"].num_nodes = 2
    ei = torch.tensor([[0, 1], [1, 0]])
    g[("n", "r0", "n")].edge_index = ei
    g[("n", "r0", "n")].edge_type = torch.zeros(ei.size(1), dtype=torch.long)
    torch.save(g, path)


def _make_attr_graph(path: Path) -> None:
    g = HeteroData()
    g["n"].x = torch.randn(2, 4)
    g["n"].num_nodes = 2
    g["n"].bar_id = torch.tensor([0, 1])
    g["n"].baz_id = torch.tensor([1, 0])
    ei = torch.tensor([[0, 1], [1, 0]])
    g[("n", "r0", "n")].edge_index = ei
    g[("n", "r0", "n")].edge_type = torch.zeros(ei.size(1), dtype=torch.long)
    torch.save(g, path)


def test_auto_reinit_with_meta(tmp_path, caplog):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_graph(gdir / "a.pt", 6)
        (data_root / split / "labels.csv").write_text("sha256,label\na,0\n")

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    ckpt_path = tmp_path / "enc.pt"
    torch.save({"model": enc.state_dict()}, ckpt_path)

    meta_path = tmp_path / "enc.meta.pkl"
    torch.save(
        {
            "node_types": ["n"],
            "edge_types": [("n", "r0", "n")],
            "in_dims": {"n": 4},
            "num_relations": 1,
        },
        meta_path,
    )

    out_file = tmp_path / "model.pt"
    argv = [
        "train_res_gcl",
        "--encoder-checkpoint",
        str(ckpt_path),
        "--meta-path",
        str(meta_path),
        "--splits-dir",
        str(data_root),
        "--epochs",
        "1",
        "--batch-size",
        "1",
        "--device",
        "cpu",
        "--output",
        str(out_file),
    ]

    mod = importlib.import_module("src.cli.train_res_gcl")
    caplog.set_level("INFO")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert any("reinitializing" in rec.message or "dimension mismatch" in rec.message for rec in caplog.records)
    assert any("Epoch 1" in rec.message for rec in caplog.records)
    meta_file = out_file.with_suffix(".meta.pkl")
    assert meta_file.is_file()
    meta = torch.load(meta_file)
    assert "vocab_size" in meta


def test_meta_relation_count_used(tmp_path):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_graph(gdir / "a.pt", 4)
        (data_root / split / "labels.csv").write_text("sha256,label\na,0\n")

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n"), ("n", "r1", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    ckpt = tmp_path / "enc.pt"
    torch.save({"model": enc.state_dict()}, ckpt)

    meta_path = tmp_path / "enc.meta.pkl"
    torch.save(
        {
            "node_types": ["n"],
            "edge_types": [("n", "r0", "n"), ("n", "r1", "n")],
            "in_dims": {"n": 4},
            "num_relations": 2,
        },
        meta_path,
    )

    out_path = tmp_path / "model.pt"
    argv = [
        "train_res_gcl",
        "--encoder-checkpoint",
        str(ckpt),
        "--meta-path",
        str(meta_path),
        "--splits-dir",
        str(data_root),
        "--epochs",
        "1",
        "--batch-size",
        "1",
        "--device",
        "cpu",
        "--output",
        str(out_path),
    ]

    mod = importlib.import_module("src.cli.train_res_gcl")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    state = torch.load(out_path)["model"]
    assert state["encoder.convs.0.weight"].size(0) == 2
    assert out_path.with_suffix(".meta.pkl").is_file()


def test_reinit_metadata_mismatch_error(tmp_path):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_graph(gdir / "a.pt", 4)
        (data_root / split / "labels.csv").write_text("sha256,label\na,0\n")

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    ckpt = tmp_path / "enc.pt"
    torch.save({"model": enc.state_dict()}, ckpt)

    meta_path = tmp_path / "enc.meta.pkl"
    torch.save(
        {
            "node_types": ["n"],
            "edge_types": [("n", "r0", "n"), ("n", "r1", "n")],
            "in_dims": {"n": 4},
            "num_relations": 2,
        },
        meta_path,
    )

    argv = [
        "train_res_gcl",
        "--encoder-checkpoint",
        str(ckpt),
        "--meta-path",
        str(meta_path),
        "--splits-dir",
        str(data_root),
        "--epochs",
        "1",
        "--batch-size",
        "1",
        "--device",
        "cpu",
        "--output",
        str(tmp_path / "out.pt"),
    ]

    mod = importlib.import_module("src.cli.train_res_gcl")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        with pytest.raises(RuntimeError,
                           match="Dataset metadata incompatible"):
            mod.main()
    finally:
        sys.argv = orig_argv


def test_dataloaders_recreated_after_reinit(tmp_path, monkeypatch, caplog):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_attr_graph(gdir / "a.pt")
        (data_root / split / "labels.csv").write_text("sha256,label\na,0\n")

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 5},
        attr_names={"n": ["foo"]},
        attr_dim=1,
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    ckpt = tmp_path / "enc.pt"
    torch.save({"model": enc.state_dict()}, ckpt)

    meta_path = tmp_path / "enc.meta.pkl"
    torch.save(
        {
            "node_types": ["n"],
            "edge_types": [("n", "r0", "n")],
            "in_dims": {"n": 5},
            "num_relations": 1,
        },
        meta_path,
    )

    calls = []
    importlib.invalidate_caches()
    mod = importlib.import_module("src.cli.train_res_gcl")

    orig_make = mod.make_dataloaders

    def rec_make(*args, **kwargs):
        calls.append(kwargs.get("attr_names"))
        return orig_make(*args, **kwargs)

    monkeypatch.setattr(mod, "make_dataloaders", rec_make)

    out_path = tmp_path / "model.pt"
    argv = [
        "train_res_gcl",
        "--encoder-checkpoint",
        str(ckpt),
        "--meta-path",
        str(meta_path),
        "--splits-dir",
        str(data_root),
        "--epochs",
        "1",
        "--batch-size",
        "1",
        "--device",
        "cpu",
        "--output",
        str(out_path),
    ]

    orig_argv = sys.argv
    sys.argv = argv
    caplog.set_level("INFO")
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert len(calls) >= 2
    assert calls[0] == {"n": ["foo"]}
    assert calls[-1] == {"n": ["bar", "baz"]}
    assert any("Epoch 1" in rec.message for rec in caplog.records)
    assert out_path.with_suffix(".meta.pkl").is_file()


def test_meta_embed_expansion(tmp_path):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        g = HeteroData()
        g["n"].x = torch.randn(1, 4)
        g["n"].num_nodes = 1
        g["n"].foo_id = torch.tensor([3])
        ei = torch.tensor([[0], [0]])
        g[("n", "r0", "n")].edge_index = ei
        g[("n", "r0", "n")].edge_type = torch.zeros(1, dtype=torch.long)
        torch.save(g, gdir / "a.pt")
        (data_root / split / "labels.csv").write_text("sha256,label\na,0\n")

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        attr_names={"n": ["foo"]},
        vocab_size=2,
        attr_dim=1,
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    ckpt = tmp_path / "enc.pt"
    torch.save({"model": enc.state_dict()}, ckpt)

    out_path = tmp_path / "model.pt"
    argv = [
        "train_res_gcl",
        "--encoder-checkpoint",
        str(ckpt),
        "--splits-dir",
        str(data_root),
        "--epochs",
        "1",
        "--batch-size",
        "1",
        "--device",
        "cpu",
        "--output",
        str(out_path),
        "--force-reinit",
    ]

    mod = importlib.import_module("src.cli.train_res_gcl")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    state = torch.load(out_path)["model"]
    assert state["encoder.meta_embed.weight"].size(0) >= 4
