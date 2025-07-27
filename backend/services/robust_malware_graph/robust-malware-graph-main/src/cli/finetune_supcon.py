#!/usr/bin/env python3
"""robust-malware-graph – *Supervised Contrast* Fine-tuning CLI
================================================================
This script fine-tunes a pre-trained **SelfGraphCL** encoder with the
*Supervised Contrastive Head* (`SupContrastHead`) on labeled malware graphs.

Key Features
------------
* **PyG (torch_geometric)** data pipeline – no DGL dependency.
* Supports **time- or random-based splits** under `data/splits/`.
* Optional **LoRA** adapter injection for parameter-efficient tuning.
* ``--force-reinit`` rebuilds input layers when feature sizes changed.
* **WandB** / CSV logging, early-stopping, and automatic checkpointing.
* Hydra-compatible – pass `--cfg hydra` to dump merged config.

Example Usage
-------------
```bash
python -m cli.finetune_supcon \
       --encoder-checkpoint models/gnn/encoder.pt \
       --splits-dir data/splits \
       --split "2023Q4" \
       --epochs 10 --batch-size 128 \
       --lr 1e-4 --patience 3 \
       --force-reinit
```
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterable, Tuple

import torch
from torch.serialization import add_safe_globals
import torch.multiprocessing as mp
from torch import nn, optim
from torch.utils.data import DataLoader, WeightedRandomSampler
from torch_geometric.data import InMemoryDataset, Batch, HeteroData
import torch_geometric.transforms as T
import matplotlib.pyplot as plt

# Local project imports ----------------------------------------------------- #
from src.common.utils import set_random_seed, get_logger, ensure_dir, filter_state_dict
from graphs.dataset.graph_dataset import GraphDataset
from src.graphs.normalizers.schema import NodeType
from src.models.gnn.encoder import RGCNEncoder
from src.models.contrast.sup_con import SupContrastHead

LOGGER = get_logger(__name__)

# --------------------------------------------------------------------------- #
# Argument Parsing
# --------------------------------------------------------------------------- #


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Fine-tune SupCon head on malware graphs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Data ------------------------------------------------------------------ #
    p.add_argument(
        "--splits-dir",
        type=Path,
        default=Path("data/splits"),
        help="Root directory with train/val/test folders",
    )
    p.add_argument(
        "--split",
        type=str,
        default="latest",
        help="Optional subfolder under --splits-dir",
    )
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument(
        "--balanced",
        action="store_true",
        help="Use class-balanced sampling for the training loader",
    )
    p.add_argument(
        "--embed-dir",
        type=Path,
        help="Directory containing token embeddings",
    )
    p.add_argument(
        "--strict-metadata",
        action="store_true",
        help="Raise error on invalid edge_type indices in graphs",
    )

    # Model / Training ------------------------------------------------------ #
    p.add_argument(
        "--encoder-checkpoint",
        type=Path,
        required=True,
        help="Path to pre-trained encoder .pt file",
    )
    p.add_argument(
        "--meta-path", type=Path, help="Path to encoder meta snapshot (.meta.pkl)"
    )
    p.add_argument(
        "--force-reinit",
        action="store_true",
        help="Rebuild input projection layers using dataset feature dimensions",
    )
    p.add_argument(
        "--lora",
        action="store_true",
        help="Inject LoRA adapters instead of full fine-tuning",
    )
    p.add_argument("--epochs", type=int, default=20)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--weight-decay", type=float, default=1e-5)
    p.add_argument("--patience", type=int, default=5, help="Early-stop patience")
    p.add_argument(
        "--monitor",
        choices=["f1", "auroc", "both"],
        default="both",
        help="Metric to monitor for early stopping",
    )

    # Misc / Repro ---------------------------------------------------------- #
    p.add_argument("--device", type=str, default="cuda:0")
    p.add_argument("--num-workers", type=int, default=0, help="Number of DataLoader worker processes")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--logdir", type=Path, default=Path("runs/finetune_supcon"))
    p.add_argument(
        "--plot-path",
        type=Path,
        help="Where to save training curve PNG; defaults to logdir/train.png",
    )
    p.add_argument("--wandb", action="store_true", help="Enable WandB logging")

    # Hydra inspection ------------------------------------------------------ #
    p.add_argument("--cfg", choices=["hydra"], help="Dump merged config and exit")
    return p


# --------------------------------------------------------------------------- #
# Data Utilities
# --------------------------------------------------------------------------- #


def make_dataloaders(
    splits_dir: Path,
    split: str,
    batch_size: int,
    num_workers: int, # num_workers 인자 추가
    *,
    attr_names: dict[str, list[str]] | None = None,
    balanced: bool = False,
    embed_dir: Path | None = None,
) -> Tuple[DataLoader, DataLoader]:
    """Load GraphDataset splits and wrap in PyG ``DataLoader`` objects."""
    root = splits_dir / split if (splits_dir / split).is_dir() else splits_dir

    use_cuda = torch.cuda.is_available()

    transform = T.Compose(
        [
            T.NormalizeFeatures(),
        ]
    )

    train_ds = GraphDataset(
        root=root,
        split="train",
        transform=transform,
        require_labels=True,
        embed_dir=embed_dir,
    )
    val_ds = GraphDataset(
        root=root,
        split="val",
        transform=transform,
        require_labels=True,
        embed_dir=embed_dir,
    )

    sampler = None
    shuffle = True
    if balanced:
        labels = [train_ds.labels[sha] for sha in train_ds.samples]
        label_tensor = torch.tensor(labels, dtype=torch.long)
        counts = torch.bincount(label_tensor)
        weights = 1.0 / counts[label_tensor]
        sampler = WeightedRandomSampler(weights.tolist(), len(weights), replacement=True)
        shuffle = False

    train_dl = DataLoader(
        train_ds,
        batch_size=batch_size,
        shuffle=shuffle,
        sampler=sampler,
        num_workers=num_workers,
        collate_fn=lambda batch: GraphDataset.collate_fn(batch, attr_names=attr_names),
        pin_memory=not use_cuda,
    )
    val_dl = DataLoader(
        val_ds,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        collate_fn=lambda batch: GraphDataset.collate_fn(batch, attr_names=attr_names),
        pin_memory=not use_cuda,
    )
    return train_dl, val_dl


# --------------------------------------------------------------------------- #
# Training / Evaluation Loops
# --------------------------------------------------------------------------- #


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: optim.Optimizer,
    device: torch.device,
) -> float:
    """Train ``model`` for a single epoch."""
    model.train()
    running_loss = 0.0

    for batch in loader:
        if isinstance(batch, dict):
            g = batch["graph"].to(device)
            y = batch.get("label")
            if y is not None:
                y = y.to(device)
            else:
                raise ValueError("Batch contains unlabeled graphs.")
        else:  # fallback: Batch directly
            g = batch.to(device)
            y = batch.y
            if y is None:
                raise ValueError("Batch contains unlabeled graphs.")

        z = model.encoder(g)
        loss = model.head(z, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * g.num_graphs

    return running_loss / len(loader.dataset) if len(loader.dataset) > 0 else 0.0


def evaluate_loss(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    """Calculate the supervised contrastive loss on the validation set."""
    model.eval()
    running_loss = 0.0
    with torch.no_grad():
        for batch in loader:
            if isinstance(batch, dict):
                g = batch["graph"].to(device)
                y = batch.get("label")
                if y is not None:
                    y = y.to(device)
                else:
                    raise ValueError("Batch contains unlabeled graphs.")
            else:  # fallback: Batch directly
                g = batch.to(device)
                y = batch.y
                if y is None:
                    raise ValueError("Batch contains unlabeled graphs.")

            z = model.encoder(g)
            loss = model.head(z, y)
            running_loss += loss.item() * g.num_graphs

    return running_loss / len(loader.dataset) if len(loader.dataset) > 0 else 0.0


def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> dict:
    """Evaluate via a logistic regression on SupCon embeddings."""
    model.eval()
    embeds, labels = [], []
    with torch.no_grad():
        for batch in loader:
            if isinstance(batch, dict):
                g = batch["graph"].to(device)
                y = batch.get("label")
                if y is not None:
                    y = y.to(device)
                else:
                    raise ValueError("Batch contains unlabeled graphs.")
            else:
                g = batch.to(device)
                y = batch.y
                if y is None:
                    raise ValueError("Batch contains unlabeled graphs.")

            z = model.encoder(g)
            embeds.append(model.head.embed(z).cpu())
            labels.append(y.cpu())

    X = torch.cat(embeds).numpy()
    y = torch.cat(labels).numpy()

    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score, f1_score
    from sklearn.model_selection import train_test_split

    if len(set(y.tolist())) < 2:
        return {"AUROC": float("nan"), "MacroF1": float("nan")}

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_tr, y_tr)
    prob = clf.predict_proba(X_te)
    pred = clf.predict(X_te)

    if prob.shape[1] == 2:
        auroc = roc_auc_score(y_te, prob[:, 1])
    else:
        auroc = roc_auc_score(y_te, prob, multi_class="ovr")
    f1 = f1_score(y_te, pred, average="macro", zero_division=0)
    return {"AUROC": float(auroc), "MacroF1": float(f1)}


def save_plot(
    history: dict,
    plot_path: Path,
) -> None:
    """Saves a plot of training and validation metrics to a file."""
    if not history["train_loss"]:
        return
    epochs_r = range(1, len(history["train_loss"]) + 1)
    plt.figure(figsize=(12, 8))
    
    # Plot losses
    ax1 = plt.subplot(2, 1, 1)
    ax1.plot(epochs_r, history["train_loss"], label="Train Loss", marker='o')
    ax1.plot(epochs_r, history["val_loss"], label="Validation Loss", marker='o')
    ax1.set_ylabel("Loss")
    ax1.legend()
    ax1.grid(True)

    # Plot metrics
    ax2 = plt.subplot(2, 1, 2)
    ax2.plot(epochs_r, history["val_auroc"], label="Validation AUROC", marker='x')
    ax2.plot(epochs_r, history["val_macro_f1"], label="Validation MacroF1", marker='x')
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Metric")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
    LOGGER.debug(f"Training plot updated at {plot_path}")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main() -> None:
    mp.set_start_method("spawn", force=True)
    args = build_parser().parse_args()

    if args.cfg == "hydra":
        print(json.dumps(vars(args), indent=2))
        return

    set_random_seed(args.seed)
    device = torch.device(args.device)

    ensure_dir(args.logdir)
    plot_path = args.plot_path or (args.logdir / "train.png")
    ensure_dir(plot_path.parent)
    if args.wandb:
        import wandb
        wandb.init(project="robust-malware-graph", name="finetune_supcon", config=vars(args))

    encoder_state = torch.load(args.encoder_checkpoint, map_location=device).get('model')
    meta_path = args.meta_path or args.encoder_checkpoint.with_suffix(".meta.pkl")
    if not meta_path.is_file():
        raise FileNotFoundError(f"Meta file not found: {meta_path}.")
    
    add_safe_globals([NodeType])
    meta_info = torch.load(meta_path, weights_only=False)

    train_dl, val_dl = make_dataloaders(
        args.splits_dir,
        args.split,
        args.batch_size,
        attr_names=meta_info.get("attr_names"),
        balanced=args.balanced,
        embed_dir=args.embed_dir,
        num_workers=args.num_workers,
    )

    if args.force_reinit:
        LOGGER.info("--force-reinit: Re-collecting metadata from the current dataset...")
        from graphs.dataset.graph_dataset import collect_dataset_metadata
        _, new_in_dims, _, _, _ = collect_dataset_metadata(
            [train_dl.dataset, val_dl.dataset],
            attr_dim=meta_info.get("attr_dim", 32),
            strict=args.strict_metadata
        )
        meta_info["in_dims"] = new_in_dims

    encoder = RGCNEncoder(
        metadata=(meta_info["node_types"], meta_info["edge_types"]),
        in_dims=meta_info["in_dims"],
        attr_names=meta_info.get("attr_names"),
        vocab_size=meta_info.get("vocab_size", 0),
        attr_dim=meta_info.get("attr_dim", 32),
        hidden_dim=meta_info.get("hidden_dim", 128),
        num_layers=meta_info.get("num_layers", 2),
        out_dim=meta_info.get("out_dim", 256),
        target_node=meta_info.get("target_node"),
        **{k: v for k, v in meta_info.items() if k in ["codebert_dim", "token_original_dim"]}
    )
    
    if args.force_reinit:
        filtered_encoder_state = {k: v for k, v in encoder_state.items() if not k.startswith('input_proj')}
        encoder.load_state_dict(filtered_encoder_state, strict=False)
    else:
        encoder.load_state_dict(encoder_state, strict=True)

    encoder.to(device)
    head = SupContrastHead(in_dim=encoder.out_dim)
    model = nn.Module()
    model.encoder = encoder
    model.head = head
    model.to(device)

    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)

    best_val_loss = float('inf')
    best_macro_f1 = 0.0
    no_improve = 0
    history = {"train_loss": [], "val_loss": [], "val_auroc": [], "val_macro_f1": []}

    try:
        for epoch in range(1, args.epochs + 1):
            train_loss = train_one_epoch(model, train_dl, optimizer, device)
            val_loss = evaluate_loss(model, val_dl, device)
            val_metrics = evaluate(model, val_dl, device)
            val_f1 = val_metrics["MacroF1"]

            history["train_loss"].append(train_loss)
            history["val_loss"].append(val_loss)
            history["val_auroc"].append(val_metrics["AUROC"])
            history["val_macro_f1"].append(val_f1)

            improved_loss = val_loss < best_val_loss
            improved_f1 = val_f1 > best_macro_f1
            improved = improved_loss or improved_f1

            LOGGER.info(
                "Epoch %d | train_loss=%.4f | val_loss=%.4f%s | val_macroF1=%.4f%s | val_AUROC=%.4f",
                epoch, train_loss, val_loss, " ↓" if improved_loss else "", val_f1, " ↑" if improved_f1 else "", val_metrics["AUROC"],
            )
            if args.wandb:
                wandb.log({"epoch": epoch, "train_loss": train_loss, "val_loss": val_loss, **val_metrics})

            if improved:
                if improved_loss:
                    best_val_loss = val_loss
                if improved_f1:
                    best_macro_f1 = val_f1
                no_improve = 0
                best_model_state = model.state_dict()
                LOGGER.info(f"✓ New best model found (Loss: {best_val_loss:.4f}, F1: {best_macro_f1:.4f}). Saving model...")
                torch.save(best_model_state, args.logdir / "best_model.pt")
                encoder_state = {k.replace('encoder.', ''): v for k, v in best_model_state.items() if k.startswith('encoder.')}
                torch.save({"model": encoder_state}, args.logdir / "best_encoder.pt")
                try:
                    torch.save(meta_info, args.logdir / "best_model.meta.pkl")
                except Exception as exc:
                    LOGGER.warning("Failed to save meta snapshot: %s", exc)
            else:
                no_improve += 1
                if no_improve >= args.patience:
                    LOGGER.info("Early stopping at epoch %d", epoch)
                    break

            if epoch % 10 == 0:
                periodic_checkpoint_path = args.logdir / f"checkpoint_epoch_{epoch}.pt"
                torch.save(model.state_dict(), periodic_checkpoint_path)
                LOGGER.info(f"Saved periodic checkpoint to {periodic_checkpoint_path}")

            save_plot(history, plot_path)

    except KeyboardInterrupt:
        LOGGER.warning("--- Training interrupted by user ---")
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred: {e}", exc_info=True)
        raise
    finally:
        LOGGER.info("--- Fine-tuning Finished or Interrupted ---")
        save_plot(history, plot_path)
        LOGGER.info(f"Final training plot saved to {plot_path}")
        LOGGER.info(f"Finished. Best validation loss = {best_val_loss:.4f}, Best Macro F1 = {best_macro_f1:.4f}")
        if args.wandb:
            wandb.finish()


if __name__ == "__main__":
    main()