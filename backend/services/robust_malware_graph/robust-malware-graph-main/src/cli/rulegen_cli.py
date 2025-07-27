#!/usr/bin/env python3
"""robust‑malware‑graph – Rule Generation CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Command‑line entry‑point that stitches together the *rulegen* package
(feature mining, PPO training, rule emission & evaluation).

Typical work‑flow
-----------------
1) **Mine discriminative features** from labeled graphs::

      python -m cli.rulegen_cli feature-mine \
             --graph-dir data/hetero \
             --labels data/splits/train.json \
             --out features.json

2) **Train the PPO rule‑agent** to convert those features into rules::

      python -m cli.rulegen_cli ppo-train \
             --train-features features.json \
             --val-features val_features.json \
             --config configs/rulegen/ppo.yaml \
             --checkpoint models/rulebank/ppo_agent.pt

3) **Generate rules** with the trained agent::

      python -m cli.rulegen_cli generate \
             --agent-checkpoint models/rulebank/ppo_agent.pt \
             --features features.json \
             --n-rules 200 \
             --rule-type yara \
             --out models/rulebank/yara/generated_rules.yar

4) **Evaluate** the resulting rules against a held‑out split::

      python -m cli.rulegen_cli evaluate \
             --rule-path models/rulebank/yara/generated_rules.yar \
             --dataset data/splits/test.json \
             --metrics auroc f1 precision recall

All sub‑commands share a unified *argparse* interface so that they can be
composed in bash pipelines or invoked programmatically.

Implementation notes
--------------------
* Graph loading relies on **torch_geometric** (mandatory project req).
* PPO agent & builders live under ``src/rulegen``.
* YAML configs are parsed with **OmegaConf** but kept optional – sensible
  defaults are hard‑coded for rapid prototyping.
"""
from __future__ import annotations

import argparse
import json
import csv
import datetime as _dt
import logging
import sys

from pathlib import Path
from typing import List, Sequence

from common.utils import set_random_seed

import pandas as pd
import torch
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from tqdm import tqdm
from src.cli.preprocessing import ensure_dir
from src.graphs.utils import prune_graph_by_selection

# ---------------------------------------------------------------------------
# Internal imports – lazily resolved to keep import‑time light‑weight.
# ---------------------------------------------------------------------------


def _lazy_imports():
    global FeatureMiner, PPORuleAgent, YaraBuilder, CapaBuilder, GraphDataset, rulegen
    from rulegen.feature_miner import FeatureMiner  # type: ignore
    from rulegen.rl_agent import PPORuleAgent  # type: ignore
    from rulegen.yara_builder import YaraBuilder  # type: ignore
    from rulegen.capa_builder import CapaBuilder  # type: ignore
    from graphs.dataset.graph_dataset import GraphDataset  # type: ignore
    import rulegen


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


def _setup_logger(verbose: bool = False, log_file: str | None = None) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    handlers: list[logging.Handler] = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))
    logging.basicConfig(
        format="[%(asctime)s] %(levelname)s – %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=level,
        handlers=handlers,
    )


def _read_json_lines(path: Path) -> List[dict]:
    """Load a ``jsonl`` file or a JSON array into a list of dicts."""
    text = path.read_text(encoding="utf-8")
    try:
        obj = json.loads(text)
        if isinstance(obj, list):
            return obj
    except json.JSONDecodeError:
        pass

    items: List[dict] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            items.append(json.loads(line))
        except json.JSONDecodeError as exc:  # pragma: no cover - simple error wrapper
            raise ValueError(
                "file must be JSON lines or a JSON array of objects"
            ) from exc
    return items


def _read_labels(path: Path) -> List[dict]:
    """Load labels from a JSONL or CSV file."""
    if path.suffix == ".csv":
        items: List[dict] = []
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    items.append({"sha256": row["sha256"], "label": int(row["label"])})
                except KeyError as exc:
                    raise ValueError(
                        "labels file must have sha256 and label columns"
                    ) from exc
        return items
    return _read_json_lines(path)


def _parse_reward_weights(text: str) -> dict:
    """Parse reward weights from JSON string or file path."""
    p = Path(text)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover - simple I/O errors
            raise argparse.ArgumentTypeError(str(exc))
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise argparse.ArgumentTypeError(f"invalid JSON: {exc}") from exc


def generate_explainer_hints(
    dataset_dir: Path,
    classifier_ckpt: str,
    device: str,
    explainer_ckpt: str | None = None,
    saliency_top_percent: float | None = None,
) -> list[str]:
    """Generate rule hints using gradients or a pretrained explainer."""

    _lazy_imports()
    from src.models.gnn.res_wrapper import RESGCLClassifier

    graphs = torch.load(dataset_dir / "dummy.pt", weights_only=False)
    classifier = RESGCLClassifier.load_pretrained(
        classifier_ckpt, map_location=device
    )
    classifier.to(device).eval()

    explainer = None
    if explainer_ckpt:
        try:
            explainer = torch.load(explainer_ckpt, map_location=device, weights_only=False)
            if hasattr(explainer, "eval"):
                explainer.eval()
        except Exception as exc:  # pragma: no cover - simple I/O errors
            raise RuntimeError(f"failed to load explainer: {exc}")

    benign_freqs = None
    if args.benign_freqs and Path(args.benign_freqs).is_file():
        benign_freqs = json.loads(Path(args.benign_freqs).read_text(encoding="utf-8"))
    miner = FeatureMiner(
        benign_freqs=benign_freqs,
        freq_threshold=args.freq_threshold,
        saliency_top_percent=saliency_top_percent,
    )
    hints: list[str] = []

    for g in graphs:
        g = g.to(device)

        if explainer is None:
            for nt in g.node_types:
                x = g[nt].get("x")
                if x is not None and torch.is_floating_point(x):
                    g[nt].x = x.clone().detach().requires_grad_(True)

            out = classifier(g, return_logits=True)
            if isinstance(out, (list, tuple)):
                out = out[0]
            out = out.view(-1).sum()
            classifier.zero_grad()
            out.backward()

            saliency: dict[str, torch.Tensor] = {}
            for nt in g.node_types:
                x = g[nt].get("x")
                if x is not None and x.grad is not None:
                    saliency[nt] = x.grad.abs().sum(dim=1).detach().cpu()
                else:
                    saliency[nt] = torch.zeros(g[nt].num_nodes)
        else:
            clf_for_embed = getattr(explainer, "model", None) or getattr(explainer, "classifier", None) or classifier
            from src.cli.explainer_train import _compute_node_embeddings

            embeds = _compute_node_embeddings(g, clf_for_embed.encoder)
            mask_prob = explainer(g, embeddings=embeds)
            if hasattr(explainer, "get_node_saliency"):
                saliency = explainer.get_node_saliency(g, mask_prob)
            else:
                saliency = mask_prob

        g_cpu = g.cpu()
        for nt in g_cpu.node_types:
            if hasattr(g_cpu[nt], "x"):
                g_cpu[nt].x = g_cpu[nt].x.detach()
        hints.extend(miner.mine(g_cpu, saliency))

    seen = set()
    return [h for h in hints if not (h in seen or seen.add(h))]


