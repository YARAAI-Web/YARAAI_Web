from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import torch
from torch_geometric.data import HeteroData

from src.models.gnn.res_wrapper import RESGCLClassifier
from src.graphs.dataset import GraphDataset


def load_graph(path: Path) -> HeteroData:
    g = torch.load(path, weights_only=False)
    return GraphDataset._ensure_x(GraphDataset._ensure_num_nodes(g))


def compute_score(model: RESGCLClassifier, g: HeteroData, device: torch.device) -> float:
    for nt in g.node_types:
        g[nt].batch = torch.zeros(g[nt].num_nodes, dtype=torch.long)
    g = g.to(device)
    with torch.no_grad():
        logits = model(g, return_logits=True).squeeze()
    return float(logits.cpu().item())


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Precompute full graph scores")
    parser.add_argument("--model", type=Path, required=True, help="Classifier checkpoint")
    parser.add_argument("--device", type=str, default="cpu")
    parser.add_argument("--output", type=Path, required=True, help="Score cache JSON path")
    parser.add_argument("graphs", nargs="+", type=Path, help="Graph files (*.pt)")
    args = parser.parse_args(argv)

    device = torch.device(args.device)
    model = RESGCLClassifier.load_from_checkpoint(args.model, map_location=device)
    model.to(device).eval()

    scores: dict[str, float] = {}
    for gp in args.graphs:
        g = load_graph(gp)
        g = GraphDataset._ensure_meta_ids(g, model.encoder.attr_names)
        sha = getattr(g, "sha256", gp.stem)
        scores[sha] = compute_score(model, g, device)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as fp:
        json.dump(scores, fp, indent=2)
    print(f"[OK] scores saved -> {args.output}")


if __name__ == "__main__":
    main()
