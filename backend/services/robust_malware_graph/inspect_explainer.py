import torch
from pathlib import Path
from torch.serialization import add_safe_globals
import sys

# Add src to path to allow importing PGExplainer
sys.path.insert(0, str(Path(__file__).parent / 'src'))

try:
    from explain.pg_explainer import PGExplainer
    # Allow deserialization of PGExplainer
    add_safe_globals([PGExplainer])

    explainer_path = Path('models/explainers/explainer.pt')
    if explainer_path.exists():
        try:
            # Explicitly use weights_only=False as required by the error message
            explainer = torch.load(explainer_path, map_location='cpu', weights_only=False)
            print(f"Explainer object type: {type(explainer)}")
            
            print("\n--- Attributes ---")
            for attr in dir(explainer):
                if not attr.startswith('_'):
                    try:
                        attr_val = getattr(explainer, attr)
                        print(f"  - {attr}: {type(attr_val)}")
                    except Exception:
                        print(f"  - {attr}: (Could not get type)")

            if hasattr(explainer, 'model'):
                print("\n--- explainer.model ---")
                model = explainer.model
                print(f"Type: {type(model)}")
                if hasattr(model, 'encoder'):
                     print("\n--- explainer.model.encoder ---")
                     print(model.encoder)
                else:
                    print("explainer.model has no 'encoder' attribute.")
            elif hasattr(explainer, 'encoder'):
                print("\n--- explainer.encoder ---")
                encoder = explainer.encoder
                print(f"Type: {type(encoder)}")
                print(encoder)
            else:
                print("\nExplainer has no 'model' or 'encoder' attribute.")

        except Exception as e:
            print(f"Error loading or inspecting explainer: {e}")
    else:
        print(f"Explainer file not found at: {explainer_path}")

except ImportError as e:
    print(f"Failed to import necessary modules: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
