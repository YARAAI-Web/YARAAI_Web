import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.explain.utils.hetero import (
    get_edge_store,
    edge_mask_to_global,
    iter_edge_types,
    filter_view,
)


def _make_graph():
    g = HeteroData()
    g["a"].num_nodes = 3
    g["b"].num_nodes = 2
    g[("a", "rel", "a")].edge_index = torch.tensor([[0, 1], [1, 2]])
    g[("a", "rel2", "b")].edge_index = torch.tensor([[0], [1]])
    return g


def test_get_edge_store_global_index():
    g = _make_graph()
    ei, store, gid = get_edge_store(g, ("a", "rel", "a"))
    assert store is g[("a", "rel", "a")]
    assert torch.equal(ei, g[("a", "rel", "a")].edge_index)
    assert gid.tolist() == [0, 1]

    _, _, gid2 = get_edge_store(g, ("a", "rel2", "b"))
    assert gid2.tolist() == [2]


def test_edge_mask_to_global():
    g = _make_graph()
    _, _, gid = get_edge_store(g, ("a", "rel", "a"))
    mask = torch.tensor([1, 0], dtype=torch.float)
    out = edge_mask_to_global(mask, gid, 3)
    assert out.tolist() == [1, 0, 0]


def test_iter_edge_types_wildcard():
    g = _make_graph()
    etypes = list(iter_edge_types(g, "rel*"))
    assert set(etypes) == {("a", "rel", "a"), ("a", "rel2", "b")}
    etypes = list(iter_edge_types(g, "rel2"))
    assert etypes == [("a", "rel2", "b")]


def test_iter_edge_types_none_returns_all():
    g = _make_graph()
    assert list(iter_edge_types(g, None)) == list(g.edge_types)
    # also test default argument
    assert list(iter_edge_types(g)) == list(g.edge_types)


def test_filter_view_removes_edges_and_nodes():
    g = _make_graph()
    out = filter_view(g, "rel")
    assert ("a", "rel", "a") in out.edge_types
    assert ("a", "rel2", "b") not in out.edge_types
    assert "b" not in out.node_types


def test_filter_view_none_returns_graph():
    g = _make_graph()
    out = filter_view(g, None)
    assert list(out.edge_types) == list(g.edge_types)
    assert list(out.node_types) == list(g.node_types)


def test_iter_edge_types_explicit_none():
    g = _make_graph()
    result = list(iter_edge_types(g, None))
    assert result == list(g.edge_types)


def test_filter_view_explicit_none_identity():
    g = _make_graph()
    out = filter_view(g, None)
    assert out is g
