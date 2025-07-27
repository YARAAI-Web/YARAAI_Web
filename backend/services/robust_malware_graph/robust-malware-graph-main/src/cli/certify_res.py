#!/usr/bin/env python3
"""robust‑malware‑graph – *RES‑GCL* Certification CLI
====================================================
Randomised **Edge‑Drop Smoothing** certification for robust malware graph
classifiers trained with *RES‑GCL* ("Robust & Efficient Smoothing in Graph
Contrastive Learning", NeurIPS 2023).

This script estimates a **certified perturbation radius *r*** (in number of
edges) within which the model's prediction is provably unchanged.
The procedure follows Section 5 of the paper ... and is equivalent to
`core.smoothing.certify()` but adds CLI conveniences (CSV output, tqdm, WandB…).

Example
-------
```bash
python -m cli.certify_res \
    --checkpoint models/gnn/res_gcl.pt \
    --hetero-dir data/hetero \
    --split test \
    --batch-size 32 --n-samples 100 --alpha 0.001 \
    --out results/res_certified_test.csv
```

Highlights
~~~~~~~~~~
* **torch_geometric** end‑to‑end (no DGL)
* Supports **time‑split** datasets under `data/splits/`
* Fast **numba** implementation of edge‑drop perturbations
* Optional **WandB** logging & CSV export
* Multiprocessing‑friendly (uses `torch.multiprocessing` spawn)

"""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
from typing import List

import torch
from torch.utils.data import DataLoader
from tqdm.auto import tqdm
import torch_geometric as tg

try:
    import wandb  # optional
except ImportError:  # pragma: no cover
    wandb = None

from common.logger import get_logger
from common.utils import ensure_dir
from graphs.splits import load_split_ids
from graphs.datasets.hetero_dataset import HeteroMalwareDataset
from models.gnn.res_wrapper import RESGCLClassifier
from evaluation.certification import certify_batch

LOGGER = get_logger(__name__)

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Certify RES‑GCL model via randomized edge smoothing.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--checkpoint", type=Path, required=True,
                   help="Path to trained RES‑GCL *.pt checkpoint.")
    p.add_argument("--hetero-dir", type=Path, default=Path("data/hetero"),
                   help="Directory with cached hetero‑graphs (Parquet)")
    p.add_argument("--split", choices=["train", "val", "test"], default="test",
                   help="Dataset split to certify.")
    p.add_argument("--splits-dir", type=Path, default=Path("data/splits"),
                   help="Folder containing split JSON files.")
    p.add_argument("--batch-size", type=int, default=32)
    p.add_argument("--n-samples", type=int, default=100,
                   help="# Monte‑Carlo samples per graph.")
    p.add_argument("--alpha", type=float, default=0.001,
                   help="Failure probability for Clopper‑Pearson bound.")
    p.add_argument("--device", type=str, default="cuda",
                   help="torch device")
    p.add_argument("--num-workers", type=int, default=4)
    p.add_argument("--out", type=Path, required=True,
                   help="Output CSV path (SHA256, pred, certified_r)")
    p.add_argument("--wandb", action="store_true",
                   help="Log per‑sample radii to Weights & Biases")
    return p.parse_args()

def make_dataloader(args: argparse.Namespace) -> DataLoader:
    ids = load_split_ids(args.splits_dir, args.split)
    ds = HeteroMalwareDataset(args.hetero_dir, ids)
    return DataLoader(ds, batch_size=args.batch_size, shuffle=False,
                      num_workers=args.num_workers, collate_fn=ds.collate_fn)

def main() -> None:
    args = parse_args()
    ensure_dir(args.out.parent)

    LOGGER.info("Loading model from %s", args.checkpoint)
    model = RESGCLClassifier.load_from_checkpoint(args.checkpoint)
    model.eval().to(args.device)

    loader = make_dataloader(args)

    if args.wandb and wandb is not None:
        wandb.init(project="robust‑malware‑graph", name=f"certify_{args.split}")
        wandb.config.update(vars(args))

    results: List[dict] = []
    with torch.no_grad():
        for batch in tqdm(loader, desc="Certifying", unit="batch"):
            batch = batch.to(args.device)
            preds, radii = certify_batch(
                model=model,
                data=batch,
                n_samples=args.n_samples,
                alpha=args.alpha,
            )
            for sha256, pred, r in zip(batch.sha256, preds.tolist(), radii.tolist()):
                results.append({"sha256": sha256, "pred": pred, "cert_r": r})
                if wandb and args.wandb:
                    wandb.log({"cert_r": r})

    # save CSV
    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["sha256", "pred", "cert_r"])
        writer.writeheader()
        writer.writerows(results)
    LOGGER.info("Saved certification results to %s (%d samples)", args.out, len(results))

    if wandb and args.wandb:
        wandb.save(str(args.out))
        wandb.finish()

if __name__ == "__main__":
    main()
