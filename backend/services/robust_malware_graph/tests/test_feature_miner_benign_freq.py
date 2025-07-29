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
    miner = FeatureMiner(
        top_k=1, benign_freqs={"call:CreateFileW": 10}, freq_threshold=5
    )
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


def test_restore_returns_multiple_tokens_when_configured():
    g = HeteroData()
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["CreateFileA", "CreateFileW"]

    sal = torch.tensor([1.0, 0.9])
    miner = FeatureMiner(
        top_k=2,
        benign_freqs={"call:CreateFileA": 20, "call:CreateFileW": 10},
        freq_threshold=5,
        restore_top_n=2,
    )
    feats = miner(g, sal)

    assert feats == ["call:CreateFileW", "call:CreateFileA"]


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


def test_select_high_mal_freq_token_with_verification():
    g = HeteroData()
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["Foo", "Bar"]

    sal = torch.tensor([0.8, 0.6])

    def _verify(feats):
        return feats[0] == "call:Bar"

    miner = FeatureMiner(
        top_k=2,
        benign_freqs={"call:Foo": 30, "call:Bar": 20},
        mal_freqs={"call:Foo": 90, "call:Bar": 45},
        freq_threshold=5,
        verify_func=_verify,
    )

    feats = miner(g, sal)

    assert feats == ["call:Bar"]


def test_restore_selects_lowest_ratio_when_no_high_mal():
    g = HeteroData()
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["Foo", "Bar"]

    sal = torch.tensor([0.8, 0.6])

    miner = FeatureMiner(
        top_k=2,
        benign_freqs={"call:Foo": 10, "call:Bar": 20},
        mal_freqs={"call:Foo": 5, "call:Bar": 20},
        freq_threshold=5,
    )

    feats = miner(g, sal)

    assert feats == ["call:Bar"]


def test_benign_weight_affects_ranking():
    g = HeteroData()
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["Foo", "Bar"]

    sal = torch.tensor([0.6, 0.5])
    freqs = {"call:Foo": 5, "call:Bar": 1}

    miner = FeatureMiner(
        top_k=2,
        benign_freqs=freqs,
        freq_threshold=100,
        benign_weight=0.0,
    )
    feats = miner(g, sal)
    assert feats[0] == "call:Foo"

    miner_w = FeatureMiner(
        top_k=2,
        benign_freqs=freqs,
        freq_threshold=100,
        benign_weight=1.0,
    )
    feats_w = miner_w(g, sal)
    assert feats_w[0] == "call:Bar"
