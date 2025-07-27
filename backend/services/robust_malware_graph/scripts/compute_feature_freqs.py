import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import argparse
import json
from collections import Counter
import csv

import torch
from torch_geometric.data import Data, HeteroData

from src.graphs.dataset.graph_dataset import GraphDataset, _guess_graph_path
from rulegen.feature_miner import FeatureMiner


def load_graph(path: Path) -> HeteroData | Data:
    g = torch.load(path, map_location="cpu", weights_only=False)
    g = GraphDataset._ensure_num_nodes(g)
    return g


def num_nodes(g: HeteroData | Data) -> int:
    if isinstance(g, HeteroData):
        return sum(int(g[nt].num_nodes or 0) for nt in g.node_types)
    return int(getattr(g, "num_nodes", 0) or 0)

def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(
        description="Compute feature frequency statistics. Output format is"
        " {feature: [mal_count, ben_count]}"
    )
    p.add_argument("--graph-dir", type=Path, required=True, help="Directory containing graphs")
    p.add_argument("--meta-csv", type=Path, help="CSV with filename,sha256,label")
    p.add_argument("--out", type=Path, required=True, help="Output JSON path")
    args = p.parse_args(argv)

    miner = FeatureMiner(top_k_percent=1.0, min_saliency=0.0)
    counts_mal: Counter[str] = Counter()
    counts_ben: Counter[str] = Counter()

    graph_dir = Path(args.graph_dir)

    mal_graph_paths: list[Path] = []
    benign_graph_paths: list[Path] = []
    if args.meta_csv and args.meta_csv.is_file():
        seen_mal: set[Path] = set()
        seen_ben: set[Path] = set()
        with args.meta_csv.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    label = int(row.get("label", "1"))
                except ValueError:
                    continue
                sha = row.get("sha256") or row.get("sha")
                alt = row.get("filename") or row.get("name")
                path = None
                if sha:
                    cand = _guess_graph_path(graph_dir, sha)
                    if cand.is_file():
                        path = cand
                if path is None and alt:
                    alt_path = graph_dir / alt
                    if alt_path.is_file():
                        path = alt_path
                    else:
                        stem = Path(alt).stem
                        for c in graph_dir.glob(f"{stem}.*"):
                            if c.is_file():
                                path = c
                                break
                if not path or not path.is_file():
                    continue
                if label == 0:
                    if path not in seen_ben:
                        benign_graph_paths.append(path)
                        seen_ben.add(path)
                else:
                    if path not in seen_mal:
                        mal_graph_paths.append(path)
                        seen_mal.add(path)
    else:
        mal_graph_paths = sorted(graph_dir.glob("*.pt"))
        benign_graph_paths = []

    for gp in mal_graph_paths:
        g = load_graph(gp)
        sal = torch.zeros(num_nodes(g))
        feats = miner(g, sal)
        counts_mal.update(feats)

    for gp in benign_graph_paths:
        g = load_graph(gp)
        sal = torch.zeros(num_nodes(g))
        feats = miner(g, sal)
        counts_ben.update(feats)

    all_keys = set(counts_mal) | set(counts_ben)
    result = {
        k: [counts_mal.get(k, 0), counts_ben.get(k, 0)] for k in sorted(all_keys)
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"[OK] saved -> {args.out}")


if __name__ == "__main__":  # pragma: no cover
    main()