# ---------------------------------------------------------------------------
# Sub‑command implementations
# ---------------------------------------------------------------------------


def cmd_feature_mine(args: argparse.Namespace) -> None:
    """Extract candidate features across a graph corpus."""
    _lazy_imports()
    logger = logging.getLogger("feature-mine")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    graph_dir = Path(args.graph_dir).expanduser().resolve()
    out_path = Path(args.out)
    label_map: dict[str, int] | None = None
    if args.labels:
        try:
            label_items = _read_labels(Path(args.labels))
            label_map = {item["sha256"]: item["label"] for item in label_items}
        except ValueError as exc:
            logger.error(str(exc))
            raise SystemExit(1)
        logger.debug("Loaded %d labels for supervision", len(label_map))

    selector = None
    if args.selector_checkpoint:
        try:
            selector = torch.load(
                args.selector_checkpoint, map_location="cpu", weights_only=False
            )
        except FileNotFoundError:
            logger.error(
                "Selector checkpoint not found at %s", args.selector_checkpoint
            )
            raise SystemExit(1)
        except Exception as exc:  # e.g. file corrupted or incompatible
            logger.error(
                "Failed to load selector checkpoint %s: %s",
                args.selector_checkpoint,
                exc,
            )
            raise SystemExit(1)
        if hasattr(selector, "eval"):
            selector.eval()
        selector.to(device)  # Move selector to the correct device
        logger.info("Loaded selector from %s", args.selector_checkpoint)

    classifier = None
    dataset = GraphDataset(
        root=args.graph_dir,
        split="train",
        embed_dir=args.embed_dir,
    )

    # Load classifier first to get its configuration
    classifier = None
    if args.classifier_ckpt:
        try:
            from src.models import RESGCLClassifier

            classifier = RESGCLClassifier.load_from_checkpoint(
                args.classifier_ckpt, map_location="cpu"
            )
        except FileNotFoundError:
            logger.error("Classifier checkpoint not found at %s", args.classifier_ckpt)
            raise SystemExit(1)
        except Exception as e:
            logger.error(f"Failed to load classifier: {e}")
            raise SystemExit(1)

    # Collect metadata from the current dataset to get the correct input dimensions
    from src.graphs.dataset.graph_dataset import collect_dataset_metadata

    attr_dim = (
        classifier.encoder.attr_dim
        if (classifier and hasattr(classifier, "encoder"))
        else 32
    )
    _, in_dims, _, attr_names, vocab = collect_dataset_metadata(
        [dataset], attr_dim=attr_dim
    )
    logger.info("Collected metadata from the dataset: in_dims=%s", in_dims)

    projection_layer = None
    if classifier and selector:
        try:
            # Re-initialize input dimensions to match the current dataset
            vocab_size = max(vocab.values()) + 1 if vocab else 0
            classifier.reinit_input_dims(
                in_dims=in_dims, attr_names=attr_names, vocab_size=vocab_size
            )
            logger.info(
                "Re-initialized classifier input dimensions based on the dataset."
            )

            # CRITICAL: Synchronize the selector's encoder with the re-initialized one from the classifier
            if hasattr(selector, "model") and hasattr(selector.model, "encoder"):
                selector.model.encoder = classifier.encoder
                logger.info(
                    "Synchronized selector's encoder with the re-initialized classifier's encoder."
                )

                # If embedding dimensions mismatch, create a projection layer
                new_embed_dim = classifier.encoder.out_proj.in_features
                if (
                    hasattr(selector, "embed_dim")
                    and selector.embed_dim != new_embed_dim
                ):
                    logger.info(
                        f"Embedding dimension mismatch detected. Creating projection layer: {new_embed_dim} -> {selector.embed_dim}"
                    )
                    projection_layer = torch.nn.Linear(
                        new_embed_dim, selector.embed_dim
                    ).to(device)

        except Exception as e:
            logger.error(
                f"Failed to re-initialize classifier or create projection layer: {e}"
            )
            raise SystemExit(1)

    miner = FeatureMiner(
        freq_threshold=args.freq_threshold,
        saliency_top_percent=args.saliency_top_percent,
    )

    all_features: List[dict] = []
    num_features_per_graph: List[int] = []
    missing_label_shas: List[str] = []
    labels_df = pd.read_csv(args.labels).set_index("sha256") if args.labels else None

    for i in tqdm(range(len(dataset)), desc="Mining features"):
        item = dataset[i]
        if isinstance(item, tuple) and len(item) == 3:
            graph, ds_label, sha = item
        else:  # backward compatibility
            graph, ds_label, sha = item, None, getattr(item, "sha256", "unknown")

        label = labels_df.loc[sha, "label"] if sha in labels_df.index else ds_label

        if label is None:
            logger.debug("No label found for SHA %s", sha)
            missing_label_shas.append(sha)

        if selector:
            with torch.no_grad():
                embeds = None
                # Always compute embeddings using the (potentially re-initialized) classifier's encoder
                if classifier is not None:
                    from src.cli.explainer_train import _compute_node_embeddings

                    embeds = _compute_node_embeddings(graph, classifier.encoder)

                if embeds is not None:
                    # If a projection layer was created, apply it
                    if projection_layer:
                        projected_embeds = {}
                        for node_type, emb in embeds.items():
                            projected_embeds[node_type] = projection_layer(emb)
                        embeds = projected_embeds

                    # Assign final embeddings to graph.x_dict for the selector
                    graph.x_dict = embeds

                # Move graph to the correct device before passing to selector
                graph = graph.to(device)

                selection = selector(graph, embeddings=embeds)

                if isinstance(selection, tuple):
                    selection, *_ = selection

                # Convert edge mask to node saliency
                node_saliency = selector.get_node_saliency(graph, selection)

                # Mine features BEFORE pruning the graph
                features = miner.mine(graph, saliency=node_saliency)

                # Pruning is not strictly necessary for mining, but can be useful for other purposes
                # graph = prune_graph_by_selection(graph, selection, threshold=0.01)
        else:
            features = miner.mine(graph, saliency=None)
        # Handle label type for JSON serialization
        final_label = None
        if label is not None:
            # If label is a pandas Series (due to duplicate SHAs), take the first value
            if isinstance(label, pd.Series):
                if not label.empty:
                    final_label = int(label.iloc[0])
            else:  # It's likely a numpy/python scalar
                final_label = int(label)

        entry = {"sha256": sha, "label": final_label, "features": features}
        all_features.append(entry)
        if i == 0 and features:
            logger.info(f"DEBUG: Graph 0 - Appended entry to all_features: {entry}")

        num_features_per_graph.append(len(features))

    avg_features = (
        sum(num_features_per_graph) / len(num_features_per_graph)
        if num_features_per_graph
        else 0
    )

    # Add a final check before writing the file
    features_found = sum(1 for item in all_features if item.get("features"))
    logger.info(
        f"DEBUG: Final check before saving - {features_found} out of {len(all_features)} entries have features."
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fp:
        json.dump(all_features, fp, indent=2)
    logger.info(
        "Saved mined features to %s (%d samples, avg %.2f features/graph)",
        out_path,
        len(all_features),
        avg_features,
    )

    # Post-save verification to ensure file content is correct
    try:
        with out_path.open("r", encoding="utf-8") as f:
            saved_data = json.load(f)
        if saved_data:
            num_features_from_file = [
                len(item.get("features", [])) for item in saved_data
            ]
            avg_from_file = (
                sum(num_features_from_file) / len(num_features_from_file)
                if num_features_from_file
                else 0
            )
            logger.info(
                f"DEBUG: Post-save verification of {out_path}: avg {avg_from_file:.2f} features/graph from file."
            )
        else:
            logger.warning(
                f"DEBUG: Post-save verification: {out_path} is empty or invalid."
            )
    except Exception as e:
        logger.error(
            f"DEBUG: Post-save verification failed while reading {out_path}: {e}"
        )

    if missing_label_shas:
        logger.info("Could not find labels for %d files.", len(missing_label_shas))
        missing_labels_path = Path("missing_labels.csv")
        with missing_labels_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["sha256"])
            for sha in missing_label_shas:
                writer.writerow([sha])
        logger.info(
            "Saved list of files with missing labels to %s", missing_labels_path
        )


