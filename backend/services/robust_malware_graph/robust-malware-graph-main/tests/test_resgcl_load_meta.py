import types
import pytest

pytest.importorskip("torch")

import torch

# stub modules for minimal encoder operations
stub_tg = types.ModuleType("torch_geometric")
stub_nn = types.ModuleType("torch_geometric.nn")

class DummyRGCNConv(torch.nn.Module):
    def __init__(self, in_channels, out_channels, num_relations, num_bases):
        super().__init__()
        self.weight = torch.nn.Parameter(torch.empty(num_relations, in_channels, out_channels))
    def forward(self, x, edge_index, edge_type):
        return x

def global_mean_pool(x, batch):
    return x

stub_nn.RGCNConv = DummyRGCNConv
stub_nn.global_mean_pool = global_mean_pool
stub_tg.nn = stub_nn
import sys
sys.modules.setdefault("torch_geometric", stub_tg)
sys.modules.setdefault("torch_geometric.nn", stub_nn)

from src.models.gnn.encoder import RGCNEncoder
from src.models.gnn.res_wrapper import RESGCLClassifier


def test_load_with_meta(tmp_path):
    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    model = RESGCLClassifier(encoder=enc)
    ckpt = tmp_path / "model.pt"
    torch.save({"model": model.state_dict()}, ckpt)
    meta = {
        "node_types": ["n"],
        "edge_types": [("n", "r0", "n")],
        "in_dims": {"n": 4},
        "num_relations": 1,
    }
    torch.save(meta, ckpt.with_suffix(".meta.pkl"))

    loaded = RESGCLClassifier.load_from_checkpoint(ckpt)
    assert isinstance(loaded.encoder, RGCNEncoder)
    assert loaded.encoder.node_types == ["n"]


def test_head_uses_encoder_out_dim():
    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=5,
    )
    model = RESGCLClassifier(encoder=enc, head="binary_mlp")
    assert model.head.fc1.in_features == enc.out_dim
