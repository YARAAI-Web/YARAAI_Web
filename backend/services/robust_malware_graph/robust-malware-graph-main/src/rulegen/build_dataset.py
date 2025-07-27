from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, List

import torch

from common.logger import get_logger
from common.utils import ensure_dir
from graphs.dataset.graph_dataset import GraphDataset, _guess_graph_path

LOGGER = get_logger(__name__)


def _load_labels(path: Path) -> Dict[str, int]:
    labels: Dict[str, int] = {}
    suffix = path.suffix.lower()
    if suffix in {".csv", ".tsv"}:
        with path.open("r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sha = row.get("sha256")
                label = row.get("label")
                if sha is None or label is None:
                    continue
                labels[sha] = int(label)
    elif suffix in {".jsonl", ".json"}:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                obj = json.loads(line)
                sha = obj.get("sha256")
                label = obj.get("label")
                if sha is None or label is None:
                    continue
                labels[sha] = int(label)
    else:
        raise ValueError(f"Unsupported labels file: {path}")
    return labels


def _load_graph(graph_dir: Path, sha: str, binary_dir: Path | None = None):
    path = _guess_graph_path(graph_dir, sha)
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.suffix == ".pyg.pkl":
        import pickle

        with path.open("rb") as f:
            g = pickle.load(f)
    else:
        g = torch.load(path, map_location="cpu", weights_only=False)

    try:
        g.file_path = str(binary_dir / sha) if binary_dir is not None else str(path)
        g.sha256 = sha
    except Exception:
        pass
    return g


def build_dataset(
    *,
    hetero_dir: Path,
    labels: Path,
    out_dir: Path,
    metadata_vocab: Path | None = None,
    meta_path: Path | None = None,
    binary_dir: Path | None = None,
    clean_label: int = 0,
    dummy_label: int = 1,
) -> None:
    """Build clean/dummy datasets for PPO training."""
    ensure_dir(out_dir)

    if meta_path is not None:
        meta = torch.load(meta_path, map_location="cpu", weights_only=False)
        attr_names_meta = meta.get("attr_names")
        max_ids = meta.get("max_ids")
        if attr_names_meta is None or max_ids is None:
            raise RuntimeError("Meta snapshot missing attr_names or max_ids")
        vocab = {
            nt: {name: int(max_ids.get(name, 0)) for name in names}
            for nt, names in attr_names_meta.items()
        }
        if metadata_vocab is None:
            metadata_vocab = out_dir / "metadata_vocab.json"
            with metadata_vocab.open("w", encoding="utf-8") as fp:
                json.dump(vocab, fp)
    else:
        if metadata_vocab is None:
            raise ValueError("Either metadata_vocab or meta_path is required")
        with metadata_vocab.open("r", encoding="utf-8") as f:
            vocab = json.load(f)

    attr_names: Dict[str, List[str]] = {}
    for nt, attrs in vocab.items():
        if isinstance(attrs, dict):
            attr_names[nt] = sorted(attrs.keys())
        elif isinstance(attrs, list):
            attr_names.setdefault("", []).append(nt)
        else:
            raise TypeError(f"Unsupported value type for {nt!r}: {type(attrs).__name__}")

    label_map = _load_labels(labels)
    clean_graphs: List[object] = []
    dummy_graphs: List[object] = []

    for sha, lab in label_map.items():
        try:
            g = _load_graph(hetero_dir, sha, binary_dir)
            g = GraphDataset._sanitize_attrs(g)
            g = GraphDataset._ensure_num_nodes(g)
            g = GraphDataset._ensure_x(g)
            g = GraphDataset._sanitize_edges(g)
            g = GraphDataset._ensure_meta_ids(g, attr_names)
        except FileNotFoundError:
            LOGGER.warning("Graph for %s not found", sha)
            continue

        if lab == clean_label:
            clean_graphs.append(g)
        elif lab == dummy_label:
            dummy_graphs.append(g)
        else:
            LOGGER.warning("Unknown label %s for %s", lab, sha)

    torch.save(clean_graphs, out_dir / "clean.pt")
    torch.save(dummy_graphs, out_dir / "dummy.pt")
    LOGGER.info(
        "Saved dataset \u2192 %s (clean:%d, dummy:%d)",
        out_dir,
        len(clean_graphs),
        len(dummy_graphs),
    )

