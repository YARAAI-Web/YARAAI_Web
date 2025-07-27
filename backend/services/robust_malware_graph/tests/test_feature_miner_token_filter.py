import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

from rulegen.feature_miner import FeatureMiner


def test_normalize_and_rank_filters_tokens():
    miner = FeatureMiner(top_k=1)
    feats = [
        "FOO",
        "call:sub_1234",
        "call:0x401000",
        '".rsrc" ascii nocase',
        "\"0123456789ABCDEF0123456789ABCDEF\" wide ascii nocase",
        "call:CreateFileW",
    ]
    out = miner._normalize_and_rank(feats)
    assert len(out) < len(feats)
    assert "call:CreateFileW" in out
    assert "FOO" not in out
    assert "call:sub_1234" not in out
    assert '".rsrc" ascii nocase' not in out
    assert "call:0x401000" not in out
    assert "\"0123456789ABCDEF0123456789ABCDEF\" wide ascii nocase" not in out
