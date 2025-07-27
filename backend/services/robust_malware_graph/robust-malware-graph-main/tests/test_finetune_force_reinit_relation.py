import importlib
import sys
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.models.gnn.encoder import RGCNEncoder


def _make_graph(path: Path, rels: list[str]) -> None:
    g = HeteroData()
    g["n"].x = torch.randn(2, 4)
    g["n"].num_nodes = 2
    for i, r in enumerate(rels):
        ei = torch.tensor([[0, 1], [1, 0]])
        g[("n", r, "n")].edge_index = ei
        g[("n", r, "n")].edge_type = torch.full((ei.size(1),), i, dtype=torch.long)
    torch.save(g, path)


def test_force_reinit_ignores_meta_rel_count(tmp_path, caplog):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_graph(gdir / "a.pt", ["r0", "r1", "r2", "r3"])
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
            "edge_types": [
                ("n", "r0", "n"),
                ("n", "r1", "n"),
                ("n", "r2", "n"),
                ("n", "r3", "n"),
            ],
            "in_dims": {"n": 4},
            "num_relations": 5,
        },
        meta_path,
    )

    logdir = tmp_path / "log"
    argv = [
        "finetune_supcon",
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
        "--logdir",
        str(logdir),
        "--force-reinit",
    ]

    mod = importlib.import_module("src.cli.finetune_supcon")
    caplog.set_level("INFO")
    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert any("Epoch 1" in rec.message for rec in caplog.records)
