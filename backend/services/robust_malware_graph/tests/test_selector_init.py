import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.explain.cfg_explainer.selector import GumbelMaskSelector


def test_selector_initializes_on_hetero():
    g = HeteroData()
    g["bb"].num_nodes = 3
    ei = torch.tensor([[0, 1], [1, 2]], dtype=torch.long)
    g[("bb", "cfg", "bb")].edge_index = ei

    selector = GumbelMaskSelector(view="cfg")
    assert not selector.initialized
    mask = selector(g)
    assert selector.initialized
    key = str(("bb", "cfg", "bb"))
    assert key in selector.logits
    assert selector.logits[key].shape == (ei.size(1),)
    assert mask.numel() == ei.size(1)


def test_selector_initializes_custom_view():
    g = HeteroData()
    g["bb"].num_nodes = 2
    ei = torch.tensor([[0], [1]], dtype=torch.long)
    g[("bb", "ast", "bb")].edge_index = ei

    selector = GumbelMaskSelector(view="ast")
    mask = selector(g)
    key = str(("bb", "ast", "bb"))
    assert key in selector.logits
    assert mask.numel() == ei.size(1)

