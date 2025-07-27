import sys
from pathlib import Path
import math
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")
pytest.importorskip("sklearn")
pytest.importorskip("matplotlib")

import torch
from torch.utils.data import DataLoader
from torch_geometric.data import Data, Batch
from torch_geometric.nn import global_mean_pool

from src.cli.finetune_supcon import evaluate
from src.models.contrast.sup_con import SupContrastHead


class DummyDataset:
    def __init__(self, num_graphs=8, num_classes=2):
        self.graphs = []
        self.labels = []
        for i in range(num_graphs):
            x = torch.randn(3, 1) + i
            g = Data(x=x, edge_index=torch.tensor([[0, 1], [1, 2]]), num_nodes=3)
            self.graphs.append(g)
            self.labels.append(i % num_classes)

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


class DummyEncoder(torch.nn.Module):
    def __init__(self, in_dim=1, out_dim=2):
        super().__init__()
        self.lin = torch.nn.Linear(in_dim, out_dim)
        self.out_dim = out_dim

    def forward(self, batch):
        h = self.lin(batch.x.float())
        return global_mean_pool(h, batch.batch)


def make_model():
    enc = DummyEncoder()
    head = SupContrastHead(in_dim=enc.out_dim, proj_dim=enc.out_dim)
    model = torch.nn.Module()
    model.encoder = enc
    model.head = head
    return model


def _check_metrics(metrics):
    assert set(metrics) == {"AUROC", "MacroF1"}
    assert all(not math.isnan(v) for v in metrics.values())


def test_evaluate_binary():
    ds = DummyDataset(num_graphs=8, num_classes=2)
    loader = DataLoader(ds, batch_size=4, collate_fn=collate)
    model = make_model()
    metrics = evaluate(model, loader, torch.device("cpu"))
    _check_metrics(metrics)


def test_evaluate_multiclass():
    ds = DummyDataset(num_graphs=9, num_classes=3)
    loader = DataLoader(ds, batch_size=3, collate_fn=collate)
    model = make_model()
    metrics = evaluate(model, loader, torch.device("cpu"))
    _check_metrics(metrics)
