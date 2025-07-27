import pytest
import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import Data
import json
from src.graphs.loaders.ast_loader import ASTLoader

from src.graphs.normalizers.ast_norm import ASTNormalizer
from src.graphs.normalizers.fcg_norm import FCGNormalizer
from src.graphs.normalizers.syscall_norm import SysCallNormalizer
from src.graphs.normalizers.schema import NodeType, EdgeRel


def test_fcg_normalizer_name_list():
    g = Data(
        x=torch.randn(3, 2),
        addr=[0x1000, 0x2000, 0x3000],
        name=["main", "foo", "bar"],
        is_external=torch.tensor([False, True, False]),
        edge_index=torch.tensor([[0, 1], [1, 2]], dtype=torch.long),
        num_nodes=3,
    )

    norm = FCGNormalizer()
    out = norm.normalize(g)

    fn_store = out[NodeType.FUNCTION.value]
    assert fn_store.name == ["main", "foo", "bar"]
    assert fn_store.num_nodes == 3


def test_fcg_normalizer_rev_child_edges():
    g = Data(
        kind_str=["function", "function", "token"],
        edge_index=torch.tensor([[0, 0], [1, 2]], dtype=torch.long),
        num_nodes=3,
    )

    out = FCGNormalizer().normalize(g)

    rel_key = (
        NodeType.TOKEN.value,
        EdgeRel.CHILD.value,
        NodeType.FUNCTION.value,
    )

    assert rel_key in out.edge_types
    rev_store = out[rel_key]
    assert rev_store.edge_index.tolist() == [[0], [0]]


def test_ast_normalizer_num_nodes():
    g = Data(
        kind_id=torch.tensor([1, 2], dtype=torch.long),
        edge_index=torch.tensor([[0], [1]], dtype=torch.long),
        num_nodes=2,
    )

    out = ASTNormalizer().normalize(g)
    tok_store = out[NodeType.TOKEN.value]
    assert tok_store.num_nodes == 2


def test_syscall_normalizer_num_nodes():
    g = Data(
        sc_id=torch.tensor([1, 2, 3], dtype=torch.long),
        sc_name=["open", "read", "close"],
        edge_index=torch.tensor([[0, 1], [1, 2]], dtype=torch.long),
        num_nodes=3,
    )

    out = SysCallNormalizer().normalize(g)
    sc_store = out[NodeType.SYSCALL.value]
    assert sc_store.num_nodes == 3


def test_ast_loader_normalizer_token_texts(tmp_path):
    sample = {
        "nodes": [
            {"id": 0, "kind": "file"},
            {"id": 1, "kind": "token", "text": "foo"},
        ],
        "edges": [[0, 1]],
    }
    path = tmp_path / "ast.json"
    path.write_text(json.dumps(sample))

    loader = ASTLoader()
    data = loader._parse(path)
    g_norm = ASTNormalizer().normalize(data)

    tok_store = g_norm[NodeType.TOKEN.value]
    assert hasattr(tok_store, "text")
    assert len(tok_store.text) == tok_store.num_nodes
