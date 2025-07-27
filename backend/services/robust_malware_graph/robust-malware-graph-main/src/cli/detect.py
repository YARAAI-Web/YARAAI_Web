#!/usr/bin/env python3
"""robust‑malware‑graph – Malware *Inference / Detection* CLI
================================================================
Run (batched) inference on **heterogeneous program graphs** using a trained
classifier (e.g. `RESGCLClassifier`, distilled *StudentSGCN*, or any
PyTorch Geometric‑compatible model checkpoint).  The script is **framework‑
agnostic** w.r.t. the encoder ‑ it only assumes an `nn.Module` that accepts a
`torch_geometric.data.HeteroData` (or `Data`) object and returns *logits* with
shape `[B]` (sigmoid not applied).

Highlights
----------
* **torch_geometric**‑first batching via `DataLoader`, no DGL required.
* Certified inference supported when the checkpoint stores the extra
  `edge_smoothing_radius` attribute (RES‑GCL).
* Works **CPU‑only** (distilled checkpoints) *or* GPU/ multi‑GPU via
  `torchrun`.  CUDA amp/autocast enabled by default on GPUs.
* Saves CSV report (`sha256,pred,prob,cert_radius`) and optional per‑sample
  JSON explanation stub (for later XAI pipeline).

Example
~~~~~~~
```bash
$ python -m cli.detect \
    --graph-dir data/hetero/test \
    --ckpt models/gnn/res_gcl.pt \
    --batch-size 32 --outfile results/test_preds.csv
```
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Iterator, Tuple
from functools import partial
from contextlib import nullcontext

import torch
from torch import nn
from torch.utils.data import DataLoader
from torch_geometric.data import Batch, HeteroData, InMemoryDataset
from torch_geometric.loader import DataLoader as GeoDataLoader

from src.graphs.dataset import GraphDataset

# ---------------------------------------------------------------------------
#  Utilities
# ---------------------------------------------------------------------------


def list_graph_files(graph_dir: Path, suffix: str = ".pt") -> Iterator[Path]:
    """Yield all graph tensors saved via `torch.save(HeteroData, *.pt)`."""
    for path in graph_dir.rglob(f"*{suffix}"):
        yield path


def load_graph(pt_path: Path) -> HeteroData:
    return torch.load(pt_path, map_location="cpu", weights_only=False)


class GraphFileDataset(InMemoryDataset):
    """Lightweight wrapper that lazily loads *.pt graphs on‑the‑fly."""

    def __init__(self, file_paths: list[Path]):
        self.file_paths = file_paths
        super().__init__(None, None, None, None)

    def len(self) -> int:  # type: ignore[override]
        return len(self.file_paths)

    def get(self, idx: int) -> HeteroData:  # type: ignore[override]
        data = load_graph(self.file_paths[idx])
        data.sha256 = self.file_paths[idx].stem  # attach ID for later
        return data


def collate_graphs(
    graphs: list[HeteroData],
    *,
    attr_names: dict[str, list[str]] | None = None,
) -> Batch:
    """Collate a list of graphs into a :class:`~torch_geometric.data.Batch`."""

    fixed = [GraphDataset._ensure_num_nodes(g) for g in graphs]
    fixed = [GraphDataset._ensure_x(g) for g in fixed]
    fixed = [GraphDataset._sanitize_edges(g) for g in fixed]
    if attr_names is not None:
        fixed = [GraphDataset._ensure_meta_ids(g, attr_names) for g in fixed]

    batch = Batch.from_data_list(fixed)
    batch.sha256 = [g.sha256 for g in graphs]
    return batch


# ---------------------------------------------------------------------------
#  Model loading
# ---------------------------------------------------------------------------


def load_model(ckpt_path: Path, device: torch.device) -> nn.Module:
    """Load a model checkpoint along with its meta snapshot if present."""

    from src.models.gnn.res_wrapper import RESGCLClassifier  # noqa: E402
    from src.models.distill.sgcn_kd import StudentSGCN  # noqa: E402

    meta_path = ckpt_path.with_suffix(".meta.pkl")
    if not ckpt_path.is_file():
        raise FileNotFoundError(ckpt_path)
    if meta_path.is_file():
        try:
            torch.load(meta_path, map_location="cpu", weights_only=False)
        except Exception as exc:  # pragma: no cover - I/O handling
            print(
                f"[WARN] Failed to load meta snapshot {meta_path}: {exc}",
                file=sys.stderr,
            )

    try:
        model = RESGCLClassifier.load_from_checkpoint(ckpt_path, map_location=device)
    except Exception:
        model = StudentSGCN.load_from_checkpoint(ckpt_path, map_location=device)

    model.to(device)
    model.eval()
    return model


# ---------------------------------------------------------------------------
#  Inference
# ---------------------------------------------------------------------------


def infer(
    model: nn.Module,
    loader: DataLoader,
    device: torch.device,
    threshold: float,
    amp: bool,
) -> Iterator[Tuple[str, int, float, float]]:
    """Yield (sha256, pred\_int, prob\_float, cert\_radius) per sample."""
    scaler_ctx = (
        partial(torch.amp.autocast, device_type="cuda")
        if (device.type == "cuda" and amp)
        else nullcontext
    )

    for batch in loader:
        batch = batch.to(device, non_blocking=True)
        with scaler_ctx():
            logits = model(batch, return_logits=True)  # shape [B]
            probs = logits.sigmoid().detach().cpu()
        preds = (probs >= threshold).int()

        # Certified radius if RES‑GCL stores `edge_smoothing_radius`
        cert_radius = getattr(model, "edge_smoothing_radius", 0.0)
        for sha, p, pr in zip(batch.sha256, preds, probs):
            yield sha, int(p.item()), float(pr.item()), float(cert_radius)


# ---------------------------------------------------------------------------
#  Main
# ---------------------------------------------------------------------------


def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Malware graph inference")
    p.add_argument(
        "--graph-dir", type=Path, required=True, help="Directory of *.pt graphs"
    )
    p.add_argument("--ckpt", type=Path, required=True, help="Model checkpoint path")
    p.add_argument("--batch-size", type=int, default=64)
    p.add_argument("--num-workers", type=int, default=2)
    p.add_argument(
        "--device", type=str, default="cuda:0" if torch.cuda.is_available() else "cpu"
    )
    p.add_argument(
        "--threshold", type=float, default=0.5, help="Positive class threshold"
    )
    p.add_argument("--outfile", type=Path, default=Path("predictions.csv"))
    p.add_argument(
        "--explain", action="store_true", help="Dump per‑sample JSON stub for XAI"
    )
    p.add_argument(
        "--amp",
        action="store_true",
        default=False,
        help="Enable mixed‑precision (CUDA) and halve feature precision",
    )
    return p


def main(argv: list[str] | None = None) -> None:
    args = build_argparser().parse_args(argv)

    device = torch.device(args.device)
    graph_files = list(list_graph_files(args.graph_dir))
    if not graph_files:
        print(f"[ERR] No *.pt graphs found under {args.graph_dir}", file=sys.stderr)
        sys.exit(1)

    model = load_model(args.ckpt, device)
    attr_names = getattr(getattr(model, "encoder", None), "attr_names", None)

    # ------------------------------------------------------------------
    # Load meta snapshot to obtain original input dimensions
    # ------------------------------------------------------------------
    meta_in_dims: dict[str, int] = {}
    meta_path = args.ckpt.with_suffix(".meta.pkl")
    if meta_path.is_file():
        try:
            from torch.serialization import add_safe_globals  # type: ignore
            from src.graphs.normalizers.schema import NodeType

            add_safe_globals([NodeType])
            meta = torch.load(meta_path, map_location="cpu", weights_only=False)
            if isinstance(meta, dict):
                meta_in_dims = {k: int(v) for k, v in meta.get("in_dims", {}).items()}
        except Exception as exc:  # pragma: no cover - optional I/O
            print(
                f"[WARN] Failed to load meta snapshot {meta_path}: {exc}",
                file=sys.stderr,
            )

    ds = GraphFileDataset(graph_files)

    # Inspect the first graph to check for feature dimension mismatches
    sample_dims: dict[str, int] = {}
    if len(ds) > 0:
        try:
            sample = ds.get(0)
            for nt in sample.node_types:
                if hasattr(sample[nt], "x") and sample[nt].x is not None:
                    sample_dims[nt] = int(sample[nt].x.size(1))
        except Exception:
            sample_dims = {}

    if sample_dims and any(
        meta_in_dims.get(nt) != sample_dims.get(nt) for nt in sample_dims
    ):
        vocab_size = (
            model.encoder.meta_embed.num_embeddings
            if getattr(getattr(model, "encoder", None), "meta_embed", None) is not None
            else 0
        )
        model.reinit_input_dims(
            in_dims=sample_dims,
            attr_names=getattr(getattr(model, "encoder", None), "attr_names", None),
            vocab_size=vocab_size,
        )

    loader: DataLoader = GeoDataLoader(
        ds,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.num_workers,
        pin_memory=device.type == "cuda",
        collate_fn=lambda batch: collate_graphs(batch, attr_names=attr_names),
    )

    # ------------------------------------------------------------------
    # Inference loop
    # ------------------------------------------------------------------
    args.outfile.parent.mkdir(parents=True, exist_ok=True)
    csv_f = args.outfile.open("w", encoding="utf‑8")
    csv_f.write("sha256,pred,prob,cert_radius\n")

    explain_dir = args.outfile.with_suffix("").parent / "explanations"
    if args.explain:
        explain_dir.mkdir(parents=True, exist_ok=True)

    for sha, pred, prob, radius in infer(
        model, loader, device, args.threshold, args.amp
    ):
        csv_f.write(f"{sha},{pred},{prob:.6f},{radius}\n")
        if args.explain:
            (explain_dir / f"{sha}.json").write_text(
                json.dumps({"sha256": sha, "placeholder": True})
            )

    csv_f.close()
    print(f"[OK] Saved predictions → {args.outfile}  ({len(graph_files)} samples)")


if __name__ == "__main__":
    main()
