"""Wrapper module for explainer rule evaluation utilities."""
from __future__ import annotations

from .evaluation import (
    LOGGER,
    evaluate_single,
    adaptive_fp_retry,
    verify_features,
    extract_json_tokens,
    _compute_saliency_with_explainer,
    _extract_tokens,
    compute_dynamic_group_min_count,
)
from .fp_token_utils import (
    TokenCache,
    _load_fp_exclude,
    _save_fp_exclude,
    estimate_token_cache_size,
    tokens_to_bitvec,
    _FP_EXCLUDE_COUNTS,
    _FP_EXCLUDE_SET,
    _FP_EXCLUDE_PATH,
    _load_token_index,
    _cache_version_info,
    _load_clean_cache,
    _save_clean_cache,
)
from .optimizer_utils import (
    _optimizer_loss,
    _optimizer_step,
    CategoricalOptimizer,
    PopulationOptimizer,
)
from rulegen.feature_miner import FeatureMiner
from .cli import build_parser, main

__all__ = [
    "LOGGER",
    "evaluate_single",
    "adaptive_fp_retry",
    "verify_features",
    "extract_json_tokens",
    "_compute_saliency_with_explainer",
    "_extract_tokens",
    "TokenCache",
    "_load_fp_exclude",
    "_save_fp_exclude",
    "estimate_token_cache_size",
    "tokens_to_bitvec",
    "FeatureMiner",
    "_FP_EXCLUDE_COUNTS",
    "_FP_EXCLUDE_SET",
    "_FP_EXCLUDE_PATH",
    "_optimizer_loss",
    "_optimizer_step",
    "CategoricalOptimizer",
    "PopulationOptimizer",
    "compute_dynamic_group_min_count",
    "build_parser",
    "main",
    "_load_token_index",
    "_cache_version_info",
    "_load_clean_cache",
    "_save_clean_cache",
]
