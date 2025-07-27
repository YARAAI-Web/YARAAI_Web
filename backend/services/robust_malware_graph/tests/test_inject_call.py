import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

from torch_geometric.data import HeteroData

from src.augment.ops.inject_call import InjectAPICall
import torch
import importlib.util
from pathlib import Path

schema_spec = importlib.util.spec_from_file_location(
    "schema", Path("src/graphs/normalizers/schema.py")
)
schema = importlib.util.module_from_spec(schema_spec)
assert schema_spec.loader is not None
schema_spec.loader.exec_module(schema)
EDGE_REL_ID = schema.EDGE_REL_ID
EdgeRel = schema.EdgeRel


def test_inject_api_call_handles_missing_bb():
    g = HeteroData()
    aug = InjectAPICall()
    out = aug(g)
    assert isinstance(out, HeteroData)


def test_inject_api_call_edge_type():
    g = HeteroData()
    g["bb"].num_nodes = 1
    g["api"].num_nodes = 1
    etype = ("bb", "calls", "api")
    g[etype].edge_index = torch.tensor([[0], [0]])
    g[etype].edge_type = torch.tensor(
        [EDGE_REL_ID[EdgeRel.CALLS.value]], dtype=torch.long
    )

    aug = InjectAPICall(k=2, seed=0)
    out = aug(g)

    store = out[etype]
    assert store.edge_type.size(0) == store.edge_index.size(1)
    assert torch.all(
        store.edge_type == EDGE_REL_ID[EdgeRel.CALLS.value]
    )
