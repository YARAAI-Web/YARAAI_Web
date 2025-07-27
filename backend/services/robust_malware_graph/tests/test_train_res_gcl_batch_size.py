import importlib
import sys
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData, Data, Batch

from src.models.gnn.encoder import RGCNEncoder
from src.graphs.normalizers.schema import NodeType, EdgeRel


def _make_token_graph(path: Path, dim: int) -> None:
    g = HeteroData()
    g[NodeType.TOKEN.value].x = torch.randn(2, dim)
    g[NodeType.TOKEN.value].num_nodes = 2
    ei = torch.tensor([[0, 1], [1, 0]])
    et = (NodeType.TOKEN.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)
    g[et].edge_index = ei
    g[et].edge_type = torch.zeros(ei.size(1), dtype=torch.long)
    torch.save(g, path)


def test_batch_size_auto_reduce(tmp_path, monkeypatch, caplog):
    data_root = tmp_path / "data"
    for split in ("train", "val"):
        gdir = data_root / split / "graphs"
        gdir.mkdir(parents=True)
        _make_token_graph(gdir / "a.pt", 512)
        (data_root / split / "labels.csv").write_text("sha256,label\na,0\n")

    enc = RGCNEncoder(
        metadata=([NodeType.TOKEN.value], [(NodeType.TOKEN.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)]),
        in_dims={NodeType.TOKEN.value: 512},
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
            "in_dims": {NodeType.TOKEN.value: 512},
            "num_relations": 1,
        },
        meta_path,
    )

    importlib.invalidate_caches()
    mod = importlib.import_module("src.cli.train_res_gcl")
    called = {}
    orig = mod.make_dataloaders

    def rec_make(root, batch_size, *args, **kwargs):
        called["batch"] = batch_size
        return orig(root, batch_size, *args, **kwargs)

    monkeypatch.setattr(mod, "make_dataloaders", rec_make)

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
        "4",
        "--device",
        "cpu",
        "--output",
        str(tmp_path / "model.pt"),
    ]

    orig_argv = sys.argv
    sys.argv = argv
    caplog.set_level("WARNING", logger=mod.LOGGER.name)
    try:
        mod.main()
    finally:
        sys.argv = orig_argv

    assert called.get("batch") == 2
    assert any("reducing batch size" in rec.message for rec in caplog.records)


class DummyDataset:
    def __init__(self, num_graphs=1):
        self.graphs = []
        self.labels = []
        for i in range(num_graphs):
            x = torch.randn(3, 1)
            g = Data(x=x, edge_index=torch.tensor([[0, 1], [1, 2]]), num_nodes=3)
            self.graphs.append(g)
            self.labels.append(i % 2)

    def __len__(self):
        return len(self.graphs)

    def __getitem__(self, idx):
        return self.graphs[idx], self.labels[idx], f"id{idx}"


def collate(batch):
    return {
        "graph": Batch.from_data_list([b[0] for b in batch]),
        "label": torch.tensor([b[1] for b in batch], dtype=torch.long),
        "ids": [b[2] for b in batch],
    }


class BoomModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(1, 1)

    def forward(self, g, return_logits=True):
        raise RuntimeError("CUDA out of memory")


def test_train_one_epoch_oom(caplog):
    import src.cli.train_res_gcl as mod

    ds = DummyDataset()
    loader = torch.utils.data.DataLoader(ds, batch_size=1, collate_fn=collate)
    model = BoomModel()
    opt = torch.optim.SGD(model.parameters(), lr=0.1)

    caplog.set_level("ERROR", logger=mod.LOGGER.name)
    with pytest.raises(RuntimeError):
        mod.train_one_epoch(model, loader, opt, torch.device("cpu"))

    assert any("배치 크기를 줄이라" in rec.message for rec in caplog.records)
