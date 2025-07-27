import rulegen

def test_feature_miner_accessible():
    assert rulegen.FeatureMiner.__name__ == "FeatureMiner"
