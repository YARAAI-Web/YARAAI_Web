#!/usr/bin/env python3
"""robust-malware-graph – CFGExplainer *Selector* Training CLI
=================================================================
Train the Gumbel-Mask selector used for CFG explanations.
"""
from __future__ import annotations

import argparse
import json
import gc
import math
import inspect
from pathlib import Path
from contextlib import nullcontext
from functools import partial
import logging
from typing import Dict

import psutil


def _log_memory_usage(device: torch.device, stage: str):
    """Logs CPU and GPU memory usage."""
    # cpu_mem = psutil.virtual_memory()
    # log_message = f"[{stage}] CPU Memory: {cpu_mem.percent}% used ({cpu_mem.used / 1024**3:.2f}GB / {cpu_mem.total / 1024**3:.2f}GB)"
    # LOGGER.info(log_message)
    # if device.type == "cuda" and torch.cuda.is_available():
    #     torch.cuda.synchronize(device)
    #     gpu_mem = torch.cuda.memory_stats(device)
    #     log_message = f"[{stage}] GPU Memory (Allocated): {torch.cuda.memory_allocated(device) / 1024**3:.2f}GB"
    #     LOGGER.info(log_message)
    #     log_message = f"[{stage}] GPU Memory (Reserved): {torch.cuda.memory_reserved(device) / 1024**3:.2f}GB"
    #     LOGGER.info(log_message)
    pass


def _cast_graph_dtype(g: HeteroData, dtype: torch.dtype) -> None:
    """Cast floating-point attributes of ``g`` in-place to ``dtype``."""
    if dtype == torch.float32:
        return
    for store in g.node_stores + g.edge_stores:
        for key, val in list(store.items()):
            if (
                torch.is_tensor(val)
                and torch.is_floating_point(val)
                and val.dtype != dtype
            ):
                store[key] = val.to(dtype)


import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch_geometric.data import HeteroData
from torch_geometric.nn import HeteroConv, GraphConv, MessagePassing
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from robust_malware_graph.explain import (
    explain_cfg,
    GumbelMaskSelector,
    PGExplainer,
)
from src.graphs.normalizers.schema import EDGE_TYPES
from src.explain.cfg_explainer.selector import gumbel_sigmoid
from src.explain.utils import ensure_edgeaware_selector
from explain.utils.hetero import (
    iter_edge_types,
    drop_unselected_nodes,
    filter_view,
    get_edge_store,
)
from torch_geometric.loader import NeighborLoader
from src.common.utils import (
    get_logger,
    filter_state_dict,
)
from src.graphs.dataset.graph_dataset import collect_dataset_metadata
from src.graphs.builders.hetero_builder import HeteroGraphBuilder
from src.graphs.transforms.pruner import GraphPruner
from src.graphs.loaders.factory import get_loader
from src.graphs.normalizers import get_normalizer
from src.models.gnn.encoder import RGCNEncoder

LOGGER = get_logger(__name__, level=logging.INFO)


from src.models.gnn.res_wrapper import RESGCLClassifier


def perturb_graph(g: HeteroData, return_mask: bool = False):
    """Return a slightly perturbed clone of ``g``.

    The current implementation randomly drops a small fraction of edges to
    introduce structural noise.  When ``return_mask`` is ``True`` the boolean
    mask indicating which edges were kept is also returned.
    """

    from src.augment.ops.drop_edge import EdgeDrop

    drop = EdgeDrop(keep_prob=0.95)

    if not return_mask:
        return drop(g)

    # Manual edge drop to capture the keep mask
    sg = g.clone()
    masks = []
    for etype in sg.edge_types:
        rel_type = etype[1]
        keep_p = drop.keep_prob.get(rel_type, drop.keep_prob.get("*", 1.0))
        store = sg[etype]
        num_e = store.num_edges
        if num_e == 0:
            mask = torch.zeros(0, dtype=torch.bool)
        elif math.isclose(keep_p, 1.0):
            mask = torch.ones(num_e, dtype=torch.bool)
        else:
            mask_np = drop._rng.rand(num_e) < keep_p
            if not mask_np.any():
                mask_np[drop._rng.randint(0, num_e)] = True
            mask = torch.from_numpy(mask_np).to(torch.bool)

        edge_index = store.edge_index
        store.edge_index = edge_index[:, mask]
        for key, val in list(store.items()):
            if key == "edge_index":
                continue
            if torch.is_tensor(val) and val.size(0) == num_e:
                store[key] = val[mask]
        masks.append(mask)

    keep_mask = torch.cat(masks) if masks else torch.tensor([], dtype=torch.bool)
    return sg, keep_mask


def compute_stability_loss(
    graph: HeteroData,
    explainer: PGExplainer,
    mask_prob: torch.Tensor,
    use_hard_mask: bool,
) -> torch.Tensor:
    """Return MSE between current and perturbed masks."""

    g_pert, keep_mask = perturb_graph(graph, return_mask=True)
    encoder = getattr(explainer.model, "encoder", None)
    embeds = (
        _compute_node_embeddings(g_pert, encoder) if encoder is not None else None
    )
    new_mask = explainer(g_pert, embeddings=embeds, hard=use_hard_mask)
    if new_mask.numel() == 0:
        return torch.tensor(0.0, device=mask_prob.device)
    mask_prob_filtered = mask_prob[keep_mask.to(mask_prob.device)]
    return F.mse_loss(new_mask, mask_prob_filtered.detach())


