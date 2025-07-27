"""
src.continual.cli.online_eval
=============================

▶ 학습된 모델을 스트리밍 그래프(test split) 위에서 온라인 평가
   python -m continual.cli.online_eval \
       --config configs/eval.yaml \
       --weights checkpoints/supcon/final_best.pt \
       --device cuda

필요 YAML 필드 (예시: configs/eval.yaml)
--------------------------------------
seed: 42
data:
  root: data/splits/time
  split: test
eval:
  batch_size: 256
  num_workers: 8
metrics: [auroc, f1, ap]         # 선택
model:                           # OnlineSupConLearner 또는 RESGCLClassifier args
  name: RESGCLClassifier
  encoder: RGCNEncoder
  hidden_dim: 256
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List

import torch
import yaml
from sklearn.metrics import (
    average_precision_score,
    f1_score,
    roc_auc_score,
)
from torch_geometric.loader import DataLoader
from tqdm.auto import tqdm

# ---------------- 프로젝트 모듈 ---------------- #
from continual.utils import set_random_seed
from continual.callbacks import StdoutLogger
from graphs.dataset.graph_dataset import GraphDataset

# 모델 빌더 유틸 (간단 레지스트리)
def build_model(cfg: Dict) -> torch.nn.Module:
    name = cfg.get("name", "RESGCLClassifier")
    if name == "RESGCLClassifier":
        from models.gnn.res_wrapper import RESGCLClassifier

        return RESGCLClassifier(**{k: v for k, v in cfg.items() if k != "name"})
    elif name == "StudentSGCN":
        from models.distill.sgcn_kd import StudentSGCN

        return StudentSGCN(**{k: v for k, v in cfg.items() if k != "name"})
    else:  # fallback
        raise ValueError(f"Unknown model name '{name}'")


# ---------------- CLI 파싱 ---------------- #
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Online evaluation of trained model")
    p.add_argument("--config", type=str, required=True, help="YAML config path")
    p.add_argument("--weights", type=str, required=True, help="model .pt|.ckpt path")
    p.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    p.add_argument("--out", type=str, default="eval_results.json", help="save metric json")
    return p.parse_args()


# ---------------- 메인 ---------------- #
def main() -> None:
    args = parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())

    set_random_seed(cfg.get("seed", 42))
    device = torch.device(args.device)

    # ---------------- Dataset & Loader ---------------- #
    split = cfg["data"].get("split", "test")
    ds = GraphDataset(root=cfg["data"]["root"], split=split)
    loader = DataLoader(
        ds,
        batch_size=cfg["eval"]["batch_size"],
        shuffle=False,
        num_workers=cfg["eval"].get("num_workers", 4),
        pin_memory=True,
    )

    # ---------------- Model ---------------- #
    model = build_model(cfg["model"]).to(device)
    sd = torch.load(args.weights, map_location="cpu", weights_only=False)
    model.load_state_dict(sd["model_state"] if isinstance(sd, dict) and "model_state" in sd else sd)
    model.eval()

    # ---------------- Logger ---------------- #
    logger = StdoutLogger(print_freq=cfg.get("logging", {}).get("print_freq", 100))

    # ---------------- Evaluation Loop ---------------- #
    preds: List[float] = []
    gts: List[int] = []

    logger.on_train_start()  # 재사용
    with torch.no_grad():
        for step, batch in enumerate(tqdm(loader, desc="Evaluating")):
            batch = batch.to(device)
            out = model(batch)  # (B,) logits or prob
            if out.dim() > 1:
                out = out.squeeze(-1)
            prob = torch.sigmoid(out).cpu().tolist()
            preds.extend(prob)
            gts.extend(batch.y.cpu().tolist())  # 데이터셋에서 .y 레이블 필드 가정
            logger.on_step_end(step=step, loss=0.0)  # loss 없음 → placeholder

    logger.on_train_end()

    # ---------------- Metric 계산 ---------------- #
    y_true = torch.tensor(gts)
    y_score = torch.tensor(preds)

    metrics_to_run = cfg.get("metrics", ["auroc", "f1", "ap"])
    results: Dict[str, float] = {}
    if "auroc" in metrics_to_run:
        results["AUROC"] = roc_auc_score(y_true, y_score).item()
    if "ap" in metrics_to_run:
        results["mAP"] = average_precision_score(y_true, y_score).item()
    if "f1" in metrics_to_run:
        y_pred = (y_score >= 0.5).int()
        results["F1@0.5"] = f1_score(y_true, y_pred).item()

    # ---------------- 결과 출력 ---------------- #
    print("\n=== Evaluation Metrics ===")
    for k, v in results.items():
        print(f"{k:<8}: {v:.4f}")

    # ---------------- JSON 저장 ---------------- #
    Path(args.out).write_text(json.dumps(results, indent=2))
    print(f"\nSaved metrics → {args.out}")


# ---------------- Entry ---------------- #
if __name__ == "__main__":
    main()
