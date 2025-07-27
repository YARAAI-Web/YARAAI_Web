import sys
import types
import logging
import pytest

pytest.importorskip("torch")

import torch

# stub minimal torch_geometric modules
stub_tg = types.ModuleType("torch_geometric")
stub_nn = types.ModuleType("torch_geometric.nn")

class DummyRGCNConv(torch.nn.Module):
    def __init__(self, in_channels, out_channels, num_relations, num_bases):
        super().__init__()
        self.weight = torch.nn.Parameter(
            torch.randn(num_relations, in_channels, out_channels)
        )
        self.comp = torch.nn.Parameter(torch.randn(num_relations, num_relations))

    def forward(self, x, edge_index, edge_type):  # pragma: no cover
        return x

stub_nn.RGCNConv = DummyRGCNConv
stub_nn.global_mean_pool = lambda x, batch: x
stub_tg.nn = stub_nn
sys.modules.setdefault("torch_geometric", stub_tg)
sys.modules.setdefault("torch_geometric.nn", stub_nn)

from src.models.gnn.encoder import RGCNEncoder
from src.common.utils import filter_state_dict


class DummyCompConv(torch.nn.Module):
    def __init__(self, rels: int, bases: int) -> None:
        super().__init__()
        self.comp = torch.nn.Parameter(torch.randn(bases, rels))

    def forward(self, x):  # pragma: no cover - unused
        return x


class SimpleModel(torch.nn.Module):
    def __init__(self, rels: int, bases: int) -> None:
        super().__init__()
        self.convs = torch.nn.ModuleList([DummyCompConv(rels, bases)])


def test_filter_rgcnconv_partial_copy(caplog):
    enc_old = RGCNEncoder(
        metadata=(["n"], [("n", f"r{i}", "n") for i in range(3)]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=4,
        residual=False,
    )
    enc_new = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=4,
        residual=False,
    )

    state = enc_old.state_dict()
    logger = logging.getLogger("test")
    caplog.set_level("INFO", logger="test")
    filtered = filter_state_dict(enc_new, state, logger=logger)

    w_key = "convs.0.weight"
    assert torch.allclose(filtered[w_key], state[w_key][:1])
    c_key = "convs.0.comp"
    assert torch.allclose(filtered[c_key], state[c_key][:1, :1])
    assert caplog.text.count("copied 1/3 relations") == 2


def test_filter_comp_rectangular(caplog):
    old = SimpleModel(rels=3, bases=2)
    new = SimpleModel(rels=1, bases=2)

    state = old.state_dict()
    logger = logging.getLogger("test")
    caplog.set_level("INFO", logger="test")
    filtered = filter_state_dict(new, state, logger=logger)

    key = "convs.0.comp"
    assert filtered[key].shape == (2, 1)
    assert torch.allclose(filtered[key], state[key][:2, :1])
    assert "bases and" in caplog.text
