from __future__ import annotations

import argparse
import json
import os
import pickle
import logging
import tempfile
from pathlib import Path
from typing import Any, Dict, Sequence, Mapping

from collections import Counter
from rulegen.yara_builder import YaraBuilder

import torch
import torch.multiprocessing as mp
from tqdm.auto import tqdm
from src.common.utils import get_logger, tqdm_wrap, human_bytes

from .evaluation import (
    evaluate_single,
    adaptive_fp_retry,
    _init_worker,
    _init_saliency_worker,
    _eval_task,
    _saliency_task,
    compute_dynamic_group_min_count,
    TokenCache,
    _cache_version_info,
    _load_clean_cache,
    extract_json_tokens,
)
from .fp_token_utils import estimate_token_cache_size, _save_clean_cache
from .optimizer_utils import CategoricalOptimizer, PopulationOptimizer

LOGGER = get_logger(__name__)
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Evaluate explainer output by generating a YARA rule",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--graph", type=Path, help="HeteroData graph")
    p.add_argument("--sample", type=Path, help="Binary to scan")
    p.add_argument("--graph-dir", type=Path, help="Directory of graphs for batch mode")
    p.add_argument(
        "--sample-dir", type=Path, help="Directory containing binaries/JSONs"
    )
    p.add_argument("--meta-csv", type=Path, help="CSV with sha256,label,filename")
    p.add_argument(
        "--clean-dir", type=Path, help="Directory of clean binaries for FP check"
    )
    p.add_argument(
        "--saliency", type=Path, help="Precomputed node saliency (.pt or json)"
    )
    p.add_argument(
        "--precomputed-saliency-dir",
        type=Path,
        help="Directory with precomputed saliency files",
    )
    p.add_argument(
        "--cache-saliency",
        action="store_true",
        help="Cache computed saliency next to graph",
    )
    p.add_argument(
        "--optimize",
        action="store_true",
        help="Enable online optimization of rule parameters",
    )
    p.add_argument(
        "--optimizer-pkl",
        type=Path,
        default=Path("optimizer_state.pkl"),
        help="Path to load and save optimizer state",
    )
    p.add_argument(
        "--save-optimizer",
        type=Path,
        help="Save optimizer state to this path after execution",
    )
    p.add_argument(
        "--opt-beta",
        type=float,
        default=0.5,
        help="Weight for detection rate term in optimizer loss",
    )
    p.add_argument("--pop-size", type=int, default=1, help="Population size for global search")
    p.add_argument("--global-steps", type=int, default=0, help="Number of global optimization steps")
    p.add_argument("--mutation-rate", type=float, default=0.1, help="Mutation rate for global search")
    p.add_argument("--explainer", type=Path, help="Explainer checkpoint")
    p.add_argument(
        "--classifier", type=Path, required=True, help="Classifier checkpoint"
    )
    p.add_argument("--device", type=str, default="cpu")
    p.add_argument("--top-k", type=int, default=40)
    p.add_argument("--top-k-percent", type=float, default=None)
    p.add_argument(
        "--saliency-top-percent",
        type=float,
        default=None,
        help="Limit nodes by cumulative saliency percentage",
    )
    p.add_argument("--dynamic-k", action="store_true")
    p.add_argument("--keep-per-type", type=int, default=20)
    p.add_argument(
        "--max-per-prefix",
        type=int,
        default=3,
        help="Limit number of features per prefix after ranking",
    )
    p.add_argument("--min-saliency", type=float, default=1e-3)
    p.add_argument(
        "--benign-freqs", type=Path, help="JSON with benign feature frequencies"
    )
    p.add_argument(
        "--mal-freqs", type=Path, help="JSON with malicious feature frequencies"
    )
    p.add_argument(
        "--freq-ratio",
        type=float,
        default=1.0,
        help="Filter token when benign >= malicious * ratio",
    )
    p.add_argument(
        "--saliency-stats", type=Path, help="JSON with feature saliency stats"
    )
    p.add_argument(
        "--freq-threshold",
        type=float,
        default=10.0,
        help="Frequency threshold for filtering",
    )
    p.add_argument(
        "--min-freq-threshold",
        type=float,
        default=0.0,
        help="Lower bound for freq_threshold during FP retries",
    )
    p.add_argument(
        "--no-auto-relax",
        dest="auto_relax",
        action="store_false",
        help="Disable automatic relaxation of frequency thresholds",
    )
    p.add_argument(
        "--condition-type",
        choices=["any", "all", "percentage", "count", "combo"],
        default="combo",
        help="YARA condition type",
    )
    p.add_argument(
        "--percentage",
        type=int,
        default=70,
        help="Percentage value if using percentage condition",
    )
    p.add_argument(
        "--min-count",
        type=int,
        default=None,
        help="Minimum match count if using count condition",
    )
    p.add_argument(
        "--group-percentage",
        type=int,
        default=70,
        help=(
            "combo mode: percentage of each group; if only one group or two "
            "features are present the condition falls back to 'any'."
        ),
    )
    p.add_argument(
        "--group-min-count",
        type=int,
        help="combo mode: minimum matches per group",
    )
    class _GroupMinRatioAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, float(values))
            setattr(namespace, "auto_group_min", True)

    p.add_argument(
        "--group-min-ratio",
        action=_GroupMinRatioAction,
        type=float,
        default=0.0,
        help=(
            "combo mode: ratio for minimum matches per group; works with "
            "--group-min-count so smaller groups are relaxed automatically"
        ),
    )
    p.set_defaults(auto_group_min=False)
    p.add_argument(
        "--adjust-group-percentage",
        action="store_true",
        help="lower group percentage automatically for many features",
    )
    p.add_argument(
        "--num-rules", type=int, default=1, help="Number of rules to generate"
    )
    p.add_argument(
        "--chunk-size",
        type=int,
        default=None,
        help="Number of features per rule chunk",
    )
    p.add_argument(
        "--combine-mode",
        choices=["or", "and"],
        default="or",
        help="Combine multiple rules with logical OR/AND when saving",
    )
    p.add_argument(
        "--combine-min-ratio",
        type=float,
        default=0.7,
        help="When combining rules in OR mode, require this fraction to match",
    )
    p.add_argument(
        "--combine-max-ratio",
        type=float,
        default=1.0,
        help="Maximum value for combine_min_ratio during FP retries",
    )
    p.add_argument(
        "--fp-retries",
        type=int,
        default=0,
        help="Retry rule generation this many times if false positives occur",
    )
    p.add_argument(
        "--freq-threshold-step",
        type=float,
        default=0.0,
        help="Decrease freq_threshold by this value on each FP retry",
    )
    p.add_argument(
        "--comb-ratio-step",
        type=float,
        default=0.1,
        help="Increase combine_min_ratio by this value on each FP retry",
    )
    p.add_argument(
        "--chunk-size-step",
        type=int,
        default=1,
        help="Increase chunk_size by this amount on first FP retry",
    )
    p.add_argument(
        "--fp-timeout",
        type=float,
        default=None,
        help="Abort FP retries after this many seconds",
    )
    p.add_argument(
        "--max-exclude-tokens",
        type=int,
        default=5,
        help="Maximum number of tokens to try excluding individually during FP retry",
    )
    p.add_argument(
        "--num-rules-min",
        type=int,
        default=1,
        help="Minimum number of rules when adjusting due to FP",
    )
    p.add_argument(
        "--clean-sample", type=Path, help="Optional clean sample for FP check"
    )
    p.add_argument(
        "--save-clean-cache",
        type=Path,
        help="Save/load clean token cache to this path",
    )
    p.add_argument("--out", type=Path, help="Save JSON result path")
    p.add_argument("--out-csv", type=Path, help="Save CSV results for batch mode")
    p.add_argument(
        "--flush-every",
        type=int,
        default=None,
        help="Write CSV results every N graphs (append mode)",
    )
    p.add_argument(
        "--sample-rules-out",
        type=Path,
        help="Directory to write example rules",
    )
    p.add_argument(
        "--low-fp-rules-out",
        type=Path,
        help="Directory to write rules with no false positives",
    )
    p.add_argument(
        "--fp-rules-out",
        type=Path,
        help="Directory to write rules that triggered false positives",
    )
    p.add_argument(
        "--num-workers",
        type=int,
        default=1,
        help="Number of parallel worker processes for batch mode",
    )
    p.add_argument(
        "--batch-size",
        type=int,
        default=1,
        help="Optimizer batch size when using multiple workers",
    )
    p.add_argument(
        "--fp-scan-workers",
        type=int,
        default=1,
        help="Number of threads for scanning clean files for FP checks",
    )
    p.add_argument(
        "--json-match",
        action="store_true",
        help="Verify features in sample JSON instead of YARA match",
    )
    p.add_argument(
        "--exclude-tokens",
        nargs="*",
        help="특정 토큰을 제외하고 규칙을 생성",
    )
    p.add_argument(
        "--persist-fp-exclude",
        type=Path,
        help="JSON file to persist tokens excluded due to false positives",
    )
    p.add_argument(
        "--enforce-self-detect",
        action="store_true",
        help="relax thresholds until the sample is detected",
    )
    p.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
    return p
