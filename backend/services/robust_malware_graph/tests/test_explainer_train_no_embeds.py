import importlib
import sys
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from tests.test_explainer_train_cli import DummyModel, DummySelector
from src.graphs.normalizers.schema import NodeType, EdgeRel
from src.graphs.features.cache import save_tensor


def _make_graph(path: Path, embed_dir: Path) -> None:
    g = HeteroData()
    g[NodeType.TOKEN.value].x = torch.randn(1, 2)
    g[NodeType.TOKEN.value].num_nodes = 1
    ei = torch.tensor([[0], [0]])
    et = (NodeType.TOKEN.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)
    g[et].edge_index = ei
    g[et].edge_type = torch.zeros(1, dtype=torch.long)
    torch.save(g, path)
    save_tensor(path.stem, torch.randn(1, 2), embed_dir)


def test_explainer_train_batch_no_embeds(tmp_path, monkeypatch):
    data_root = tmp_path / "data"
    embed_dir = data_root / "embeds"
    gdir = data_root / "train" / "graphs"
    gdir.mkdir(parents=True)
    _make_graph(gdir / "a.pt", embed_dir)
    (data_root / "train" / "labels.csv").write_text("sha256,label\na,1\n")

    meta_csv = tmp_path / "meta.csv"
    meta_csv.write_text("sha256,label\na,1\n")

    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    dummy_model = DummyModel()
    monkeypatch.setattr("src.cli.explainer_train._load_model", lambda p, d: dummy_model)
    monkeypatch.setattr(
        "src.cli.explainer_train._train_selector_for_graph",
        lambda *a, **kw: (DummySelector(), HeteroData(), {"pred": 0, "prob": 0.0}),
    )

    importlib.invalidate_caches()
    mod = importlib.import_module("src.cli.explainer_train")

    calls = []
    orig_init = mod.GraphDataset.__init__

    def rec_init(self, *args, **kwargs):
        calls.append(kwargs.get("load_embeds", True))
        orig_init(self, *args, **kwargs)

    monkeypatch.setattr(mod.GraphDataset, "__init__", rec_init)

    argv = [
        "batch",
        "--graph-dir",
        str(gdir),
        "--meta-csv",
        str(meta_csv),
        "--output-dir",
        str(tmp_path / "out"),
        "--model",
        str(mpath),
        "--epochs",
        "1",
        "--no-embeds",
    ]

    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert calls
    assert all(c is False for c in calls)
