# src/evaluation/ci_runner.py
"""
Continuous-Integration Regression Tester
────────────────────────────────────────

Usage (로컬 / CI):
$ python -m src.evaluation.ci_runner \
    --model-checkpoint models/gnn/encoder.pt \
    --split-path data/splits/val.parquet \
    --metric-targets f1:0.85 auroc:0.92 latency:15 \
    --batch-size 256 --device cuda:0

• 지정 split(또는 임의 샘플)으로 간단 추론 후 metrics.py 지표 계산
• --metric-targets 로 threshold 설정 → 미달 시 exit-code 1
• (선택) --save-json 으로 결과를 artifacts 로 업로드
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List

import torch
from torch.utils.data import DataLoader

# 내부 모듈
from src.common.logger import get_logger
from src.evaluation.metrics import (Accuracy, AUROC, F1, LatencyMeter,
                                    format_metrics)
from src.models.gnn.encoder import RGCNEncoder  # 예시; 프로젝트별로 수정
from src.graphs.dataset import GraphDataset  # ↳ data/hetero/*.parquet 로더

logger = get_logger(__name__)


# ────────────────────────────── helpers ────────────────────────────────────
def parse_metric_targets(pairs: List[str]) -> Dict[str, float]:
    """f1:0.85 auroc:0.9 형태를 dict 로 변환"""
    out = {}
    for p in pairs:
        try:
            k, v = p.split(":")
        except ValueError as e:
            raise argparse.ArgumentTypeError(
                f"--metric-targets '{p}' must be key:value"
            ) from e
        out[k.lower()] = float(v)
    return out


def sanity_check_targets(targets: Dict[str, float]):
    allowed = {"acc", "accuracy", "f1", "auroc", "latency"}
    unknown = set(targets) - allowed
    if unknown:
        raise ValueError(f"Unknown metric keys in --metric-targets: {unknown}")


# ────────────────────────── evaluation loop ────────────────────────────────
@torch.no_grad()
def evaluate(
    model: torch.nn.Module,
    loader: DataLoader,
    device: torch.device,
    max_steps: int | None = None,
):
    """단일 프로세스 평가 (DDP 미지원: CI 속도용)"""
    model.eval()
    model.to(device)

    metrics = {
        "f1": F1(average="macro"),
        "auroc": AUROC(average="macro"),
        "latency": LatencyMeter(),
    }

    step = 0
    tic = time.time()
    for batch in loader:
        if max_steps and step >= max_steps:
            break
        g, y = batch  # GraphDataset __getitem__ 반환
        g = g.to(device)
        y = y.to(device)

        metrics["latency"].start()
        logits = model(g)  # (B, C)
        metrics["latency"].stop(len(y))

        # probability → 필요하면 softmax/sigmoid
        probs = torch.sigmoid(logits) if y.ndim == 2 else torch.softmax(logits, 1)

        metrics["f1"].update(logits, y)
        metrics["auroc"].update(probs, y)

        step += 1

    wall = time.time() - tic
    logger.info("Evaluation finished in %.1f s (%d batches)", wall, step)

    results = {k: m.compute() for k, m in metrics.items()}
    return results


# ─────────────────────────────── main ──────────────────────────────────────
def main():
    p = argparse.ArgumentParser(description="CI regression test runner")
    p.add_argument("--model-checkpoint", required=True, type=Path)
    p.add_argument("--split-path", required=True, type=Path)
    p.add_argument("--batch-size", type=int, default=512)
    p.add_argument("--device", default="cpu")
    p.add_argument("--num-workers", type=int, default=4)
    p.add_argument("--metric-targets", nargs="+", type=str, default=[])
    p.add_argument("--sample", type=int, default=0, help="샘플링 개수(0=전부)")
    p.add_argument("--save-json", type=Path, default=None)
    args = p.parse_args()

    # ───── metric threshold 파싱 ───────────────────
    metric_targets = parse_metric_targets(args.metric_targets)
    sanity_check_targets(metric_targets)
    logger.info("Targets → %s", metric_targets)

    # ───── 데이터 & 모델 로드 ───────────────────────
    dataset = GraphDataset(args.split_path, sample=args.sample or None)
    loader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.num_workers,
        collate_fn=dataset.collate_fn,
    )
    model = RGCNEncoder.load_from_checkpoint(args.model_checkpoint)

    # ───── 평가 ────────────────────────────────────
    results = evaluate(model, loader, torch.device(args.device))
    logger.info("Results  |  %s", format_metrics({k: torch.tensor(v) if not isinstance(v, torch.Tensor) else v
                                                 for k, v in results.items()}))

    # ───── JSON 저장 (선택) ─────────────────────────
    if args.save_json:
        args.save_json.parent.mkdir(parents=True, exist_ok=True)
        with open(args.save_json, "w") as fp:
            json.dump(results, fp, indent=2)
        logger.info("Saved → %s", args.save_json)

    # ───── threshold 체크 → 실패 시 exit 1 ───────────
    failed = []
    for k, thr in metric_targets.items():
        if k in {"acc", "accuracy"}:
            cur = results.get("accuracy", results.get("acc"))
            ok = cur >= thr
        elif k in {"f1", "auroc"}:
            ok = results[k] >= thr
        elif k == "latency":  # ms/샘플, 작을수록 좋음
            ok = results[k] <= thr
        else:
            continue
        if not ok:
            failed.append(f"{k} {results[k]:.4f} vs target {thr}")

    if failed:
        logger.error("❌  Regression detected:\n  " + "\n  ".join(failed))
        sys.exit(1)

    logger.info("✅  All metric targets satisfied.")


if __name__ == "__main__":
    main()
