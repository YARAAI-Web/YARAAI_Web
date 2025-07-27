"""
src.continual.evaluation.evaluator
==================================
Continual Learning 용 범용 평가 루틴.

주요 구성
---------
* BatchEvaluator : 단일 DataLoader → 지정 메트릭 계산
* ContinualEvaluator
    - task-incremental 평가 (학습 후 각 태스크 성능 측정)
    - CLMatrix 자동 갱신 (final ACC, BWT, FWT, Forgetting 등)
* OnlineEvaluator : 스트리밍 환경에서 로그-프리 AUROC 포함 실시간 지표

사용 전제
---------
모델 forward(x) → raw logits (… , C)
DataLoader 에서 (data, labels) 튜플 또는
torch_geometric.data.Data / HeteroData (labels 는 .y 속성) 반환.

필요 의존
---------
numpy, torch, scikit-learn ▶ metrics.py
"""

from __future__ import annotations

import contextlib
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence

import numpy as np
import torch
from torch.utils.data import DataLoader

from .metrics import (
    CLMatrix,
    OnlineAUC,
    auroc,
    f1_score_macro,
    topk_accuracy,
)

__all__ = [
    "BatchEvaluator",
    "ContinualEvaluator",
    "OnlineEvaluator",
]

# --------------------------------------------------------------------------- #
# 1. 단일 로더 평가 ----------------------------------------------------------- #
# --------------------------------------------------------------------------- #
_METRIC_FUNCS = {
    "acc": topk_accuracy,
    "auroc": auroc,
    "f1": f1_score_macro,
}

class BatchEvaluator:
    """
    한 DataLoader 전체에 대한 분류 지표 산출기.

    Parameters
    ----------
    metrics : Sequence[str], default=("acc",)
        {"acc", "auroc", "f1"} 중 선택.
    multi_label : bool, default=False
        True → y.shape=(N, L) 0/1 매트릭스 다중 라벨.
    topk : int, default=1
        "acc" 선택 시 Top-k.
    device : str | torch.device, default="cpu"
        배치 데이터를 복사할 디바이스.
    """

    def __init__(
        self,
        metrics: Sequence[str] | None = None,
        *,
        multi_label: bool = False,
        topk: int = 1,
        device: str | torch.device = "cpu",
    ) -> None:
        if metrics is None:
            metrics = ("acc",)
        for m in metrics:
            if m not in _METRIC_FUNCS:
                raise KeyError(f"Unknown metric: {m}")
        self.metrics = tuple(metrics)
        self.multi_label = multi_label
        self.topk = topk
        self.device = torch.device(device)
        self._y_true: list[np.ndarray] = []
        self._y_score: list[np.ndarray] = []

    # ------------------- Public API ------------------------------------ #
    def reset(self) -> None:  # noqa: D401
        """모든 내부 버퍼 초기화."""
        self._y_true.clear()
        self._y_score.clear()

    def update(
        self,
        logits: torch.Tensor,
        labels: torch.Tensor | np.ndarray,
    ) -> None:
        """
        한 배치 결과를 버퍼에 추가.

        logits : (B, C) raw score
        labels : (B,) or (B, L)
        """
        self._y_score.append(logits.detach().cpu().float().numpy())
        self._y_true.append(
            labels.detach().cpu().float().numpy()
            if isinstance(labels, torch.Tensor)
            else np.asarray(labels)
        )

    def compute(self) -> Dict[str, float]:
        """`metrics` 이름 → 스칼라 값 dict 반환."""
        y_true = np.concatenate(self._y_true, axis=0)
        y_score = np.concatenate(self._y_score, axis=0)

        y_pred = (
            y_score.argmax(-1) if y_score.ndim == 2 and not self.multi_label else None
        )
        out: dict[str, float] = {}

        for m in self.metrics:
            if m == "acc":
                out["acc"] = topk_accuracy(
                    y_score, y_true, k=self.topk
                )
            elif m == "auroc":
                out["auroc"] = auroc(
                    y_score, y_true, multi_label=self.multi_label, average="macro"
                )
            elif m == "f1":
                if y_pred is None:
                    raise RuntimeError("f1: multi-label엔 사용 불가")
                out["f1"] = f1_score_macro(y_pred, y_true)
        return out


