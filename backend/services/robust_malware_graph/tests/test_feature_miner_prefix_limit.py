import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

from rulegen.feature_miner import FeatureMiner


def test_prefix_limit_applied():
    miner = FeatureMiner(top_k=1, max_per_prefix=3)
    feats = [
        "call:FuncA",
        "call:FuncB",
        "call:FuncC",
        "call:FuncD",
        "import:libA",
        "import:libB",
        "import:libC",
        "import:libD",
        '"str1" ascii nocase',
        '"str2" ascii nocase',
        '"str3" ascii nocase',
        '"str4" ascii nocase',
    ]
    sal_map = {f: 1.0 for f in feats}
    out = miner._normalize_and_rank(feats, sal_map)
    call_feats = [f for f in out if f.startswith("call:")]
    import_feats = [f for f in out if f.startswith("import:")]
    string_feats = [f for f in out if f.startswith('"')]
    assert len(call_feats) == 3
    assert len(import_feats) == 3
    assert len(string_feats) == 3
