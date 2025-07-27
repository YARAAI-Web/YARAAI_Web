import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import Data

from src.augment.view_generators.standard_pair import StandardPair
from src.augment.base import AugmentBase


class BadEdges(AugmentBase):
    """Augmenter that injects invalid edges."""

    def __call__(self, g: Data) -> Data:  # type: ignore[override]
        g.edge_index = torch.tensor([[0, 5], [1, -1]])
        return g


def test_standard_pair_sanitizes_edges():
    g = Data(x=torch.randn(2, 1), edge_index=torch.tensor([[0], [1]]), num_nodes=2)

    aug = BadEdges()
    vg = StandardPair([aug], [aug])
    g1, g2 = vg(g)

    assert g1.edge_index.numel() == 0
    assert g2.edge_index.numel() == 0
