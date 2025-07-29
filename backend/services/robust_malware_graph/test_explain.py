from pathlib import Path
import json
from scripts.single_sample_explainer_tokens import extract_top_tokens

with open("data/raw/000077419ead44800537b34f5c2137e572c472698a13c39151f90eaabde7c94e.json", "r", encoding="utf-8") as f:
    js = json.load(f)

print(extract_top_tokens(js,Path("models/explainers_cli/explainer.pt")))