import pytest
pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import Data

from src.explain.cfg_explainer.mapper import CFGASTMapper
from src.explain.cfg_explainer.ranker import ShapleyNodeRanker


def test_cfgastmapper_tuple_keys():
    cfg = Data(
        addr=torch.tensor([[0, 1], [2, 3]], dtype=torch.long),
        x=torch.zeros(2, 1),
        num_nodes=2,
    )
    ast = Data(
        span=torch.tensor([[0, 0], [1, 1], [2, 2], [3, 3]], dtype=torch.long),
        num_nodes=4,
    )
    mapper = CFGASTMapper(cfg, ast, cfg_node_type="bb")
    assert mapper.cfg_nodes_to_tokens([("bb", 0)]) == [0, 1]
    assert mapper.tokens_to_cfg_nodes([0]) == [("bb", 0)]

    d = mapper.to_dict()
    restored = CFGASTMapper.from_dict(d, cfg, ast)
    assert restored.cfg_nodes_to_tokens([("bb", 1)]) == [2, 3]


def test_ranker_edge_regularisation():
    g = Data(
        x=torch.ones(2, 1),
        edge_index=torch.tensor([[0, 1], [1, 0]], dtype=torch.long),
        edge_type=torch.tensor([0, 0], dtype=torch.long),
        num_nodes=2,
    )

    ranker = ShapleyNodeRanker(g, score_fn=lambda d: float(d.num_nodes), seed=0)
    mask = torch.tensor([1.0, 0.0])
    phi = ranker.shapley_values(
        num_permutations=2,
        progress=False,
        edge_mask=mask,
        edge_types=g.edge_type,
        sparsity_beta=1.0,
    )
    for v in phi.values():
        assert pytest.approx(0.5, rel=1e-5) == v
