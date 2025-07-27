# src/evaluation/__init__.py
"""
Evaluation Package
──────────────────
간단 사용 예시
>>> import evaluation as ev
>>> m = ev.F1()
>>> m.update(logits, target); print(m())   # F1 스코어
>>> ev.quick_eval(model, loader, device="cuda")

공개 객체
---------
Metric base / 각종 Metric  : Accuracy, F1, AUROC, AUPRC, ConfusionMatrix
Contrastive 특화           : Alignment, Uniformity
성능·속도 편의 함수        : quick_eval, metric_summary
CI 자동화                  : run_ci  (src.evaluation.ci_runner.main 래퍼)
"""

from __future__ import annotations

# ───────────────── Metric 클래스 재노출 ─────────────────
from .metrics import (  # noqa: F401
    Accuracy,
    AUPRC,
    AUROC,
    Alignment,
    ConfusionMatrix,
    F1,
    LatencyMeter,
    Metric,
    Uniformity,
    format_metrics as _format_metrics,
)
from .rule_evaluator import RuleEvaluator

__all_metrics = [
    "Accuracy",
    "AUPRC",
    "AUROC",
    "Alignment",
    "ConfusionMatrix",
    "F1",
    "LatencyMeter",
    "Metric",
    "Uniformity",
]

# ───────────────── Quick Evaluation Helper ────────────
from typing import Dict

import torch
from torch.utils.data import DataLoader

# 기본 메트릭 세트 (필요 시 수정)
_DEFAULT_METRICS = {
    "f1": F1(average="macro"),
    "auroc": AUROC(average="macro"),
    "latency": LatencyMeter(),
}


@torch.no_grad()
def quick_eval(
    model: torch.nn.Module,
    loader: DataLoader,
    *,
    metrics: Dict[str, Metric] | None = None,
    device: str | torch.device = "cpu",
    max_batches: int | None = None,
) -> Dict[str, float]:
    """
    ▪ 작은 스크립트·노트북에서 즉석 검증용
    ▪ latency 포함
    """
    metrics = {**_DEFAULT_METRICS, **(metrics or {})}
    model.eval().to(device)

    for i, (g, y) in enumerate(loader):
        if max_batches and i >= max_batches:
            break
        g, y = g.to(device), y.to(device)

        metrics["latency"].start()
        logits = model(g)
        metrics["latency"].stop(len(y))

        probs = (
            torch.sigmoid(logits)
            if y.ndim == 2 or logits.size(1) == 1
            else torch.softmax(logits, 1)
        )

        for m in metrics.values():
            if isinstance(m, LatencyMeter):
                continue
            # heuristic: AUROC/AUPRC use prob, F1 use logits
            if isinstance(m, (AUROC, AUPRC)):
                m.update(probs, y)
            else:
                m.update(logits, y)

    return {k: v.compute() for k, v in metrics.items()}


def metric_summary(results: Dict[str, float]) -> str:  # noqa: D401
    """Dictionary → 사람이 읽기 쉬운 문자열"""
    # `format_metrics` 는 Metric 인스턴스를 요구하므로 래퍼 구현
    outs = []
    for k, v in results.items():
        outs.append(f"{k}: {v:.4f}" if isinstance(v, (int, float)) else f"{k}: {v}")
    return " | ".join(outs)


# ───────────────── CI Runner Short-Cut ─────────────────
def run_ci(argv: list[str] | None = None):  # noqa: D401
    """
    shell 대신 파이썬에서 직접 호출 가능:
        >>> import evaluation as ev
        >>> ev.run_ci(["--model-checkpoint", "...", "--split-path", "..."])
    """
    from .ci_runner import main as _ci_main

    import sys as _sys

    _orig_argv = _sys.argv
    try:
        _sys.argv = ["ci_runner"] + (argv or [])
        _ci_main()
    finally:
        _sys.argv = _orig_argv


__all__ = (
    __all_metrics
    + [
        "quick_eval",
        "metric_summary",
        "run_ci",
        "RuleEvaluator",
    ]
)
