import sys
import types
import pytest

pytest.importorskip("torch")

import torch

# Stub minimal torch_geometric modules to allow importing the encoder
stub_tg = types.ModuleType("torch_geometric")
stub_nn = types.ModuleType("torch_geometric.nn")

class DummyRGCNConv(torch.nn.Module):
    def __init__(self, in_channels, out_channels, num_relations, num_bases):
        super().__init__()
        self.weight = torch.nn.Parameter(
            torch.empty(num_relations, in_channels, out_channels)
        )

    def forward(self, x, edge_index, edge_type):  # pragma: no cover
        return x

def global_mean_pool(x, batch):
    return x

stub_nn.RGCNConv = DummyRGCNConv
stub_nn.global_mean_pool = global_mean_pool
stub_tg.nn = stub_nn
sys.modules.setdefault("torch_geometric", stub_tg)
sys.modules.setdefault("torch_geometric.nn", stub_nn)

from src.models.gnn.encoder import RGCNEncoder


def test_from_state_dict_with_meta_embed():
    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        vocab_size=3,
        attr_dim=2,
        hidden_dim=4,
        num_layers=1,
        out_dim=8,
    )
    state = enc.state_dict()
    loaded = RGCNEncoder._from_state_dict(state)
    assert loaded.meta_embed is not None
    assert loaded.meta_embed.weight.shape == enc.meta_embed.weight.shape


def test_load_checkpoint_with_external_attr_names(tmp_path):
    pytest.importorskip("torch_geometric")
    from torch_geometric.data import HeteroData

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 6},
        attr_names={"n": ["foo"]},
        vocab_size=5,
        attr_dim=2,
        hidden_dim=4,
        num_layers=1,
        out_dim=8,
    )
    ckpt = {"model": enc.state_dict()}
    path = tmp_path / "enc.pt"
    torch.save(ckpt, path)

    g = HeteroData()
    g["n"].x = torch.randn(1, 4)
    g["n"].foo_id = torch.tensor([1])
    g["n"].num_nodes = 1

    attr_names = {nt: [k[:-3] for k in g[nt].keys() if k.endswith("_id")]
                  for nt in g.node_types}

    loaded = RGCNEncoder.load_from_checkpoint(path, attr_names=attr_names)
    loaded(g)


def test_load_checkpoint_with_saved_attr_names(tmp_path):
    pytest.importorskip("torch_geometric")
    from torch_geometric.data import HeteroData

    enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 6},
        attr_names={"n": ["foo"]},
        vocab_size=5,
        attr_dim=2,
        hidden_dim=4,
        num_layers=1,
        out_dim=8,
    )
    ckpt = {"model": enc.state_dict(), "attr_names": enc.attr_names}
    path = tmp_path / "enc.pt"
    torch.save(ckpt, path)

    g = HeteroData()
    g["n"].x = torch.randn(1, 4)
    g["n"].foo_id = torch.tensor([1])
    g["n"].num_nodes = 1

    loaded = RGCNEncoder.load_from_checkpoint(path)
    loaded(g)