def compute_necessity_loss(
    graph: HeteroData,
    mask_prob: torch.Tensor,
    explainer: PGExplainer,
    model: RESGCLClassifier,
    full_score: torch.Tensor,
    use_hard_prune: bool = False,
    *,
    drop_ratio: float = 0.2,
) -> torch.Tensor:
    """Return necessity loss based on dropping salient nodes.

    ``drop_ratio`` controls the fraction of the highest-scoring nodes that are
    dropped when computing the loss. When ``use_hard_prune`` is ``False``
    (default) edges incident to the selected nodes are softly masked by setting
    their mask probability to ``0``. If ``True`` the previous behaviour of
    physically removing those nodes is used instead.
    """

    saliency = explainer.get_node_saliency(graph, mask_prob)
    keep_idx: dict[str, torch.Tensor] = {}
    drop_mask: dict[str, torch.Tensor] = {}
    for nt, score in saliency.items():
        if score.numel() == 0:
            continue
        k = max(1, int(score.numel() * drop_ratio))
        _, drop_idx = torch.topk(score, k)
        keep = torch.ones(score.size(0), dtype=torch.bool, device=score.device)
        keep[drop_idx] = False
        keep_idx[nt] = keep.nonzero(as_tuple=False).view(-1)
        dm = torch.zeros(score.size(0), dtype=torch.bool, device=score.device)
        dm[drop_idx] = True
        drop_mask[nt] = dm

    if use_hard_prune:
        selected = {}
        for nt in graph.node_types:
            device = getattr(graph[nt], "device", None)
            if device is None:
                for val in graph[nt].values():
                    if isinstance(val, torch.Tensor):
                        device = val.device
                        break
            if device is None:
                device = mask_prob.device
            mask = torch.zeros(graph[nt].num_nodes, dtype=torch.float, device=device)
            idx = keep_idx.get(nt)
            if idx is not None and idx.numel() > 0:
                mask[idx] = 1.0
            selected[nt] = mask

        pruner = GraphPruner(selected, thresh=0.5, keep_edge_attrs="mask")
        pruned = pruner.apply(graph)

        masks = []
        ptr = 0
        for et in iter_edge_types(graph, explainer.view):
            num_e = graph[et].edge_index.size(1)
            orig = mask_prob[ptr : ptr + num_e]
            keep = pruned[et].edge_mask
            if keep.numel() == 0:
                masks.append(orig.new_empty(0))
            else:
                masks.append(orig[keep])
            ptr += num_e
            del pruned[et].edge_mask
        pruned_mask = torch.cat(masks) if masks else mask_prob.new_empty(0)
        logits = _soft_masked_score(pruned, 1 - pruned_mask, explainer.view, model)
    else:
        pruned_mask = mask_prob.clone()
        ptr = 0
        for et in iter_edge_types(graph, explainer.view):
            num_e = graph[et].edge_index.size(1)
            mask_slice = pruned_mask[ptr : ptr + num_e]
            src, dst = graph[et].edge_index
            dm_src = drop_mask.get(et[0])
            dm_dst = drop_mask.get(et[2])
            if dm_src is not None:
                mask_slice[dm_src[src]] = 0.0
            if dm_dst is not None:
                mask_slice[dm_dst[dst]] = 0.0
            pruned_mask[ptr : ptr + num_e] = mask_slice
            ptr += num_e
        logits = _soft_masked_score(graph, pruned_mask, explainer.view, model)
    target = 1 - torch.sigmoid(full_score.detach())
    return F.binary_cross_entropy_with_logits(logits, target)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Train Gumbel-Mask selector",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    sub = p.add_subparsers(dest="command", required=True, metavar="<command>")

    def add_common(pp: argparse.ArgumentParser) -> None:
        pp.add_argument(
            "--model", type=Path, required=True, help="Classifier checkpoint"
        )
        pp.add_argument("--device", type=str, default="cpu")
        pp.add_argument(
            "--no-embeds", action="store_true", help="Skip loading token embeddings"
        )
        pp.add_argument(
            "--embed-dir",
            type=Path,
            default="data/embeds",
            help="Directory containing token embeddings",
        )
        pp.add_argument("--epochs", type=int, default=1000)
        pp.add_argument("--lr", type=float, default=2e-3)
        pp.add_argument("--alpha", type=float, default=1.0)
        pp.add_argument("--beta", type=float, default=2e-2)
        pp.add_argument(
            "--gamma",
            type=float,
            default=0.01,
            help="Entropy weight (nonzero enables exploration)",
        )
        pp.add_argument(
            "--loss-type",
            choices=["bce", "mse", "smooth_l1"],
            default="bce",
            help="Type of fidelity loss to use.",
        )
        pp.add_argument("--batch-size", type=int, default=2048)
        pp.add_argument(
            "--num-workers", type=int, default=0, help="DataLoader worker processes"
        )
        pp.add_argument("--num-neighbors", type=int, default=15)
        pp.add_argument("--num-hops", type=int, default=2)
        pp.add_argument(
            "--saint", choices=["node", "edge"], help="Use GraphSAINT loader"
        )
        pp.add_argument(
            "--walk-length", type=int, default=2, help="GraphSAINT walk length"
        )
        pp.add_argument(
            "--sample-coverage", type=int, default=0, help="GraphSAINT sample coverage"
        )
        pp.add_argument(
            "--num-steps", type=int, default=1, help="GraphSAINT steps per epoch"
        )
        pp.add_argument(
            "--plot-path", type=Path, help="Where to save training curve (.png)"
        )
        pp.add_argument(
            "--score-cache", type=Path, help="JSON file with precomputed full scores"
        )
        pp.add_argument(
            "--no-full-score",
            action="store_true",
            help="Skip full score computation when cache is missing",
        )
        pp.add_argument(
            "--amp",
            action="store_true",
            help="Enable mixed precision (CUDA) and halve feature precision",
        )
        pp.add_argument(
            "--fp16",
            action="store_true",
            help="Cast graph features and model parameters to float16",
        )
        pp.add_argument(
            "--full-cpu", action="store_true", help="Compute full graph score on CPU"
        )
        pp.add_argument(
            "--full-mini-batch",
            action="store_true",
            help="Approximate full score via NeighborLoader mini-batches",
        )
        pp.add_argument(
            "--cluster-parts",
            type=int,
            default=0,
            help="Number of graph partitions for ClusterLoader (0=disable)",
        )
        pp.add_argument(
            "--cluster-batch-size",
            type=int,
            default=1,
            help="Mini-batch size per partition",
        )
        pp.add_argument(
            "--cluster-dir",
            type=Path,
            help="Directory with precomputed cluster *.npz files",
        )
        pp.add_argument(
            "--view",
            type=str,
            default=None,
            help="Optional view name or directory containing view graphs",
        )
        flag = pp.add_mutually_exclusive_group()
        flag.add_argument("--ast", action="store_true", help="Load AST view graphs")
        flag.add_argument("--cfg", action="store_true", help="Load CFG view graphs")
        flag.add_argument("--fcg", action="store_true", help="Load FCG view graphs")
        flag.add_argument(
            "--syscall", action="store_true", help="Load SysCall view graphs"
        )
        pp.add_argument(
            "--checkpoint", action="store_true", help="Enable gradient checkpointing"
        )
        pp.add_argument(
            "--detect-anomaly",
            action="store_true",
            help="Enable PyTorch anomaly detection for debugging.",
        )

    # --- single graph ---
    s = sub.add_parser("single", help="Train selector on a single graph")
    s.add_argument("cfg_graph", type=Path, help="Path to single CFG *.pt graph")
    s.add_argument("--output", type=Path, required=True, help="Output selector path")
    s.add_argument("--mine-features", type=Path, help="Save mined features as JSON")
    add_common(s)
    s.set_defaults(func=train_single)

    # --- dataset/batch ---
    b = sub.add_parser("batch", help="Train selectors for a graph dataset")
    b.add_argument(
        "--graph-dir", type=Path, required=True, help="Directory containing *.pt graphs"
    )
    b.add_argument("--meta-csv", type=Path, help="Optional CSV with sha256,label")
    b.add_argument(
        "--output-dir", type=Path, required=True, help="Directory to save selectors"
    )
    b.add_argument("--mine-features", type=Path, help="Save mined features as JSON")
    add_common(b)
    b.set_defaults(func=train_batch)

    # --- global PGExplainer ---
    g = sub.add_parser(
        "global",
        help="Train PGExplainer on multiple graphs (node dims inferred)",
    )
    g.add_argument(
        "--graph-dir", type=Path, required=True, help="Directory containing *.pt graphs"
    )
    g.add_argument("--output", type=Path, required=True, help="Output explainer path")
    g.add_argument(
        "--val-graph-dir",
        type=Path,
        help="Directory with validation *.pt graphs",
    )
    g.add_argument(
        "--val-meta-csv",
        type=Path,
        help="Optional CSV with sha256,label for validation",
    )
    g.add_argument("--tau-decay", type=float, default=0.995, help="Temperature decay")
    g.add_argument("--tau-min", type=float, default=0.5, help="Minimum temperature")
    g.add_argument(
        "--tau-start",
        type=float,
        default=1.0,
        help="Initial temperature value",
    )
    g.add_argument(
        "--init-bias",
        type=float,
        default=1.0,
        help="Initial bias value for PGExplainer MLPs",
    )
    g.add_argument(
        "--grad-accum-steps",
        type=int,
        default=8,
        help="Number of batches to accumulate gradients over before performing an optimizer step.",
    )
    g.add_argument(
        "--soft-mask-epochs",
        type=int,
        default=5,
        help="Number of initial epochs to train with soft masks before switching to hard masks.",
    )
    g.add_argument(
        "--noise-epochs",
        type=int,
        default=0,
        help="Number of initial epochs to add Gaussian noise to mask probabilities.",
    )
    g.add_argument(
        "--noise-std",
        type=float,
        default=0.05,
        help="Standard deviation of the added Gaussian noise.",
    )
    g.add_argument(
        "--hard-mask-mode",
        choices=["weight", "delete"],
        default="weight",
        help="How to apply hard masks: 'weight' uses edge weights (straight-through), 'delete' removes edges.",
    )
    g.add_argument(
        "--clip-grad-norm",
        type=float,
        default=5.0,
        help="Max norm for gradient clipping. Set to 0 to disable.",
    )
    g.add_argument(
        "--explainer-hidden-dim",
        type=int,
        default=64,
        help="Hidden dimension for the explainer's MLP.",
    )
    g.add_argument(
        "--explainer-num-layers",
        type=int,
        default=2,
        help="Number of layers in the explainer's MLP.",
    )
    g.add_argument(
        "--explainer-dropout",
        type=float,
        default=0.2,
        help="Dropout rate for the explainer's MLP. Set to 0 to disable.",
    )
    g.add_argument(
        "--explainer-norm-type",
        choices=["none", "batch", "layer"],
        default="layer",
        help="Type of normalization to use in the explainer's MLP.",
    )
    g.add_argument(
        "--weight-decay",
        type=float,
        default=0.0,
        help="Weight decay for the optimizer.",
    )
    g.add_argument(
        "--val-samples",
        type=int,
        default=1,
        help="Number of masks to sample for stabilizing validation metrics.",
    )
    g.add_argument(
        "--use-cosine-annealing",
        action="store_true",
        help="Use Cosine Annealing learning rate scheduler.",
    )
    g.add_argument(
        "--cosine-t-max",
        type=int,
        default=None,
        help="T_max for Cosine Annealing LR scheduler. Defaults to the total number of epochs.",
    )
    g.add_argument(
        "--cosine-eta-min",
        type=float,
        default=0.0,
        help="Minimum learning rate for Cosine Annealing LR scheduler.",
    )
    g.add_argument(
        "--lr-warmup-epochs",
        type=int,
        default=0,
        help="Number of epochs for linear learning rate warmup. Only used with --use-cosine-annealing.",
    )
    g.add_argument(
        "--lr-warmup-start-factor",
        type=float,
        default=0.1,
        help="Initial learning rate factor for warmup (lr * start_factor).",
    )
    beta_grp = g.add_mutually_exclusive_group()
    beta_grp.add_argument(
        "--beta-schedule",
        dest="beta_schedule",
        action="store_true",
        default=True,
        help="Enable beta scheduling to gradually increase sparsity pressure.",
    )
    beta_grp.add_argument(
        "--no-beta-schedule",
        dest="beta_schedule",
        action="store_false",
        help="Disable beta scheduling.",
    )
    g.add_argument(
        "--beta-start",
        type=float,
        default=1e-4,
        help="Initial beta value when scheduling is enabled.",
    )
    g.add_argument(
        "--beta-schedule-factor",
        type=float,
        default=1.5,
        help="Multiplicative factor to increase beta at each step of the schedule.",
    )
    g.add_argument(
        "--beta-schedule-epochs",
        type=int,
        default=10,
        help="Number of epochs between beta increases.",
    )
    g.add_argument(
        "--beta-max",
        type=float,
        default=None,
        help="Maximum value for beta under the schedule. Defaults to --beta.",
    )
    g.add_argument("--stability-weight", type=float, default=0.0, help="Weight for stability loss")
    g.add_argument("--stability-start", type=int, default=0, help="Epoch to start applying stability loss")
    g.add_argument("--necessity-weight", type=float, default=0.0, help="Weight for necessity loss")
    g.add_argument("--necessity-start", type=int, default=0, help="Epoch to start applying necessity loss")
    g.add_argument(
        "--necessity-schedule",
        action="store_true",
        help="Enable scheduling for necessity weight",
    )
    g.add_argument(
        "--necessity-weight-start",
        type=float,
        default=1e-4,
        help="Initial necessity weight when scheduling is enabled",
    )
    g.add_argument(
        "--necessity-schedule-factor",
        type=float,
        default=1.5,
        help="Multiplicative factor to increase necessity weight at each schedule step",
    )
    g.add_argument(
        "--necessity-schedule-epochs",
        type=int,
        default=10,
        help="Number of epochs between necessity weight increases",
    )
    g.add_argument(
        "--necessity-weight-max",
        type=float,
        default=None,
        help="Maximum value for necessity weight under the schedule. Defaults to --necessity-weight",
    )
    g.add_argument(
        "--hard-necessity",
        action="store_true",
        help="Use hard node pruning when computing necessity loss",
    )
    g.add_argument(
        "--necessity-drop-ratio",
        type=float,
        default=0.2,
        help="Fraction of nodes to drop when computing necessity loss",
    )
    add_common(g)
    g.set_defaults(func=train_global)

    # --- feature mining only ---
    m = sub.add_parser("mine-features", help="Extract discriminative tokens")
    m.add_argument(
        "--model-path", type=Path, required=True, help="Classifier checkpoint"
    )
    m.add_argument(
        "--dataset-path", type=Path, required=True, help="Directory with *.pt graphs"
    )
    m.add_argument("--output-path", type=Path, required=True, help="Output JSON path")
    m.add_argument("--embed-dir", type=Path, default=Path("data/embeds"))
    m.add_argument(
        "--device", type=str, default="cuda:0" if torch.cuda.is_available() else "cpu"
    )
    m.set_defaults(func=mine_features)

    # --- feature mining alias ---
    fm = sub.add_parser("feature-mine", help="Mine discriminative tokens")
    fm.add_argument(
        "--model-path", type=Path, required=True, help="Classifier checkpoint"
    )
    fm.add_argument(
        "--dataset-path", type=Path, required=True, help="Directory with *.pt graphs"
    )
    fm.add_argument("--output-path", type=Path, required=True, help="Output JSON path")
    fm.add_argument("--embed-dir", type=Path, default=Path("data/embeds"))
    fm.add_argument(
        "--device", type=str, default="cuda:0" if torch.cuda.is_available() else "cpu"
    )
    fm.set_defaults(func=feature_mine)

    return p


def _load_model(args: argparse.Namespace, device: torch.device):
    # LOGGER.info("Loading model and metadata from %s", args.model)
    _log_memory_usage(device, "Before model load")

    # --- Load Model and Metadata (adapted from train_res_gcl.py) ---
    encoder_state = torch.load(args.model, map_location=device).get("model")
    meta_path = args.model.with_suffix(".meta.pkl")
    if not meta_path.is_file():
        raise FileNotFoundError(
            f"Meta file not found: {meta_path}. Explainer requires the .meta.pkl from RES-GCL training."
        )

    # This is required to load the custom NodeType enum
    from src.graphs.normalizers.schema import NodeType
    from torch.serialization import add_safe_globals

    add_safe_globals([NodeType])

    meta_info = torch.load(meta_path, weights_only=False)

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
    )

    # Filter out unexpected keys before loading state dict
    encoder_state_filtered = filter_state_dict(encoder, encoder_state)
    encoder.load_state_dict(encoder_state_filtered, strict=False)

    # --- Assemble Classifier ---
    model = RESGCLClassifier(encoder=encoder)
    model.load_state_dict(
        encoder_state, strict=False
    )  # Load full weights including head if available

    model.to(device)
    model.eval()
    for p in model.parameters():
        p.requires_grad_(False)

    # LOGGER.info("Model loaded and re-assembled successfully.")
    _log_memory_usage(device, "After model load")
    return model, meta_info


