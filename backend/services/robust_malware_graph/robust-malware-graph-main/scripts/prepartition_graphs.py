import argparse
import sys
from pathlib import Path
import torch
import numpy as np

# add repo root for local imports when executed directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from torch_geometric.loader import ClusterData


def load_graph(path: Path):
    return torch.load(path, weights_only=False)


def main(argv=None):
    p = argparse.ArgumentParser(description="Pre-partition graphs with METIS")
    p.add_argument("graph_dir", type=Path, help="Directory with *.pt graphs")
    p.add_argument("--parts", type=int, default=1500, help="Number of partitions")
    p.add_argument("--output-dir", type=Path, default=Path("cluster"), help="Directory to save *.npz files")
    args = p.parse_args(argv)

    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    paths = sorted(args.graph_dir.glob("*.pt"))
    for gp in paths:
        g = load_graph(gp)
        cd = ClusterData(g, num_parts=args.parts, recursive=False)
        part = cd.partition
        np.savez_compressed(
            out_dir / f"{gp.stem}.npz",
            indptr=part.indptr.cpu().numpy(),
            index=part.index.cpu().numpy(),
            partptr=part.partptr.cpu().numpy(),
            node_perm=part.node_perm.cpu().numpy(),
            edge_perm=part.edge_perm.cpu().numpy(),
            sparse_format=part.sparse_format,
        )
        print(f"[OK] {gp.name} -> {gp.stem}.npz")


if __name__ == "__main__":
    main()
