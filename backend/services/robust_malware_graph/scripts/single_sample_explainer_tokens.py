#!/usr/bin/env python3
"""Extract saliency tokens from a single JSON sample using a trained explainer."""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path
from typing import Sequence

__all__ = ["extract_top_tokens", "main"]

# Allow running from outside repository root
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

import torch

from src.common.logger import get_logger
from rulegen.feature_miner import FeatureMiner
from src.cli.explainer_rule_eval import _compute_saliency_with_explainer, _extract_tokens
from scripts.single_sample_classify import preprocess

logger = get_logger(__name__)


def extract_top_tokens(
    json_obj: dict,
    explainer_ckpt: Path,
    *,
    threshold: int = 5,
    device: str = "cuda" if torch.cuda.is_available() else "cpu",
) -> list[str]:
    """Return top ``threshold`` tokens by saliency in ``json_obj``."""
    device_t = torch.device(device)
    explainer = torch.load(explainer_ckpt, map_location=device_t, weights_only=False)
    classifier = getattr(explainer, "model", None) or getattr(explainer, "classifier", None)
    if classifier is None:
        raise RuntimeError("Explainer checkpoint missing classifier model")

    with tempfile.TemporaryDirectory() as tmpdir:
        work_dir = Path(tmpdir)
        json_path = work_dir / "sample.json"
        with json_path.open("w", encoding="utf-8") as f:
            json.dump(json_obj, f)

        graph_path, _ = preprocess(json_path, work_dir, device)
        # ``preprocess`` returns the path to the generated graph
        graph = torch.load(graph_path, map_location="cpu", weights_only=False)
        saliency = _compute_saliency_with_explainer(graph, classifier, explainer, device_t)

        miner = FeatureMiner(top_k=threshold * 5)
        feats = miner.mine(graph, saliency)

        tokens: list[str] = []
        seen: set[str] = set()
        for feat in feats:
            for tok in _extract_tokens(feat):
                tok = tok.lower()
                if tok not in seen:
                    seen.add(tok)
                    tokens.append(tok)
                    if len(tokens) >= threshold:
                        break
            if len(tokens) >= threshold:
                break
    return tokens


def main(argv: Sequence[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Print top saliency tokens")
    p.add_argument("--json", type=Path, required=True, help="Path to JSON sample")
    p.add_argument("--explainer", type=Path, required=True, help="Explainer checkpoint")
    p.add_argument("--threshold", type=int, default=5, help="Number of tokens to output")
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = p.parse_args(argv)

    with args.json.open("r", encoding="utf-8") as f:
        js = json.load(f)

    tokens = extract_top_tokens(js, args.explainer, threshold=args.threshold, device=args.device)
    for t in tokens:
        print(t)


if __name__ == "__main__":  # pragma: no cover
    main()