def _attach_embeddings(graph: HeteroData, sha: str, embed_dir: Path) -> None:
    if "token" in graph.node_types:
        embed_file = embed_dir / f"{sha}.ftr"
        if embed_file.is_file():
            try:
                # Disable memory mapping to avoid excessive open file handles
                feat = load_tensor(sha, embed_dir, mmap=False)
                store = graph["token"]

                # track original feature dimension to avoid duplicating embeds
                if not hasattr(store, "_orig_feat_dim"):
                    if hasattr(store, "x") and store.x is not None:
                        store._orig_feat_dim = store.x.size(-1)
                    else:
                        store._orig_feat_dim = 0

                if hasattr(store, "x") and store.x is not None:
                    if store.x.size(1) >= store._orig_feat_dim + feat.size(1):
                        return
                    store.x = torch.cat([store.x, feat], dim=-1)
                else:
                    store.x = feat
            except Exception as e:
                LOGGER.warning(f"Could not attach embedding for {sha}: {e}")


def _reinit_input_proj(
    graph: HeteroData, model: RESGCLClassifier, device: torch.device
) -> Dict[str, int]:
    """Dynamically re-initializes the model's input projection layers to match the
    feature dimensions of the provided graph. This is necessary when running the
    explainer on graphs with features (e.g., high-dimensional embeddings) that
    differ from the ones used during the original model training.
    """
    in_dims: Dict[str, int] = {}
    # Calculate actual feature dimensions from the graph object for each node type.
    for nt in graph.node_types:
        if not hasattr(graph[nt], "x"):
            continue  # Skip node types without features

        # Start with the dimension of the .x attribute
        dim = graph[nt].x.shape[1]

        # Add dimensions of attribute embeddings if they are used by the encoder
        if model.encoder.attr_names and nt in model.encoder.attr_names:
            dim += len(model.encoder.attr_names[nt]) * model.encoder.attr_dim

        in_dims[nt] = dim

    # Re-initialize layers where dimensions don't match
    for nt, proj in model.encoder.input_proj.items():
        if nt not in in_dims:
            continue

        actual_dim = in_dims.get(nt)
        if actual_dim and proj.in_features != actual_dim:
            LOGGER.info(f"Re-initializing input_proj for node type '{nt}': {proj.in_features} -> {actual_dim}")
            out_features = proj.out_features
            model.encoder.input_proj[nt] = torch.nn.Linear(actual_dim, out_features).to(
                device
            )

    return in_dims


def _mine_tokens(graph: HeteroData, model, device: torch.device) -> list[str]:
    result = explain_cfg(graph, graph, model, device=device, top_k=5)
    ranked_nodes = [n for n, _ in result["ranked"]]
    tokens = result["mapper"].cfg_nodes_to_tokens(ranked_nodes)
    if hasattr(result["mapper"].ast_graph, "x_vocab"):
        vocab = result["mapper"].ast_graph.x_vocab
        return [vocab[t] for t in tokens]
    return [str(t) for t in tokens]


