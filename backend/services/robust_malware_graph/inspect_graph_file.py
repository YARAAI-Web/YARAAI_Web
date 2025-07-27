

import torch
from pathlib import Path
import tqdm
import sys
from torch_geometric.data import HeteroData

def inspect_graph_files(directory: Path):
    """
    Inspects all graph files in a directory to find inconsistencies.
    Checks if max(edge_index) >= num_nodes.
    """
    print(f"🔍 Inspecting graph files in: {directory}")
    problematic_files = []
    
    if not directory.is_dir():
        print(f"❌ Error: Directory not found at '{directory}'")
        sys.exit(1)
        
    graph_files = sorted(list(directory.glob("*.pt")))

    if not graph_files:
        print("No graph files (.pt) found.")
        return

    for graph_path in tqdm.tqdm(graph_files, desc="Inspecting graphs"):
        try:
            # PyTorch 2.6+ requires weights_only=False for unpickling custom classes
            data = torch.load(graph_path, map_location='cpu', weights_only=False)
            
            if not isinstance(data, HeteroData):
                 problematic_files.append((graph_path.name, f"File is not a HeteroData object, but a {type(data)}"))
                 continue

            num_nodes = data.num_nodes if hasattr(data, 'num_nodes') and data.num_nodes is not None else 0
            if num_nodes == 0:
                for store in data.node_stores:
                    num_nodes += store.num_nodes
            
            if num_nodes == 0:
                 problematic_files.append((graph_path.name, "Could not determine num_nodes, it is zero."))
                 continue

            # Validate the graph structure
            data.validate()

            for store in data.edge_stores:
                if hasattr(store, 'edge_index') and store.edge_index is not None:
                    if store.edge_index.numel() > 0:
                        max_index = store.edge_index.max()
                        if max_index >= num_nodes:
                            problematic_files.append((
                                graph_path.name, 
                                f"edge_index.max() ({max_index}) >= num_nodes ({num_nodes}) in edge type '{store._key}'"
                            ))
                            break
        
        except Exception as e:
            problematic_files.append((graph_path.name, f"Failed to load or process: {e}"))

    if problematic_files:
        print("\n" + "="*30)
        print("❌ Found problematic files:")
        print("="*30)
        for filename, reason in problematic_files:
            print(f"  - {filename}: {reason}")
        print("="*30)
        print("\nTo fix this, you may need to delete these files and regenerate them, or run the sanitisation script.")
    else:
        print("\n" + "="*30)
        print("✅ All graph files seem consistent.")
        print("="*30)

if __name__ == "__main__":
    default_dir = "data/hetero_clean"
    
    if len(sys.argv) > 1:
        data_dir_str = sys.argv[1]
    else:
        data_dir_str = default_dir
        
    data_dir = Path(data_dir_str)
    inspect_graph_files(data_dir)
