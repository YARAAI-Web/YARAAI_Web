import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from rulegen.feature_miner import FeatureMiner


def test_select_nodes_limits_to_top_k():
    sal = torch.arange(10.0, 0.0, -1.0)
    miner = FeatureMiner(top_k=5, min_saliency=0.0)
    idx = miner._select_nodes(sal)
    assert len(idx) <= 5
    assert set(idx.tolist()) == set(range(5))


def test_mine_limits_nodes_per_type():
    from torch_geometric.data import HeteroData

    g = HeteroData()
    g["func"].x = torch.zeros(3, 1)
    g["func"].name = ["func0", "func1", "func2"]
    g["str"].x = torch.zeros(3, 1)
    g["str"].value = ["data0", "data1", "data2"]

    sal = torch.tensor([0.9, 0.8, 0.7, 0.6, 0.5, 0.4])
    miner = FeatureMiner(top_k=6, min_saliency=0.0, keep_per_type=2)
    feats = miner(g, sal)

    func_feats = [f for f in feats if f.startswith("call:")]
    str_feats = [f for f in feats if "wide ascii" in f]
    assert len(func_feats) == 2
    assert len(str_feats) == 2
    assert "call:func2" not in func_feats
    assert '"s2" wide ascii nocase' not in str_feats


def test_select_nodes_saliency_top_percent():
    sal = torch.tensor([10.0, 9.0, 8.0, 7.0, 6.0])
    miner = FeatureMiner(top_k=5, min_saliency=0.0, saliency_top_percent=0.5)
    idx = miner._select_nodes(sal)
    assert set(idx.tolist()) == {0, 1, 2}