def _train_selector_for_graph(
    graph: HeteroData | str, model, args, device: torch.device
):
    sha = None
    if isinstance(graph, str):
        sha = graph
    else:
        sha = getattr(graph, "sha256", None)
        if sha is None:
            sha = getattr(getattr(graph, "metadata", {}), "get", lambda _x: None)(
                "sha256"
            )

    # LOGGER.info("Starting selector training for graph: %s", sha)
    _log_memory_usage(device, f"Start of _train_selector_for_graph for {sha}")

    cluster_file = None
    if args.cluster_dir and sha:
        cluster_file = Path(args.cluster_dir) / f"{sha}.npz"
    has_cluster = cluster_file is not None and cluster_file.is_file()

    view_flag = None
    if args.ast:
        view_flag = "ast"
    elif args.cfg:
        view_flag = "cfg"
    elif args.fcg:
        view_flag = "fcg"
    elif args.syscall:
        view_flag = "syscall"

    view_dir = args.view
    view_name = Path(args.view).name if args.view is not None else None
    if view_flag:
        # LOGGER.info("Loading view graph '%s' for %s", view_flag, sha)
        _log_memory_usage(device, f"Before loading view graph for {sha}")
        # treat args.view as the root directory when a view flag is specified
        view_dir = Path(args.view) / view_flag
        view_name = view_flag
        if not sha:
            raise ValueError("sha256 required to load view graph")
        fp = view_dir / f"{sha}.json"
        if not fp.is_file():
            gz = fp.with_suffix(fp.suffix + ".gz")
            if gz.is_file():
                fp = gz
        g = get_loader(view_flag).load(fp)
        _log_memory_usage(device, f"After loading view graph for {sha}")
        if not isinstance(g, HeteroData):
            # Normalize single-view graph into HeteroData schema first
            try:
                _log_memory_usage(device, f"Before normalizing view graph for {sha}")
                g = get_normalizer(view_flag).normalize(g)
                _log_memory_usage(device, f"After normalizing view graph for {sha}")
            except Exception:  # pragma: no cover - best effort fallback
                builder = HeteroGraphBuilder()
                builder.add_view(g, view_flag)
                g = builder.build()
        graph = g
    else:
        if isinstance(graph, str):
            raise TypeError("expected HeteroData when no view flag is set")

    # LOGGER.info("Graph loaded. Preparing for training.")
    _log_memory_usage(device, f"After graph load for {sha}")

    # Log graph size details
    num_nodes = sum(graph[nt].num_nodes for nt in graph.node_types)
    num_edges = sum(graph[et].num_edges for et in graph.edge_types)
    # LOGGER.info(f"Graph {sha} details: {num_nodes} nodes, {num_edges} edges.")

    # Ensure edge_index is contiguous before passing to loader
    for store in graph.edge_stores:
        if "edge_index" in store:
            store.edge_index = store.edge_index.contiguous()

    _log_memory_usage(device, f"Before GraphDataset._ensure_num_nodes for {sha}")
    graph = GraphDataset._ensure_num_nodes(graph)
    _log_memory_usage(device, f"After GraphDataset._ensure_num_nodes for {sha}")

    _log_memory_usage(device, f"Before GraphDataset._ensure_x for {sha}")
    graph = GraphDataset._ensure_x(graph)
    _log_memory_usage(device, f"After GraphDataset._ensure_x for {sha}")

    _log_memory_usage(device, f"Before GraphDataset._ensure_meta_ids for {sha}")
    graph = GraphDataset._ensure_meta_ids(graph, model.encoder.attr_names)
    _log_memory_usage(device, f"After GraphDataset._ensure_meta_ids for {sha}")

    if view_name is not None:
        _log_memory_usage(device, f"Before filter_view for {sha}")
        graph = filter_view(graph, view_name)
        _log_memory_usage(device, f"After filter_view for {sha}")

    # Re-initialize model's input layers to match the actual feature dimensions of the graph.
    # This is crucial because the explainer might be using graphs with different features
    # (e.g., with loaded embeddings) than the original trained model.
    _ = _reinit_input_proj(graph, model, device)

    _log_memory_usage(device, f"Before adding batch attribute for {sha}")
    for nt in graph.node_types:
        graph[nt].batch = torch.zeros(graph[nt].num_nodes, dtype=torch.long)
    _log_memory_usage(device, f"After adding batch attribute for {sha}")

    # Explicitly set num_nodes to 0 if it's None to prevent TypeError
    """
    _log_memory_usage(device, f"Before ensuring all num_nodes are set for {sha}")
    for node_store in graph.node_stores:
        if node_store.num_nodes is None:
            node_store.num_nodes = 0
    _log_memory_usage(device, f"After ensuring all num_nodes are set for {sha}")
    """

    # _log_memory_usage(device, f"Before _reinit_input_proj for {sha}")
    # _reinit_input_proj(graph, model, device)
    # _log_memory_usage(device, f"After _reinit_input_proj for {sha}")

    if args.fp16:
        _log_memory_usage(device, f"Before model.half() for {sha}")
        model.half()
        _log_memory_usage(device, f"After model.half() for {sha}")

    param_dtype = (
        torch.float16
        if args.fp16 or (args.amp and device.type == "cuda")
        else next(model.parameters()).dtype
    )

    _log_memory_usage(device, f"Before _cast_graph_dtype for {sha}")
    _cast_graph_dtype(graph, param_dtype)
    _log_memory_usage(device, f"After _cast_graph_dtype for {sha}")

    sainth_loader = None
    if args.saint:
        # LOGGER.info("Using GraphSAINT loader.")
        from src.graphs.builders.graph_sampler import sainth_loader_hetero

        _log_memory_usage(device, f"Before sainth_loader_hetero for {sha}")
        sainth_loader = sainth_loader_hetero(
            graph,
            mode=args.saint,
            batch_size=args.batch_size,
            walk_length=args.walk_length,
            sample_coverage=args.sample_coverage,
            num_steps=args.num_steps,
        )
        _log_memory_usage(device, f"After sainth_loader_hetero for {sha}")

    score_cache: dict[str, float] = {}
    if args.score_cache and args.score_cache.is_file():
        try:
            with args.score_cache.open() as fp:
                score_cache = json.load(fp)
        except Exception as e:  # pragma: no cover - best effort
            LOGGER.warning("Failed to load score cache %s: %s", args.score_cache, e)

    skip_full = args.no_full_score and not (
        args.score_cache and sha and sha in score_cache
    )

    if args.amp and device.type == "cuda":

        def score_fn(g):
            with torch.amp.autocast(device_type="cuda"):
                return model(
                    g,
                    return_logits=True,
                    checkpoint_layers=args.checkpoint,
                ).squeeze()

    else:
        score_fn = lambda g: model(
            g, return_logits=True, checkpoint_layers=args.checkpoint
        ).squeeze()

    _log_memory_usage(device, f"Before attaching edge_id for {sha}")
    offset = 0
    for et in graph.edge_types:
        if "edge_id" not in graph[et]:
            num_e = graph[et].edge_index.size(1)
            graph[et].edge_id = torch.arange(offset, offset + num_e, dtype=torch.int32)
            offset += num_e
    _log_memory_usage(device, f"After attaching edge_id for {sha}")

    _log_memory_usage(device, f"Before GumbelMaskSelector init for {sha}")
    selector = GumbelMaskSelector(view=view_name, device=device)
    _log_memory_usage(device, f"After GumbelMaskSelector init for {sha}")

    _log_memory_usage(device, f"Before ensure_edgeaware_selector for {sha}")
    ensure_edgeaware_selector(selector, graph)
    selector.to(device)
    _log_memory_usage(device, f"After ensure_edgeaware_selector for {sha}")

    _log_memory_usage(device, f"Before Adam optimizer init for {sha}")
    optim = torch.optim.Adam(selector.parameters(), lr=args.lr)
    _log_memory_usage(device, f"After Adam optimizer init for {sha}")

    full_score: torch.Tensor | None = None
    # LOGGER.info("Calculating full graph score...")
    _log_memory_usage(device, f"Before full score calculation block for {sha}")
    if args.score_cache and sha and sha in score_cache:
        _log_memory_usage(device, f"Loading full score from cache for {sha}")
        full_score = torch.tensor(score_cache[sha], device=device)
    elif not skip_full:
        with torch.no_grad():
            if args.full_cpu:
                LOGGER.info("Calculating full score on CPU.")
                _log_memory_usage(device, f"Before model.to(cpu) for {sha}")
                model_cpu = model.to("cpu") if device.type == "cuda" else model
                _log_memory_usage(device, f"After model.to(cpu) for {sha}")

                _log_memory_usage(device, f"Before graph.to(cpu) for {sha}")
                graph_cpu = graph.to("cpu")
                _log_memory_usage(device, f"After graph.to(cpu) for {sha}")

                ctx = nullcontext
                with ctx():
                    _log_memory_usage(
                        device, f"Before full_score calculation (CPU) for {sha}"
                    )
                    full_score = model_cpu(
                        graph_cpu, return_logits=True, checkpoint_layers=args.checkpoint
                    ).squeeze()
                    _log_memory_usage(
                        device, f"After full_score calculation (CPU) for {sha}"
                    )

                del graph_cpu
                if device.type == "cuda":
                    _log_memory_usage(device, f"Before model.to(device) for {sha}")
                    model.to(device)
                    _log_memory_usage(device, f"After model.to(device) for {sha}")

            elif args.full_mini_batch:
                # LOGGER.info("Calculating full score with mini-batches.")
                _log_memory_usage(
                    device, f"Before NeighborLoader for full_score for {sha}"
                )
                num_neigh = {
                    et: [args.num_neighbors] * args.num_hops for et in graph.edge_types
                }
                num_target_nodes = graph[model.encoder.target_node].num_nodes or 0
                loader = NeighborLoader(
                    graph,
                    input_nodes=(
                        model.encoder.target_node,
                        torch.arange(num_target_nodes),
                    ),
                    batch_size=args.batch_size,
                    num_neighbors=num_neigh,
                    shuffle=False,
                )
                _log_memory_usage(
                    device, f"After NeighborLoader for full_score for {sha}"
                )
                pred_sum = torch.tensor(0.0)
                n = 0
                ctx = (
                    partial(torch.amp.autocast, device_type="cuda")
                    if (device.type == "cuda" and args.amp)
                    else nullcontext
                )
                for i, batch in enumerate(loader):
                    _log_memory_usage(
                        device, f"Start of full_score batch {i} for {sha}"
                    )
                    batch = batch.to(device)
                    _cast_graph_dtype(batch, param_dtype)
                    with ctx():
                        pred_sum += (
                            model(
                                batch,
                                return_logits=True,
                                checkpoint_layers=args.checkpoint,
                            )
                            .squeeze()
                            .cpu()
                        )
                    n += 1
                    _log_memory_usage(device, f"End of full_score batch {i} for {sha}")
                full_score = pred_sum / n
            elif has_cluster:
                LOGGER.info("Calculating full score with cluster loader.")
                _log_memory_usage(
                    device, f"Before ClusterLoader for full_score for {sha}"
                )
                from src.graphs.builders.graph_sampler import cluster_file_loader_hetero

                loader = cluster_file_loader_hetero(
                    graph,
                    cluster_file,
                    batch_size=args.cluster_batch_size,
                    shuffle=False,
                )
                _log_memory_usage(
                    device, f"After ClusterLoader for full_score for {sha}"
                )
                pred_sum = torch.tensor(0.0)
                n = 0
                ctx = (
                    partial(torch.amp.autocast, device_type="cuda")
                    if (device.type == "cuda" and args.amp)
                    else nullcontext
                )
                for i, part in enumerate(loader):
                    _log_memory_usage(
                        device, f"Start of cluster full_score batch {i} for {sha}"
                    )
                    part = part.to(device)
                    _cast_graph_dtype(part, param_dtype)
                    with ctx():
                        pred_sum += (
                            model(
                                part,
                                return_logits=True,
                                checkpoint_layers=args.checkpoint,
                            )
                            .squeeze()
                            .cpu()
                        )
                    n += 1
                    _log_memory_usage(
                        device, f"End of cluster full_score batch {i} for {sha}"
                    )
                full_score = pred_sum / n
            elif args.cluster_parts > 0:
                LOGGER.info("Calculating full score with cluster loader (on-the-fly).")
                _log_memory_usage(
                    device, f"Before on-the-fly ClusterLoader for full_score for {sha}"
                )
                from src.graphs.builders.graph_sampler import cluster_loader_hetero

                loader = cluster_loader_hetero(
                    graph,
                    batch_size=args.cluster_batch_size,
                    num_parts=args.cluster_parts,
                    shuffle=False,
                )
                _log_memory_usage(
                    device, f"After on-the-fly ClusterLoader for full_score for {sha}"
                )
                pred_sum = torch.tensor(0.0)
                n = 0
                ctx = (
                    partial(torch.amp.autocast, device_type="cuda")
                    if (device.type == "cuda" and args.amp)
                    else nullcontext
                )
                for i, part in enumerate(loader):
                    _log_memory_usage(
                        device,
                        f"Start of on-the-fly cluster full_score batch {i} for {sha}",
                    )
                    part = part.to(device)
                    _cast_graph_dtype(part, param_dtype)
                    with ctx():
                        pred_sum += (
                            model(
                                part,
                                return_logits=True,
                                checkpoint_layers=args.checkpoint,
                            )
                            .squeeze()
                            .cpu()
                        )
                    n += 1
                    _log_memory_usage(
                        device,
                        f"End of on-the-fly cluster full_score batch {i} for {sha}",
                    )
                full_score = pred_sum / n
            elif args.saint:
                LOGGER.info("Calculating full score with GraphSAINT loader.")
                pred_sum = torch.tensor(0.0)
                n = 0
                ctx = (
                    partial(torch.amp.autocast, device_type="cuda")
                    if (device.type == "cuda" and args.amp)
                    else nullcontext
                )
                _log_memory_usage(
                    device, f"Before GraphSAINT full_score loop for {sha}"
                )
                for i, part in enumerate(sainth_loader):
                    _log_memory_usage(
                        device, f"Start of GraphSAINT full_score batch {i} for {sha}"
                    )
                    part = part.to(device)
                    _cast_graph_dtype(part, param_dtype)
                    with ctx():
                        pred_sum += (
                            model(
                                part,
                                return_logits=True,
                                checkpoint_layers=args.checkpoint,
                            )
                            .squeeze()
                            .cpu()
                        )
                    n += 1
                    _log_memory_usage(
                        device, f"End of GraphSAINT full_score batch {i} for {sha}"
                    )
                full_score = pred_sum / n
                _log_memory_usage(device, f"After GraphSAINT full_score loop for {sha}")
            else:
                LOGGER.info("Calculating full score with default NeighborLoader.")
                _log_memory_usage(
                    device, f"Before default NeighborLoader for full_score for {sha}"
                )
                num_neigh = {et: [3] * args.num_hops for et in graph.edge_types}
                loader = NeighborLoader(
                    graph,
                    input_nodes=(
                        model.encoder.target_node,
                        torch.arange(graph[model.encoder.target_node].num_nodes),
                    ),
                    batch_size=256,
                    num_neighbors=num_neigh,
                    shuffle=False,
                )
                _log_memory_usage(
                    device, f"After default NeighborLoader for full_score for {sha}"
                )
                pred_sum = torch.tensor(0.0)
                n = 0
                ctx = (
                    partial(torch.amp.autocast, device_type="cuda")
                    if (device.type == "cuda" and args.amp)
                    else nullcontext
                )
                for i, batch in enumerate(loader):
                    _log_memory_usage(
                        device, f"Start of default full_score batch {i} for {sha}"
                    )
                    batch = batch.to(device)
                    _cast_graph_dtype(batch, param_dtype)
                    with ctx():
                        pred_sum += (
                            model(
                                batch,
                                return_logits=True,
                                checkpoint_layers=args.checkpoint,
                            )
                            .squeeze()
                            .cpu()
                        )
                    n += 1
                    _log_memory_usage(
                        device, f"End of default full_score batch {i} for {sha}"
                    )
                full_score = pred_sum / n
    else:
        LOGGER.info("Skipping full score calculation.")
        full_score = torch.tensor(0.0, device=device)

    _log_memory_usage(device, f"After full score calculation block for {sha}")

    # ... (rest of the function is the same)
    if args.score_cache and sha and full_score is not None:
        score_cache[sha] = float(full_score.detach().cpu().item())
        try:
            args.score_cache.parent.mkdir(parents=True, exist_ok=True)
            with args.score_cache.open("w", encoding="utf-8") as fp:
                json.dump(score_cache, fp, indent=2)
        except Exception as e:  # pragma: no cover - best effort
            LOGGER.warning("Failed to update score cache %s: %s", args.score_cache, e)

    def step_subgraph(sub):
        # Ensure the model's input layers are compatible with the subgraph's features.
        # This is critical as subgraphs from a sampler might have different feature
        # structures than the full graph.
        _ = _reinit_input_proj(sub, model, device)
        _cast_graph_dtype(sub, param_dtype)
        masks = []
        optim.zero_grad()
        τ = float(selector.tau)
        original = {}
        for et in iter_edge_types(sub, view_name):
            _, store, gid = get_edge_store(sub, et)
            logits = selector.logits[str(et)][gid]
            mask = gumbel_sigmoid(logits, τ, False)
            masks.append(mask)
            keep = mask > 0.5
            if keep.sum() == 0:
                if len(mask) > 0:
                    keep[mask.argmax()] = True
                else:
                    continue
            backup = {}
            for k, v in store.items():
                if torch.is_tensor(v) and v.size(0) == mask.size(0):
                    backup[k] = v
                    store[k] = v[keep]
            original[str(et)] = backup

        with torch.no_grad():
            masked_score = score_fn(sub)

        for et_str, backup in original.items():
            etype = eval(et_str)
            store = sub[etype]
            for k, v in backup.items():
                store[k] = v

        m_prob = torch.cat(masks) if masks else torch.empty(0, device=device)
        loss = selector.loss(
            full_score, masked_score, m_prob, alpha=args.alpha, beta=args.beta
        )
        loss.backward()
        optim.step()
        selector.tau.mul_(selector.tau_decay).clamp_(min=selector.tau_min)
        del masked_score, m_prob, loss
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    # prepare a mini-batch loader for repeated sampling
    # LOGGER.info("Starting selector training loop.")
    if has_cluster:
        from src.graphs.builders.graph_sampler import cluster_file_loader_hetero

        LOGGER.info("Using ClusterLoader from file.")
        loader = cluster_file_loader_hetero(
            graph,
            cluster_file,
            batch_size=args.cluster_batch_size,
            shuffle=True,
        )
    elif args.saint:
        # LOGGER.info("Using GraphSAINTLoader.")
        loader = sainth_loader
    else:
        LOGGER.info("Using NeighborLoader.")
        neigh_args = {
            et: [args.num_neighbors] * args.num_hops for et in graph.edge_types
        }
        loader = NeighborLoader(
            graph,
            input_nodes=(
                model.encoder.target_node,
                torch.arange(graph[model.encoder.target_node].num_nodes),
            ),
            batch_size=args.batch_size,
            num_neighbors=neigh_args,
            shuffle=True,
        )

    _log_memory_usage(device, f"Before iter(loader) for {sha}")
    loader_iter = iter(loader)
    _log_memory_usage(device, f"After iter(loader) for {sha}")

    for epoch in range(args.epochs):
        _log_memory_usage(device, f"Start of epoch {epoch+1}/{args.epochs} for {sha}")
        try:
            _log_memory_usage(device, f"Before next(loader_iter) in epoch {epoch+1}")
            sub = next(loader_iter)
            _log_memory_usage(device, f"After next(loader_iter) in epoch {epoch+1}")
        except StopIteration:
            _log_memory_usage(
                device, f"Re-initializing loader iterator in epoch {epoch+1}"
            )
            loader_iter = iter(loader)
            _log_memory_usage(
                device, f"After re-initializing loader iterator in epoch {epoch+1}"
            )
            sub = next(loader_iter)
            _log_memory_usage(
                device, f"After next(loader_iter) following re-init in epoch {epoch+1}"
            )

        # --- BEGIN MODIFICATION ---
        # Manually copy node features and required attribute IDs from the full graph to the subgraph.
        # The GraphSAINT sampler may not preserve all attributes, so this step ensures that
        # the subgraph has the correct feature tensors ('x') and metadata IDs ('..._id')
        # needed by the RGCNEncoder.
        for nt in graph.node_types:
            if nt not in sub.node_types:
                # If a node type is completely missing, clone it from the original graph.
                # This can happen if the sampler drops all nodes of a certain type.
                sub.node_stores[sub.node_type_to_key[nt]] = graph.node_stores[
                    graph.node_type_to_key[nt]
                ].clone()
                continue

            if hasattr(sub[nt], "n_id"):
                original_node_indices = sub[nt].n_id
                if original_node_indices.numel() > 0:
                    # Copy the main node features
                    if hasattr(graph[nt], "x"):
                        sub[nt].x = graph[nt].x[original_node_indices]

                    # Copy all required '_id' attributes that the encoder uses
                    if model.encoder.attr_names and nt in model.encoder.attr_names:
                        for attr_name in model.encoder.attr_names[nt]:
                            attr_id_key = f"{attr_name}_id"
                            if hasattr(graph[nt], attr_id_key):
                                sub[nt][attr_id_key] = graph[nt][attr_id_key][
                                    original_node_indices
                                ]
        # --- END MODIFICATION ---

        if has_cluster:
            builder = HeteroGraphBuilder()
            builder.add_view(sub, view_name)
            sub = builder.build()

        _log_memory_usage(device, f"Before sub.to(device) in epoch {epoch+1}")
        sub = sub.to(device)
        _log_memory_usage(device, f"After sub.to(device) in epoch {epoch+1}")

        for nt in sub.node_types:
            if "batch" not in sub[nt]:
                sub[nt].batch = torch.zeros(
                    sub[nt].num_nodes, dtype=torch.long, device=device
                )

        _log_memory_usage(device, f"Before step_subgraph in epoch {epoch+1}")
        step_subgraph(sub)
        _log_memory_usage(device, f"After step_subgraph in epoch {epoch+1}")

        del sub
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        _log_memory_usage(device, f"End of epoch {epoch+1}/{args.epochs} for {sha}")

    LOGGER.info("Selector training loop finished.")
    # release loader resources explicitly
    del loader
    if sainth_loader is not None:
        del sainth_loader
    gc.collect()

    pred_info = None
    try:
        LOGGER.info("Pruning graph and making prediction.")
        sel = selector.hard_selection(graph)
        keep: dict[str, set[int]] = {}
        for et in iter_edge_types(graph, view_name):
            idx = sel.get(str(et))
            if idx is None or len(idx) == 0:
                continue
            ei = graph[et].edge_index[:, idx]
            keep.setdefault(et[0], set()).update(ei[0].tolist())
            keep.setdefault(et[2], set()).update(ei[1].tolist())
        keep_idx = {nt: sorted(v) for nt, v in keep.items()}
        pruned = drop_unselected_nodes(graph, keep_idx, view_name)
        builder = HeteroGraphBuilder()
        builder.add_view(pruned, view_name)
        pruned_graph = builder.build()
        _cast_graph_dtype(pruned_graph, param_dtype)
        with torch.no_grad():
            ctx = (
                partial(torch.amp.autocast, device_type="cuda")
                if (device.type == "cuda" and args.amp)
                else nullcontext
            )
            with ctx():
                logits = model(
                    pruned_graph,
                    return_logits=True,
                    checkpoint_layers=args.checkpoint,
                ).squeeze()
            prob = float(logits.sigmoid().cpu().item())
            pred = int(prob >= 0.5)
            pred_info = {"pred": pred, "prob": prob}
    except Exception as e:  # pragma: no cover - best effort
        LOGGER.warning("Prediction on pruned graph failed: %s", e)

    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    LOGGER.info("Finished selector training for graph: %s", sha)
    _log_memory_usage(device, f"End of _train_selector_for_graph for {sha}")
    return selector, graph, pred_info


