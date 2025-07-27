import importlib
from pathlib import Path
import types
import sys
import pytest

pytest.importorskip("torch")
aug = importlib.import_module("src.augment")
sys.modules.setdefault("augment", aug)
for n, m in list(sys.modules.items()):
    if n.startswith("src.augment"):
        sys.modules.setdefault(n.replace("src.", "", 1), m)
exp = importlib.import_module("src.explain")
sys.modules.setdefault("explain", exp)
for n, m in list(sys.modules.items()):
    if n.startswith("src.explain"):
        sys.modules.setdefault(n.replace("src.", "", 1), m)
if "pyarrow" not in sys.modules:
    pa = types.ModuleType("pyarrow")
    pa.__version__ = "0.0"
    sys.modules["pyarrow"] = pa
    sys.modules["pyarrow.feather"] = types.ModuleType("pyarrow.feather")
    sys.modules["pyarrow.parquet"] = types.ModuleType("pyarrow.parquet")

class DummyModel:
    def __init__(self):
        self.encoder = types.SimpleNamespace(target_node="bb", input_proj={})

    def to(self, device):
        return self

    def eval(self):
        return self


def test_global_cli_invokes(tmp_path, monkeypatch):
    gdir = tmp_path / "graphs"
    gdir.mkdir()
    (gdir / "a.pt").write_text("stub")
    mpath = tmp_path / "model.pt"
    mpath.write_text("stub")

    captured = {}

    def fake_train(args):
        captured["graph_dir"] = args.graph_dir
        captured["output"] = args.output
        captured["init_bias"] = args.init_bias
        captured["tau_start"] = args.tau_start
        captured["stability_weight"] = args.stability_weight
        captured["stability_start"] = args.stability_start
        captured["necessity_weight"] = args.necessity_weight
        captured["necessity_start"] = args.necessity_start
        captured["necessity_schedule"] = args.necessity_schedule
        captured["necessity_weight_start"] = args.necessity_weight_start
        captured["necessity_schedule_factor"] = args.necessity_schedule_factor
        captured["necessity_schedule_epochs"] = args.necessity_schedule_epochs
        captured["necessity_weight_max"] = args.necessity_weight_max
        captured["necessity_drop_ratio"] = args.necessity_drop_ratio

    import torch.serialization
    monkeypatch.setattr(
        torch.serialization,
        "add_safe_globals",
        lambda *a, **kw: None,
        raising=False,
    )
    import types, sys
    for mod in ["gensim", "gensim.downloader", "sentencepiece", "gensim.models"]:
        if mod not in sys.modules:
            sys.modules[mod] = types.ModuleType(mod)
    sys.modules.setdefault("gensim.models", types.ModuleType("gensim.models"))
    sys.modules["gensim.models"].Word2Vec = object
    for mod in ["pefile", "lief", "capstone", "r2pipe", "ghidra_bridge", "angr", "archinfo"]:
        if mod not in sys.modules:
            sys.modules[mod] = types.ModuleType(mod)

    monkeypatch.setattr("src.cli.explainer_train.train_global", fake_train)
    mod = importlib.import_module("src.cli.explainer_train")

    out = tmp_path / "out.pt"
    mod.main([
        "global",
        "--graph-dir",
        str(gdir),
        "--model",
        str(mpath),
        "--output",
        str(out),
    ])

    assert captured["graph_dir"] == gdir
    assert captured["output"] == out
    assert captured["init_bias"] == 1.0
    assert captured["tau_start"] == 1.0
    assert captured["stability_weight"] == 0.0
    assert captured["stability_start"] == 0
    assert captured["necessity_weight"] == 0.0
    assert captured["necessity_start"] == 0
    assert captured["necessity_schedule"] is False
    assert captured["necessity_weight_start"] == 1e-4
    assert captured["necessity_schedule_factor"] == 1.5
    assert captured["necessity_schedule_epochs"] == 10
    assert captured["necessity_weight_max"] is None
    assert captured["necessity_drop_ratio"] == 0.2
