import importlib
import pytest
from pathlib import Path

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import Data, HeteroData
import types


class DummyModel:
    def __init__(self):
        self.encoder = types.SimpleNamespace(target_node="bb", input_proj={})

    def to(self, device):
        return self

    def eval(self):
        return self

    def __call__(self, *args, **kwargs):
        return torch.tensor([0.0])


class DummySelector:
    def hard_selection(self, g):
        key = next(iter(g.edge_types))
        num = g[key].edge_index.size(1)
        return {str(key): torch.arange(num)}


def test_cli_invokes_train_selector(tmp_path, monkeypatch):
    cfg = Data(x=torch.zeros(1, 1), edge_index=torch.tensor([[0], [0]]), num_nodes=1)
    gpath = tmp_path / "cfg.pt"
    torch.save(cfg, gpath)
    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    dummy_model = DummyModel()
    orig_load = torch.load

    def fake_load(path, map_location=None):
        if Path(path) == gpath:
            return cfg
        if Path(path) == mpath:
            return dummy_model
        return orig_load(path, map_location=map_location)

    monkeypatch.setattr(torch, "load", fake_load)

    captured = {}

    def fake_train(graph, model, *a, **kw):
        captured["graph"] = graph
        captured["model"] = model
        return DummySelector(), graph, {"pred": 0, "prob": 0.0}

    monkeypatch.setattr("src.cli.explainer_train._train_selector_for_graph", fake_train)

    mod = importlib.import_module("src.cli.explainer_train")
    out = tmp_path / "out.pt"
    mod.main(["single", str(gpath), "--model", str(mpath), "--output", str(out), "--epochs", "1"])

    assert captured["graph"] is cfg
    assert captured["model"] is dummy_model
    assert out.exists()
    assert out.with_suffix(".pred.json").exists()


def test_cli_handles_heterodata(tmp_path, monkeypatch):
    g = HeteroData()
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "cfg.pt"
    torch.save(g, gpath)
    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    dummy_model = DummyModel()
    orig_load = torch.load

    def fake_load(path, map_location=None):
        if Path(path) == gpath:
            return g
        if Path(path) == mpath:
            return dummy_model
        return orig_load(path, map_location=map_location)

    monkeypatch.setattr(torch, "load", fake_load)

    monkeypatch.setattr(
        "src.cli.explainer_train._train_selector_for_graph",
        lambda *a, **kw: (DummySelector(), g, {"pred": 0, "prob": 0.0}),
    )

    mod = importlib.import_module("src.cli.explainer_train")
    out = tmp_path / "out.pt"
    mod.main(["single", str(gpath), "--model", str(mpath), "--output", str(out), "--epochs", "1"])

    assert out.exists()
    assert out.with_suffix(".pred.json").exists()


def test_cli_dataset_mode(tmp_path, monkeypatch):
    g = HeteroData()
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "a.pt"
    torch.save(g, gpath)
    csv = tmp_path / "meta.csv"
    csv.write_text("sha256,label\na,1\n")
    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    dummy_model = DummyModel()

    def fake_load(path, weights_only=False, map_location=None):
        if Path(path) == gpath:
            return g
        if Path(path) == mpath:
            return dummy_model
        raise FileNotFoundError

    monkeypatch.setattr(torch, "load", fake_load)
    monkeypatch.setattr(
        "src.cli.explainer_train._train_selector_for_graph",
        lambda *a, **kw: (DummySelector(), g, {"pred": 0, "prob": 0.0}),
    )

    mod = importlib.import_module("src.cli.explainer_train")
    outdir = tmp_path / "out"
    mod.main([
        "batch",
        "--graph-dir",
        str(tmp_path),
        "--meta-csv",
        str(csv),
        "--output-dir",
        str(outdir),
        "--model",
        str(mpath),
        "--epochs",
        "1",
    ])

    assert (outdir / "a_selector.pt").exists()
    assert (outdir / "a_pred.json").exists()


def test_cli_ast_flag_loads_view(tmp_path, monkeypatch):
    import json

    view_root = tmp_path / "data" / "views"
    view_dir = view_root / "ast"
    view_dir.mkdir(parents=True)
    sha = "sample"
    (view_dir / f"{sha}.json").write_text(json.dumps({"nodes": [{"id": 0, "kind": "file"}], "edges": []}))

    gpath = tmp_path / f"{sha}.pt"
    gpath.write_text("stub")  # unused placeholder
    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    dummy_model = DummyModel()

    orig_load = torch.load

    def fake_load(path, map_location=None, weights_only=False):
        if Path(path) == mpath:
            return dummy_model
        return orig_load(path, map_location=map_location)

    monkeypatch.setattr(torch, "load", fake_load)

    captured = {}

    def fake_train(graph, model, *a, **kw):
        captured["type"] = type(graph)
        return DummySelector(), graph, {"pred": 0, "prob": 0.0}

    monkeypatch.setattr("src.cli.explainer_train._train_selector_for_graph", fake_train)

    mod = importlib.import_module("src.cli.explainer_train")
    monkeypatch.chdir(tmp_path)
    out = tmp_path / "out.pt"
    mod.main([
        "single",
        str(gpath),
        "--model",
        str(mpath),
        "--output",
        str(out),
        "--epochs",
        "1",
        "--ast",
    ])

    assert out.exists()
    assert out.with_suffix(".pred.json").exists()
    assert captured["type"].__name__ == "HeteroData"