def cmd_ppo_train(args: argparse.Namespace) -> None:
    """Train a PPO agent to convert features into high‑quality rules."""
    logger = logging.getLogger("ppo-train")

    from omegaconf import OmegaConf

    dataset_dir = Path(args.dataset_dir).expanduser().resolve()
    if (
        not (dataset_dir / "clean.pt").exists()
        or not (dataset_dir / "dummy.pt").exists()
    ):
        logger.error("Dataset directory missing required files clean.pt and dummy.pt")
        raise SystemExit(1)

    _lazy_imports()

    # ------------------------------------------------------------------
    # 1) Configuration & device selection
    # ------------------------------------------------------------------
    cfg = OmegaConf.load(args.config) if args.config else OmegaConf.create()
    device = torch.device(
        "cuda" if torch.cuda.is_available() and not args.cpu else "cpu"
    )
    policy_net = cfg.get("model", {}).get("policy_net", "gru")
    if getattr(args, "policy", None):
        policy_net = args.policy
    tok = None
    if str(policy_net).startswith("gpt2"):
        try:
            from transformers import AutoTokenizer
        except Exception as exc:  # pragma: no cover - optional dep
            logger.error("transformers 라이브러리가 필요합니다: %s", exc)
            raise
        tok = AutoTokenizer.from_pretrained(policy_net)

    logger.info("Training on %s", device)

    # ------------------------------------------------------------------
    # 2) Data loading (currently unused but kept for compatibility)
    # ------------------------------------------------------------------
    train_feats = _read_json_lines(Path(args.train_features))
    val_feats = _read_json_lines(Path(args.val_features)) if args.val_features else []

    val_hint_feats: list[str] = []
    for item in val_feats:
        fs = item.get("features")
        if isinstance(fs, list):
            val_hint_feats.extend(str(f) for f in fs)
    seen = set()
    val_hint_feats = [f for f in val_hint_feats if not (f in seen or seen.add(f))]

    hint_feats = None
    if getattr(args, "hint_file", None):
        hint_feats = _read_json_lines(Path(args.hint_file))
    elif getattr(args, "use_explainer_hints", False):
        feats: list[str] = []
        for item in train_feats:
            fs = item.get("features")
            if isinstance(fs, list):
                feats.extend(str(f) for f in fs)
        # deduplicate while preserving order
        seen = set()
        hint_feats = [f for f in feats if not (f in seen or seen.add(f))]
    elif getattr(args, "hint_features", None):
        hint_feats = _read_json_lines(Path(args.hint_features))
    elif getattr(args, "generate_hints_from_explainer", False):
        if not getattr(args, "explainer_checkpoint", None):
            logger.error("--generate-hints-from-explainer requires --explainer-checkpoint")
            raise SystemExit(1)
        try:
            hint_feats = generate_explainer_hints(
                dataset_dir,
                args.classifier_checkpoint,
                args.classifier_device,
                args.explainer_checkpoint,
                saliency_top_percent=args.saliency_top_percent,
            )
        except Exception as exc:
            logger.error("Failed to generate explainer hints: %s", exc)
            raise SystemExit(1)
    else:
        # Use train features as hints by default for vocab consistency
        feats: list[str] = []
        for item in train_feats:
            fs = item.get("features")
            if isinstance(fs, list):
                feats.extend(str(f) for f in fs)
        # deduplicate while preserving order
        seen = set()
        hint_feats = [f for f in feats if not (f in seen or seen.add(f))]

    # Collect token vocabulary from hint features
    from collections import Counter

    token_counter: Counter[str] = Counter()
    try:
        rule_tokenize = rulegen.rl_env.RuleGenEnv._rule_tokenize  # type: ignore[attr-defined]
    except AttributeError:  # fallback in tests where rulegen.rl_env is stubbed

        def rule_tokenize(text: str) -> list[str]:
            return (
                text.replace("(", " ( ").replace(")", " ) ").replace(":", " : ").split()
            )

    for f in hint_feats or []:
        for tok in rule_tokenize(str(f)):
            token_counter[tok] += 1
            tok_lower = tok.lower()
            if "file" in tok_lower:
                token_counter["<FileOp>"] += 1
            if "reg" in tok_lower:
                token_counter["<RegistryOp>"] += 1

    if args.max_vocab:
        token_list = [t for t, _ in token_counter.most_common(args.max_vocab)]
    else:
        token_list = sorted(token_counter)
    hint_tokens = token_list

    # ------------------------------------------------------------------
    # 3) Environment & agent instantiation
    # ------------------------------------------------------------------
    env_cfg = cfg.get("env", {})
    curriculum_cfg = cfg.get("curriculum", {})
    adjust_cfg = env_cfg.get("weight_adjust", {})
    auto_adjust_cfg = cfg.get("auto_adjust")
    if auto_adjust_cfg:
        auto_adjust_cfg = OmegaConf.to_container(auto_adjust_cfg, resolve=True)
    else:
        auto_adjust_cfg = None

    phase_sched = None
    if curriculum_cfg:
        phase_sched = OmegaConf.to_container(curriculum_cfg, resolve=True)
        phase1 = phase_sched.get("phase1", {})
        rw = phase1.get("reward_weights", env_cfg.get("reward_weights"))
        fps = phase1.get("fp_penalty_start", env_cfg.get("fp_penalty_start", 0.01))
        fpe = phase1.get("fp_penalty_end", env_cfg.get("fp_penalty_end", 0.5))
        fpd = phase1.get("fp_penalty_delay", env_cfg.get("fp_penalty_delay", 0))
        rlps = phase1.get(
            "rule_len_penalty_start",
            env_cfg.get("rule_len_penalty_start")
        )
        rlpe = phase1.get(
            "rule_len_penalty_end",
            env_cfg.get("rule_len_penalty_end")
        )
        rlstep = int(
            phase1.get(
                "rule_len_steps",
                env_cfg.get("rule_len_steps", env_cfg.get("curriculum_steps", 20000)),
            )
        )
        rldelay = int(
            phase1.get(
                "rule_len_penalty_delay",
                env_cfg.get("rule_len_penalty_delay", 0),
            )
        )
    else:
        rw = args.reward_weights or env_cfg.get("reward_weights")
        fps = env_cfg.get("fp_penalty_start", 0.01)
        fpe = env_cfg.get("fp_penalty_end", 0.5)
        fpd = env_cfg.get("fp_penalty_delay", 0)
        rlps = (
            args.rule_len_penalty_start
            if args.rule_len_penalty_start is not None
            else env_cfg.get("rule_len_penalty_start")
        )
        rlpe = (
            args.rule_len_penalty_end
            if args.rule_len_penalty_end is not None
            else env_cfg.get("rule_len_penalty_end")
        )
        rlstep = int(
            args.rule_len_steps
            if args.rule_len_steps is not None
            else env_cfg.get("rule_len_steps", env_cfg.get("curriculum_steps", 20000))
        )
        rldelay = int(
            args.rule_len_penalty_delay
            if args.rule_len_penalty_delay is not None
            else env_cfg.get("rule_len_penalty_delay", 0)
        )

    env = rulegen.make_env(
        rule_type=env_cfg.get("mode", "yara"),
        max_len=int(env_cfg.get("max_tokens", 512)),
        dataset_dir=dataset_dir,
        device=device,
        hint_features=hint_tokens,
        classifier_ckpt=args.classifier_checkpoint,
        classifier_device=args.classifier_device,
        seed=args.seed,
        reward_weights=rw,
        fp_penalty_start=fps,
        fp_penalty_end=fpe,
        fp_penalty_delay=int(fpd),
        curriculum_steps=int(env_cfg.get("curriculum_steps", 20000)),
        rule_len_penalty_start=rlps,
        rule_len_penalty_end=rlpe,
        rule_len_steps=rlstep,
        rule_len_penalty_delay=rldelay,
        off_target_penalty=float(
            args.off_target_penalty
            if args.off_target_penalty is not None
            else env_cfg.get("off_target_penalty", 0.25)
        ),
        off_target_penalty_start=(
            args.off_target_penalty_start
            if args.off_target_penalty_start is not None
            else env_cfg.get("off_target_penalty_start")
        ),
        off_target_penalty_end=(
            args.off_target_penalty_end
            if args.off_target_penalty_end is not None
            else env_cfg.get("off_target_penalty_end")
        ),
        off_target_steps=int(
            args.off_target_steps
            if args.off_target_steps is not None
            else env_cfg.get(
                "off_target_steps",
                env_cfg.get("curriculum_steps", 20000),
            )
        ),
        no_tp_penalty=float(
            args.no_tp_penalty
            if args.no_tp_penalty is not None
            else env_cfg.get("no_tp_penalty", 1.0)
        ),
        improve_bonus=float(env_cfg.get("improve_bonus", 0.2)),
        use_lookahead=getattr(args, "use_lookahead", False),
        use_shaping=getattr(args, "use_shaping", False),
        single_target_mode=getattr(args, "single_target_mode", False),
        meta_path=getattr(args, "meta_path", None),
        tokenizer=policy_net,
        max_hint_tokens=getattr(args, "max_hint_tokens", None),
        core_tokens=hint_tokens if getattr(args, "use_shaping", False) else None,
    )

    adjust_interval = int(adjust_cfg.get("interval", 0))
    delta_dummy = float(adjust_cfg.get("delta_f1_dummy", 0.0))
    delta_clean = float(adjust_cfg.get("delta_f1_clean", 0.0))
    next_adjust = adjust_interval if adjust_interval > 0 else None
    sched_cfg = cfg.get("scheduler", {})
    sched_name = sched_cfg.get("name")
    total_steps = int(sched_cfg.get("total_updates", args.epochs))
    ppo_cfg = cfg.get("ppo", {})
    agent_kwargs = {
        "use_amp": getattr(args, "amp", False),
        "checkpoint_layers": getattr(args, "grad_checkpoint", False),
        "load_4bit": getattr(args, "load_4bit", False),
        "load_8bit": getattr(args, "load_8bit", False),
        "n_steps": args.num_steps,
        "minibatch_size": args.minibatch_size,
        "n_epochs": args.ppo_epochs,
        "accum_steps": args.accum_steps,
        "use_hint": True,
    }
    if "entropy_coef" in ppo_cfg:
        agent_kwargs["entropy_coef"] = float(ppo_cfg["entropy_coef"])
    if "entropy_coef_final" in ppo_cfg:
        agent_kwargs["entropy_coef_final"] = float(ppo_cfg["entropy_coef_final"])
    if "entropy_coef_steps" in ppo_cfg:
        agent_kwargs["entropy_coef_steps"] = int(ppo_cfg["entropy_coef_steps"])
    if any(
        getattr(args, n) is not None for n in ["lora_r", "lora_alpha", "lora_dropout"]
    ):
        agent_kwargs["lora_cfg"] = {
            "r": args.lora_r,
            "alpha": args.lora_alpha,
            "dropout": args.lora_dropout,
        }
    try:
        agent = rulegen.load_agent(
            env=env,
            policy_net=policy_net,
            schedule_type=sched_name,
            total_updates=total_steps,
            seed=args.seed,
            constraint_thresh=args.constraint_thresh,
            lagrange_lr=args.lagrange_lr,
            agent_kwargs=agent_kwargs,
        )
    except TypeError:
        # backward compatibility with older API in tests
        agent = rulegen.load_agent(env=env)
    log_interval = int(cfg.get("checkpoint", {}).get("save_every_updates", 10_000))

    def _evaluate_agent(
        agent: PPORuleAgent,
        env: rulegen.RuleGenEnv,
        n_rules: int,
        *,
        hint_features: list[str] | None = None,
    ) -> dict:
        builder = (
            YaraBuilder(
                condition_type=args.condition_type,
                group_percentage=args.group_percentage,
                group_min_count=args.group_min_count,
            )
            if getattr(env, "rule_type", "yara") == "yara"
            else CapaBuilder()
        )
        f1_c = f1_d = r_sum = 0.0
        orig_hints = getattr(env, "hint_features", None)
        if hint_features is not None and hasattr(env, "hint_features"):
            env.hint_features = hint_features
        if not hasattr(agent, "sample_rules") or not hasattr(env, "_compute_reward"):
            return {"f1_clean": 0.0, "f1_dummy": 0.0, "reward": 0.0}
        rules = agent.sample_rules(n=n_rules)
        for toks in rules:
            rule_text = builder.build(toks)
            reward, metrics, _ = env._compute_reward(rule_text, update_stats=False)
            f1_c += float(metrics.get("f1_clean", 0.0))
            f1_d += float(metrics.get("f1_dummy", 0.0))
            r_sum += float(reward)
        n = max(len(rules), 1)
        if hint_features is not None and hasattr(env, "hint_features"):
            env.hint_features = orig_hints
        return {
            "f1_clean": f1_c / n,
            "f1_dummy": f1_d / n,
            "reward": r_sum / n,
        }

    eval_interval = int(getattr(args, "eval_interval", total_steps))
    n_eval_rules = int(getattr(args, "num_eval_rules", 5))
    history: list[tuple[int, float]] = []
    val_history: list[tuple[int, float, float, float]] = []

    def _plot_history() -> None:
        if not args.plot_path:
            return
        steps, rets = zip(*history) if history else ([], [])
        val_steps = [v[0] for v in val_history]
        val_rewards = [v[3] for v in val_history]
        out = Path(args.plot_path)
        ensure_dir(out.parent)
        plt.figure()
        if steps:
            plt.plot(steps, rets, label="train avg return")
        if val_steps:
            plt.plot(val_steps, val_rewards, label="val reward")
        plt.xlabel("Step")
        plt.ylabel("Reward")
        plt.legend()
        plt.tight_layout()
        plt.savefig(out)
        plt.close()
        logger.info("Training curve saved → %s", out)

    for step in range(0, total_steps, eval_interval):
        seg = min(eval_interval, total_steps - step)
        history.extend(
            agent.train(
                total_timesteps=seg,
                log_interval=log_interval,
                save_path=args.checkpoint,
                phase_schedule=phase_sched,
                auto_adjust=auto_adjust_cfg,
            )
        )
        if next_adjust is not None:
            while env.total_steps >= next_adjust:
                env.update_reward_weights(
                    f1_dummy=env.reward_weights.get("f1_dummy", 0.0) + delta_dummy,
                    f1_clean=env.reward_weights.get("f1_clean", 0.0) + delta_clean,
                )
                logger.info(
                    "Adjusted reward weights to %s at step %d",
                    env.reward_weights,
                    next_adjust,
                )
                next_adjust += adjust_interval
        metrics = _evaluate_agent(
            agent,
            env,
            n_eval_rules,
            hint_features=val_hint_feats if val_hint_feats else None,
        )
        if args.eval_log:
            with Path(args.eval_log).open("a", encoding="utf-8") as fp:
                for entry in env.get_rule_eval_history():
                    fp.write(json.dumps(entry) + "\n")
        val_history.append(
            (step + seg, metrics["f1_clean"], metrics["f1_dummy"], metrics["reward"])
        )
        logger.info(
            "Validation @%d: f1_clean=%.4f f1_dummy=%.4f reward=%.4f",
            step + seg,
            metrics["f1_clean"],
            metrics["f1_dummy"],
            metrics["reward"],
        )
        _plot_history()

        if args.checkpoint:
            ckpt_path = Path(args.checkpoint)
            ckpt_path.parent.mkdir(parents=True, exist_ok=True)
            agent.save(ckpt_path)
            step_path = ckpt_path.with_name(
                f"{ckpt_path.stem}_step{step + seg:04d}{ckpt_path.suffix}"
            )
            agent.save(step_path)
            logger.info("Checkpoint saved → %s", step_path)

    _plot_history()

    if args.eval_log:
        with Path(args.eval_log).open("a", encoding="utf-8") as fp:
            for entry in env.get_rule_eval_history():
                fp.write(json.dumps(entry) + "\n")

    if args.checkpoint:
        Path(args.checkpoint).parent.mkdir(parents=True, exist_ok=True)
        agent.save(args.checkpoint)
        logger.info("Agent checkpoint saved → %s", args.checkpoint)

        # NOTE: 학습에 사용된 설정 파일과 생성된 예시 룰을
        #       동일한 디렉터리 아래에 보관하면 관리가 용이하다.

        builder = YaraBuilder(
            condition_type=args.condition_type,
            group_percentage=args.group_percentage,
            group_min_count=args.group_min_count,
        )
        sample_tokens = agent.sample_rules(n=1)[0]
        sample_rule = builder.build(sample_tokens)
        out_dir = Path("results")
        ensure_dir(out_dir)
        (out_dir / "sample_rule.yar").write_text(sample_rule, encoding="utf-8")
        logger.info("Sample rule saved → %s", out_dir / "sample_rule.yar")


