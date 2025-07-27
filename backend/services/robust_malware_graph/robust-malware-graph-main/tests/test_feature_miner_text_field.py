import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from rulegen.feature_miner import FeatureMiner


def test_miner_accepts_text_field():
    g = HeteroData()
    g["token"].x = torch.zeros(1, 1)
    g["token"].text = ["example"]
    sal = torch.tensor([1.0])
    feats = FeatureMiner(top_k=1)(g, sal)
    assert "\"example\" wide ascii nocase" in feats
