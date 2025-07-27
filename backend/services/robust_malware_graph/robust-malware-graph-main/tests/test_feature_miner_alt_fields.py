import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from rulegen.feature_miner import FeatureMiner


def test_miner_accepts_dll_field():
    g = HeteroData()
    g["import"].x = torch.zeros(1, 1)
    g["import"].dll = ["WS2_32.dll"]
    sal = torch.tensor([0.9])
    feats = FeatureMiner(top_k=1)(g, sal)
    assert "import:WS2_32.dll" in feats


def test_miner_accepts_name_as_syscall():
    g = HeteroData()
    g["syscall"].x = torch.zeros(1, 1)
    g["syscall"].name = ["NtCreateFile"]
    sal = torch.tensor([0.8])
    feats = FeatureMiner(top_k=1)(g, sal)
    assert "syscall:NtCreateFile" in feats
