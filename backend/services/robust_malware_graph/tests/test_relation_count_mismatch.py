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
    for r in rels:
        ei = torch.tensor([[0, 1], [1, 0]])
        g[("n", r, "n")].edge_index = ei
        idx = int(r[1:]) if r.startswith("r") else 0
        g[("n", r, "n")].edge_type = torch.full((ei.size(1),), idx, dtype=torch.long)
    torch.save(g, path)


def test_relation_mismatch_raises(tmp_path):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_graph(gdir / "a.pt", ["r0", "r1"])
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
    orig_argv = sys.argv
    sys.argv = argv
    try:
        with pytest.raises(ValueError, match="Relation count mismatch"):
            mod.main()
    finally:
        sys.argv = orig_argv
