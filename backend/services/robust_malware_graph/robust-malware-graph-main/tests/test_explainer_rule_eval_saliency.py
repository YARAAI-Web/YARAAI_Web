import importlib
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData
import types
import sys


class DummyEncoder:
    def __init__(self):
        self.attr_names: dict[str, list[str]] = {}
        self.metadata = (["n"], [])


class DummyClassifier:
    def __init__(self):
        self.encoder = DummyEncoder()

    def to(self, device):
        return self

    def eval(self):
        return self


class DummyExplainer:
    def __init__(self, classifier):
        self.model = classifier
        self.last_mask = None

    def eval(self):
        return self

    def __call__(self, g, embeddings=None):
        return torch.tensor([0.5]), {"aux": True}

    def get_node_saliency(self, g, mask):
        self.last_mask = mask
        return {nt: torch.ones(g[nt].num_nodes) for nt in g.node_types}


def test_compute_saliency_handles_tuple(monkeypatch):
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    for h in mod.LOGGER.handlers:
        h.filters.clear()

    g = HeteroData()
    g["n"].x = torch.zeros(1, 1)
    g["n"].num_nodes = 1
    g[("n", "r", "n")].edge_index = torch.tensor([[0], [0]])

    classifier = DummyClassifier()
    explainer = DummyExplainer(classifier)
    stub = types.ModuleType("src.cli.explainer_train")
    stub._compute_node_embeddings = lambda g, enc: {"n": torch.zeros(g["n"].num_nodes, 1)}
    sys.modules["src.cli.explainer_train"] = stub

    sal = mod._compute_saliency_with_explainer(
        g, classifier, explainer, torch.device("cpu")
    )

    assert isinstance(sal, dict)
    assert sal["n"].tolist() == [1.0]
    assert isinstance(explainer.last_mask, torch.Tensor)