def test_cli_custom_view_dir(tmp_path, monkeypatch):
    import json

    view_root = tmp_path / "views"
    view_dir = view_root / "cfg"
    view_dir.mkdir(parents=True)
    sha = "sample"
    (view_dir / f"{sha}.json").write_text(json.dumps({"nodes": [{"id": 0, "kind": "file"}], "edges": []}))

    gpath = tmp_path / f"{sha}.pt"
    gpath.write_text("stub")
    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    dummy_model = DummyModel()
    orig_load = torch.load

    def fake_load(path, map_location=None, weights_only=False):
        if Path(path) == mpath:
            return dummy_model
        return orig_load(path, map_location=map_location)

    monkeypatch.setattr(torch, "load", fake_load)

    captured = {}

    def fake_train(graph, model, *a, **kw):
        captured["type"] = type(graph)
        return DummySelector(), graph, {"pred": 0, "prob": 0.0}

    monkeypatch.setattr("src.cli.explainer_train._train_selector_for_graph", fake_train)

    mod = importlib.import_module("src.cli.explainer_train")
    monkeypatch.chdir(tmp_path)
    out = tmp_path / "out.pt"
    mod.main([
        "single",
        str(gpath),
        "--model",
        str(mpath),
        "--output",
        str(out),
        "--epochs",
        "1",
        "--cfg",
    ])

    assert out.exists()
    assert out.with_suffix(".pred.json").exists()
    assert captured["type"].__name__ == "HeteroData"


def test_cli_view_flag_mismatch(tmp_path, monkeypatch):
    g = HeteroData()
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    dummy_model = DummyModel()
    orig_load = torch.load

    def fake_load(path, map_location=None, weights_only=False):
        if Path(path) == gpath:
            return g
        if Path(path) == mpath:
            return dummy_model
        return orig_load(path, map_location=map_location)

    monkeypatch.setattr(torch, "load", fake_load)
    monkeypatch.setattr(
        "src.cli.explainer_train._train_selector_for_graph",
        lambda *a, **kw: (DummySelector(), g, {"pred": 0, "prob": 0.0}),
    )

    view_root = tmp_path / "views"
    view_path = view_root / "cfg"
    (view_path / "ast").mkdir(parents=True)
    (view_path / "ast" / "graph.json").write_text("{}")

    mod = importlib.import_module("src.cli.explainer_train")
    out = tmp_path / "out.pt"
    mod.main([
        "single",
        str(gpath),
        "--model",
        str(mpath),
        "--output",
        str(out),
        "--epochs",
        "1",
        "--ast",
    ])
    assert out.exists()
    assert out.with_suffix(".pred.json").exists()


def test_cli_view_flag_sets_view(tmp_path, monkeypatch):
    import json

    view_root = tmp_path / "data" / "views"
    view_dir = view_root / "ast"
    view_dir.mkdir(parents=True)
    sha = "sample"
    (view_dir / f"{sha}.json").write_text(
        json.dumps({"nodes": [{"id": 0, "kind": "file"}], "edges": []})
    )

    gpath = tmp_path / f"{sha}.pt"
    gpath.write_text("stub")  # unused placeholder
    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    dummy_model = DummyModel()

    orig_load = torch.load

    def fake_load(path, map_location=None, weights_only=False):
        if Path(path) == mpath:
            return dummy_model
        return orig_load(path, map_location=map_location)

    monkeypatch.setattr(torch, "load", fake_load)

    captured = {}

    def fake_train(graph, model, *a, **kw):
        captured["type"] = type(graph)
        return DummySelector(), graph, {"pred": 0, "prob": 0.0}

    monkeypatch.setattr(
        "src.cli.explainer_train._train_selector_for_graph",
        fake_train,
    )

    mod = importlib.import_module("src.cli.explainer_train")
    monkeypatch.chdir(tmp_path)
    out = tmp_path / "out.pt"
    mod.main([
        "single",
        str(gpath),
        "--model",
        str(mpath),
        "--output",
        str(out),
        "--epochs",
        "1",
        "--ast",
    ])

    assert out.exists()
    assert out.with_suffix(".pred.json").exists()
    assert captured["type"].__name__ == "HeteroData"
