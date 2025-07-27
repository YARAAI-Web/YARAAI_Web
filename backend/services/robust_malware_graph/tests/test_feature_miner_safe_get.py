import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from rulegen.feature_miner import FeatureMiner


def test_feature_miner_handles_short_attribute_list():
    g = HeteroData()
    g["func"].num_nodes = 2
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["CreateFileW"]  # only one entry

    sal = torch.tensor([0.9, 0.8])
    miner = FeatureMiner(top_k=2)
    feats = miner(g, sal)
    assert isinstance(feats, list)


def test_feature_miner_resolves_alias_fields():
    g = HeteroData()
    g["import"].num_nodes = 1
    g["import"].x = torch.zeros(1, 1)
    g["import"].import_ = ["WS2_32.dll"]  # field uses alias

    sal = torch.tensor([1.0])
    miner = FeatureMiner(top_k=1)
    feats = miner(g, sal)
    assert "import:WS2_32.dll" in feats


def test_feature_miner_reads_from_meta_dict():
    g = HeteroData()
    g["func"].num_nodes = 1
    g["func"].x = torch.zeros(1, 1)
    g["func"].meta = {"name": ["CreateFileW"]}

    sal = torch.tensor([1.0])
    miner = FeatureMiner(top_k=1)
    feats = miner(g, sal)
    assert "call:CreateFileW" in feats


def test_feature_miner_uses_nested_meta_dict_value():
    g = HeteroData()
    g["token"].num_nodes = 1
    g["token"].x = torch.zeros(1, 1)
    g["token"].meta = {"name": "CreateFileW"}

    sal = torch.tensor([1.0])
    feats = FeatureMiner(top_k=1)(g, sal)
    assert feats == ["call:CreateFileW"]