# --------------------------------------------------------------------------- #
# 2. Task-incremental Continual 평가 ----------------------------------------- #
# --------------------------------------------------------------------------- #
class ContinualEvaluator:
    """
    Task-IL (offline 단계별 학습) 평가 유틸리티.

    예)
    ----
    >>> ceval = ContinualEvaluator(model, num_tasks=5, device="cuda")
    >>> for t, loader in enumerate(task_loaders):
    ...     train_one_task(t)              # 사용자 코드
    ...     ceval.evaluate_task(t, loader) # 성능 기록
    >>> print("Final ACC :", ceval.cl_matrix.final_acc())
    """

    def __init__(
        self,
        model: torch.nn.Module,
        num_tasks: int,
        *,
        metrics: Sequence[str] | None = ("acc",),
        multi_label: bool = False,
        topk: int = 1,
        device: str | torch.device = "cpu",
    ) -> None:
        self.model = model
        self.device = torch.device(device)
        self.model.to(self.device)

        self.batch_eval = BatchEvaluator(
            metrics, multi_label=multi_label, topk=topk, device=self.device
        )
        self.cl_matrix = CLMatrix(num_tasks)
        self.history: list[dict[str, float]] = []

    # ----------------- Core -------------------------------------------- #
    @torch.no_grad()
    def evaluate_task(
        self,
        task_id: int,
        loader: DataLoader,
        *,
        progress_bar: bool | str = False,
    ) -> Dict[str, float]:
        """
        task_id 학습 직후, 해당 loader 로 모든 메트릭 측정.

        loader : 샘플·배치 순서는 무관 (shuffle=False 권장)
        progress_bar:
            True  → tqdm 표시
            str   → desc 로 tqdm 표시
            False → 비표시
        """
        self.model.eval()
        self.batch_eval.reset()

        iterator: Iterable = loader
        if progress_bar:
            try:
                from tqdm.auto import tqdm
                desc = progress_bar if isinstance(progress_bar, str) else f"Eval T{task_id}"
                iterator = tqdm(loader, desc=desc, leave=False)
            except ModuleNotFoundError:  # pragma: no cover
                pass

        for batch in iterator:
            data, labels = _split_batch(batch)
            data = _move_to_device(data, self.device)
            labels = labels.to(self.device) if isinstance(labels, torch.Tensor) else labels
            logits = self.model(data)
            self.batch_eval.update(logits, labels)

        metrics = self.batch_eval.compute()
        # CLMatrix 는 주 메트릭 (acc) 로 기록하는 것이 일반적
        main_metric = metrics.get("acc") or next(iter(metrics.values()))
        self.cl_matrix.update(task_id, [main_metric])
        self.history.append(metrics)
        return metrics

    # ----------------- Convenience ------------------------------------- #
    def save_history(self, path: str | Path) -> None:
        """CSV 로 메트릭 log 저장."""
        import csv, os
        path = Path(path)
        if not path.parent.exists():
            os.makedirs(path.parent, exist_ok=True)
        with path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.history[0].keys())
            writer.writeheader()
            writer.writerows(self.history)


# --------------------------------------------------------------------------- #
# 3. Online / Streaming 평가 ------------------------------------------------- #
# --------------------------------------------------------------------------- #
class OnlineEvaluator:
    """
    스트리밍 데이터에서 O(1) 메모리 AUROC, 정확도 추적.

    >>> oe = OnlineEvaluator()
    >>> for data, label in stream_loader:
    ...     score = model(data)
    ...     oe.update(score, label)
    >>> print(oe.compute())
    """

    def __init__(self) -> None:
        self.auc_meter = OnlineAUC()
        self.correct = 0
        self.total = 0

    def update(
        self,
        logits: torch.Tensor | np.ndarray,
        labels: torch.Tensor | np.ndarray,
    ) -> None:
        if isinstance(logits, torch.Tensor):
            logits = logits.detach().cpu().float().numpy()
        if isinstance(labels, torch.Tensor):
            labels = labels.detach().cpu().numpy()
        # binary assumption (sigmoid > 0.5)
        preds = (logits.ravel() > 0).astype(int)
        self.correct += int((preds == labels).sum())
        self.total += labels.size
        self.auc_meter.update(logits.ravel(), labels.ravel())

    def compute(self) -> Mapping[str, float]:
        return {
            "acc": self.correct / max(self.total, 1),
            "auroc": self.auc_meter.compute(),
        }


# --------------------------------------------------------------------------- #
# 4. 헬퍼 -------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
def _split_batch(batch):
    """
    다양한 Loader 반환 타입 지원.

    - (data, labels)
    - torch_geometric.data.Data : batch.y
    """
    if isinstance(batch, (tuple, list)) and len(batch) == 2:
        return batch
    # PyG Data/HeteroData 일때
    if hasattr(batch, "y"):
        return batch, batch.y
    raise TypeError("Batch format not supported")


def _move_to_device(obj, device):
    """Tensor/Data/HeteroData 재귀 디바이스 이동."""
    if torch.is_tensor(obj):
        return obj.to(device)
    # PyG Data 객체인 경우
    if hasattr(obj, "to"):
        return obj.to(device)
    if isinstance(obj, Mapping):
        return {k: _move_to_device(v, device) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return type(obj)(_move_to_device(x, device) for x in obj)
    return obj  # numpy/others 그대로
