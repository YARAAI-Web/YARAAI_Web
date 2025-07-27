import pytest

pytest.importorskip("torch")

from src.models.gnn import heads


def test_default_head_registration():
    available = heads.available_heads()
    assert "binary_mlp" in available
    assert "multi_class_mlp" in available
    assert "multi_label_mlp" in available
    assert "regression_mlp" in available
