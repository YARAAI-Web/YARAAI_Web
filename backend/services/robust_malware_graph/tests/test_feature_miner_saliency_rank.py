import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

from rulegen.feature_miner import FeatureMiner


def test_normalize_and_rank_prefers_higher_saliency():
    miner = FeatureMiner(top_k=1)
    feats = ["call:FuncA", "call:FuncB", "call:FuncB"]
    sal_map = {"call:FuncA": 5.0, "call:FuncB": 1.0}
    out = miner._normalize_and_rank(feats, sal_map)
    assert out[0] == "call:FuncA"
    assert out[1] == "call:FuncB"
