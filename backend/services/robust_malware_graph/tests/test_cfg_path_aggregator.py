import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData
from src.explain.cfg_explainer.aggregator import CFGPathAggregator

def build_graph():
    g = HeteroData()
    g["bb"].num_nodes = 4
    g["bb"].feat = torch.zeros(4, 1)
    ei1 = torch.tensor([[0, 1], [1, 2]], dtype=torch.long)
    g[("bb", "jump", "bb")].edge_index = ei1
    g[("bb", "jump", "bb")].edge_type = torch.zeros(ei1.size(1), dtype=torch.long)
    ei2 = torch.tensor([[0, 2], [2, 3]], dtype=torch.long)
    g[("bb", "fallthrough", "bb")].edge_index = ei2
    g[("bb", "fallthrough", "bb")].edge_type = torch.ones(ei2.size(1), dtype=torch.long)
    return g

def test_aggregator_hetero_paths():
    g = build_graph()
    agg = CFGPathAggregator(g)
    paths = agg.aggregate([0, 1, 2, 3])
    assert len(paths) == 1
    p = paths[0]
    assert p["nodes"] == [0, 1, 2, 3]
    assert p["edge_ids"].tolist() == [0, 1, 2, 3]
    assert p["edge_map"][0][0] == ("bb", "jump", "bb")
    assert p["edge_map"][2][0] == ("bb", "fallthrough", "bb")

def test_edge_embedding_feat():
    g = build_graph()
    emb = torch.nn.Embedding(2, 3)
    torch.nn.init.constant_(emb.weight, 1.0)
    agg = CFGPathAggregator(g, edge_emb=emb)
    paths = agg.aggregate([0, 1, 2, 3])
    assert paths[0]["feat"].shape == (3,)
