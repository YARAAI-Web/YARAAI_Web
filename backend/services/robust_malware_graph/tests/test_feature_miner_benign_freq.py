import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from rulegen.feature_miner import FeatureMiner


def test_benign_freq_filter_removes_common_token():
    g = HeteroData()
    g["func"].x = torch.zeros(1, 1)
    g["func"].name = ["CreateFileW"]
    sal = torch.tensor([1.0])
    miner = FeatureMiner(top_k=1, benign_freqs={"call:CreateFileW": 10}, freq_threshold=5)
    feats = miner(g, sal)
    assert feats == ["call:CreateFileW"]


def test_benign_freq_filter_selects_lowest_freq_token():
    g = HeteroData()
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["CreateFileA", "CreateFileW"]

    sal = torch.tensor([1.0, 0.9])
    miner = FeatureMiner(
        top_k=2,
        benign_freqs={"call:CreateFileA": 20, "call:CreateFileW": 10},
        freq_threshold=5,
    )
    feats = miner(g, sal)

    assert feats == ["call:CreateFileW"]


def test_benign_freq_filter_breaks_tie_with_saliency():
    g = HeteroData()
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["CreateFileA", "CreateFileW"]

    sal = torch.tensor([0.5, 0.9])
    miner = FeatureMiner(
        top_k=2,
        benign_freqs={"call:CreateFileA": 10, "call:CreateFileW": 10},
        freq_threshold=5,
    )
    feats = miner(g, sal)

    assert feats == ["call:CreateFileW"]


def test_mal_freq_ratio_filters_token(tmp_path):
    g = HeteroData()
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["CreateFileA", "CreateFileW"]

    sal = torch.tensor([1.0, 0.9])
    miner = FeatureMiner(
        top_k=2,
        benign_freqs={"call:CreateFileA": 10, "call:CreateFileW": 5},
        mal_freqs={"call:CreateFileA": 5, "call:CreateFileW": 10},
        freq_threshold=100,
        freq_ratio=1.0,
    )
    feats = miner(g, sal)

    assert feats == ["call:CreateFileW"]
