import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData, Data

from src.explain.cfg_explainer import explain_cfg, GumbelMaskSelector
from src.explain.utils.hetero import ensure_edgeaware_selector


class DummyModel(torch.nn.Module):
    def forward(self, g):
        return torch.tensor([0.5])


def build_cfg_graph():
    g = HeteroData()
    g["bb"].num_nodes = 3
    g["bb"].x = torch.zeros(3, 1)
    ei = torch.tensor([[0, 1], [1, 2]], dtype=torch.long)
    g[("bb", "cfg", "bb")].edge_index = ei
    g[("bb", "cfg", "bb")].edge_type = torch.zeros(ei.size(1), dtype=torch.long)
    return g


def build_ast_graph():
    ast = Data(span=torch.tensor([[0, 0], [1, 1], [2, 2]], dtype=torch.long), num_nodes=3)
    return ast


def test_explain_cfg_runs(monkeypatch):
    cfg = build_cfg_graph()
    ast = build_ast_graph()

    selector = GumbelMaskSelector(view="cfg")

    def fake_train_selector(graph, model, **kw):
        ensure_edgeaware_selector(selector, graph)
        return selector

    monkeypatch.setattr("robust_malware_graph.explain.train_selector", fake_train_selector)

    result = explain_cfg(
        cfg,
        ast,
        DummyModel(),
        selector_kwargs={},
        ranker_kwargs={"k": 1, "num_permutations": 1},
    )

    assert isinstance(result["sel_nodes"], list)
