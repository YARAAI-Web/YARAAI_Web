import argparse
import types
import json
from pathlib import Path

import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.cli.explainer_train import _train_selector_for_graph


class DummyModel:
    def __init__(self):
        self.encoder = types.SimpleNamespace(target_node="bb", input_proj={})
        self.calls = 0

    def to(self, device):
        return self

    def eval(self):
        return self

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return torch.tensor([0.0])


def build_graph():
    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    ei = torch.tensor([[0], [0]])
    g[("bb", "cfg", "bb")].edge_index = ei
    g[("bb", "cfg", "bb")].edge_type = torch.zeros(1, dtype=torch.long)
    g.sha256 = "abc"
    return g


def make_args(cache_path):
    return argparse.Namespace(
        ast=False,
        cfg=False,
        fcg=False,
        syscall=False,
        view=Path("data/views/cfg"),
        full_cpu=False,
        full_mini_batch=False,
        cluster_parts=0,
        cluster_batch_size=1,
        cluster_train=False,
        amp=False,
        num_neighbors=1,
        num_hops=1,
        batch_size=1,
        epochs=0,
        lr=1e-3,
        alpha=1.0,
        beta=0.0,
        plot_path=None,
        score_cache=cache_path,
        no_full_score=False,
    )


def test_score_cache(tmp_path):
    cache = tmp_path / "scores.json"
    g = build_graph()
    model = DummyModel()
    args = make_args(cache)
    device = torch.device("cpu")

    _train_selector_for_graph(g, model, args, device)
    assert cache.exists()
    data = json.loads(cache.read_text())
    assert data["abc"] == 0.0
    first_calls = model.calls

    model.calls = 0
    _train_selector_for_graph(g, model, args, device)
    # second call should skip full score computation
    assert model.calls < first_calls


def test_no_full_score_option(tmp_path):
    cache = tmp_path / "scores.json"
    g = build_graph()
    model = DummyModel()
    args = make_args(cache)
    args.no_full_score = True
    device = torch.device("cpu")

    _train_selector_for_graph(g, model, args, device)
    assert not cache.exists()
    assert model.calls == 0


class ParamModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = types.SimpleNamespace(target_node="bb", input_proj={})
        self.w = torch.nn.Parameter(torch.zeros(1, 1))

    def to(self, device):
        return self

    def eval(self):
        return self

    def forward(self, *args, **kwargs):
        return self.w.sum().unsqueeze(0)


def test_fp16_cast(tmp_path):
    g = build_graph()
    model = ParamModel()
    args = make_args(tmp_path / "scores.json")
    args.fp16 = True
    device = torch.device("cpu")

    _, out, _ = _train_selector_for_graph(g, model, args, device)

    assert next(model.parameters()).dtype == torch.float16
    for store in out.node_stores + out.edge_stores:
        for val in store.values():
            if torch.is_tensor(val) and torch.is_floating_point(val):
                assert val.dtype == torch.float16
