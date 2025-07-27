import importlib
import types
import sys
import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

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

from robust_malware_graph.explain import PGExplainer
from src.cli.explainer_train import compute_stability_loss

class DummyModel(torch.nn.Module):
    def forward(self, graph, return_logits=False):
        return torch.tensor([0.0])


def build_graph():
    g = HeteroData()
    g["n"].x = torch.zeros(2, 1)
    g["n"].num_nodes = 2
    ei = torch.tensor([[0, 1], [1, 0]])
    g[("n", "r", "n")].edge_index = ei
    g[("n", "r", "n")].edge_type = torch.zeros(2, dtype=torch.long)
    return g


def test_compute_stability_loss_runs():
    g = build_graph()
    model = DummyModel()
    explainer = PGExplainer(model, {"n": 1}, [("n", "r", "n")], view="r")
    mask_prob = explainer(g)
    loss = compute_stability_loss(g, explainer, mask_prob, False)
    assert isinstance(loss, torch.Tensor)
    assert loss.numel() == 1