def _train_batch_impl(args, model, device: torch.device) -> None:
    LOGGER.info("Starting batch training process.")
    _log_memory_usage(device, "Start of _train_batch_impl")

    # --- BEGIN MODIFICATION ---
    # Initialize GraphDataset with a dummy path first, then override
    # the necessary attributes directly from the command-line arguments.
    # This bypasses the problematic path logic in the constructor.
    try:
        ds = GraphDataset(root=".", split="_dummy_split_")
    except FileNotFoundError:
        # The dummy path might not exist, which is fine. Create a placeholder.
        ds = object().__new__(GraphDataset)
        ds.root = Path(args.graph_dir).parent
        ds.labels = {}  # Initialize labels to prevent errors
        ds.transform = None
        ds.id_col = "sha256"
        ds.label_col = "label"
        ds.require_labels = False
        ds.over_length_policy = "trim"
        ds.load_embeds = not args.no_embeds

    ds.graph_dir = Path(args.graph_dir)
    ds.embed_dir = Path(args.embed_dir)
    if ds.graph_dir.is_dir():
        ds.samples = sorted(p.stem for p in ds.graph_dir.iterdir() if p.is_file())
    else:
        ds.samples = []
    # --- END MODIFICATION ---

    if args.meta_csv:
        if not args.meta_csv.is_file():
            LOGGER.error(f"Meta CSV not found: {args.meta_csv}")
            return
        try:
            df = pd.read_csv(args.meta_csv)
            allowed = set(df[df.get("label", 1) == 1]["sha256"].tolist())
            ds.samples = [s for s in ds.samples if s in allowed]
        except Exception as e:
            LOGGER.error(f"Failed to read meta CSV: {e}", exc_info=True)
            return

    loader = DataLoader(
        range(len(ds)),
        batch_size=1,
        shuffle=False,
    )

    features_out: list[dict] = []
    for batch_idx in tqdm(loader, desc="Training Explainers"):
        idx = int(batch_idx[0])
        sha = ds.samples[idx]
        # LOGGER.info("Processing graph %s (%d/%d)", sha, idx + 1, len(ds))

        # Reload model if it was deleted in the previous iteration's finally block.
        if "model" not in locals() or model is None:
            model, _ = _load_model(args, device)

        _log_memory_usage(device, f"Before processing {sha}")
        graph_data, _, _ = ds[idx]

        # --- LOGGING START ---
        LOGGER.info(f"--- Processing {sha} ---")
        if "token" in graph_data.node_types and hasattr(graph_data["token"], "x"):
            LOGGER.info(
                f"[{sha}] After GraphDataset: 'token' features shape: {graph_data['token'].x.shape}"
            )
        else:
            LOGGER.warning(
                f"[{sha}] After GraphDataset: 'token' nodes or features are MISSING or have no .x attribute."
            )
        # --- LOGGING END ---

        graph = None
        selector = None
        try:
            graph_input = graph_data
            graph_input.sha256 = sha
            if not isinstance(graph_input, HeteroData):
                LOGGER.warning(f"Skipping {sha}: not a HeteroData")
                continue
            if (
                model.encoder.target_node not in graph_input.node_types
                or graph_input[model.encoder.target_node].num_nodes == 0
            ):
                LOGGER.warning(f"Skipping {sha}: no target nodes")
                continue
            if not any(
                et[1] == "cfg" and graph_input[et].num_edges > 0
                for et in graph_input.edge_types
            ):
                LOGGER.warning(f"Skipping {sha}: no CFG edges")
                continue

            selector, graph, pred_info = _train_selector_for_graph(
                graph_input, model, args, device
            )

            # Memory is managed in the 'finally' block.

            out_path = args.output_dir / f"{sha}_selector.pt"
            args.output_dir.mkdir(parents=True, exist_ok=True)
            torch.save(selector, out_path)
            LOGGER.debug(f"Selector saved → {out_path}")
            if pred_info is not None:
                pred_path = args.output_dir / f"{sha}_pred.json"
                with pred_path.open("w", encoding="utf-8") as fp:
                    json.dump(pred_info, fp)

            if args.mine_features:
                try:
                    # Model is guaranteed to exist here.
                    feats = _mine_tokens(graph, model, device)
                    features_out.append({"sha256": sha, "features": feats})
                except Exception as e:
                    LOGGER.error(f"Feature mining failed for {sha}: {e}", exc_info=True)

        except Exception as e:
            LOGGER.error(f"Failed to process {sha}: {e}", exc_info=True)
        finally:
            del graph
            del selector
            # Manage model memory at the end of each iteration.
            if "model" in locals() and model is None:
                del model
                model = None  # Explicitly set to None for the check at the start of the loop
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                clear_memory_cache()
                LOGGER.debug("CUDA and feature caches cleared")
            _log_memory_usage(device, f"After processing {sha}")

    if args.mine_features and features_out:
        with args.mine_features.open("w", encoding="utf-8") as fp:
            json.dump(features_out, fp, indent=2)
        LOGGER.info(f"Saved mined features → {args.mine_features}")
    LOGGER.info("Batch training process finished.")
    _log_memory_usage(device, "End of _train_batch_impl")


def train_batch(args: argparse.Namespace) -> None:
    device = torch.device(args.device)
    model, _ = _load_model(args, device)
    _train_batch_impl(args, model, device)


