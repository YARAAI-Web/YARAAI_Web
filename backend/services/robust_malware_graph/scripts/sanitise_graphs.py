import argparse
from pathlib import Path
import pickle
import sys
import torch
from tqdm import tqdm

# Add the repository root to the module search path so that "src" can be
# imported when this script is executed directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.graphs.dataset import GraphDataset


def load_graph(path: Path):
    if path.suffix == ".pt":
        return torch.load(path, weights_only=False)
    if path.name.endswith(".pyg.pkl"):
        with path.open("rb") as f:
            return pickle.load(f)
    raise ValueError(f"Unsupported file type: {path}")


def save_graph(graph, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".pt":
        torch.save(graph, path)
    elif path.name.endswith(".pyg.pkl"):
        with path.open("wb") as f:
            pickle.dump(graph, f)
    else:
        raise ValueError(f"Unsupported file type: {path}")


def main():
    parser = argparse.ArgumentParser(
        description="Rewrite graph files with sanitised edge_index values"
    )
    parser.add_argument("input_dir", type=Path, help="directory with original graphs")
    parser.add_argument(
        "output_dir", type=Path, help="directory to save cleaned graphs"
    )
    args = parser.parse_args()

    in_dir = args.input_dir
    out_dir = args.output_dir

    paths = list(in_dir.rglob("*.pt")) + list(in_dir.rglob("*.pyg.pkl"))
    for src_path in tqdm(paths, desc="sanitize", unit="file"):
        rel = src_path.relative_to(in_dir)
        dst_path = out_dir / rel
        try:
            graph = load_graph(src_path)
            graph = GraphDataset._ensure_num_nodes(graph)
            graph = GraphDataset._sanitize_edges(graph)
            save_graph(graph, dst_path)
        except Exception as e:
            tqdm.write(f"Error processing {src_path}: {e}")


if __name__ == "__main__":
    main()
