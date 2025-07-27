
import torch
from pathlib import Path
import argparse
from torch_geometric.data import HeteroData, storage
from torch.serialization import add_safe_globals

from src.graphs.sampling import sample_subgraph
from src.models.gnn.res_wrapper import RESGCLClassifier
from src.explain import train_selector, ensure_edgeaware_selector
from src.graphs.dataset import GraphDataset
from src.graphs.features.cache import load_tensor

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Train Gumbel-Mask selector with sub-sampling.")
    p.add_argument("--model-path", type=Path, required=True, help="Classifier checkpoint")
    p.add_argument("--dataset-path", type=Path, required=True, help="*.pt graph dataset")
    p.add_argument("--output-path", type=Path, required=True, help="Save trained selector")
    p.add_argument("--embed-dir", type=Path, default=Path("data/embeds"))
    p.add_argument("--device", type=str, default="cuda:0" if torch.cuda.is_available() else "cpu")
    p.add_argument("--epochs", type=int, default=300)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--sampling-method", type=str, choices=["neighbor", "hgt"], default="neighbor", help="Subgraph sampler type")
    p.add_argument("--batch-size", type=int, default=2048, help="Number of target-type nodes per mini-batch")
    p.add_argument("--num-neighbors", type=int, default=15, help="Neighbors to sample per hop")
    p.add_argument("--num-hops", type=int, default=2, help="K-hop neighborhood")
    p.add_argument("--view", type=str, default="cfg", help="Edge relation view")
    p.add_argument(
        "--amp",
        action="store_true",
        help="Enable mixed precision (CUDA) and halve feature precision",
    )
    return p

def select_cfg_graph(dataset, model, selector_type) -> HeteroData:
    """Selects a single, small, valid graph from the dataset for training."""
    from src.explain import GumbelMaskSelector
    
    for i, g_path in enumerate(dataset):
        g = torch.load(g_path, weights_only=False)
        
        if not isinstance(g, HeteroData):
            continue
            
        if model.encoder.target_node not in g.node_types:
            continue
            
        if g[model.encoder.target_node].num_nodes == 0:
            continue
            
        if not any(et[1] == "cfg" and g[et].num_edges > 0 for et in g.edge_types):
            continue
            
        # Check if the graph has parameters for the selector
        try:
            temp_selector = GumbelMaskSelector(view="cfg")
            temp_selector._init_params(g)
            if not list(temp_selector.parameters()):
                continue
        except Exception as e:
            continue

        return g

    raise ValueError("No suitable graph found for training the explainer.")

def main():
    args = build_parser().parse_args()
    add_safe_globals([storage.BaseStorage, storage.GlobalStorage, storage.NodeStorage])

    device = torch.device(args.device)

    model = RESGCLClassifier.load_from_checkpoint(args.model_path, map_location=device)
    model.to(device).eval()

    graph_files = list(Path(args.dataset_path).glob("*.pt"))
    if not graph_files:
        raise ValueError(f"No graph files found in {args.dataset_path}")

    graph = None
    for g_path in sorted(graph_files, key=lambda p: p.stat().st_size): # sort by size
        g = torch.load(g_path, weights_only=False)
        if isinstance(g, HeteroData) and model.encoder.target_node in g.node_types and g[model.encoder.target_node].num_nodes > 0:
            if any(et[1] == "cfg" and g[et].num_edges > 0 for et in g.edge_types):
                from src.explain import GumbelMaskSelector
                temp_selector = GumbelMaskSelector(view="cfg")
                temp_selector._init_params(g)
                if list(temp_selector.parameters()):
                    graph = g
                    # Free up memory
                    del temp_selector
                    break
        del g # Free up memory
    
    if graph is None:
        raise ValueError("No suitable graph found for training the explainer.")
        
    sha = getattr(graph, "sha256", None) or getattr(graph, "name", None)

    if sha and "token" in graph.node_types:
        embed_file = args.embed_dir / f"{sha}.ftr"
        if embed_file.is_file():
            # Use mmap=False to prevent "Too many open files" errors in
            # environments with limited file descriptors.
            graph["token"].x = load_tensor(sha, args.embed_dir, mmap=False)

    graph = GraphDataset._ensure_num_nodes(graph)
    graph = GraphDataset._ensure_x(graph)
    graph = GraphDataset._ensure_meta_ids(graph, model.encoder.attr_names)
    for nt in graph.node_types:
        graph[nt].batch = torch.zeros(graph[nt].num_nodes, dtype=torch.long)

    from src.graphs.dataset.graph_dataset import collect_dataset_metadata
    
    class SingleGraphDataset:
        def __init__(self, graph):
            self.graph = graph
        def __len__(self):
            return 1
        def __getitem__(self, idx):
            g = GraphDataset._ensure_num_nodes(self.graph)
            g = GraphDataset._ensure_x(g)
            g = GraphDataset._sanitize_edges(g)
            return g

    _, in_dims, _, _ = collect_dataset_metadata(
        [SingleGraphDataset(graph)], attr_dim=model.encoder.attr_dim
    )
    for nt, proj in model.encoder.input_proj.items():
        act_dim = in_dims.get(nt)
        if act_dim and proj.in_features != act_dim:
            model.encoder.input_proj[nt] = torch.nn.Linear(
                act_dim, proj.out_features, device=device
            )

    score_fn = lambda g: model(g, return_logits=True).squeeze()

    selector = train_selector(
        graph,
        model,
        view=args.view,
        device=device,
        epochs=args.epochs,
        lr=args.lr,
        amp=args.amp,
        score_fn=score_fn,
    )
    ensure_edgeaware_selector(selector, graph)
    selector.to(device)

    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(selector, args.output_path)
    print(f"[OK] selector saved → {args.output_path}")

if __name__ == "__main__":
    main()
