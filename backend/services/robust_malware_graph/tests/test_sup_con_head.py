import pytest

pytest.importorskip("torch")

import torch
from src.models.contrast.sup_con import SupContrastHead


def test_forward_requires_labels():
    head = SupContrastHead(in_dim=2, proj_dim=2)
    z = torch.randn(4, 2)
    with pytest.raises(ValueError, match="Labels are required"):
        head(z, None)  # type: ignore[arg-type]


def test_forward_subset_shared_labels_returns_finite_scalar():
    head = SupContrastHead(in_dim=4, proj_dim=4)
    z = torch.randn(4, 4)
    y = torch.tensor([0, 0, 1, 2])
    loss = head(z, y)
    assert loss.dim() == 0
    assert torch.isfinite(loss).item()


def test_forward_unique_labels_returns_zero():
    head = SupContrastHead(in_dim=4, proj_dim=4)
    z = torch.randn(4, 4)
    y = torch.arange(4)
    loss = head(z, y)
    assert loss.dim() == 0
    assert torch.isfinite(loss).item()
    assert loss.item() == 0.0


def test_forward_mismatched_batch_size_raises():
    head = SupContrastHead(in_dim=4, proj_dim=4)
    z = torch.randn(4, 4)
    y = torch.arange(5)
    with pytest.raises(ValueError, match="batch size"):
        head(z, y)
