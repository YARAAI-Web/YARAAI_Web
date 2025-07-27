import pytest

pytest.importorskip("torch")

import torch
from src.models.gnn.layers import AttentionGate


def _make_graph():
    x = torch.randn(3, 4)
    edge_index = torch.tensor([[0, 1], [1, 2]], dtype=torch.long)
    return x, edge_index


def test_attention_gate_shared_edges():
    x, edge_index = _make_graph()
    gate = AttentionGate(in_dim=4, edge_share=True)
    x_out, ei_out, alpha = gate(x, edge_index)
    assert x_out.shape == x.shape
    assert torch.equal(ei_out, edge_index)
    assert alpha.shape == (edge_index.size(1),)


def test_attention_gate_direction_specific():
    x, edge_index = _make_graph()
    gate = AttentionGate(in_dim=4, edge_share=False)
    x_out, ei_out, alpha = gate(x, edge_index)
    E = edge_index.size(1)
    assert x_out.shape == x.shape
    assert ei_out.shape == (2, 2 * E)
    assert torch.equal(ei_out[:, :E], edge_index)
    assert torch.equal(ei_out[:, E:], edge_index.flip(0))
    assert alpha.shape == (2 * E,)