def train_single(args: argparse.Namespace) -> None:
    device = torch.device(args.device)
    model, _ = _load_model(args, device)

    if args.ast or args.cfg or args.fcg or args.syscall:
        sha = args.cfg_graph.stem
        graph_input = sha
        cfg_graph = None  # loaded inside helper
    else:
        data = torch.load(args.cfg_graph, map_location="cpu", weights_only=False)
        cfg_graph = None
        if isinstance(data, HeteroData):
            if any(et[1] == "cfg" and data[et].num_edges > 0 for et in data.edge_types):
                cfg_graph = data
        else:
            for g in data:
                if isinstance(g, HeteroData) and any(
                    et[1] == "cfg" and g[et].num_edges > 0 for et in g.edge_types
                ):
                    cfg_graph = g
                    break
        if cfg_graph is None:
            raise ValueError("No valid graph with CFG edges found in the dataset.")

        sha = getattr(cfg_graph, "sha256", None)
        if sha and not args.no_embeds:
            _attach_embeddings(cfg_graph, sha, args.embed_dir)
        graph_input = cfg_graph

    selector, cfg_graph, pred_info = _train_selector_for_graph(
        graph_input, model, args, device
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    torch.save(selector, args.output)
    LOGGER.info("Saved selector → %s", args.output)
    if pred_info is not None:
        pred_path = args.output.with_suffix(".pred.json")
        with pred_path.open("w", encoding="utf-8") as fp:
            json.dump(pred_info, fp)
        LOGGER.info("Saved prediction → %s", pred_path)

    if args.mine_features:
        feats = _mine_tokens(cfg_graph, model, device)
        with args.mine_features.open("w", encoding="utf-8") as fp:
            json.dump(
                [{"sha256": sha or args.cfg_graph.stem, "features": feats}],
                fp,
                indent=2,
            )
        LOGGER.info("Saved mined features → %s", args.mine_features)


def _compute_node_embeddings(graph: HeteroData, encoder) -> dict[str, torch.Tensor]:
    x_dict: dict[str, torch.Tensor] = {}

    # Step 1: Apply input projection to all node types
    for nt in graph.node_types:
        if not hasattr(graph[nt], "x"):
            continue
        feats = [graph[nt].x]
        if getattr(encoder, "meta_embed", None):
            for name in encoder.attr_names.get(nt, []):
                attr = getattr(graph[nt], f"{name}_id", None)
                if attr is not None:
                    feats.append(encoder.meta_embed(attr))
        node_feat = torch.cat(feats, dim=-1) if len(feats) > 1 else feats[0]

        # --- BEGIN MODIFICATION (Robust Dimension Handling) ---
        # Dynamically adjust tensor dimension to match the model's expected input layer size.
        # This prevents runtime errors when a graph's feature dimension differs from the
        # dimension the model was originally trained on. This is a stable approach as
        # it preserves the learned weights of the model.
        if nt in encoder.input_proj:
            target_dim = encoder.input_proj[nt].in_features
            actual_dim = node_feat.shape[1]

            if actual_dim != target_dim:
                if actual_dim > target_dim:
                    # Truncate if the actual dimension is larger
                    node_feat = node_feat[:, :target_dim]
                else:
                    # Pad with zeros if the actual dimension is smaller
                    padding_size = target_dim - actual_dim
                    padding = torch.zeros(
                        (node_feat.shape[0], padding_size),
                        dtype=node_feat.dtype,
                        device=node_feat.device,
                    )
                    node_feat = torch.cat([node_feat, padding], dim=1)
        # --- END MODIFICATION ---

        if nt in encoder.input_proj:
            x_dict[nt] = encoder.input_proj[nt](node_feat)
        elif encoder.input_proj:
            # If a projection doesn't exist (e.g., for 'api'), create one on the fly
            # instead of just creating zero embeddings.
            hidden_dim = next(iter(encoder.input_proj.values())).out_features
            
            # Create a new projection layer for this node type
            # We can't add it to encoder.input_proj directly as it might cause issues with state_dict
            # So we create it locally and apply it.
            proj = torch.nn.Linear(node_feat.shape[1], hidden_dim).to(node_feat.device)
            x_dict[nt] = proj(node_feat)
            LOGGER.debug(f"Created on-the-fly projection for node type '{nt}'")
        else:
            # Fallback if the encoder has no projection layers at all.
            LOGGER.warning(f"Node type '{nt}' not in encoder schema and no fallback projection found. Skipping.")
            continue

    # Step 2: Pass through convolutional layers
    for conv in encoder.convs:
        if isinstance(conv, HeteroConv):
            new_dict: dict[str, torch.Tensor] = {}
            for (src, rel, dst), sub_conv in conv.convs.items():
                if (src, rel, dst) not in graph.edge_index_dict:
                    continue
                if src not in x_dict or dst not in x_dict:
                    continue
                edge_index = graph[(src, rel, dst)].edge_index
                out = sub_conv((x_dict[src], x_dict[dst]), edge_index)
                new_dict[dst] = new_dict.get(dst, 0) + out
            for nt in x_dict:
                new_dict.setdefault(nt, x_dict[nt])
            x_dict = new_dict
        elif isinstance(conv, MessagePassing):
            new_dict: dict[str, torch.Tensor] = {}
            for (src, rel, dst) in graph.edge_types:
                if src not in x_dict or dst not in x_dict:
                    continue
                edge_index = graph[(src, rel, dst)].edge_index
                out = conv((x_dict[src], x_dict[dst]), edge_index)
                new_dict[dst] = new_dict.get(dst, 0) + out
            for nt in x_dict:
                new_dict.setdefault(nt, x_dict[nt])
            x_dict = new_dict
        else:
            sig = inspect.signature(conv.forward)
            params = sig.parameters
            if "edge_index" in params or "edge_index_dict" in params:
                try:
                    x_dict = conv(x_dict, graph.edge_index_dict)
                except TypeError:
                    LOGGER.debug(
                        "Wrapper layer detected; retrying with keyword argument"
                    )
                    try:
                        x_dict = conv(
                            x_dict, edge_index_dict=graph.edge_index_dict
                        )
                    except TypeError:
                        x_dict = conv(x_dict)
            else:
                x_dict = conv(x_dict)
        x_dict = {k: encoder.drop(encoder.act(v)) for k, v in x_dict.items()}

    # Step 3: Determine the target embedding dimension from the encoder's architecture
    # The hidden dimension is the input feature count to the final output projection layer.
    actual_hidden_dim = encoder.out_proj.in_features

    # Step 4: Ensure all node types have the same, correct embedding dimension.
    # This is crucial for PGExplainer, which expects consistent dimensions across all node types.
    for nt in list(x_dict.keys()):
        if x_dict[nt].shape[-1] != actual_hidden_dim:
            LOGGER.warning(
                f"Node type '{nt}' embedding dimension mismatch. "
                f"Expected {actual_hidden_dim}, got {x_dict[nt].shape[-1]}. Projecting to correct dimension."
            )
            projection = torch.nn.Linear(x_dict[nt].shape[-1], actual_hidden_dim).to(x_dict[nt].device)
            x_dict[nt] = projection(x_dict[nt])

    if not x_dict:
        LOGGER.warning("x_dict is empty after computing node embeddings.")
        return {}

    LOGGER.debug(
        f"DEBUG (_compute_node_embeddings): Output x_dict dimensions: {{nt: x_dict[nt].shape for nt in x_dict}}"
    )
    return x_dict


def _masked_score(
    graph: HeteroData, mask_prob: torch.Tensor, view: str | None, model
) -> torch.Tensor:
    """Return logits with straight-through hard masking via ``edge_weight``."""
    ptr = 0
    original: dict[str, torch.Tensor | None] = {}
    for et in iter_edge_types(graph, view):
        store = graph[et]
        num_e = store.edge_index.size(1)
        mask = mask_prob[ptr : ptr + num_e]
        ptr += num_e
        if num_e == 0:
            continue
        mask_hard = (mask > 0.5).float()
        st_mask = mask_hard + (mask - mask_hard).detach()
        original[str(et)] = getattr(store, "edge_weight", None)
        store.edge_weight = st_mask

    out = model(graph, return_logits=True).squeeze()

    for et in iter_edge_types(graph, view):
        backup = original.get(str(et))
        if backup is None:
            if hasattr(graph[et], "edge_weight"):
                del graph[et].edge_weight
        else:
            graph[et].edge_weight = backup

    return out


def _delete_masked_score(
    graph: HeteroData, mask_prob: torch.Tensor, view: str | None, model
) -> torch.Tensor:
    """Return logits for ``graph`` after deleting edges with mask<0.5."""
    ptr = 0
    original: dict[str, dict[str, torch.Tensor]] = {}
    for et in iter_edge_types(graph, view):
        store = graph[et]
        num_e = store.edge_index.size(1)
        mask = mask_prob[ptr : ptr + num_e]
        ptr += num_e
        keep = mask > 0.5
        if keep.sum() == 0:
            if len(mask) > 0:
                keep[mask.argmax()] = True
            else:
                continue
        backup = {}
        for k, v in store.items():
            if not torch.is_tensor(v):
                continue
            if k == "edge_index":
                backup[k] = v
                store[k] = v[:, keep]
            elif v.size(0) == mask.size(0):
                backup[k] = v
                store[k] = v[keep]
        original[str(et)] = backup

    out = model(graph, return_logits=True).squeeze()

    for et_str, backup in original.items():
        etype = eval(et_str)
        store = graph[etype]
        for k, v in backup.items():
            store[k] = v

    return out


def _soft_masked_score(
    graph: HeteroData, mask_prob: torch.Tensor, view: str | None, model
) -> torch.Tensor:
    """Return logits for ``graph`` with ``mask_prob`` passed via ``edge_weight_dict``."""
    ptr = 0
    edge_weight_dict: dict[tuple[str, str, str], torch.Tensor] = {}
    for et in iter_edge_types(graph, view):
        store = graph[et]
        num_e = store.edge_index.size(1)
        mask = mask_prob[ptr : ptr + num_e]
        ptr += num_e
        if num_e == 0:
            continue
        edge_weight_dict[et] = mask

    out = model(graph, edge_weight_dict=edge_weight_dict, return_logits=True).squeeze()

    return out


def _ensure_fallback_features(
    g: HeteroData,
    all_node_types: list[str],
    fallback_dim: int = 1,
) -> None:
    """
    For any node type in the graph that is present in the global schema but lacks
    an 'x' feature tensor, create a fallback feature tensor of ones.
    This ensures that all nodes can be processed by the model.
    """
    for nt in all_node_types:
        if nt in g.node_types and not hasattr(g[nt], "x"):
            if g[nt].num_nodes > 0:
                LOGGER.info(
                    f"Node type '{nt}' has no features. Creating fallback features with dim={fallback_dim}."
                )
                g[nt].x = torch.ones((g[nt].num_nodes, fallback_dim))


def _evaluate_global(
    explainer: PGExplainer,
    model: RESGCLClassifier,
    paths: list[Path],
    device: torch.device,
    args: argparse.Namespace,
    all_node_types: list[str],
    current_beta: float,
) -> tuple[float, float, float, float, float]:
    """Return average loss, fidelity, sparsity, stability and necessity."""
    if not paths:
        return 0.0, 0.0, 0.0, 0.0, 0.0

    total_loss = 0.0
    total_fid = 0.0
    total_spars = 0.0
    total_stab = 0.0
    total_nec = 0.0
    count = 0
    param_dtype = next(model.parameters()).dtype

    for gp in paths:
        g = torch.load(gp, map_location="cpu", weights_only=False)
        if not isinstance(g, HeteroData):
            continue
        sha = getattr(g, "sha256", gp.stem)
        if not args.no_embeds:
            _attach_embeddings(g, sha, args.embed_dir)
        g = GraphDataset._ensure_num_nodes(g)
        g = GraphDataset._ensure_x(g)
        g = GraphDataset._ensure_meta_ids(g, model.encoder.attr_names)
        _ensure_fallback_features(g, all_node_types, fallback_dim=1)
        view_name = Path(args.view).name if args.view is not None else None
        if view_name is not None:
            g = filter_view(g, view_name)
        for nt in g.node_types:
            g[nt].batch = torch.zeros(g[nt].num_nodes, dtype=torch.long)
        # _ = _reinit_input_proj(g, model, device)
        _cast_graph_dtype(g, param_dtype)
        g = g.to(device)

        with torch.no_grad():
            embeds = _compute_node_embeddings(g, model.encoder)
            full_score = model(g, return_logits=True).squeeze()

            avg_fidelity = 0.0
            avg_sparsity = 0.0
            avg_loss = 0.0
            avg_stab = 0.0
            avg_nec = 0.0

            for _ in range(args.val_samples):
                mask_prob = explainer(g, embeddings=embeds, hard=True)
                if mask_prob.numel() == 0:
                    continue
                if args.hard_mask_mode == "delete":
                    masked_score = _delete_masked_score(g, mask_prob, args.view, model)
                else:
                    masked_score = _masked_score(g, mask_prob, args.view, model)

                target_prob = torch.sigmoid(full_score.detach()).clamp(1e-4, 1 - 1e-4)
                fidelity = F.binary_cross_entropy_with_logits(
                    masked_score, target_prob
                )
                sparsity = mask_prob.mean()
                stab_loss = compute_stability_loss(
                    g, explainer, mask_prob, True
                )
                nec_loss = compute_necessity_loss(
                    g,
                    mask_prob,
                    explainer,
                    model,
                    full_score,
                    use_hard_prune=args.hard_necessity,
                    drop_ratio=args.necessity_drop_ratio,
                )
                loss = explainer.loss(
                    full_score,
                    masked_score,
                    mask_prob,
                    alpha=args.alpha,
                    beta=current_beta,
                    gamma=args.gamma,
                    loss_type=args.loss_type,
                )
                avg_fidelity += float(fidelity)
                avg_sparsity += float(sparsity)
                avg_loss += float(loss)
                avg_stab += float(stab_loss)
                avg_nec += float(nec_loss)

            if args.val_samples > 0:
                fidelity = avg_fidelity / args.val_samples
                sparsity = avg_sparsity / args.val_samples
                loss = avg_loss / args.val_samples
                stab_loss = avg_stab / args.val_samples
                nec_loss = avg_nec / args.val_samples

        total_loss += float(loss)
        total_fid += float(fidelity)
        total_spars += float(sparsity)
        total_stab += float(stab_loss)
        total_nec += float(nec_loss)
        count += 1

    if count == 0:
        return 0.0, 0.0, 0.0, 0.0, 0.0
    return (
        total_loss / count,
        total_fid / count,
        total_spars / count,
        total_stab / count,
        total_nec / count,
    )


def _schedule_beta(current: float, args: argparse.Namespace, cap: float) -> float:
    """Return the next beta value according to the schedule."""
    new_beta = current * args.beta_schedule_factor
    return min(new_beta, cap)


def _schedule_necessity_weight(
    current: float, args: argparse.Namespace, cap: float
) -> float:
    """Return the next necessity weight value according to the schedule."""
    new_weight = current * args.necessity_schedule_factor
    return min(new_weight, cap)


import matplotlib.pyplot as plt


def save_plot(history: dict, plot_path: Path):
    """Saves a plot of training and validation metrics."""
    if not history["train_loss"]:
        return

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        LOGGER.warning("matplotlib not found, skipping plot generation.")
        return

    # Create a figure with 5 subplots in a single column
    fig, axes = plt.subplots(5, 1, figsize=(12, 30), sharex=True)
    epochs_r = range(1, len(history["train_loss"]) + 1)

    # Subplot 1: Training and Validation Loss
    axes[0].plot(
        epochs_r,
        history["train_loss"],
        label="Train Loss",
        color="tab:red",
        marker="o",
    )
    if history.get("val_loss"):
        axes[0].plot(
            epochs_r,
            history["val_loss"],
            label="Validation Loss",
            color="tab:orange",
            marker="x",
        )
    axes[0].set_ylabel("Loss")
    axes[0].set_title("Train and Validation Loss over Epochs")
    axes[0].grid(True)
    axes[0].legend()

    # Subplot 2: Validation Fidelity
    if history.get("val_fid"):
        axes[1].plot(
            epochs_r,
            history["val_fid"],
            label="Validation Fidelity",
            color="tab:blue",
            marker="x",
        )
        axes[1].set_ylabel("Fidelity (Lower is Better)")
        axes[1].set_title("Validation Fidelity over Epochs")
        axes[1].grid(True)
        axes[1].legend()

    # Subplot 3: Validation Sparsity
    if history.get("val_spars"):
        axes[2].plot(
            epochs_r,
            history["val_spars"],
            label="Validation Sparsity",
            color="tab:green",
            marker="s",
        )
        axes[2].set_ylabel("Sparsity")
        axes[2].set_title("Validation Sparsity over Epochs")
        axes[2].grid(True)
        axes[2].legend()

    # Subplot 4: Validation Stability
    if history.get("val_stab"):
        axes[3].plot(
            epochs_r,
            history["val_stab"],
            label="Validation Stability",
            color="tab:purple",
            marker="^",
        )
        axes[3].set_ylabel("Stability")
        axes[3].set_title("Validation Stability over Epochs")
        axes[3].grid(True)
        axes[3].legend()

    # Subplot 5: Validation Necessity
    if history.get("val_nec"):
        axes[4].plot(
            epochs_r,
            history["val_nec"],
            label="Validation Necessity",
            color="tab:brown",
            marker="v",
        )
        axes[4].set_ylabel("Necessity")
        axes[4].set_xlabel("Epoch")
        axes[4].set_title("Validation Necessity over Epochs")
        axes[4].grid(True)
        axes[4].legend()

    fig.tight_layout()
    plot_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(plot_path)
    plt.close(fig)
    LOGGER.debug(f"Training plot updated at {plot_path}")


def train_global(args: argparse.Namespace) -> None:
    device = torch.device(args.device)
    model, meta_info = _load_model(args, device)
    encoder_hidden_dim = meta_info.get("hidden_dim", 128)

    graph_paths = sorted(Path(args.graph_dir).glob("*.pt"))
    if not graph_paths:
        raise ValueError(f"No graphs found in {args.graph_dir}")

    val_graph_paths = []
    if args.val_graph_dir and args.val_graph_dir.is_dir():
        val_graph_paths = sorted(Path(args.val_graph_dir).glob("*.pt"))
        if args.val_meta_csv and args.val_meta_csv.is_file():
            try:
                import pandas as pd

                df = pd.read_csv(args.val_meta_csv)
                allowed = set(df[df.get("label", 1) == 1]["sha256"].tolist())
                val_graph_paths = [p for p in val_graph_paths if p.stem in allowed]
            except Exception as e:
                LOGGER.warning(f"Failed to read val meta CSV: {e}")

    all_edge_types = set()
    LOGGER.debug("Scanning dataset to discover all edge types...")
    for gp in tqdm(graph_paths, desc="Scanning graph edge types"):
        try:
            g = torch.load(gp, map_location="cpu", weights_only=False)
            if isinstance(g, HeteroData):
                all_edge_types.update(g.edge_types)
        except Exception as e:
            LOGGER.warning(f"Could not read or process graph {gp}: {e}")
    all_edge_types.update(model.encoder.metadata[1])
    final_edge_types = sorted(list(all_edge_types), key=str)

    def normalize_nodetype_name(nt):
        return str(nt).split(".")[-1].lower()

    all_node_types = set()
    for src_type, _, dst_type in final_edge_types:
        all_node_types.add(normalize_nodetype_name(src_type))
        all_node_types.add(normalize_nodetype_name(dst_type))
    for nt in model.encoder.metadata[0]:
        all_node_types.add(normalize_nodetype_name(nt))
    final_node_types = sorted(list(all_node_types))
    explainer_in_dims = {nt: encoder_hidden_dim for nt in final_node_types}

    explainer = PGExplainer(
        model=model,
        in_dims=explainer_in_dims,
        node_types=final_node_types,
        edge_types=final_edge_types,
        view=args.view,
        init_bias=args.init_bias,
        tau_start=args.tau_start,
        device=device,
        hidden_dim=args.explainer_hidden_dim,
        num_layers=args.explainer_num_layers,
        dropout=args.explainer_dropout,
        norm_type=args.explainer_norm_type,
    )
    optim = torch.optim.Adam(explainer.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = None
    if args.use_cosine_annealing:
        main_scheduler_t_max = (
            args.cosine_t_max
            if args.cosine_t_max is not None
            else args.epochs - args.lr_warmup_epochs
        )
        main_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optim, T_max=main_scheduler_t_max, eta_min=args.cosine_eta_min
        )

        if args.lr_warmup_epochs > 0:
            warmup_scheduler = torch.optim.lr_scheduler.LinearLR(
                optim,
                start_factor=args.lr_warmup_start_factor,
                total_iters=args.lr_warmup_epochs,
            )
            scheduler = torch.optim.lr_scheduler.SequentialLR(
                optim,
                schedulers=[warmup_scheduler, main_scheduler],
                milestones=[args.lr_warmup_epochs],
            )
            LOGGER.info(
                f"Using SequentialLR with Linear Warmup for {args.lr_warmup_epochs} epochs "
                f"(start_factor={args.lr_warmup_start_factor}) and Cosine Annealing."
            )
        else:
            scheduler = main_scheduler
            LOGGER.info(
                f"Using CosineAnnealingLR scheduler with T_max={main_scheduler_t_max} and eta_min={args.cosine_eta_min}"
            )
    param_dtype = next(model.parameters()).dtype

    history = {
        "train_loss": [],
        "val_loss": [],
        "val_fid": [],
        "val_spars": [],
        "val_stab": [],
        "val_nec": [],
    }
    best_val_fid = float("inf")
    log_dir = args.output.parent
    log_dir.mkdir(parents=True, exist_ok=True)
    if args.plot_path:
        args.plot_path.parent.mkdir(parents=True, exist_ok=True)

    scaler = torch.amp.GradScaler("cuda", enabled=(args.amp and device.type == "cuda"))

    beta_cap = args.beta if args.beta_max is None else args.beta_max
    current_beta = args.beta_start if args.beta_schedule else args.beta
    if args.beta_schedule:
        LOGGER.info(
            f"Beta scheduling enabled: start={args.beta_start}, "
            f"factor={args.beta_schedule_factor}, "
            f"epochs_per_step={args.beta_schedule_epochs}, "
            f"target={beta_cap}"
        )

    nec_cap = (
        args.necessity_weight
        if args.necessity_weight_max is None
        else args.necessity_weight_max
    )
    current_necessity_weight = (
        args.necessity_weight_start
        if args.necessity_schedule
        else args.necessity_weight
    )
    if args.necessity_schedule:
        LOGGER.info(
            f"Necessity weight scheduling enabled: start={args.necessity_weight_start}, "
            f"factor={args.necessity_schedule_factor}, "
            f"epochs_per_step={args.necessity_schedule_epochs}, "
            f"target={nec_cap}"
        )

    with logging_redirect_tqdm():
        for epoch in range(args.epochs):
            total_loss = 0.0
            graph_count = 0
            skipped_count = 0

            explainer.train()
            optim.zero_grad()

            pbar = tqdm(
                enumerate(graph_paths),
                total=len(graph_paths),
                desc=f"Epoch {epoch + 1}/{args.epochs}",
            )

            for i, gp in pbar:
                g = torch.load(gp, map_location="cpu", weights_only=False)
                if not isinstance(g, HeteroData):
                    continue
                sha = getattr(g, "sha256", gp.stem)
                if not args.no_embeds:
                    _attach_embeddings(g, sha, args.embed_dir)
                g = GraphDataset._ensure_num_nodes(g)
                g = GraphDataset._ensure_x(g)
                g = GraphDataset._ensure_meta_ids(g, model.encoder.attr_names)
                _ensure_fallback_features(g, final_node_types, fallback_dim=1)
                view_name = Path(args.view).name if args.view is not None else None
                if view_name is not None:
                    g = filter_view(g, view_name)
                for nt in g.node_types:
                    g[nt].batch = torch.zeros(g[nt].num_nodes, dtype=torch.long)
                _cast_graph_dtype(g, param_dtype)
                g = g.to(device)

                with torch.amp.autocast(
                    "cuda", enabled=(args.amp and device.type == "cuda")
                ):
                    embeds = _compute_node_embeddings(g, model.encoder)
                    with torch.no_grad():
                        full_score = model(g, return_logits=True).squeeze()

                    use_hard_mask = epoch >= args.soft_mask_epochs
                    mask_prob = explainer(g, embeddings=embeds, hard=use_hard_mask)
                    if epoch < args.noise_epochs:
                        mask_prob = mask_prob + torch.randn_like(mask_prob) * args.noise_std
                        mask_prob.clamp_(0, 1)
                    if mask_prob.numel() == 0:
                        skipped_count += 1
                        continue
                    if use_hard_mask:
                        if args.hard_mask_mode == "delete":
                            masked = _delete_masked_score(g, mask_prob, args.view, model)
                        else:
                            masked = _masked_score(g, mask_prob, args.view, model)
                    else:
                        masked = _soft_masked_score(g, mask_prob, args.view, model)
                    loss = explainer.loss(
                        full_score,
                        masked,
                        mask_prob,
                        alpha=args.alpha,
                        beta=current_beta,
                        gamma=args.gamma,
                        loss_type=args.loss_type,
                    )
                    if epoch >= args.stability_start and args.stability_weight > 0:
                        loss = loss + args.stability_weight * compute_stability_loss(
                            g, explainer, mask_prob, use_hard_mask
                        )
                    if epoch >= args.necessity_start and current_necessity_weight > 0:
                        loss = loss + current_necessity_weight * compute_necessity_loss(
                            g,
                            mask_prob,
                            explainer,
                            model,
                            full_score,
                            use_hard_prune=args.hard_necessity,
                            drop_ratio=args.necessity_drop_ratio,
                        )

                loss_item = loss.item()
                scaler.scale(loss / args.grad_accum_steps).backward()

                if not (math.isnan(loss_item) or math.isinf(loss_item)):
                    total_loss += loss_item
                    graph_count += 1
                else:
                    LOGGER.debug(
                        f"Detected non-finite loss ({loss_item}) for graph {sha}. "
                        "Skipping from avg loss calculation."
                    )

                if (i + 1) % args.grad_accum_steps == 0 or (i + 1) == len(
                    graph_paths
                ):
                    if args.clip_grad_norm > 0:
                        scaler.unscale_(optim)
                        torch.nn.utils.clip_grad_norm_(
                            explainer.parameters(), args.clip_grad_norm
                        )

                    scaler.step(optim)
                    scaler.update()
                    optim.zero_grad()

                if graph_count > 0:
                    avg_loss_so_far = total_loss / graph_count
                    pbar.set_description(
                        "Epoch {}/{} (Loss: {:.4f}, Beta: {:.4f}, NecW: {:.4f})".format(
                            epoch + 1,
                            args.epochs,
                            avg_loss_so_far,
                            current_beta,
                            current_necessity_weight,
                        )
                    )

            if graph_count > 0:
                avg_loss = total_loss / graph_count
                history["train_loss"].append(avg_loss)
                log_msg = f"Epoch {epoch + 1}/{args.epochs} finished. Avg Train Loss: {avg_loss:.4f}."

                if val_graph_paths:
                    explainer.eval()
                    val_loss, val_fid, val_spars, val_stab, val_nec = _evaluate_global(
                        explainer,
                        model,
                        val_graph_paths,
                        device,
                        args,
                        final_node_types,
                        current_beta,
                    )
                    history["val_loss"].append(val_loss)
                    history["val_fid"].append(val_fid)
                    history["val_spars"].append(val_spars)
                    history["val_stab"].append(val_stab)
                    history["val_nec"].append(val_nec)
                    log_msg += (
                        f" Val Loss: {val_loss:.4f}, Val Fidelity: {val_fid:.4f}, "
                        f"Val Sparsity: {val_spars:.4f}, Val Stability: {val_stab:.4f}, "
                        f"Val Necessity: {val_nec:.4f}."
                    )

                    if val_fid < best_val_fid:
                        best_val_fid = val_fid
                        torch.save(explainer, args.output)
                        log_msg += f" ✓ Best model saved to {args.output}"

                LOGGER.info(log_msg)
            else:
                LOGGER.warning(
                    f"Epoch {epoch + 1}/{args.epochs} finished. No graphs were processed."
                )

            if scheduler:
                scheduler.step()
                LOGGER.debug(
                    f"LR scheduler stepped. New LR: {scheduler.get_last_lr()[0]:.6f}"
                )

            if args.beta_schedule and (epoch + 1) % args.beta_schedule_epochs == 0:
                current_beta = _schedule_beta(current_beta, args, beta_cap)
                LOGGER.info(
                    f"Beta scheduled update: new beta is {current_beta:.6f}"
                )

            if (
                args.necessity_schedule
                and (epoch + 1) >= args.necessity_start
                and (epoch + 1 - args.necessity_start) % args.necessity_schedule_epochs == 0
            ):
                current_necessity_weight = _schedule_necessity_weight(
                    current_necessity_weight, args, nec_cap
                )
                LOGGER.info(
                    "Necessity weight scheduled update: "
                    f"new weight is {current_necessity_weight:.6f}"
                )

            # Decay tau at the end of the epoch
            if epoch < args.epochs - 1:  # No decay on the last epoch
                explainer.tau.mul_(args.tau_decay).clamp_(min=args.tau_min)
                LOGGER.info(f"Tau decayed to {float(explainer.tau):.3f} at end of epoch {epoch+1}")

            if (epoch + 1) % 10 == 0:
                checkpoint_path = log_dir / f"explainer_epoch_{epoch+1}.pt"
                torch.save(explainer, checkpoint_path)
                LOGGER.info(f"Saved periodic checkpoint to {checkpoint_path}")

            if args.plot_path:
                save_plot(history, args.plot_path)

    LOGGER.info(f"Finished training. Best validation fidelity: {best_val_fid:.4f}")
    if args.plot_path:
        LOGGER.info(f"Final training plot saved to {args.plot_path}")


def mine_features(args: argparse.Namespace) -> None:
    try:
        model = RESGCLClassifier.load_from_checkpoint(
            args.model_path, map_location=args.device
        )
        model.to(args.device).eval()
        LOGGER.info("✓ classifier loaded")
    except Exception:
        LOGGER.exception("Failed to load model")
        return

    graph_files_gen = Path(args.dataset_path).glob("*.pt")
    all_features = []
    found_files = False
    for g_path in graph_files_gen:
        found_files = True
        try:
            g = torch.load(g_path, weights_only=False)
            if (
                isinstance(g, HeteroData)
                and model.encoder.target_node in g.node_types
                and g[model.encoder.target_node].num_nodes > 0
            ):
                if any(et[1] == "cfg" and g[et].num_edges > 0 for et in g.edge_types):
                    sha = getattr(g, "sha256", g_path.stem)
                    if "token" in g.node_types:
                        embed_file = args.embed_dir / f"{sha}.ftr"
                        if embed_file.is_file():
                            g["token"].x = torch.load(embed_file)

                    result = explain_cfg(g, g, model, device=args.device, top_k=5)
                    ranked_nodes = [n for n, _ in result["ranked"]]
                    tokens = result["mapper"].cfg_nodes_to_tokens(ranked_nodes)
                    if hasattr(result["mapper"].ast_graph, "x_vocab"):
                        token_vocab = result["mapper"].ast_graph.x_vocab
                        features = [token_vocab[t] for t in tokens]
                    else:
                        features = [str(t) for t in tokens]

                    all_features.append({"sha256": sha, "features": features})
        except Exception as e:
            LOGGER.error(
                "Failed to process graph %s: %s", g_path.name, e, exc_info=True
            )
            continue

    if not found_files:
        raise ValueError(f"No graph files found in {args.dataset_path}")

    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    with args.output_path.open("w", encoding="utf-8") as fp:
        json.dump(all_features, fp, indent=2)
    LOGGER.info(
        "Saved mined features → %s (%d samples)", args.output_path, len(all_features)
    )


def feature_mine(args: argparse.Namespace) -> None:
    """Alias for :func:`mine_features` for backward compatibility."""
    mine_features(args)


from src.graphs.dataset import GraphDataset
from src.graphs.features.cache import load_tensor, clear_memory_cache


def _available_memory_gb(device: torch.device) -> float:
    """Return approximate available memory in GB for *device*."""
    if device.type == "cuda" and torch.cuda.is_available():
        free, _ = torch.cuda.mem_get_info(device)
        return free / 1024**3
    return psutil.virtual_memory().available / 1024**3


def _auto_adjust_params(args: argparse.Namespace, device: torch.device) -> None:
    """Auto-tune batch and neighbor parameters based on free memory."""
    mem_gb = _available_memory_gb(device)
    orig_bs = args.batch_size
    orig_neigh = args.num_neighbors

    if mem_gb < 4:
        if args.batch_size > 1:
            args.batch_size = max(1, args.batch_size // 2)
        if args.num_neighbors > 1:
            args.num_neighbors = max(1, args.num_neighbors // 2)

    if args.batch_size != orig_bs or args.num_neighbors != orig_neigh:
        LOGGER.info(
            "Adjusted for %.1fGB free mem -> batch_size=%d num_neighbors=%d",
            mem_gb,
            args.batch_size,
            args.num_neighbors,
        )


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    if args.detect_anomaly:
        LOGGER.info("Enabling PyTorch Anomaly Detection.")
        torch.autograd.set_detect_anomaly(True)
    device = torch.device(args.device)
    _auto_adjust_params(args, device)
    try:
        args.func(args)  # type: ignore[misc]
    except Exception:  # pragma: no cover - pass through for visibility
        LOGGER.exception("Explainer command failed")
        raise


if __name__ == "__main__":
    main()
