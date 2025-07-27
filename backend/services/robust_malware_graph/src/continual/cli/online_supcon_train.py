"""
src.continual.cli.online_supcon_train
=====================================

Hydra 없이 가벼운 argparse로 구성한 온라인 SupCon 학습 스크립트.
• 그래프: torch_geometric Data 객체 필수  🚨
• 모델: continual.learner.OnlineSupConLearner  (encoder + SupContrastHead)
• 콜백: StdoutLogger, TensorBoardLogger, EarlyStopping, ModelCheckpoint
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

import torch
import yaml
from torch_geometric.loader import DataLoader
from tqdm.auto import tqdm

# --- 내부 모듈 -------------------------------------------------------------- #
from continual.utils import set_random_seed
from continual.callbacks import (
    CallbackManager,
    StdoutLogger,
    TensorBoardLogger,
    EarlyStopping,
    ModelCheckpoint,
)
from continual.learner.supcon_cl import OnlineSupConLearner
from graphs.dataset.graph_dataset import GraphDataset  # PyG Dataset 래퍼

# --------------------------------------------------------------------------- #
# 1. CLI 인자 파싱
# --------------------------------------------------------------------------- #
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Online SupCon training (streaming graphs)")
    p.add_argument("--config", type=str, default="configs/sup_con.yaml", help="YAML config path")
    p.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    return p.parse_args()


# --------------------------------------------------------------------------- #
# 2. 주요 진입점
# --------------------------------------------------------------------------- #
def main() -> None:
    args = parse_args()
    cfg: Dict = yaml.safe_load(Path(args.config).read_text())

    # 재현성 & 디바이스
    set_random_seed(cfg.get("seed", 42))
    device = torch.device(args.device)

    # ---------------- 데이터 로드 (PyG) ---------------- #
    train_ds = GraphDataset(root=cfg["data"]["root"], split="train")
    val_ds = GraphDataset(root=cfg["data"]["root"], split="val")

    train_loader = DataLoader(
        train_ds,
        batch_size=cfg["training"]["batch_size"],
        shuffle=True,
        num_workers=cfg["training"].get("num_workers", 4),
        pin_memory=True,
    )
    val_loader = DataLoader(
        val_ds,
        batch_size=cfg["training"]["batch_size"],
        shuffle=False,
        num_workers=cfg["training"].get("num_workers", 4),
        pin_memory=True,
    )

    # ---------------- 모델 & 옵티마이저 ---------------- #
    learner = OnlineSupConLearner(cfg["model"]).to(device)
    optimizer = torch.optim.AdamW(
        learner.parameters(),
        lr=cfg["optim"]["lr"],
        weight_decay=cfg["optim"]["weight_decay"],
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=cfg["training"]["epochs"]
    )

    # ---------------- 콜백 초기화 ---------------- #
    callbacks = CallbackManager(
        StdoutLogger(print_freq=cfg["logging"].get("print_freq", 100)),
        TensorBoardLogger(log_dir=cfg["logging"].get("tb_dir", "./runs")),
        EarlyStopping(
            monitor="val_loss",
            mode="min",
            patience=cfg["training"].get("early_stop", 10),
        ),
        ModelCheckpoint(
            out_dir=cfg["logging"].get("ckpt_dir", "./ckpts"),
            monitor="val_loss",
            mode="min",
            save_freq=1,
        ),
    )

    # ---------------- 학습 루프 ---------------- #
    callbacks.on_train_start()
    for epoch in range(cfg["training"]["epochs"]):
        learner.train()
        callbacks.on_epoch_start(epoch=epoch)

        for step, batch in enumerate(tqdm(train_loader, desc=f"Epoch {epoch}")):
            batch = batch.to(device)
            loss = learner.training_step(batch, optimizer)
            callbacks.on_step_end(step=step, loss=loss.item())

        # --------- 검증 --------- #
        learner.eval()
        val_loss = 0.0
        with torch.no_grad():
            for batch in val_loader:
                batch = batch.to(device)
                val_loss += learner.validation_step(batch).item()
        val_loss /= max(1, len(val_loader))

        callbacks.on_epoch_end(
            epoch=epoch,
            val_loss=val_loss,
            model=learner,
            optimizer=optimizer,
            scheduler=scheduler,
        )

        if any(getattr(cb, "should_stop", False) for cb in callbacks):
            break

        scheduler.step()

    callbacks.on_train_end()

    # ------- 최고 성능 모델 저장 ------- #
    best_ckpt = next(
        (cb for cb in callbacks if isinstance(cb, ModelCheckpoint)), None
    )
    if best_ckpt and best_ckpt.best_state_dict:
        learner.load_state_dict(best_ckpt.best_state_dict)
        Path(best_ckpt.out_dir).mkdir(parents=True, exist_ok=True)
        torch.save(
            learner.state_dict(), Path(best_ckpt.out_dir) / "final_best.pt"
        )


# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    main()
