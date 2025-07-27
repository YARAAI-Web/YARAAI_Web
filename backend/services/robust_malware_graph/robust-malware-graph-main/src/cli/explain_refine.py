#!/usr/bin/env python3
"""Refine explanation by pruning and re-evaluating a graph."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import torch
from torch_geometric.data import HeteroData
from torch.serialization import add_safe_globals
from torch_geometric.data import storage

from src.common.utils import get_logger
from src.graphs.loaders import get_loader
from src.graphs.builders import HeteroGraphBuilder
from src.graphs.dataset.graph_dataset import GraphDataset
from robust_malware_graph.explain import ensure_edgeaware_selector
from src.explain.utils.prune import prune_to_selected
from src.models.gnn.res_wrapper import RESGCLClassifier

LOGGER = get_logger(__name__)


def _load_graph(path: Path, view: str, attr_names: dict[str, list[str]]) -> HeteroData:
    if path.suffix in {".pt", ".pkl", ".pyg.pkl"}:
        g = torch.load(path, weights_only=False)
    else:
        g = get_loader(view).load(path)
    if not isinstance(g, HeteroData):
        builder = HeteroGraphBuilder()
        builder.add_view(g, view)
        g = builder.build()
    g = GraphDataset._ensure_num_nodes(g)
    g = GraphDataset._ensure_x(g)
    g = GraphDataset._ensure_meta_ids(g, attr_names)
    for nt in g.node_types:
        g[nt].batch = torch.zeros(g[nt].num_nodes, dtype=torch.long)
    return g


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Prune a graph with a selector and re-evaluate",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("selector", type=Path, help="Trained selector checkpoint")
    p.add_argument("graph", type=Path, help="Single-view graph path")
    p.add_argument("--model", type=Path, required=True, help="RESGCL checkpoint")
    p.add_argument("--view", type=str, default="cfg", help="Graph view name")
    p.add_argument("--device", type=str, default="cpu")
    p.add_argument("--save-path", type=Path, help="Optional output *.pt for pruned graph")
    return p


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    add_safe_globals([storage.BaseStorage, storage.NodeStorage, storage.EdgeStorage, storage.GlobalStorage])
    selector = torch.load(args.selector, map_location="cpu")
    LOGGER.info("Selector loaded: %s", args.selector)

    device = torch.device(args.device)
    model = RESGCLClassifier.load_from_checkpoint(args.model, map_location=device)
    model.to(device).eval()

    graph = _load_graph(args.graph, args.view, model.encoder.attr_names)
    LOGGER.info("Graph loaded: %s", args.graph)

    ensure_edgeaware_selector(selector, graph)
    selector.to(device)
    sel = selector.hard_selection(graph)
    if isinstance(sel, dict):
        keep = torch.cat(list(sel.values())).tolist()
    else:
        keep = sel.tolist()
    pruned = prune_to_selected(graph, keep)

    if args.save_path:
        args.save_path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(pruned, args.save_path)
        LOGGER.info("Pruned graph saved → %s", args.save_path)

    with torch.no_grad():
        prob = model(pruned.to(device)).sigmoid().item()
    print(f"probability={prob:.6f}")


if __name__ == "__main__":
    main()