RULE_TYPE_BUILDERS = {
    "yara": YaraBuilder if "YaraBuilder" in globals() else None,
    "capa": CapaBuilder if "CapaBuilder" in globals() else None,
}


def cmd_generate(args: argparse.Namespace) -> None:
    """Generate a batch of rules with a trained agent."""
    _lazy_imports()
    logger = logging.getLogger("generate")

    RULE_TYPE_BUILDERS = {
        "yara": YaraBuilder if "YaraBuilder" in globals() else None,
        "capa": CapaBuilder if "CapaBuilder" in globals() else None,
    }

    if args.rule_type not in RULE_TYPE_BUILDERS:
        raise SystemExit(f"[!] Unsupported rule‑type: {args.rule_type}")

    builder_cls = RULE_TYPE_BUILDERS[args.rule_type]
    if builder_cls is None:
        raise SystemExit(f"[!] Missing builder implementation for {args.rule_type}")

    # Load features to build vocabulary
    train_feats = _read_json_lines(Path(args.features))
    feats: list[str] = []
    for item in train_feats:
        fs = item.get("features")
        if isinstance(fs, list):
            feats.extend(str(f) for f in fs)
    # deduplicate while preserving order
    seen = set()
    hint_feats = [f for f in feats if not (f in seen or seen.add(f))]

    if args.target_graph:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp_dir:
            g = torch.load(
                Path(args.target_graph), map_location="cpu", weights_only=False
            )
            try:
                g.file_path = str(args.target_graph)
            except Exception:
                pass

            tmp_path = Path(tmp_dir)
            torch.save([], tmp_path / "clean.pt")
            torch.save([g], tmp_path / "dummy.pt")

            env = rulegen.make_env(
                dataset_dir=tmp_path,
                device="cpu",
                hint_features=hint_feats,
                seed=args.seed,
                reward_weights=args.reward_weights,
                fp_penalty_delay=0,
                single_target_mode=True,
                off_target_penalty=args.off_target_penalty,
                off_target_penalty_start=args.off_target_penalty_start,
                off_target_penalty_end=args.off_target_penalty_end,
                off_target_steps=args.off_target_steps,
                no_tp_penalty=args.no_tp_penalty if args.no_tp_penalty is not None else 1.0,
                improve_bonus=0.2,
            )
            agent = PPORuleAgent(env, seed=args.seed, use_hint=True)
            agent.load(args.agent_checkpoint)

            builder = builder_cls()  # type: ignore[call-arg]
            rule = agent.sample_rules(n=1, temperature=args.temperature)[0]
            rule_text = builder.build(rule)
            print(rule_text)
    else:
        # Load agent with default dataset
        env = rulegen.make_env(
            dataset_dir=Path("data/rulegen_dataset"),
            device="cpu",
            hint_features=hint_feats,
            seed=args.seed,
            reward_weights=args.reward_weights,
            fp_penalty_delay=0,
            single_target_mode=getattr(args, "single_target_mode", False),
            off_target_penalty=args.off_target_penalty,
            off_target_penalty_start=args.off_target_penalty_start,
            off_target_penalty_end=args.off_target_penalty_end,
            off_target_steps=args.off_target_steps,
            no_tp_penalty=args.no_tp_penalty if args.no_tp_penalty is not None else 1.0,
            improve_bonus=0.2,
        )
        agent = PPORuleAgent(env, seed=args.seed, use_hint=True)
        agent.load(args.agent_checkpoint)

        builder = builder_cls()  # type: ignore[call-arg]
        rules = agent.sample_rules(n=args.n_rules, temperature=args.temperature)
        rules_text = "\n\n".join(builder.build(r) for r in rules)

        if args.out:
            out_path = Path(args.out)
        else:
            ts = _dt.datetime.utcnow().strftime("%Y%m%d%H%M%S")
            out_dir = Path("models") / "rulebank" / args.rule_type
            default_ext = ".yar"
            if args.rule_type == "capa":
                default_ext = ".yml"
            out_path = out_dir / f"generated_{ts}{default_ext}"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as fp:
            fp.write(rules_text)
        logger.info(
            "Generated %d %s rules → %s", len(rules), args.rule_type.upper(), out_path
        )


