# robust-malware-graph / src / explain / __init__.py
# --------------------------------------------------------------------------- #
#  📦  Explainability Top-Level Package
#
#  서브모듈 단일 진입점(one-stop import) + 간단 파이프라인 래퍼를 제공한다.
#
#  ── 주요 공개 객체 ────────────────────────────────────────────────────────
#  • cfg_explainer.*     → 노드 선택 · 랭킹·매핑 (XAI 핵심)
#  • CounterFactualGenerator  → 반례(counter-factual) 그래프 생성
#  • report.render       → HTML/Markdown 리포트 생성기
#  • run_full_pipeline   → 〈설명→리포트〉 합본 원-스톱 함수
#
#  사용 예
#  -------------------------------------------------------------------------
#  >>> import robust_malware_graph.explain as rmgx
#  >>> # 1) 설명 + 보고서 동시 생성
#  >>> paths = rmgx.run_full_pipeline(
#  ...     cfg_g, ast_g, model,
#  ...     sha256=sample_sha, out_dir="reports/", top_k=25
#  ... )
#  >>> print("HTML:", paths["html"])
#
#  >>> # 2) Counter-factual만 별도로
#  >>> cf_gen = rmgx.CounterFactualGenerator(model, cfg_g, device="cuda")
#  >>> cf = cf_gen.generate(target_label=0)
# --------------------------------------------------------------------------- #
from __future__ import annotations

from pathlib import Path
from typing import Dict

import torch
from torch_geometric.data import Data

# ── Re-export sub-packages ──────────────────────────────────────────────── #
from .cfg_explainer import (  # noqa: F401
    CFGASTMapper,
    CFGPathAggregator,
    GumbelMaskSelector,
    ShapleyNodeRanker,
    aggregate_paths,
    explain_cfg,
    quick_rank,
    train_selector,
)
from .cf_generator import CFResult, CounterFactualGenerator  # noqa: F401
from .report import render as render_report  # noqa: F401
from .utils.hetero import (  # noqa: F401
    edge_mask_to_global,
    get_edge_store,
    iter_edge_types,
    ensure_edgeaware_selector,
)
from .pg_explainer import PGExplainer  # noqa: F401

__all__ = [
    # cfg_explainer
    "CFGASTMapper",
    "CFGPathAggregator",
    "GumbelMaskSelector",
    "ShapleyNodeRanker",
    "aggregate_paths",
    "explain_cfg",
    "quick_rank",
    "train_selector",
    # counter-factual
    "CFResult",
    "CounterFactualGenerator",
    # report util
    "render_report",
    # util helpers
    "get_edge_store",
    "edge_mask_to_global",
    "iter_edge_types",
    "ensure_edgeaware_selector",
    "PGExplainer",
    # high-level
    "run_full_pipeline",
]

__version__: str = "0.1.0"  # bumped with project CI


# --------------------------------------------------------------------------- #
#                     High-level “explain + report” wrapper                   #
# --------------------------------------------------------------------------- #
def run_full_pipeline(
    cfg_graph: Data,
    ast_graph: Data,
    model,
    *,
    sha256: str,
    out_dir: str | Path = "./reports",
    device: str | torch.device = "cpu",
    view: str = "cfg",
    selector_kwargs: Dict | None = None,
    ranker_kwargs: Dict | None = None,
    report_kwargs: Dict | None = None,
    top_k: int | None = 20,
) -> Dict[str, Path]:
    """
    **One-call** convenience: 〈Selector → Aggregator → Ranker → Report〉.

    Parameters
    ----------
    cfg_graph / ast_graph : Data
        CFG & AST graphs of the sample.
    model : nn.Module or callable
        Frozen GNN classifier returning single logit/prob.
    sha256 : str
        Unique sample identifier => report filename prefix.
    out_dir : str | Path
        Output directory for HTML / MD / JSON.
    device : torch device
        GPU/CPU for selector & ranking ops.
    view : str
        Edge relation view for explanation.
    *kwargs
        Forwarded to underlying functions:
          • selector_kwargs → `train_selector`
          • ranker_kwargs   → `quick_rank`
          • report_kwargs   → `render_report`

    Returns
    -------
    dict { "html": Path, "md": Path, "json": Path }
    """
    # ─ 1) Explain CFG (selector+rank+mapping)
    result = explain_cfg(
        cfg_graph,
        ast_graph,
        model,
        view=view,
        device=device,
        selector_kwargs=selector_kwargs,
        ranker_kwargs=ranker_kwargs,
        top_k=top_k,
    )

    # ─ 2) Render SOC-friendly report
    report_paths = render_report(
        result,
        out_dir=out_dir,
        sha256=sha256,
        top_k=top_k,
        **(report_kwargs or {}),
    )
    return report_paths