def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    if args.verbose:
        LOGGER.setLevel(logging.DEBUG)


    combine_mode = args.combine_mode
    condition_type = args.condition_type
    dynamic_k = args.dynamic_k
    auto_relax = args.auto_relax
    adjust_group_percentage = args.adjust_group_percentage
    group_min_ratio = args.group_min_ratio
    combine_min_ratio = args.combine_min_ratio

    benign_freqs = None
    if args.benign_freqs and args.benign_freqs.is_file():
        benign_freqs = json.loads(args.benign_freqs.read_text(encoding="utf-8"))

    mal_freqs = None
    if args.mal_freqs and args.mal_freqs.is_file():
        mal_freqs = json.loads(args.mal_freqs.read_text(encoding="utf-8"))

    saliency_stats = None
    if args.saliency_stats and args.saliency_stats.is_file():
        saliency_stats = json.loads(args.saliency_stats.read_text(encoding="utf-8"))

    device = torch.device(args.device)

    optimizer: CategoricalOptimizer | PopulationOptimizer | None = None
    opt_state = None
    opt_lock = None
    mp_manager = None
    if args.optimize:
        if args.pop_size > 1 or args.global_steps > 0:
            optimizer = PopulationOptimizer(
                population_size=args.pop_size,
                mutation_rate=args.mutation_rate,
                steps=args.global_steps,
                beta=args.opt_beta,
            )
        else:
            optimizer = CategoricalOptimizer(beta=args.opt_beta)
        if args.optimizer_pkl and args.optimizer_pkl.is_file():
            try:
                state = torch.load(args.optimizer_pkl, map_location="cpu")
                optimizer.load_state_dict(state)
            except Exception as exc:  # noqa: BLE001
                LOGGER.warning("Failed to load optimizer state %s: %s", args.optimizer_pkl, exc)
        mp_manager = mp.Manager()
        opt_state = mp_manager.dict(optimizer.state_dict())
        opt_lock = mp_manager.Lock()
    
    classifier = None
    explainer = None
    need_model = args.saliency is None or (args.graph_dir and args.meta_csv)
    if need_model:
        from src.models.gnn.res_wrapper import RESGCLClassifier

        LOGGER.debug("Loading classifier from %s", args.classifier)
        classifier = RESGCLClassifier.load_pretrained(
            str(args.classifier), map_location=device
        )
        if args.explainer and Path(args.explainer).is_file():
            LOGGER.debug("Loading explainer from %s", args.explainer)
            explainer = torch.load(
                args.explainer, map_location=device, weights_only=False
            )

    if args.graph_dir and args.meta_csv:
        import pandas as pd

        df = pd.read_csv(args.meta_csv)
        rows = df[df.get("label", 1) == 1]
        benign_paths: list[Path] = []
        benign_rows = df[df.get("label", 1) == 0]
        for _, b_row in benign_rows.iterrows():
            bsha = b_row["sha256"]
            bname = b_row.get("filename") or b_row.get("name") or f"{bsha}.bin"
            benign_paths.append(Path(args.sample_dir or args.graph_dir) / bname)

        token_cache = TokenCache()
        cache_version = _cache_version_info(benign_paths)
        if args.save_clean_cache and args.save_clean_cache.is_file():
            loaded = _load_clean_cache(args.save_clean_cache)
            if loaded is not None and loaded[1] == cache_version:
                token_cache, _ = loaded
                LOGGER.debug("Loaded clean cache from %s", args.save_clean_cache)
        if not token_cache.tokens and args.clean_dir is None and args.clean_sample is None:
            for p in tqdm_wrap(benign_paths, desc="preload clean json", unit="file"):
                j = p.with_suffix(".json")
                if not j.is_file():
                    continue
                try:
                    obj = json.loads(j.read_text(encoding="utf-8"))
                    toks = extract_json_tokens(obj)
                    token_cache.add(p, toks)
                    del obj
                except Exception as exc:  # noqa: BLE001
                    LOGGER.warning("failed to read %s: %s", j, exc)

        cache_bytes = estimate_token_cache_size(token_cache)
        LOGGER.debug(
            "Preloaded clean token cache: %d samples (%s)",
            len(token_cache.tokens),
            human_bytes(cache_bytes),
        )
        if args.save_clean_cache:
            _save_clean_cache(args.save_clean_cache, token_cache, cache_version)
        token_index_file: Path | None = None
        if args.num_workers > 1 and token_cache.index and not args.save_clean_cache:
            tmpdir = Path(tempfile.mkdtemp(prefix="token_index_"))
            token_index_file = tmpdir / "index.json"
            token_index_file.write_text(
                json.dumps({k: [str(p) for p in v] for k, v in token_cache.index.items()})
            )

        global_fp_tokens: list[str] = []
        freq_threshold_val: float | int = args.freq_threshold

        def _apply_params_main(params: dict[str, object]) -> None:
            nonlocal condition_type, combine_mode, dynamic_k, auto_relax
            nonlocal adjust_group_percentage, group_min_ratio, combine_min_ratio
            nonlocal global_fp_tokens, freq_threshold_val
            condition_type = params.get("condition_type", condition_type)
            combine_mode = params.get("combine_mode", combine_mode)
            dynamic_k = params.get("dynamic_k", dynamic_k)
            auto_relax = params.get("auto_relax", auto_relax)
            adjust_group_percentage = params.get(
                "adjust_group_percentage", adjust_group_percentage
            )
            group_min_ratio = params.get("group_min_ratio", group_min_ratio)
            combine_min_ratio = params.get("combine_min_ratio", combine_min_ratio)
            if "exclude_tokens" in params:
                global_fp_tokens = list(params["exclude_tokens"])
            if "freq_threshold" in params:
                freq_threshold_val = params["freq_threshold"]

        def _current_params() -> dict[str, object]:
            excl = list({*(args.exclude_tokens or []), *global_fp_tokens})
            return {
                "condition_type": condition_type,
                "combine_mode": combine_mode,
                "dynamic_k": dynamic_k,
                "auto_relax": auto_relax,
                "adjust_group_percentage": adjust_group_percentage,
                "group_min_ratio": group_min_ratio,
                "combine_min_ratio": combine_min_ratio,
                "exclude_tokens": excl,
                "freq_threshold": freq_threshold_val,
            }
        results: list[dict[str, Any]] = []
        fp_token_counter_all: Counter[str] = Counter()
        flush_buffer: list[dict[str, Any]] = []
        first_flush = True
        skipped = 0
        tasks: list[tuple[str, Path, Path, Path, dict]] = []
        for _, row in rows.iterrows():
            sha = row["sha256"]
            filename = row.get("filename") or row.get("name") or f"{sha}.bin"
            gpath = Path(args.graph_dir) / f"{sha}.pt"
            spath = Path(args.sample_dir or args.graph_dir) / filename
            jpath = Path(args.sample_dir or args.graph_dir) / f"{sha}.json"

            task_kwargs = {
                "top_k": args.top_k,
                "top_k_percent": args.top_k_percent,
                "saliency_top_percent": args.saliency_top_percent,
                "dynamic_k": dynamic_k,
                "min_saliency": args.min_saliency,
                "keep_per_type": args.keep_per_type,
                "max_per_prefix": args.max_per_prefix,
                "benign_freqs": benign_freqs,
                "mal_freqs": mal_freqs,
                "freq_ratio": args.freq_ratio,
                "freq_threshold": args.freq_threshold,
                "auto_relax": auto_relax,
                "condition_type": condition_type,
                "percentage": args.percentage,
                "min_count": args.min_count,
                "group_percentage": args.group_percentage,
                "group_min_count": args.group_min_count,
                "group_min_ratio": group_min_ratio,
                "auto_group_min": args.auto_group_min,
                "adjust_group_percentage": adjust_group_percentage,
                "num_rules": args.num_rules,
                "chunk_size": args.chunk_size,
                "clean_dir": args.clean_dir,
                "clean_sample": None,
                "clean_paths": (
                    benign_paths
                    if args.clean_dir is None and args.clean_sample is None
                    else None
                ),
                "json_match": args.json_match,
                "saliency_stats": saliency_stats,
                "combine_min_ratio": combine_min_ratio,
                "combine_max_ratio": args.combine_max_ratio,
                "fp_retries": args.fp_retries,
                "freq_threshold_step": args.freq_threshold_step,
                "comb_ratio_step": args.comb_ratio_step,
                "chunk_size_step": args.chunk_size_step,
                "num_rules_min": args.num_rules_min,
                "exclude_tokens": args.exclude_tokens,
                "persist_fp_exclude": args.persist_fp_exclude,
                "enforce_self_detect": args.enforce_self_detect,
                "fp_scan_workers": args.fp_scan_workers,
                "token_cache": (
                    None if args.num_workers > 1 and args.save_clean_cache else token_cache if args.num_workers <= 1 else None
                ),
                "fp_timeout": args.fp_timeout,
                "max_exclude_tokens": args.max_exclude_tokens,
                "cache_saliency": args.cache_saliency,
            }
            tasks.append((sha, gpath, spath, jpath, task_kwargs))
        graph_bar = tqdm(total=len(tasks), desc="graphs", unit="graph", position=0)
        fp_bar = tqdm(total=args.fp_retries or 1, desc="fp retries", unit="try", position=1, leave=True)

        import multiprocessing as mp_mod
        from concurrent.futures import (
            ProcessPoolExecutor,
            wait,
            FIRST_COMPLETED,
            as_completed,
        )

        sal_dir = args.precomputed_saliency_dir or Path(tempfile.mkdtemp(prefix="saliency_"))
        sal_dir.mkdir(parents=True, exist_ok=True)

        if not args.precomputed_saliency_dir:
            ctx_sal = mp_mod.get_context("spawn")
            with ProcessPoolExecutor(
                max_workers=1,
                mp_context=ctx_sal,
                initializer=_init_saliency_worker,
                initargs=(str(args.classifier), str(args.explainer) if args.explainer else None, args.device),
            ) as sexec:
                fut_map = {
                    sexec.submit(_saliency_task, (sha, gpath, sal_dir / f"{sha}.pt")): sha
                    for sha, gpath, _, _, _ in tasks
                }
                for fut in tqdm(as_completed(fut_map), total=len(fut_map), desc="saliency", unit="graph"):
                    try:
                        fut.result()
                    except FileNotFoundError as exc:
                        skipped += 1
                        LOGGER.debug("Skipping %s: %s", fut_map[fut], exc)
                        continue

        if args.num_workers > 1:
            ctx = mp_mod.get_context("forkserver")
            manager = mp_mod.Manager()
            result_q: mp_mod.Queue = manager.Queue()
            with ProcessPoolExecutor(
                max_workers=args.num_workers,
                mp_context=ctx,
                initializer=_init_worker,
                initargs=(
                    None,
                    None,
                    args.device,
                    str(token_index_file) if token_index_file else None,
                    str(args.save_clean_cache) if args.save_clean_cache else None,
                ),
            ) as executor:
                future_map: dict[any, str] = {}
                task_iter = iter(tasks)

                def _submit_next() -> None:
                    try:
                        sha, gpath, spath, jpath, kw = next(task_iter)
                    except StopIteration:
                        return
                    kw = kw.copy()
                    kw.update(_current_params())
                    kw["saliency_path"] = sal_dir / f"{sha}.pt"
                    fut = executor.submit(
                        _eval_task,
                        (sha, gpath, spath, jpath, kw),
                        None,
                        None,
                        None,
                        result_queue=result_q,
                    )
                    future_map[fut] = sha

                for _ in range(min(args.num_workers, len(tasks))):
                    _submit_next()

                batch: list[dict[str, Any]] = []
                while future_map:
                    done, _ = wait(list(future_map.keys()), return_when=FIRST_COMPLETED)
                    for fut in done:
                        fp_bar.reset()
                        sha = future_map.pop(fut)
                        try:
                            fut.result()
                        except FileNotFoundError as exc:
                            skipped += 1
                            LOGGER.debug("Skipping %s: %s", sha, exc)
                            _submit_next()
                            continue

                        sha_res, res = result_q.get()
                        sha = sha_res
                        res["sha256"] = sha
                        results.append(res)
                        if optimizer:
                            batch.append(res)
                            if len(batch) >= args.batch_size:
                                optimizer.step(batch)
                                if opt_state is not None:
                                    with opt_lock:
                                        opt_state.clear()
                                        opt_state.update(optimizer.state_dict())
                                _apply_params_main(optimizer.discrete_params())
                                batch.clear()
                        cnts = res.get("fp_token_counts_total")
                        if cnts:
                            fp_token_counter_all.update({k.lower(): int(v) for k, v in cnts.items()})
                            top_fp = [t for t, _ in sorted(fp_token_counter_all.items(), key=lambda x: (-x[1], x[0]))[: args.max_exclude_tokens]]
                            _apply_params_main({"exclude_tokens": top_fp})

                        det_rate = sum(r.get("detected", False) for r in results) / len(results)
                        fp_ratio = sum(1 for r in results if r.get("false_positive")) / len(results)
                        fp_ratio_b = sum(r.get("fp_ratio_benign", 0.0) for r in results) / len(results)
                        graph_bar.update(1)
                        graph_bar.set_postfix(
                            avg_det=f"{det_rate:.3f}", fp=f"{fp_ratio:.3f}", fpb=f"{fp_ratio_b:.3f}"
                        )

                        if args.out_csv and args.flush_every:
                            flush_buffer.append(res)
                            if len(flush_buffer) >= args.flush_every:
                                df_flush = pd.DataFrame(flush_buffer)
                                for col in (
                                    "matched_tokens",
                                    "fp_matched_tokens",
                                    "fp_token_counts",
                                    "fp_ratio_benign",
                                    "group_min_count",
                                    "freq_threshold",
                                ):
                                    if col not in df_flush.columns:
                                        df_flush[col] = [
                                            [] if col in ("fp_matched_tokens", "fp_token_counts") else None
                                            for _ in range(len(df_flush))
                                        ]
                                df_flush.to_csv(
                                    args.out_csv,
                                    mode="a" if not first_flush else "w",
                                    header=first_flush,
                                    index=False,
                                )
                                first_flush = False
                                flush_buffer.clear()

                        if args.sample_rules_out and res.get("detected"):
                            rule_dir = args.sample_rules_out / "rule"
                            rule_dir.mkdir(parents=True, exist_ok=True)
                            fname = f"{sha}.yar"
                            rule_txt = YaraBuilder().combine_rules(
                                res.get("rule_texts", [res.get("rule_text", "")]),
                                mode=combine_mode,
                                min_match_ratio=args.combine_min_ratio,
                            )
                            (rule_dir / fname).write_text(rule_txt, encoding="utf-8")
                            if args.low_fp_rules_out and not res.get("false_positive"):
                                args.low_fp_rules_out.mkdir(parents=True, exist_ok=True)
                                (args.low_fp_rules_out / fname).write_text(
                                    rule_txt, encoding="utf-8"
                                )
                            if args.fp_rules_out and res.get("false_positive"):
                                args.fp_rules_out.mkdir(parents=True, exist_ok=True)
                                (args.fp_rules_out / fname).write_text(
                                    rule_txt, encoding="utf-8"
                                )

                        _submit_next()

                while not result_q.empty():
                    _, res_left = result_q.get()
                    if optimizer:
                        batch.append(res_left)
                if optimizer and batch:
                    optimizer.step(batch)
                    if opt_state is not None:
                        with opt_lock:
                            opt_state.clear()
                            opt_state.update(optimizer.state_dict())
                    _apply_params_main(optimizer.discrete_params())
        else:
            batch: list[dict[str, Any]] = []
            for task in tasks:
                fp_bar.reset()
                sha, gpath, spath, jpath, kw = task
                kw = kw.copy()
                kw.update(_current_params())
                sal_path = sal_dir / f"{sha}.pt"
                if not args.precomputed_saliency_dir:
                    graph = torch.load(gpath, map_location=device, weights_only=False)
                    sal = _compute_saliency_with_explainer(graph, classifier, explainer, device)
                    torch.save(sal, sal_path)
                kw["saliency_path"] = sal_path
                res = _eval_task(
                    (sha, gpath, spath, jpath, kw),
                    classifier,
                    explainer,
                    device,
                    fp_bar=fp_bar,
                    optimizer=None,
                )
                sha = task[0]

                res["sha256"] = sha
                results.append(res)
                if optimizer:
                    batch.append(res)
                    if len(batch) >= args.batch_size:
                        optimizer.step(batch)
                        if opt_state is not None:
                            with opt_lock:
                                opt_state.clear()
                                opt_state.update(optimizer.state_dict())
                        _apply_params_main(optimizer.discrete_params())
                        batch.clear()
                cnts = res.get("fp_token_counts_total")
                if cnts:
                    fp_token_counter_all.update({k.lower(): int(v) for k, v in cnts.items()})
                    top_fp = [t for t, _ in sorted(fp_token_counter_all.items(), key=lambda x: (-x[1], x[0]))[: args.max_exclude_tokens]]
                    _apply_params_main({"exclude_tokens": top_fp})

                det_rate = sum(r.get("detected", False) for r in results) / len(results)
                fp_ratio = sum(1 for r in results if r.get("false_positive")) / len(results)
                fp_ratio_b = sum(r.get("fp_ratio_benign", 0.0) for r in results) / len(results)
                graph_bar.update(1)
                graph_bar.set_postfix(
                    avg_det=f"{det_rate:.3f}", fp=f"{fp_ratio:.3f}", fpb=f"{fp_ratio_b:.3f}"
                )

                if args.out_csv and args.flush_every:
                    flush_buffer.append(res)
                    if len(flush_buffer) >= args.flush_every:
                        df_flush = pd.DataFrame(flush_buffer)
                        for col in (
                            "matched_tokens",
                            "fp_matched_tokens",
                            "fp_ratio_benign",
                            "group_min_count",
                            "freq_threshold",
                        ):
                            if col not in df_flush.columns:
                                df_flush[col] = [
                                    [] if col == "fp_matched_tokens" else None
                                    for _ in range(len(df_flush))
                                ]
                        df_flush.to_csv(
                            args.out_csv,
                            mode="a" if not first_flush else "w",
                            header=first_flush,
                            index=False,
                        )
                        first_flush = False
                        flush_buffer.clear()

                if args.sample_rules_out and res.get("detected"):
                    rule_dir = args.sample_rules_out / "rule"
                    rule_dir.mkdir(parents=True, exist_ok=True)
                    fname = f"{sha}.yar"
                    rule_txt = YaraBuilder().combine_rules(
                        res.get("rule_texts", [res.get("rule_text", "")]),
                        mode=combine_mode,
                        min_match_ratio=args.combine_min_ratio,
                    )
                    (rule_dir / fname).write_text(rule_txt, encoding="utf-8")
                    if args.low_fp_rules_out and not res.get("false_positive"):
                        args.low_fp_rules_out.mkdir(parents=True, exist_ok=True)
                        (args.low_fp_rules_out / fname).write_text(
                            rule_txt, encoding="utf-8"
                        )
                    if args.fp_rules_out and res.get("false_positive"):
                        args.fp_rules_out.mkdir(parents=True, exist_ok=True)
                        (args.fp_rules_out / fname).write_text(
                            rule_txt, encoding="utf-8"
                        )

            if optimizer and batch:
                optimizer.step(batch)
                if opt_state is not None:
                    with opt_lock:
                        opt_state.clear()
                        opt_state.update(optimizer.state_dict())
                _apply_params_main(optimizer.discrete_params())
        graph_bar.close()
        fp_bar.close()
        df = pd.DataFrame(results)

        if args.out_csv:
            if args.flush_every:
                if flush_buffer:
                    df_flush = pd.DataFrame(flush_buffer)
                    for col in (
                        "matched_tokens",
                        "fp_matched_tokens",
                        "fp_token_counts",
                        "group_min_count",
                        "freq_threshold",
                    ):
                        if col not in df_flush.columns:
                            df_flush[col] = [
                                []
                                if col in ("fp_matched_tokens", "fp_token_counts")
                                else None
                                for _ in range(len(df_flush))
                            ]
                    df_flush.to_csv(
                        args.out_csv,
                        mode="a" if not first_flush else "w",
                        header=first_flush,
                        index=False,
                    )
                    first_flush = False
            else:
                for col in (
                    "matched_tokens",
                    "fp_matched_tokens",
                    "fp_token_counts",
                    "fp_ratio_benign",
                    "group_min_count",
                    "freq_threshold",
                ):
                    if col not in df.columns:
                        df[col] = [
                            []
                            if col in ("fp_matched_tokens", "fp_token_counts")
                            else None
                            for _ in range(len(df))
                        ]
                df.to_csv(args.out_csv, index=False)

        LOGGER.info("Skipped %d graphs due to missing files", skipped)

        if results:
            det_rate = sum(r.get("detected", False) for r in results) / len(results)
            fp_ratio = sum(1 for r in results if r.get("false_positive")) / len(results)
            fp_ratio_b = sum(r.get("fp_ratio_benign", 0.0) for r in results) / len(results)
            LOGGER.info(
                "average detection=%.3f, FP ratio=%.3f, FP ratio(b)=%.3f",
                det_rate,
                fp_ratio,
                fp_ratio_b,
            )
            if fp_token_counter_all:
                top_tokens = sorted(fp_token_counter_all.items(), key=lambda x: (-x[1], x[0]))[:10]
                LOGGER.info("Top FP tokens: %s", top_tokens)

            rule_texts = [
                (r.get("sha256"), r.get("rule_texts", [r.get("rule_text", "")]))
                for r in results
                if r.get("rule_texts") or r.get("rule_text")
            ]
            if args.sample_rules_out and rule_texts:
                import random

                args.sample_rules_out.mkdir(parents=True, exist_ok=True)
                selected = random.sample(rule_texts, min(5, len(rule_texts)))
                for i, (sha, texts) in enumerate(selected, start=1):
                    fname = f"{sha}.yar" if sha else f"rule_{i}.yar"
                    combined = YaraBuilder().combine_rules(
                        texts,
                        mode=combine_mode,
                        min_match_ratio=args.combine_min_ratio,
                    )
                    (args.sample_rules_out / fname).write_text(
                        combined, encoding="utf-8"
                    )
        else:
            LOGGER.warning("No samples evaluated")

        if optimizer:
            if opt_state is not None:
                with opt_lock:
                    optimizer.load_state_dict(dict(opt_state))
            if args.optimizer_pkl:
                try:
                    torch.save(optimizer.state_dict(), args.optimizer_pkl)
                except Exception as exc:  # noqa: BLE001
                    LOGGER.warning(
                        "Failed to save optimizer to %s: %s",
                        args.optimizer_pkl,
                        exc,
                    )
            if args.save_optimizer:
                try:
                    torch.save(optimizer.state_dict(), args.save_optimizer)
                except Exception as exc:  # noqa: BLE001
                    LOGGER.warning(
                        "Failed to save optimizer to %s: %s",
                        args.save_optimizer,
                        exc,
                    )

    else:
        if args.graph is None or args.sample is None:
            raise SystemExit("--graph and --sample are required for single evaluation")

        result = evaluate_single(
            args.graph,
            args.sample,
            classifier_ckpt=None,
            explainer_ckpt=None,
            classifier=classifier,
            explainer=explainer,
            saliency_path=args.saliency,
            saliency=None,
            device=device,
            top_k=args.top_k,
            top_k_percent=args.top_k_percent,
            saliency_top_percent=args.saliency_top_percent,
            dynamic_k=args.dynamic_k,
            min_saliency=args.min_saliency,
            keep_per_type=args.keep_per_type,
            max_per_prefix=args.max_per_prefix,
            benign_freqs=benign_freqs,
            mal_freqs=mal_freqs,
            freq_ratio=args.freq_ratio,
            freq_threshold=args.freq_threshold,
            min_freq_threshold=args.min_freq_threshold,
            auto_relax=args.auto_relax,
            condition_type=args.condition_type,
            percentage=args.percentage,
            min_count=args.min_count,
            group_percentage=args.group_percentage,
            group_min_count=args.group_min_count,
            group_min_ratio=args.group_min_ratio,
            auto_group_min=args.auto_group_min,
            adjust_group_percentage=args.adjust_group_percentage,
            num_rules=args.num_rules,
            chunk_size=args.chunk_size,
            clean_dir=args.clean_dir,
            clean_sample=args.clean_sample,
            clean_paths=None,
            sample_json=(
                args.sample_dir / f"{args.sample.stem}.json"
                if args.sample_dir
                else None
            ),
            json_match=args.json_match,
            fp_scan_workers=args.fp_scan_workers,
            saliency_stats=saliency_stats,
            token_cache=None,
            combine_mode=combine_mode,
            combine_min_ratio=args.combine_min_ratio,
            combine_max_ratio=args.combine_max_ratio,
            fp_retries=args.fp_retries,
            freq_threshold_step=args.freq_threshold_step,
            comb_ratio_step=args.comb_ratio_step,
            chunk_size_step=args.chunk_size_step,
            num_rules_min=args.num_rules_min,
            exclude_tokens=args.exclude_tokens,
            persist_fp_exclude=args.persist_fp_exclude,
            enforce_self_detect=args.enforce_self_detect,
            fp_timeout=args.fp_timeout,
            max_exclude_tokens=args.max_exclude_tokens,
            cache_saliency=args.cache_saliency,
            optimizer=optimizer,
        )

        text = json.dumps(result, ensure_ascii=False, indent=2)
        if args.out:
            args.out.write_text(text, encoding="utf-8")
        print(text)

        rule_txt = YaraBuilder().combine_rules(
            result.get("rule_texts", [result.get("rule_text", "")]),
            mode=combine_mode,
            min_match_ratio=args.combine_min_ratio,
        )

        if args.sample_rules_out:
            args.sample_rules_out.mkdir(parents=True, exist_ok=True)
            rule_path = args.sample_rules_out / f"{args.sample.stem}.yar"
            rule_path.write_text(rule_txt, encoding="utf-8")

            if result.get("detected"):
                rule_dir = args.sample_rules_out / "rule"
                rule_dir.mkdir(parents=True, exist_ok=True)
                (rule_dir / f"{args.sample.stem}.yar").write_text(
                    rule_txt, encoding="utf-8"
                )
                if args.low_fp_rules_out and not result.get("false_positive"):
                    args.low_fp_rules_out.mkdir(parents=True, exist_ok=True)
                    (args.low_fp_rules_out / f"{args.sample.stem}.yar").write_text(
                        rule_txt, encoding="utf-8"
                    )

        if args.fp_rules_out and result.get("false_positive"):
            args.fp_rules_out.mkdir(parents=True, exist_ok=True)
            (args.fp_rules_out / f"{args.sample.stem}.yar").write_text(
                rule_txt, encoding="utf-8"
            )

        if optimizer:
            if opt_state is not None:
                with opt_lock:
                    optimizer.load_state_dict(dict(opt_state))
            if args.optimizer_pkl:
                try:
                    torch.save(optimizer.state_dict(), args.optimizer_pkl)
                except Exception as exc:  # noqa: BLE001
                    LOGGER.warning("Failed to save optimizer to %s: %s", args.optimizer_pkl, exc)
            if args.save_optimizer:
                try:
                    torch.save(optimizer.state_dict(), args.save_optimizer)
                except Exception as exc:  # noqa: BLE001
                    LOGGER.warning("Failed to save optimizer to %s: %s", args.save_optimizer, exc)

    if mp_manager is not None:
        mp_manager.shutdown()


__all__ = ["main"]

if __name__ == "__main__":  # pragma: no cover - CLI entry
    main()
