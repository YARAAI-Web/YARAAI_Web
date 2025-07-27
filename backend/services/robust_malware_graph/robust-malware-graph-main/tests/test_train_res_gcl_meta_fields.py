import importlib
import sys
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.models.gnn.encoder import RGCNEncoder


def _make_graph(path: Path) -> None:
    g = HeteroData()
    g["n"].x = torch.randn(2, 4)
    g["n"].num_nodes = 2
    ei = torch.tensor([[0, 1], [1, 0]])
    g[("n", "r0", "n")].edge_index = ei
    g[("n", "r0", "n")].edge_type = torch.zeros(ei.size(1), dtype=torch.long)
    torch.save(g, path)


def _prepare(tmp_path: Path):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_graph(gdir / "a.pt")
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
            "edge_types": [("n", "r0", "n")],
            "in_dims": {"n": 4},
            "num_relations": 1,
        },
        meta_path,
    )

    return data_root, ckpt, meta_path


def test_meta_missing_fields_error(tmp_path):
    data_root, ckpt, meta_path = _prepare(tmp_path)

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
        str(tmp_path / "model.pt"),
    ]

    mod = importlib.import_module("src.cli.train_res_gcl")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        with pytest.raises(RuntimeError, match="Re-run pretraining or use --force-reinit"):
            mod.main()
    finally:
        sys.argv = orig_argv


def test_force_reinit_allows_missing_fields(tmp_path):
    data_root, ckpt, meta_path = _prepare(tmp_path)

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
        "--force-reinit",
    ]

    mod = importlib.import_module("src.cli.train_res_gcl")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert out_path.is_file()
