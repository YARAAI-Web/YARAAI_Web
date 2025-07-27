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


def test_main_auto_reinit_on_dim_mismatch(tmp_path, caplog):
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

    logdir = tmp_path / "log"
    argv = [
        "finetune_supcon",
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
        "--logdir",
        str(logdir),
    ]

    mod = importlib.import_module("src.cli.finetune_supcon")
    caplog.set_level("INFO")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert any("dimension mismatch" in rec.message for rec in caplog.records)
    assert any("Checkpoint was trained with smaller features" in rec.message for rec in caplog.records)
    assert any("Epoch 1" in rec.message for rec in caplog.records)
