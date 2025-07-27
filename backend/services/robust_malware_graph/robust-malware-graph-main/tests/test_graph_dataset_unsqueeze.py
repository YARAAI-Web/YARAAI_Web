import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.graphs.dataset.graph_dataset import GraphDataset


def test_collate_unsqueezes_1d_feature(tmp_path):
    graph_dir = tmp_path / "train" / "graphs"
    graph_dir.mkdir(parents=True)

    g1 = HeteroData()
    g1["n"].x = torch.tensor([1.0, 2.0])
    g1["n"].num_nodes = 2

    g2 = HeteroData()
    g2["n"].x = torch.tensor([[3.0, 4.0], [5.0, 6.0]])
    g2["n"].num_nodes = 2

    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    ds = GraphDataset(tmp_path, split="train", label_file=None)
    from torch.utils.data import DataLoader

    loader = DataLoader(ds, batch_size=2, collate_fn=GraphDataset.collate_fn)
    batch = next(iter(loader))

    assert batch["graph"]["n"].x.shape == (4, 2)
