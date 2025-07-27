import importlib
import pytest


def test_feature_miner_submodule_importable():
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")
    mod = importlib.import_module("rulegen.feature_miner")
    assert mod.__name__.endswith("feature_miner")
