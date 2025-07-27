import importlib
import sys
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.models.gnn.encoder import RGCNEncoder
from src.graphs.normalizers.schema import NodeType, EdgeRel
from src.graphs.features.cache import save_tensor


def _make_graph(path: Path, embed_dir: Path) -> None:
    g = HeteroData()
    g[NodeType.TOKEN.value].x = torch.randn(1, 2)
    g[NodeType.TOKEN.value].num_nodes = 1
    ei = torch.tensor([[0], [0]])
    et = (NodeType.TOKEN.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)
    g[et].edge_index = ei
    g[et].edge_type = torch.zeros(1, dtype=torch.long)
    torch.save(g, path)
    save_tensor(path.stem, torch.randn(1, 2), embed_dir)


def test_train_res_gcl_no_embeds(tmp_path, monkeypatch):
    data_root = tmp_path / "data"
    embed_dir = data_root / "embeds"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_graph(gdir / "a.pt", embed_dir)
        (data_root / split / "labels.csv").write_text("sha256,label\na,0\n")

    enc = RGCNEncoder(
        metadata=([NodeType.TOKEN.value], [(NodeType.TOKEN.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)]),
        in_dims={NodeType.TOKEN.value: 2},
        hidden_dim=4,
        num_layers=1,
        out_dim=2,
    )
    ckpt = tmp_path / "enc.pt"
    torch.save({"model": enc.state_dict()}, ckpt)

    meta_path = tmp_path / "enc.meta.pkl"
    torch.save(
        {
            "node_types": [NodeType.TOKEN.value],
            "edge_types": [(NodeType.TOKEN.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)],
            "in_dims": {NodeType.TOKEN.value: 2},
            "num_relations": 1,
        },
        meta_path,
    )

    out_file = tmp_path / "model.pt"
    argv = [
        "train_res_gcl",
        "--encoder-checkpoint",
        str(ckpt),
        "--meta-path",
        str(meta_path),
        "--splits-dir",
        str(data_root),
        "--epochs",
        "1",
        "--batch-size",
        "1",
        "--device",
        "cpu",
        "--output",
        str(out_file),
        "--no-embeds",
    ]

    importlib.invalidate_caches()
    mod = importlib.import_module("src.cli.train_res_gcl")

    calls = []
    orig_init = mod.GraphDataset.__init__

    def rec_init(self, *args, **kwargs):
        calls.append(kwargs.get("load_embeds", True))
        orig_init(self, *args, **kwargs)

    monkeypatch.setattr(mod.GraphDataset, "__init__", rec_init)

    orig_argv = sys.argv
    sys.argv = argv
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert calls
    assert all(c is False for c in calls)
