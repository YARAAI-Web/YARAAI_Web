import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData
from src.models.gnn.encoder import RGCNEncoder


def test_forward_raises_on_unknown_relation():
    g = HeteroData()
    g["n"].x = torch.randn(2, 4)
    g["n"].num_nodes = 2
    g["n"].batch = torch.zeros(2, dtype=torch.long)
    g[("n", "r0", "n")].edge_index = torch.tensor([[0], [1]])
    g[("n", "r1", "n")].edge_index = torch.tensor([[1], [0]])

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )

    with pytest.raises(ValueError, match="edge type index 1"):
        enc(g)


def test_forward_raises_on_negative_edge_type(monkeypatch):
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
        homo.edge_type[0] = -1
        return homo

    monkeypatch.setattr(HeteroData, "to_homogeneous", patched)

    with pytest.raises(ValueError, match="edge type index -1"):
        enc(g)

    monkeypatch.setattr(HeteroData, "to_homogeneous", orig_to_homogeneous)
