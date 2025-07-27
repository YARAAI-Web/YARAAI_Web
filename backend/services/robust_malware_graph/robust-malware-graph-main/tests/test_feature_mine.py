import json
import argparse
import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")
pytest.importorskip("numpy")

import torch
from torch_geometric.data import HeteroData
from pathlib import Path
import types

from src.cli import rulegen_cli



class DummyMiner:
    def __init__(self, calls):
        self.calls = calls

    def __call__(self, graph, sal):
        sha = graph.metadata.get("sha256")
        self.calls.append((sha, int(sal.numel())))
        return ["feat"]


class DummyDataset:
    def __init__(self, root):
        graph_dir = Path(root) / "train" / "graphs"
        self.paths = sorted(graph_dir.glob("*.pt"))

    def __len__(self):
        return len(self.paths)

    def __iter__(self):
        for p in self.paths:
            yield torch.load(p)


def _make_graph(path: Path, sha: str) -> None:
    g = HeteroData()
    g["n"].x = torch.zeros(1, 1)
    g["n"].num_nodes = 1
    g.metadata = {"sha256": sha}
    torch.save(g, path)


def test_cmd_feature_mine(tmp_path, monkeypatch):
    root = tmp_path / "data"
    gdir = root / "train" / "graphs"
    gdir.mkdir(parents=True)

    _make_graph(gdir / "a.pt", "a")
    _make_graph(gdir / "b.pt", "b")

    (root / "train" / "labels.csv").write_text("sha256,label\na,1\nb,0\n")

    ext = tmp_path / "ext_labels.csv"
    ext.write_text("sha256,label\na,9\nb,8\n")

    calls = []
    monkeypatch.setattr(rulegen_cli, "FeatureMiner", lambda: DummyMiner(calls))
    monkeypatch.setattr(rulegen_cli, "GraphDataset", DummyDataset)

    out1 = tmp_path / "out1.json"
    args = argparse.Namespace(graph_dir=str(root), labels=None, out=str(out1))
    rulegen_cli.cmd_feature_mine(args)

    data1 = json.loads(out1.read_text())
    assert {d["sha256"] for d in data1} == {"a", "b"}
    assert calls == [("a", 1), ("b", 1)]

    calls.clear()
    out2 = tmp_path / "out2.json"
    args = argparse.Namespace(graph_dir=str(root), labels=str(ext), out=str(out2))
    rulegen_cli.cmd_feature_mine(args)

    data2 = json.loads(out2.read_text())
    assert {d["sha256"] for d in data2} == {"a", "b"}
    assert calls == [("a", 1), ("b", 1)]

    # --- with selector & classifier checkpoint ---
    calls.clear()
    out3 = tmp_path / "out3.json"

    class DummySelector:
        def __init__(self):
            self.model = types.SimpleNamespace(encoder="enc")
            self.calls = []

        def eval(self):
            return self

        def __call__(self, g, embeddings=None):
            self.calls.append(embeddings)
            return torch.zeros(1)

        def get_node_saliency(self, g, mask):
            return torch.ones(sum(g[nt].num_nodes for nt in g.node_types))

    selector = DummySelector()
    classifier = types.SimpleNamespace(encoder="enc")

    orig_load = torch.load

    def fake_load(path, *a, **kw):
        if str(path).endswith("sel.pt"):
            return selector
        if str(path).endswith("clf.pt"):
            return classifier
        return orig_load(path, *a, **kw)

    monkeypatch.setattr(rulegen_cli.torch, "load", fake_load)

    embed_obj = object()

    def fake_compute(g, enc):
        assert enc == "enc"
        return embed_obj

    monkeypatch.setattr(rulegen_cli, "_compute_node_embeddings", fake_compute)

    args = argparse.Namespace(
        graph_dir=str(root),
        labels=None,
        out=str(out3),
        selector_checkpoint=str(tmp_path / "sel.pt"),
        classifier_ckpt=str(tmp_path / "clf.pt"),
        embed_dir=None,
    )
    rulegen_cli.cmd_feature_mine(args)

    assert selector.calls == [embed_obj, embed_obj]
