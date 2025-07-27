import importlib
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData


def test_cli_prunes_and_saves(tmp_path, monkeypatch):
    g = HeteroData()
    g["bb"].x = torch.zeros(2, 1)
    g["bb"].num_nodes = 2
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [1]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    class DummySelector:
        initialized = True
        view = "cfg"
        def hard_selection(self, graph):
            return {"bb": torch.tensor([0])}

    sel_path = tmp_path / "selector.pt"
    torch.save(DummySelector(), sel_path)

    class DummyModel:
        def to(self, device):
            return self
        def eval(self):
            return self
        def __call__(self, data, return_logits=False):
            return torch.tensor(1.0)

    def fake_load(path, map_location=None):
        return DummyModel()
    monkeypatch.setattr(
        "src.models.gnn.res_wrapper.RESGCLClassifier.load_from_checkpoint",
        fake_load,
    )

    mod = importlib.import_module("src.cli.explain_refine")
    out_path = tmp_path / "pruned.pt"
    mod.main([str(sel_path), str(gpath), "--model", str(tmp_path / "model.pt"), "--save-path", str(out_path)])

    assert out_path.exists()

