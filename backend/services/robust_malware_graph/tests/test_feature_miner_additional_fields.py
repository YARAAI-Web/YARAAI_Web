import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from rulegen.feature_miner import FeatureMiner


def test_miner_extracts_filepath_tokens():
    g = HeteroData()
    g["file"].x = torch.zeros(1, 1)
    g["file"].filepath = ["C:/Temp/bad.exe"]
    sal = torch.tensor([0.9])
    feats = FeatureMiner(top_k=1)(g, sal)
    assert "\"C:/Temp/bad.exe\" wide ascii nocase" in feats
    assert "path:bad.exe" in feats


def test_miner_extracts_registry_key_tokens():
    g = HeteroData()
    g["registry"].x = torch.zeros(1, 1)
    g["registry"].key = ["HKEY_LOCAL_MACHINE\\Software\\Test"]
    sal = torch.tensor([0.9])
    feats = FeatureMiner(top_k=1)(g, sal)
    assert "\"HKEY_LOCAL_MACHINE\\Software\\Test\" wide ascii nocase" in feats
    assert "reg:HKEY_LOCAL_MACHINE\\Software\\Test" in feats


def test_miner_extracts_url_tokens():
    g = HeteroData()
    g["urlnode"].x = torch.zeros(1, 1)
    g["urlnode"].url = ["https://malicious.com/path/evil"]
    sal = torch.tensor([0.9])
    feats = FeatureMiner(top_k=1)(g, sal)
    assert "url:malicious.com" in feats
    assert "url:evil" in feats


def test_miner_extracts_section_name():
    g = HeteroData()
    g["section"].x = torch.zeros(1, 1)
    g["section"].name = [".foo"]
    sal = torch.tensor([0.9])
    feats = FeatureMiner(top_k=1)(g, sal)
    assert '".foo" ascii nocase' in feats
    assert "marker:.foo" in feats