def _evaluate_metrics(preds: Sequence[int], labels: Sequence[int], metrics: List[str]):
    from sklearn import metrics as skm

    results = {}
    preds_arr = torch.tensor(preds)
    labels_arr = torch.tensor(labels)

    for m in metrics:
        if m == "auroc":
            results["auroc"] = float(skm.roc_auc_score(labels_arr, preds_arr))  # type: ignore[arg-type]
        elif m in {"f1", "precision", "recall"}:
            results[m] = float(getattr(skm, f"{m}_score")(labels_arr, preds_arr))  # type: ignore[arg-type]
        else:
            raise ValueError(f"Unsupported metric: {m}")
    return results


def cmd_evaluate(args: argparse.Namespace) -> None:
    """Evaluate an existing rule bank on a labeled test set."""
    _lazy_imports()
    logger = logging.getLogger("evaluate")

    # Load dataset labels
    samples = _read_json_lines(Path(args.dataset))
    sha_to_label = {x["sha256"]: x["label"] for x in samples}

    # Load rules
    rule_path = Path(args.rule_path)
    if rule_path.suffix.lower().endswith(".yar"):
        builder = YaraBuilder()
    elif rule_path.suffix.lower().endswith(".yml"):
        builder = CapaBuilder()
    else:
        raise SystemExit("[!] Could not infer rule type from extension")
    builder.load(rule_path)

    preds, labels = [], []
    for sha, label in tqdm(sha_to_label.items(), desc="Scanning"):
        # Inference: scan file on‑the‑fly to avoid massive RAM usage.
        # The builder is responsible for spawning yara/capa processes under‑the‑hood.
        match = builder.match_file(Path(args.sample_dir) / f"{sha}")
        preds.append(int(match))
        labels.append(int(label))

    results = _evaluate_metrics(preds, labels, args.metrics)
    for k, v in results.items():
        logger.info("%s = %.4f", k.upper(), v)

    log_path = Path("evaluation_logs.csv")
    header = ["timestamp", "rule_file", "n_rules", "n_samples", *args.metrics]
    if not log_path.exists():
        with log_path.open("w", newline="", encoding="utf-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(header)
    with log_path.open("a", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        row = [
            _dt.datetime.utcnow().isoformat(),
            str(rule_path),
            getattr(builder, "rule_count", 0),
            len(samples),
            *(results.get(m, 0.0) for m in args.metrics),
        ]
        writer.writerow(row)


def _extract_fp_updates(log_path: Path, threshold: float = 0.5) -> dict[str, int]:
    """Collect tokens from rules with high false positive rate."""

    if not log_path.is_file():
        return {}
    from rulegen.rl_env import RuleGenEnv

    counts: dict[str, int] = {}
    for line in log_path.read_text().splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        if float(entry.get("fp_rate", 0.0)) < threshold:
            continue
        for tok in RuleGenEnv._rule_tokenize(entry.get("rule", "")):
            counts[tok] = counts.get(tok, 0) + 1
    return counts


def cmd_pipeline(args: argparse.Namespace) -> None:
    """Run feature mining and PPO training iteratively updating benign freqs."""

    work = Path(args.work_dir)
    work.mkdir(parents=True, exist_ok=True)
    freq_path = Path(args.benign_freqs)

    for i in range(args.iterations):
        feat_path = work / f"features_{i}.json"
        fm_args = argparse.Namespace(
            graph_dir=args.graph_dir,
            labels=args.labels,
            embed_dir=None,
            out=str(feat_path),
            selector_checkpoint=None,
            classifier_ckpt=None,
            benign_freqs=str(freq_path) if freq_path.exists() else None,
            freq_threshold=args.freq_threshold,
            saliency_top_percent=None,
        )
        cmd_feature_mine(fm_args)

        log_file = work / f"eval_{i}.jsonl"
        train_args = argparse.Namespace(
            train_features=str(feat_path),
            val_features=None,
            dataset_dir=args.dataset_dir,
            config=args.config,
            epochs=args.epochs,
            checkpoint=str(work / f"agent_{i}.pt"),
            cpu=args.cpu,
            eval_log=str(log_file),
        )
        cmd_ppo_train(train_args)

        updates = _extract_fp_updates(log_file, args.fp_threshold)
        if updates:
            if freq_path.is_file():
                data = json.loads(freq_path.read_text())
            else:
                data = {}
            for k, v in updates.items():
                data[k] = data.get(k, 0) + v
            freq_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def cmd_build_dataset(args: argparse.Namespace) -> None:
    """Convert labeled graphs into PPO dataset format."""
    from rulegen.build_dataset import build_dataset

    logger = logging.getLogger("build-dataset")
    build_dataset(
        hetero_dir=Path(args.hetero_dir).expanduser().resolve(),
        labels=Path(args.labels).expanduser().resolve(),
        out_dir=Path(args.out_dir).expanduser().resolve(),
        metadata_vocab=(
            Path(args.metadata_vocab).expanduser().resolve()
            if args.metadata_vocab
            else None
        ),
        meta_path=(
            Path(args.meta_path).expanduser().resolve() if args.meta_path else None
        ),
        clean_label=args.clean_label,
        dummy_label=args.dummy_label,
    )


# ---------------------------------------------------------------------------
# Argument parser setup
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rulegen_cli",
        description="Rule generation pipeline for robust‑malware‑graph project",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="verbose logging")
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility",
    )

    sub = parser.add_subparsers(dest="command", required=True, metavar="<command>")

    # ------------------- feature‑mine ------------------- #
    fm = sub.add_parser("feature-mine", help="Mine discriminative graph features")
    fm.add_argument(
        "--graph-dir",
        required=True,
        help="Dataset root with train/graphs/, val/graphs/, etc.",
    )
    fm.add_argument(
        "--labels",
        help="Optional labels file (.jsonl or .csv) with sha256 and label",
    )
    fm.add_argument("--embed-dir", help="Directory containing .ftr token embeddings")
    fm.add_argument(
        "--out", required=True, help="Output path for mined features (.json)"
    )
    fm.add_argument(
        "--selector-checkpoint",
        type=Path,
        help="Optional selector checkpoint to compute node saliency",
    )
    fm.add_argument(
        "--classifier-ckpt",
        type=Path,
        help="Classifier checkpoint used during explainer training",
    )
    fm.add_argument("--benign-freqs", type=Path, help="JSON with benign feature frequencies")
    fm.add_argument(
        "--freq-threshold",
        type=float,
        default=10.0,
        help="Frequency threshold for filtering",
    )
    fm.add_argument(
        "--saliency-top-percent",
        type=float,
        default=None,
        help="Limit nodes by cumulative saliency percentage",
    )
    fm.set_defaults(func=cmd_feature_mine)

    # ------------------- build-dataset ------------------- #
    bd = sub.add_parser("build-dataset", help="Convert graphs to PPO dataset")
    bd.add_argument("--hetero-dir", required=True, help="Directory of graph files")
    bd.add_argument("--labels", required=True, help="CSV or JSONL (sha256,label)")
    bd.add_argument("--out-dir", required=True, help="Output directory")
    bd.add_argument("--metadata-vocab", help="metadata_vocab.json path")
    bd.add_argument("--meta-path", help="Path to encoder meta snapshot (.meta.pkl)")
    bd.add_argument("--clean-label", type=int, default=0, help="Label for clean graphs")
    bd.add_argument("--dummy-label", type=int, default=1, help="Label for dummy graphs")
    bd.set_defaults(func=cmd_build_dataset)

    # ------------------- ppo‑train ------------------- #
    pt = sub.add_parser("ppo-train", help="Train PPO rule agent")
    pt.add_argument("--train-features", required=True, help="JSONL mined features")
    pt.add_argument("--val-features", help="Validation feature file (optional)")
    hint_group = pt.add_mutually_exclusive_group()
    hint_group.add_argument("--hint-file", help="Path to JSONL/JSON array with hint features")
    hint_group.add_argument("--hint-features", help="Optional JSON with rule hints")
    hint_group.add_argument(
        "--use-explainer-hints",
        action="store_true",
        help="Use mined train features as rule hints",
    )
    hint_group.add_argument(
        "--generate-hints-from-explainer",
        action="store_true",
        help=(
            "학습 시작 전 classifier explainer로 각 악성 샘플의 saliency를 계산하여 "
            "힌트를 자동 생성 (--explainer-checkpoint와 함께 사용)"
        ),
    )
    pt.add_argument(
        "--explainer-checkpoint",
        help="Pretrained explainer checkpoint used with --generate-hints-from-explainer",
    )
    pt.add_argument("--config", help="Path to PPO YAML config (Hydra style)")
    pt.add_argument("--dataset-dir", required=True, help="Path to env dataset")
    pt.add_argument("--meta-path", help="Path to encoder meta snapshot (.meta.pkl)")
    pt.add_argument(
        "--classifier-checkpoint",
        default="models/gnn/res_gcl.pt",
        help="Classifier checkpoint used for reward computation. Alias: --classifier-ckpt",
        dest="classifier_checkpoint",
    )
    pt.add_argument(
        "--classifier-ckpt",
        help=argparse.SUPPRESS,
        dest="classifier_checkpoint",
    )
    pt.add_argument(
        "--classifier-device",
        default="cpu",
        help="Device for loading the reward classifier",
    )
    pt.add_argument(
        "--policy",
        help="Policy network architecture: 'gru', 'attn' or GPT model name",
    )
    pt.add_argument(
        "--condition-type",
        choices=["any", "all", "percentage", "combo"],
        default="any",
        help="Condition aggregation strategy ('any', 'all', 'percentage', 'combo'), defaults to 'any'",
    )
    pt.add_argument("--group-percentage", type=int, help="combo mode: percentage of each group")
    pt.add_argument("--group-min-count", type=int, help="combo mode: minimum matches per group")
    pt.add_argument("--epochs", type=int, default=30, help="Training epochs")
    pt.add_argument(
        "--eval-interval",
        type=int,
        default=10_000,
        help="Number of steps between validations",
    )
    pt.add_argument(
        "--num-eval-rules",
        type=int,
        default=5,
        help="How many rules to sample for validation",
    )
    pt.add_argument(
        "--max-vocab",
        type=int,
        help="Keep only the N most frequent tokens from hints",
    )
    pt.add_argument(
        "--max-hint-tokens",
        type=int,
        help="Maximum number of hint tokens to prepend to observations",
    )
    pt.add_argument("--checkpoint", help="Output checkpoint path (.pt)")
    pt.add_argument("--plot-path", type=Path, help="Save training curve PNG")
    pt.add_argument(
        "--eval-log",
        type=Path,
        help="Path to JSONL file for rule evaluation logs",
    )
    pt.add_argument(
        "--reward-weights",
        type=_parse_reward_weights,
        help="JSON mapping or path with reward weights",
    )
    pt.add_argument(
        "--constraint-thresh",
        type=float,
        default=0.5,
        help="Constraint threshold for f1_clean",
    )
    pt.add_argument(
        "--lagrange-lr",
        type=float,
        default=0.05,
        help="Lagrange multiplier learning rate",
    )
    pt.add_argument(
        "--use-lookahead",
        action="store_true",
        help="Use classifier probability as interim reward for partial rules",
    )
    pt.add_argument(
        "--use-shaping",
        action="store_true",
        help="Enable potential based reward shaping using hint tokens as core tokens",
    )
    pt.add_argument(
        "--single-target-mode",
        action="store_true",
        help="Use a single random dummy graph as target each episode",
    )
    pt.add_argument(
        "--off-target-penalty",
        type=float,
        help="Penalty per off-target match in single-target mode",
    )
    pt.add_argument(
        "--off-target-penalty-start",
        type=float,
        help="Initial weight for off-target penalty",
    )
    pt.add_argument(
        "--off-target-penalty-end",
        type=float,
        help="Final weight for off-target penalty",
    )
    pt.add_argument(
        "--off-target-steps",
        type=int,
        help="Steps over which to anneal the off-target penalty",
    )
    pt.add_argument(
        "--no-tp-penalty",
        type=float,
        default=1.0,
        help="Penalty when rule matches no dummy samples",
    )
    pt.add_argument(
        "--rule-len-penalty-start",
        type=float,
        help="Initial weight for rule length penalty",
    )
    pt.add_argument(
        "--rule-len-penalty-end",
        type=float,
        help="Final weight for rule length penalty",
    )
    pt.add_argument(
        "--rule-len-steps",
        type=int,
        help="Steps over which to anneal the rule length penalty",
    )
    pt.add_argument(
        "--rule-len-penalty-delay",
        type=int,
        help="Steps to delay application of rule length penalty",
    )
    pt.add_argument("--num-steps", type=int, default=1024, help="PPO rollout 길이")
    pt.add_argument("--minibatch-size", type=int, default=64)
    pt.add_argument("--ppo-epochs", type=int, default=4)
    pt.add_argument(
        "--accum-steps",
        type=int,
        default=1,
        help="Number of minibatches to accumulate gradients before optimizer step",
    )
    pt.add_argument(
        "--amp", action="store_true", help="Enable mixed precision training"
    )
    pt.add_argument(
        "--grad-checkpoint",
        action="store_true",
        help="Enable gradient checkpointing for GPT policies",
    )
    pt.add_argument("--lora-r", type=int, help="LoRA rank for GPT policies")
    pt.add_argument("--lora-alpha", type=float, help="LoRA alpha value")
    pt.add_argument("--lora-dropout", type=float, help="LoRA dropout")
    pt.add_argument(
        "--load-4bit", action="store_true", help="Load GPT policy in 4-bit mode"
    )
    pt.add_argument(
        "--load-8bit", action="store_true", help="Load GPT policy in 8-bit mode"
    )
    pt.add_argument(
        "--cpu", action="store_true", help="Force CPU even if CUDA available"
    )
    pt.set_defaults(func=cmd_ppo_train)

    # ------------------- generate ------------------- #
    gen = sub.add_parser(
        "generate", help="Generate YARA/CAPA rules with a trained agent"
    )
    gen.add_argument(
        "--agent-checkpoint", required=True, help="PPORuleAgent checkpoint (.pt)"
    )
    gen.add_argument(
        "--features",
        default="features.json",
        help="Path to mined feature JSON for vocabulary",
    )
    gen.add_argument(
        "--n-rules", type=int, default=100, help="Number of rules to sample"
    )
    gen.add_argument(
        "--temperature", type=float, default=1.0, help="Sampling temperature"
    )
    gen.add_argument(
        "--single-target-mode",
        action="store_true",
        help="Use a single random dummy graph as target each episode",
    )
    gen.add_argument(
        "--off-target-penalty",
        type=float,
        help="Penalty per off-target match in single-target mode",
    )
    gen.add_argument(
        "--off-target-penalty-start",
        type=float,
        help="Initial weight for off-target penalty",
    )
    gen.add_argument(
        "--off-target-penalty-end",
        type=float,
        help="Final weight for off-target penalty",
    )
    gen.add_argument(
        "--off-target-steps",
        type=int,
        help="Steps over which to anneal the off-target penalty",
    )
    gen.add_argument(
        "--no-tp-penalty",
        type=float,
        default=1.0,
        help="Penalty when rule matches no dummy samples",
    )
    gen.add_argument(
        "--target-graph",
        help="Path to a single graph (.pt or .pyg.pkl) to target",
    )
    gen.add_argument("--rule-type", choices=["yara", "capa"], default="yara")
    gen.add_argument(
        "--reward-weights",
        type=_parse_reward_weights,
        help="JSON mapping or path with reward weights",
    )
    gen.add_argument(
        "--out",
        help="Output rule file (.yar/.yml); defaults to models/rulebank/<type>/generated_<timestamp>.yar (.yml for capa)",
    )
    gen.set_defaults(func=cmd_generate)

    # ------------------- evaluate ------------------- #
    ev = sub.add_parser("evaluate", help="Evaluate rule bank on a labeled dataset")
    ev.add_argument("--rule-path", required=True, help="Path to rule file (.yar/.yml)")
    ev.add_argument(
        "--dataset",
        required=True,
        help="Test JSONL with keys: sha256, label (0/1)",
    )
    ev.add_argument(
        "--sample-dir",
        required=True,
        help="Directory containing binary samples named by sha256",
    )
    ev.add_argument(
        "--metrics",
        nargs="+",
        default=["auroc", "f1"],
        choices=["auroc", "f1", "precision", "recall"],
        help="Evaluation metrics",
    )
    ev.set_defaults(func=cmd_evaluate)

    # ------------------- pipeline ------------------- #
    pipe = sub.add_parser(
        "pipeline",
        help="Iteratively run feature-mine and ppo-train with benign freq updates",
    )
    pipe.add_argument("--graph-dir", required=True)
    pipe.add_argument("--labels")
    pipe.add_argument("--dataset-dir", required=True)
    pipe.add_argument("--work-dir", type=Path, required=True)
    pipe.add_argument("--iterations", type=int, default=2)
    pipe.add_argument("--freq-threshold", type=float, default=10.0)
    pipe.add_argument("--benign-freqs", type=Path, required=True)
    pipe.add_argument("--fp-threshold", type=float, default=0.5)
    pipe.add_argument("--epochs", type=int, default=1)
    pipe.add_argument("--cpu", action="store_true")
    pipe.add_argument("--config")
    pipe.set_defaults(func=cmd_pipeline)

    return parser


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


def main(argv: List[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    parser = _build_parser()
    args = parser.parse_args(argv)

    ts = _dt.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    run_dir = Path("runs") / args.command / ts
    ensure_dir(run_dir)
    name_map = {
        "feature-mine": "feature_mine.log",
        "build-dataset": "build_dataset.log",
        "ppo-train": "train.log",
        "generate": "generate.log",
        "evaluate": "evaluate.log",
        "pipeline": "pipeline.log",
    }
    log_path = run_dir / name_map.get(args.command, "run.log")
    _setup_logger(args.verbose, log_file=str(log_path))
    set_random_seed(args.seed, deterministic=True)

    # Dispatch to sub‑command
    args.func(args)  # type: ignore[misc]


if __name__ == "__main__":
    main()
