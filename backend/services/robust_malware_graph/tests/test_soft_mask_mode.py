import importlib
import types
from pathlib import Path
import sys

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

aug = importlib.import_module("src.augment")
sys.modules.setdefault("augment", aug)
for name, module in list(sys.modules.items()):
    if name.startswith("src.augment"):
        sys.modules.setdefault(name.replace("src.", "", 1), module)
del module, name, aug
exp = importlib.import_module("src.explain")
sys.modules.setdefault("explain", exp)
for name, module in list(sys.modules.items()):
    if name.startswith("src.explain"):
        sys.modules.setdefault(name.replace("src.", "", 1), module)
del module, name, exp
for mod_name in ["gensim", "gensim.downloader", "sentencepiece"]:
    if mod_name not in sys.modules:
        sys.modules[mod_name] = types.ModuleType(mod_name)
if "pandas" not in sys.modules:
    sys.modules["pandas"] = types.ModuleType("pandas")
if "pyarrow" not in sys.modules:
    pa = types.ModuleType("pyarrow")
    sys.modules["pyarrow"] = pa
    sys.modules["pyarrow.feather"] = types.ModuleType("pyarrow.feather")
    sys.modules["pyarrow.parquet"] = types.ModuleType("pyarrow.parquet")
sys.modules.setdefault("gensim.models", types.ModuleType("gensim.models"))
sys.modules["gensim.models"].Word2Vec = object
for mod in ["pefile", "lief", "capstone", "r2pipe", "ghidra_bridge", "angr", "archinfo"]:
    if mod not in sys.modules:
        sys.modules[mod] = types.ModuleType(mod)
mod = importlib.import_module("src.cli.explainer_train")

class DummyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        enc = types.SimpleNamespace(
            metadata=(["n"], [("n", "r", "n")]),
            attr_names={"n": []},
            target_node="n",
            input_proj={},
            out_proj=types.SimpleNamespace(in_features=1),
        )
        self.encoder = enc
        self.p = torch.nn.Parameter(torch.zeros(1))

    def to(self, device):
        return self

    def eval(self):
        return self

    def forward(self, graph, return_logits=False):
        # return sum of edge weights if present
        store = graph[("n", "r", "n")]
        w = getattr(store, "edge_weight", torch.zeros(store.edge_index.size(1)))
        return w.sum().unsqueeze(0)


def dummy_load_model(args, device):
    return DummyModel(), {"hidden_dim": 1}


class DummyExplainer:
    def __init__(self, *a, **kw):
        self.p = torch.nn.Parameter(torch.zeros(1))
        self.tau = torch.tensor(1.0)

    def parameters(self):
        return [self.p]

    def to(self, device):
        return self

    def train(self):
        pass

    def eval(self):
        pass

    def __call__(self, graph, embeddings=None, hard=False):
        # return a mask for two edges
        return torch.tensor([0.3, 0.7])

    def loss(self, *a, **kw):
        return torch.tensor(0.0, requires_grad=True)


def dummy_embeddings(g, encoder):
    return {"n": torch.zeros(g["n"].num_nodes, 1)}


class DummyScaler:
    def __init__(self, enabled=True):
        pass

    class _Obj:
        def backward(self):
            pass

    def scale(self, loss):
        return self._Obj()

    def step(self, optim):
        pass

    def update(self):
        pass

    def unscale_(self, optim):
        pass


def test_soft_mask_switch(tmp_path, monkeypatch):
    g = HeteroData()
    g["n"].x = torch.zeros(2, 1)
    g["n"].num_nodes = 2
    g[("n", "r", "n")].edge_index = torch.tensor([[0, 1], [1, 0]])
    graphs = tmp_path / "graphs"
    graphs.mkdir()
    torch.save(g, graphs / "g.pt")
    (tmp_path / "model.pt").write_text("stub")

    monkeypatch.setattr(mod, "_load_model", dummy_load_model)
    monkeypatch.setattr(mod, "_compute_node_embeddings", dummy_embeddings)
    monkeypatch.setattr(mod, "PGExplainer", DummyExplainer)
    monkeypatch.setattr(mod.torch.amp, "GradScaler", DummyScaler)

    calls = []
    monkeypatch.setattr(mod, "_soft_masked_score", lambda *a, **k: calls.append("soft") or torch.tensor(0.0))
    monkeypatch.setattr(mod, "_masked_score", lambda *a, **k: calls.append("hard") or torch.tensor(0.0))

    parser = mod.build_parser()
    args = parser.parse_args([
        "global",
        "--graph-dir",
        str(graphs),
        "--model",
        str(tmp_path / "model.pt"),
        "--output",
        str(tmp_path / "out.pt"),
        "--epochs",
        "2",
        "--soft-mask-epochs",
        "1",
    ])
    args.device = "cpu"

    mod.train_global(args)

    assert calls[0] == "soft"
    assert calls[-1] == "hard"
