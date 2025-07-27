#!/usr/bin/env python3
"""robust-malware-graph 
Train ``RESGCLClassifier`` on labeled graphs using BCE loss.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import torch
from torch.serialization import add_safe_globals
from torch import nn, optim
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch_geometric.transforms as T
from torch_geometric.data import HeteroData
import matplotlib.pyplot as plt

from src.common.utils import (
    set_random_seed,
    ensure_dir,
    get_logger,
    filter_state_dict,
)
from src.models import get_model
from graphs.dataset.graph_dataset import GraphDataset, _guess_graph_path
from src.graphs.normalizers.schema import NodeType
from src.models.gnn.encoder import RGCNEncoder
from src.models.gnn.res_wrapper import RESGCLClassifier
from src.models.contrast.sup_con import SupContrastHead
from graphs.features.cache import clear_memory_cache
from src.common.losses import FocalLoss

LOGGER = get_logger(__name__)


# --------------------------------------------------------------------------- #
# Argument parsing
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Train RES-GCL robust classifier",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--encoder-checkpoint", type=Path, required=True,
                   help="Pre-trained encoder .pt file")
    p.add_argument(
        "--meta-path",
        type=Path,
        required=True,
        help="Path to encoder meta snapshot (.meta.pkl)",
    )
    p.add_argument("--force-reinit", action="store_true",
                   help="Rebuild input layers when feature sizes changed")
    p.add_argument("--head-checkpoint", type=Path,
                   help="Load head weights from this .pt file")
    p.add_argument("--head-class", type=str, default="sup_con",
                   help="Head class name if --head-checkpoint is given")
    p.add_argument("--splits-dir", type=Path, default=Path("data/splits"),
                   help="Dataset root with train/val/test folders")
    p.add_argument("--split", type=str, default="latest",
                   help="Optional subfolder under --splits-dir")
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument("--epochs", type=int, default=20)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--weight-decay", type=float, default=1e-4)
    p.add_argument("--drop-prob", type=float, default=0.2,
                   help="Edge-drop probability during training")
    p.add_argument("--loss-fn", type=str, default="bce", choices=["bce", "focal"],
                   help="Loss function to use for training.")
    p.add_argument("--embed-dir", type=Path,
                   help="Directory containing token embeddings")
    p.add_argument("--device", type=str, default="cuda")
    p.add_argument(
        "--no-embeds",
        action="store_true",
        help="Skip loading token embeddings",
    )
    p.add_argument("--num-workers", type=int, default=0)
    p.add_argument(
        "--strict-metadata",
        action="store_true",
        help="Raise error on invalid edge_type indices in graphs",
    )
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", type=Path, required=True,
                   help="Where to save trained model")
    p.add_argument("--plot-path", type=Path, help="Path to save training plot (.png)")
    p.add_argument("--balanced", action="store_true", help="Use weighted random sampler for imbalanced training set")
    # Scheduler arguments
    p.add_argument("--use-scheduler", action="store_true", help="Use a learning rate scheduler")
    p.add_argument("--warmup-epochs", type=int, default=5, help="Number of warmup epochs for the scheduler")
    p.add_argument("--lr-min", type=float, default=1e-6, help="Minimum learning rate for CosineAnnealingLR")
    return p


# --------------------------------------------------------------------------- #
# Data
# --------------------------------------------------------------------------- #

def make_dataloaders(
    root: Path | None,
    batch_size: int,
    num_workers: int,
    *,
    attr_names: dict[str, list[str]] | None = None,
    embed_dir: Path | None = None,
    load_embeds: bool = True,
    train_ds: GraphDataset | None = None,
    val_ds: GraphDataset | None = None,
    edge_types_schema: list[tuple[str, str, str]] | None = None,
    balanced_sampler: bool = False,
) -> tuple[DataLoader, DataLoader]:
    """Construct :class:`~torch.utils.data.DataLoader` objects."""
    if train_ds is None or val_ds is None:
        if root is None:
            raise ValueError("root is required when datasets are not provided")
        transform = T.Compose([T.NormalizeFeatures()])
        train_ds = GraphDataset(
            root=root,
            split="train",
            transform=transform,
            require_labels=True,
            embed_dir=embed_dir,
            load_embeds=load_embeds,
            edge_types_schema=edge_types_schema,
        )
        val_ds = GraphDataset(
            root=root,
            split="val",
            transform=transform,
            require_labels=True,
            embed_dir=embed_dir,
            load_embeds=load_embeds,
            edge_types_schema=edge_types_schema,
        )
    
    sampler = None
    if balanced_sampler and train_ds:
        labels_dict = train_ds.labels
        # Since require_labels=True, all samples in train_ds are guaranteed to have a label.
        labels_list = [labels_dict[sha] for sha in train_ds.samples]
        labels_tensor = torch.tensor(labels_list, dtype=torch.long)

        class_counts = torch.bincount(labels_tensor)
        # Ensure float division for weights
        class_weights = 1.0 / class_counts.float()

        # Use vectorized indexing to get weights for each sample, which is more efficient
        # and safer than list comprehensions for large tensors.
        sample_weights = class_weights[labels_tensor]

        sampler = torch.utils.data.WeightedRandomSampler(
            weights=sample_weights,
            num_samples=len(sample_weights),
            replacement=False # Use False to prevent duplicates in a batch, which might be causing segfaults.
        )
        LOGGER.info("Using WeightedRandomSampler (without replacement) for balanced training.")

    use_cuda = torch.cuda.is_available()
    workers = 0 if use_cuda else num_workers
    train_dl = DataLoader(
        train_ds,
        batch_size=batch_size,
        shuffle=sampler is None, # Cannot use shuffle with sampler
        num_workers=workers,
        collate_fn=lambda batch: GraphDataset.collate_fn(batch, attr_names=attr_names, edge_types_schema=edge_types_schema),
        pin_memory=use_cuda,
        sampler=sampler,
    )
    val_dl = DataLoader(
        val_ds,
        batch_size=batch_size,
        shuffle=False,
        num_workers=workers,
        collate_fn=lambda batch: GraphDataset.collate_fn(batch, attr_names=attr_names, edge_types_schema=edge_types_schema),
        pin_memory=use_cuda,
    )
    return train_dl, val_dl


# --------------------------------------------------------------------------- #
# Training / Evaluation
# --------------------------------------------------------------------------- #

def train_one_epoch(model, loader, optimizer, device, loss_fn) -> float:
    model.train(); total = 0.0
    for i, batch in enumerate(loader):
        if not batch or "graph" not in batch or batch["graph"].num_graphs == 0:
            LOGGER.warning("Skipping empty batch")
            continue
        try:
            g = batch["graph"].to(device)
            y = batch["label"].float().to(device)
            try:
                logits = model(g, return_logits=True)
            except Exception as e:
                LOGGER.info(f"오류 발생: 모델 forward pass 중 batch {i}에서 에러가 발생했습니다: {e}")
                LOGGER.info("오류 발생 시점의 그래프(g) 정보:")
                LOGGER.info("========================================")
                if hasattr(g, 'num_nodes_dict'):
                    LOGGER.info(f"g.num_nodes_dict: {g.num_nodes_dict}")

                if hasattr(g, 'edge_index_dict'):
                    LOGGER.info("\ng.edge_index_dict 정보 (엣지 타입별 인덱스):")
                    for et, edge_index in g.edge_index_dict.items():
                        try:
                            edge_index_cpu = edge_index.cpu()
                            min_idx = edge_index_cpu.min().item() if edge_index_cpu.numel() > 0 else 'N/A'
                            max_idx = edge_index_cpu.max().item() if edge_index_cpu.numel() > 0 else 'N/A'
                            src_node_type, _, dst_node_type = et
                            src_num_nodes = g.num_nodes_dict.get(src_node_type, 'N/A')
                            dst_num_nodes = g.num_nodes_dict.get(dst_node_type, 'N/A')

                            LOGGER.info(f"  - 엣지 타입: {et}")
                            LOGGER.info(f"    - shape: {edge_index.shape}")
                            LOGGER.info(f"    - min/max: {min_idx} / {max_idx}")
                            LOGGER.info(f"    - 출발 노드({src_node_type}) 수: {src_num_nodes}, 도착 노드({dst_node_type}) 수: {dst_num_nodes}")

                            if isinstance(max_idx, int) and isinstance(src_num_nodes, int) and max_idx >= src_num_nodes:
                                LOGGER.info(f"    - [경고] 출발 노드 인덱스({max_idx})가 노드 수({src_num_nodes})의 범위를 벗어났습니다!")
                            if isinstance(max_idx, int) and isinstance(dst_num_nodes, int) and max_idx >= dst_num_nodes:
                                LOGGER.info(f"    - [경고] 도착 노드 인덱스({max_idx})가 노드 수({dst_num_nodes})의 범위를 벗어났습니다!")

                        except Exception as cpu_e:
                            LOGGER.info(f"  - 엣지 타입: {et}")
                            LOGGER.info(f"    - [오류] edge_index를 CPU로 옮기는 중 에러 발생: {cpu_e}")
                            LOGGER.info(f"    - edge_index shape: {edge_index.shape if hasattr(edge_index, 'shape') else 'N/A'}")

                if hasattr(g, 'x_dict'):
                    LOGGER.info("\ng.x_dict 정보 (노드 타입별 특징 텐서):")
                    for nt, x in g.x_dict.items():
                        LOGGER.info(f"  - 노드 타입: {nt}, shape: {x.shape}")
                
                LOGGER.info("========================================")
                LOGGER.info("오류 로깅을 마치고 학습을 중단합니다.")
                raise e
            if logits is None:
                LOGGER.warning("Skipping batch %d due to None logits", i)
                continue
            loss = loss_fn(logits, y)
            optimizer.zero_grad(); loss.backward(); optimizer.step()
            total += loss.item() * g.num_graphs
        except RuntimeError as exc:
            LOGGER.error("RuntimeError in batch %d: %s", i, exc, exc_info=True)


            if "out of memory" in str(exc).lower():
                LOGGER.error("OOM error in batch %d, skipping. Reduce batch size if this persists.", i)
                torch.cuda.empty_cache()
            raise # 예외를 다시 발생시켜 학습을 명시적으로 종료
        except Exception as exc:
            LOGGER.error("Unexpected error in batch %d: %s", i, exc, exc_info=True)
            raise # 다른 예외 발생 시에도 예외를 다시 발생시켜 학습을 명시적으로 종료
    return total / len(loader.dataset) if len(loader.dataset) > 0 else 0.0


from sklearn.metrics import accuracy_score, f1_score


def evaluate_epoch(model, loader, device, loss_fn) -> dict:
    """Evaluate model for one epoch, return loss, accuracy, and F1 score."""
    model.eval()
    total_loss = 0.0
    y_true, y_pred = [], []
    with torch.no_grad():
        for batch in loader:
            if not batch or "graph" not in batch or batch["graph"].num_graphs == 0:
                continue
            g = batch["graph"].to(device)
            y = batch["label"].float().to(device)
            logits = model(g, return_logits=True)
            if logits is None:
                continue
            loss = loss_fn(logits, y)
            total_loss += loss.item() * g.num_graphs
            
            preds = (torch.sigmoid(logits) > 0.5).long()
            y_true.append(y.long().view(-1))
            y_pred.append(preds.view(-1))

    if not y_true:
        return {"loss": 0, "accuracy": 0, "macro_f1": 0}

    y_true = torch.cat(y_true).cpu().numpy()
    y_pred = torch.cat(y_pred).cpu().numpy()
    
    dataset_len = len(loader.dataset)
    metrics = {
        "loss": total_loss / dataset_len if dataset_len > 0 else 0.0,
        "accuracy": accuracy_score(y_true, y_pred),
        "macro_f1": f1_score(y_true, y_pred, average='macro', zero_division=0)
    }
    return metrics


# --------------------------------------------------------------------------- #
# Main entry
# --------------------------------------------------------------------------- #

def save_plot(
    train_losses: list[float],
    val_losses: list[float],
    val_accs: list[float],
    val_f1s: list[float],
    plot_path: Path,
) -> None:
    """Saves a plot of training and validation metrics to a file."""
    if not train_losses:
        return
    epochs_r = range(1, len(train_losses) + 1)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Subplot 1: Losses
    ax1.plot(epochs_r, train_losses, label="Train Loss", color='tab:blue')
    ax1.plot(epochs_r, val_losses, label="Validation Loss", color='tab:orange')
    ax1.set_ylabel("Loss")
    ax1.legend()
    ax1.grid(True)

    # Subplot 2: Accuracy and F1 Score
    ax2.plot(epochs_r, val_accs, label="Validation Accuracy", color='tab:green')
    ax2.plot(epochs_r, val_f1s, label="Validation Macro F1", color='tab:red')
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Metric")
    ax2.legend()
    ax2.grid(True)

    fig.suptitle("Training and Validation Metrics", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make room for suptitle
    plt.savefig(plot_path)
    plt.close(fig) # Close the figure to free memory
    LOGGER.debug(f"Training plot updated at {plot_path}")


# --------------------------------------------------------------------------- #
# Main entry
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    set_random_seed(args.seed)
    device = torch.device(args.device)

    if not args.meta_path.is_file():
        raise RuntimeError(f"Meta snapshot not found: {args.meta_path}")

    root = (
        args.splits_dir / args.split
        if (args.splits_dir / args.split).is_dir()
        else args.splits_dir
    )

    # --- Load Model and Metadata ---
    encoder_state = torch.load(args.encoder_checkpoint, map_location=device).get('model')
    meta_path = args.meta_path or args.encoder_checkpoint.with_suffix(".meta.pkl")
    if not meta_path.is_file():
        raise FileNotFoundError(f"Meta file not found: {meta_path}. Please run pre-training first.")
    
    add_safe_globals([NodeType])
    meta_info = torch.load(meta_path, weights_only=False)

    # --- DataLoaders (must be created before re-init) ---
    train_dl, val_dl = make_dataloaders(
        root,
        args.batch_size,
        args.num_workers,
        attr_names=meta_info.get("attr_names"),
        embed_dir=args.embed_dir,
        load_embeds=not args.no_embeds,
        edge_types_schema=meta_info.get("edge_types"),
        balanced_sampler=args.balanced,
    )

    # --- [MODIFIED] force-reinit logic ---
    if args.force_reinit:
        LOGGER.info("--force-reinit: Re-collecting metadata from the current dataset...")
        from graphs.dataset.graph_dataset import collect_dataset_metadata
        
        # Collect new metadata from the current dataset
        _, new_in_dims, _, _, _ = collect_dataset_metadata(
            [train_dl.dataset, val_dl.dataset],
            attr_dim=meta_info.get("attr_dim", 32),
            strict=args.strict_metadata
        )
        LOGGER.info(f"New feature dimensions detected: {new_in_dims}")
        
        # Update meta_info with the new dimensions
        meta_info["in_dims"] = new_in_dims

    # --- Re-create Encoder ---
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

    # --- [MODIFIED] Selective state dict loading ---
    if args.force_reinit:
        LOGGER.info("Filtering state_dict to exclude re-initialized 'input_proj' layers...")
        # When force-reinit, don't load input_proj layers as their size may have changed.
        filtered_encoder_state = {k: v for k, v in encoder_state.items() if not k.startswith('input_proj')}
        encoder.load_state_dict(filtered_encoder_state, strict=False)
    else:
        # If not force-reinit, all weights should match perfectly.
        encoder.load_state_dict(encoder_state, strict=True)

    # --- Head ---
    if args.head_checkpoint:
        head_state_dict = torch.load(args.head_checkpoint, map_location=device)
        head_weights = {k.replace('head.', ''): v for k, v in head_state_dict.items() if 'head.' in k}
        head = SupContrastHead(in_dim=encoder.out_dim)
        head.load_state_dict(head_weights)
    else:
        head = "binary_mlp"

    model = RESGCLClassifier(encoder=encoder, head=head, drop_prob=args.drop_prob)
    model.to(device)

    # --- Loss Function ---
    if args.loss_fn == 'focal':
        loss_fn = FocalLoss()
        LOGGER.info("Using FocalLoss for training.")
    else: # bce
        loss_fn = F.binary_cross_entropy_with_logits
        LOGGER.info("Using BCEWithLogitsLoss for training.")

    optimizer = optim.Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    
    scheduler = None
    if args.use_scheduler:
        LOGGER.info(f"Using SequentialLR with Linear warmup for {args.warmup_epochs} epochs and CosineAnnealingLR.")
        warmup_scheduler = torch.optim.lr_scheduler.LinearLR(
            optimizer, start_factor=1e-3, end_factor=1.0, total_iters=args.warmup_epochs
        )
        main_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=args.epochs - args.warmup_epochs, eta_min=args.lr_min
        )
        scheduler = torch.optim.lr_scheduler.SequentialLR(
            optimizer, schedulers=[warmup_scheduler, main_scheduler], milestones=[args.warmup_epochs]
        )

    best_val_f1 = 0.0
    best_model_state = None
    history = {"train_loss": [], "val_loss": [], "val_acc": [], "val_f1": []}
    
    plot_path = args.plot_path or args.output.with_suffix(".png")
    ensure_dir(plot_path.parent)
    log_dir = args.output.parent
    ensure_dir(log_dir)

    try:
        for epoch in range(1, args.epochs + 1):
            tr_loss = train_one_epoch(model, train_dl, optimizer, device, loss_fn=loss_fn)
            val_metrics = evaluate_epoch(model, val_dl, device, loss_fn=loss_fn)
            
            history["train_loss"].append(tr_loss)
            history["val_loss"].append(val_metrics["loss"])
            history["val_acc"].append(val_metrics["accuracy"])
            history["val_f1"].append(val_metrics["macro_f1"])

            LOGGER.info(
                "Epoch %d | train_loss=%.4f | val_loss=%.4f | val_acc=%.4f | val_f1=%.4f",
                epoch, tr_loss, val_metrics["loss"], val_metrics["accuracy"], val_metrics["macro_f1"],
            )

            if val_metrics["macro_f1"] > best_val_f1:
                best_val_f1 = val_metrics["macro_f1"]
                best_model_state = model.state_dict()
                LOGGER.info(f"New best validation F1: {best_val_f1:.4f}. Saving model to {args.output}")
                torch.save({"model": best_model_state}, args.output)
                
                # Save the fine-tuned encoder separately
                encoder_state = {k.replace('encoder.', ''): v for k, v in best_model_state.items() if k.startswith('encoder.')}
                encoder_save_path = args.output.parent / "best_encoder.pt"
                torch.save({"model": encoder_state}, encoder_save_path)
                LOGGER.info(f"✓ Fine-tuned encoder saved separately to {encoder_save_path}")

                meta_out = args.output.with_suffix(".meta.pkl")
                try:
                    torch.save(meta_info, meta_out)
                except Exception as exc:
                    LOGGER.warning("Failed to save meta snapshot: %s", exc)

            if epoch % 10 == 0:
                checkpoint_path = log_dir / f"checkpoint_epoch_{epoch}.pt"
                torch.save({"model": model.state_dict()}, checkpoint_path)
                LOGGER.info(f"Saved periodic checkpoint to {checkpoint_path}")

            save_plot(
                history["train_loss"], 
                history["val_loss"], 
                history["val_acc"], 
                history["val_f1"], 
                plot_path
            )

            if scheduler:
                scheduler.step()

    except KeyboardInterrupt:
        LOGGER.warning("--- Training interrupted by user ---")
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred during training: {e}", exc_info=True)
        raise
    finally:
        LOGGER.info("--- Training Finished or Interrupted ---")
        if not best_model_state:
            LOGGER.warning("No best model state was saved. Was training started?")
        
        # Save the final plot one last time
        save_plot(
            history["train_loss"], 
            history["val_loss"], 
            history["val_acc"], 
            history["val_f1"], 
            plot_path
        )
        LOGGER.info(f"Final training plot saved to {plot_path}")

    # 학습 과정에서 사용된 캐시를 정리하여 메모리 사용량을 최소화한다
    clear_memory_cache()


if __name__ == "__main__": # pragma: no cover
    main()