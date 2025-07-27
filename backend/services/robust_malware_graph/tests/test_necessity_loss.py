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
from src.cli.explainer_train import compute_necessity_loss

class DummyModel(torch.nn.Module):
    def forward(self, graph, return_logits=False, edge_weight_dict=None):
        return torch.tensor([0.0])

def build_graph():
    g = HeteroData()
    g["n"].x = torch.zeros(2, 1)
    g["n"].num_nodes = 2
    g[("n", "r", "n")].edge_index = torch.tensor([[0, 1], [1, 0]])
    return g

def test_compute_necessity_loss_runs():
    g = build_graph()
    model = DummyModel()
    explainer = PGExplainer(model, {"n": 1}, [("n", "r", "n")], view="r")
    mask_prob = explainer(g)
    full_score = torch.tensor(0.0)
    loss = compute_necessity_loss(
        g, mask_prob, explainer, model, full_score, drop_ratio=0.2
    )
    loss_hard = compute_necessity_loss(
        g,
        mask_prob,
        explainer,
        model,
        full_score,
        use_hard_prune=True,
        drop_ratio=0.2,
    )
    assert isinstance(loss, torch.Tensor)
    assert loss.numel() == 1
    assert isinstance(loss_hard, torch.Tensor)
    assert loss_hard.numel() == 1
