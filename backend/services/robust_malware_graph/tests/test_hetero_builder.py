import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import Data, HeteroData

from src.graphs.builders.hetero_builder import (
    HeteroGraphBuilder,
    fill_missing_node_feats,
    ensure_num_nodes,
    OverLengthPolicy,
)
from src.graphs.normalizers.ast_norm import ASTNormalizer


def test_missing_num_nodes_error():
    g = HeteroData()
    # create an empty node store without specifying num_nodes
    _ = g["function"]
    builder = HeteroGraphBuilder()
    builder.add_view(g, "fcg")
    with pytest.raises(ValueError, match="function"):
        builder.build()


def test_builder_num_nodes_inferred(caplog):
    import logging

    g = Data(edge_index=torch.tensor([[0, 1], [1, 2]]), kind_id=torch.tensor([0, 1, 2]))
    norm = ASTNormalizer()
    g_norm = norm.normalize(g)

    caplog.set_level(logging.WARNING)
    builder = HeteroGraphBuilder()
    builder.add_view(g_norm, "ast")
    _ = builder.build()

    assert "Unable to accurately infer" not in caplog.text


def test_fill_missing_feats():
    g = HeteroData()
    g["bb"].num_nodes = 2
    fill_missing_node_feats(g, dim=1)
    assert "feat" in g["bb"]
    assert g["bb"].feat.shape == (2, 1)
    assert torch.all(g["bb"].feat.eq(0))


def test_fill_missing_feats_warn_trim():
    g = HeteroData()
    g["n"].feat = torch.randn(3, 1)
    g["n"].num_nodes = 2
    import warnings

    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        fill_missing_node_feats(g, dim=1, policy=OverLengthPolicy.TRIM)
    assert record
    msg = str(record[0].message)
    assert "n" in msg
    assert "1" in msg
    assert g["n"].feat.size(0) == 2


def test_ensure_num_nodes_no_warning():
    g = Data(edge_index=torch.tensor([[0, 1], [1, 2]]), kind_id=torch.tensor([0, 1, 2]))
    g_norm = ASTNormalizer().normalize(g)

    builder = HeteroGraphBuilder()
    builder.add_view(g_norm, "ast")
    hetero = builder.build()

    # older PyG versions warned when inferring num_nodes
    _ = len(hetero["token"])  # triggers internal inference

    ensure_num_nodes(hetero)

    import warnings

    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        _ = len(hetero["token"])
    assert not record


@pytest.mark.xfail(reason="policy not implemented")
def test_num_nodes_error_policy():
    g = HeteroData()
    g["n"].x = torch.randn(2, 1)
    g["n"].num_nodes = 1  # mismatch
    with pytest.raises(ValueError):
        ensure_num_nodes(g, policy="ERROR")


@pytest.mark.xfail(reason="policy not implemented")
def test_num_nodes_expand_policy():
    g = HeteroData()
    g["n"].x = torch.randn(3, 1)
    g["n"].num_nodes = 1
    ensure_num_nodes(g, policy="EXPAND")
    assert g["n"].num_nodes == 3


@pytest.mark.xfail(reason="policy not implemented")
def test_num_nodes_maskpad_policy():
    g = HeteroData()
    g["n"].x = torch.randn(3, 1)
    g["n"].num_nodes = 1
    ensure_num_nodes(g, policy="MASKPAD")
    assert g["n"].num_nodes == 3
    assert torch.equal(g["n"].x[:1], g["n"].x[:1])
    assert torch.all(g["n"].mask[:1])
    assert not torch.any(g["n"].mask[1:])


def test_merge_list_attribute_length():
    g1 = HeteroData()
    g1["n"].num_nodes = 2
    g1["n"].label = ["a", "b"]

    g2 = HeteroData()
    g2["n"].num_nodes = 3
    g2["n"].label = ["c", "d", "e"]

    builder = HeteroGraphBuilder()
    builder.add_view(g1, "v1")
    builder.add_view(g2, "v2")

    hetero = builder.build()
    assert len(hetero["n"].label) == g1["n"].num_nodes + g2["n"].num_nodes


def test_no_warnings_on_build():
    import warnings
    import logging

    g = Data(edge_index=torch.tensor([[0, 1], [1, 2]]))

    logging.getLogger().setLevel(logging.WARNING)
    builder = HeteroGraphBuilder()
    from src.graphs.builders.hetero_builder import _ensure_num_nodes_any

    g = _ensure_num_nodes_any(g)
    builder.add_view(g, "cfg")
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        _ = builder.build()
    assert not record


def test_infer_num_nodes_from_attrs():
    g = HeteroData()
    g["bb"].addr = [0x1000, 0x2000, 0x3000]
    g["bb"].inst_cnt = torch.tensor([1, 2, 3])
    from src.graphs.builders.hetero_builder import _ensure_num_nodes_any

    g = _ensure_num_nodes_any(g)
    assert g["bb"].num_nodes == 3


def test_infer_num_nodes_data_addr_only():
    g = Data(addr=[0x1000, 0x2000])
    from src.graphs.builders.hetero_builder import _ensure_num_nodes_any

    g = _ensure_num_nodes_any(g)
    assert g.num_nodes == 2


def test_guess_num_nodes_length_mismatch_warns():
    g = HeteroData()
    g["bb"].addr = [1, 2]
    g["bb"].inst_cnt = torch.tensor([1])
    from src.graphs.builders.hetero_builder import _ensure_num_nodes_any
    import warnings

    with warnings.catch_warnings(record=True) as rec:
        warnings.simplefilter("always")
        g = _ensure_num_nodes_any(g)
    assert rec, "expected RuntimeWarning on length mismatch"
    assert "num_nodes mismatch" in str(rec[0].message)
    assert g["bb"].num_nodes == 2


def test_guess_num_nodes_from_api_name():
    g = HeteroData()
    g["api"].api_name = ["Open", "Close", "Read"]

    from src.graphs.builders.hetero_builder import _ensure_num_nodes_any

    g = _ensure_num_nodes_any(g)

    assert g["api"].num_nodes == 3
