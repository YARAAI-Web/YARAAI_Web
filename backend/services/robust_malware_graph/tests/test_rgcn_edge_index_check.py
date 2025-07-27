import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import importlib.util
import sys
from pathlib import Path

import torch
from torch_geometric.data import HeteroData

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "src.models.gnn.encoder", root / "src" / "models" / "gnn" / "encoder.py"
)
encoder_mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = encoder_mod
spec.loader.exec_module(encoder_mod)
RGCNEncoder = encoder_mod.RGCNEncoder


def test_forward_raises_on_invalid_edge_index():
    g = HeteroData()
    g["n"].x = torch.randn(2, 4)
    g["n"].num_nodes = 2
    g["n"].batch = torch.zeros(2, dtype=torch.long)
    # edge referencing out-of-range node id 2
    g[("n", "r0", "n")].edge_index = torch.tensor([[0], [2]])

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )

    with pytest.raises(ValueError, match="edge_index contains invalid node id"):
        enc(g)


def test_forward_raises_on_negative_edge_index(monkeypatch):
    g = HeteroData()
    g["n"].x = torch.randn(2, 4)
    g["n"].num_nodes = 2
    g["n"].batch = torch.zeros(2, dtype=torch.long)
    g[("n", "r0", "n")].edge_index = torch.tensor([[0], [1]])

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )

    orig_to_homogeneous = HeteroData.to_homogeneous

    def patched(self, *args, **kwargs):
        homo = orig_to_homogeneous(self, *args, **kwargs)
        homo.edge_index[1, 0] = -1
        return homo

    monkeypatch.setattr(HeteroData, "to_homogeneous", patched)

    with pytest.raises(ValueError, match="edge_index contains negative node id"):
        enc(g)

    monkeypatch.setattr(HeteroData, "to_homogeneous", orig_to_homogeneous)
