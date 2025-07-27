#!/usr/bin/env python3
"""Generate metadata vocabulary sizes from graph dataset.

This script scans graph files under a dataset directory using
``GraphDataset`` and computes the maximum observed id value for each
``<name>_id`` tensor grouped by node type.  The resulting dictionary is
stored as JSON.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Set

import torch

# Add repository root so ``src`` can be imported when run directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.graphs.dataset import GraphDataset  # type: ignore
from torch_geometric.data import Data, HeteroData


def collect_vocab(ds: GraphDataset) -> Dict[str, Dict[str, int]]:
    """Collect maximum id values for ``<name>_id`` tensors within ``ds``."""
    vocab: Dict[str, Dict[str, int]] = {}
    for i in range(len(ds)):
        item = ds[i]
        g = item[0] if isinstance(item, tuple) else item
        if isinstance(g, HeteroData):
            for nt in g.node_types:
                store = g[nt]
                for key, val in store.items():
                    if key.endswith("_id") and isinstance(val, torch.Tensor):
                        if val.numel() == 0:
                            continue
                        attr = key[:-3]
                        nt_map = vocab.setdefault(nt, {})
                        nt_map[attr] = max(nt_map.get(attr, -1), int(val.max()))
        elif isinstance(g, Data):
            for key, val in g.items():
                if key.endswith("_id") and isinstance(val, torch.Tensor):
                    if val.numel() == 0:
                        continue
                    attr = key[:-3]
                    nt_map = vocab.setdefault("", {})
                    nt_map[attr] = max(nt_map.get(attr, -1), int(val.max()))
    return vocab


def merge_vocab(dest: Dict[str, Dict[str, int]], src: Dict[str, Dict[str, int]]) -> None:
    for nt, attrs in src.items():
        dest_nt = dest.setdefault(nt, {})
        for name, val in attrs.items():
            dest_nt[name] = max(dest_nt.get(name, -1), val)


# Gather vocabulary from view JSON by recursively scanning for lists of strings
# or single string fields.
def _collect_view(obj: Any, vocab: Dict[str, Set[str]]) -> None:
    """Recursively collect string fields from ``obj`` into ``vocab``.

    This processes lists of strings as well as single string fields, so view
    JSON files can store tokens either way.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, list) and all(isinstance(it, str) for it in v):
                vocab.setdefault(k, set()).update(v)
            elif isinstance(v, str):
                vocab.setdefault(k, set()).add(v)
            else:
                _collect_view(v, vocab)
    elif isinstance(obj, list):
        for it in obj:
            _collect_view(it, vocab)


def process_view_file(path: Path, vocab: Dict[str, Set[str]]) -> None:
    with path.open("r", encoding="utf-8") as fp:
        data = json.load(fp)
    _collect_view(data, vocab)


def cmd_graphs(args: argparse.Namespace) -> None:
    """Process dataset graphs and save vocabulary sizes."""
    vocab: Dict[str, Dict[str, int]] = {}
    for split in args.splits:
        if not (args.data_dir / split).is_dir():
            continue
        ds = GraphDataset(
            args.data_dir,
            split=split,
            label_file=args.label_file,
            require_labels=False,
            load_embeds=False,
        )
        split_vocab = collect_vocab(ds)
        merge_vocab(vocab, split_vocab)

    result = {
        nt: {name: val + 1 for name, val in attrs.items()} for nt, attrs in vocab.items()
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as fp:
        json.dump(result, fp, indent=2)
    print(f"[OK] saved -> {args.output}")


def cmd_views(args: argparse.Namespace) -> None:
    """Extract vocabulary from view JSON files."""
    vocab: Dict[str, Set[str]] = {}
    for jp in args.views_dir.rglob("*.json"):
        process_view_file(jp, vocab)

    result = {k: sorted(vals) for k, vals in vocab.items()}

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as fp:
        json.dump(result, fp, indent=2)
    print(f"[OK] saved -> {args.output}")


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Collect metadata vocabulary")
    sub = p.add_subparsers(dest="command", required=True)

    p_graphs = sub.add_parser("graphs", help="collect vocab sizes from dataset graphs")
    p_graphs.add_argument("data_dir", type=Path, help="Dataset root directory")
    p_graphs.add_argument("--output", type=Path, required=True, help="Output JSON file")
    p_graphs.add_argument(
        "--splits",
        nargs="*",
        default=("train", "val", "test"),
        help="Dataset splits to process (default: train val test)",
    )
    p_graphs.add_argument(
        "--label-file",
        dest="label_file",
        default="labels.csv",
        help="Label filename inside each split (default: labels.csv)",
    )
    p_graphs.set_defaults(func=cmd_graphs)

    p_views = sub.add_parser("views", help="collect vocab from view JSON files")
    p_views.add_argument("views_dir", type=Path, help="Directory containing view JSON files")
    p_views.add_argument("--output", type=Path, required=True, help="Output JSON file")
    p_views.set_defaults(func=cmd_views)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
