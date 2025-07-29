import types
import importlib
import sys
import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")
pytest.importorskip("yaml")

import torch
from torch_geometric.data import HeteroData
from torch_geometric.nn import GraphConv, HeteroConv

# Ensure optional modules are available to avoid import errors during setup
aug = importlib.import_module("src.augment")
sys.modules.setdefault("augment", aug)
for name, module in list(sys.modules.items()):
    if name.startswith("src.augment"):
        sys.modules.setdefault(name.replace("src.", "", 1), module)
exp = importlib.import_module("src.explain")
sys.modules.setdefault("explain", exp)
for name, module in list(sys.modules.items()):
    if name.startswith("src.explain"):
        sys.modules.setdefault(name.replace("src.", "", 1), module)
for mod_name in ["gensim", "gensim.downloader", "sentencepiece"]:
    if mod_name not in sys.modules:
        sys.modules[mod_name] = types.ModuleType(mod_name)
sys.modules.setdefault("gensim.models", types.ModuleType("gensim.models"))
sys.modules["gensim.models"].Word2Vec = object

et = importlib.import_module("src.cli.explainer_train")


def _make_graph():
    g = HeteroData()
    g["a"].x = torch.zeros(2, 4)
    g["b"].x = torch.zeros(2, 4)
    g["a"].num_nodes = 2
    g["b"].num_nodes = 2
    g[("a", "r", "b")].edge_index = torch.tensor([[0, 1], [0, 1]])
    return g


def _make_encoder(conv):
    enc = types.SimpleNamespace()
    enc.input_proj = torch.nn.ModuleDict({
        "a": torch.nn.Linear(4, 4),
        "b": torch.nn.Linear(4, 4),
    })
    enc.attr_names = {"a": [], "b": []}
    enc.meta_embed = None
    enc.convs = torch.nn.ModuleList([conv])
    enc.drop = torch.nn.Identity()
    enc.act = torch.nn.Identity()
    enc.out_proj = torch.nn.Linear(4, 2)
    return enc


def test_graphconv_embeddings():
    g = _make_graph()
    conv = GraphConv(4, 4)
    enc = _make_encoder(conv)
    out = et._compute_node_embeddings(g, enc)
    assert set(out.keys()) == {"a", "b"}
    assert out["b"].shape == (2, 4)


def test_heteroconv_embeddings():
    g = _make_graph()
    conv = HeteroConv({("a", "r", "b"): GraphConv(4, 4)}, aggr="sum")
    enc = _make_encoder(conv)
    out = et._compute_node_embeddings(g, enc)
    assert set(out.keys()) == {"b"}
    assert out["b"].shape == (2, 4)


def test_heteroconv_missing_edge_type():
    g = _make_graph()
    conv = HeteroConv(
        {("a", "r", "b"): GraphConv(4, 4), ("b", "s", "a"): GraphConv(4, 4)},
        aggr="sum",
    )
    enc = _make_encoder(conv)
    out = et._compute_node_embeddings(g, enc)
    assert set(out.keys()) == {"a", "b"}
    assert out["a"].shape == (2, 4)
    assert out["b"].shape == (2, 4)

