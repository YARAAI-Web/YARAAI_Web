import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from rulegen.feature_miner import FeatureMiner


def test_miner_filters_internal_function_names():
    g = HeteroData()
    g["func"].x = torch.zeros(1, 1)
    g["func"].name = ["sub_1000"]
    sal = torch.tensor([1.0])

    feats = FeatureMiner(top_k=1)(g, sal)
    assert "call:sub_1000" not in feats
