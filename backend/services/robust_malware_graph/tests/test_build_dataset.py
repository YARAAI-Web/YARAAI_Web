import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.rulegen.build_dataset import build_dataset


def _make_graph() -> HeteroData:
    g = HeteroData()
    g["n"].x = torch.randn(1, 1)
    g["n"].num_nodes = 1
    return g


def test_build_dataset_basic(tmp_path):
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir()

    g1 = _make_graph()
    g2 = _make_graph()
    torch.save(g1, graph_dir / "a.pt")
    torch.save(g2, graph_dir / "b.pt")

    labels = tmp_path / "labels.csv"
    labels.write_text("sha256,label\na,0\nb,1\n")

    vocab = tmp_path / "meta.json"
    vocab.write_text("{}")

    out_dir = tmp_path / "out"

    build_dataset(
        hetero_dir=graph_dir,
        labels=labels,
        out_dir=out_dir,
        metadata_vocab=vocab,
    )

    clean = torch.load(out_dir / "clean.pt", weights_only=False)
    dummy = torch.load(out_dir / "dummy.pt", weights_only=False)
    assert len(clean) == 1
    assert len(dummy) == 1


