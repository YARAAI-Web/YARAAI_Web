"""
src.continual.evaluation.metrics
================================
Continual-/Incremental-/Task-IL 학습 시 자주 쓰이는 핵심 지표 모음.

구현한 지표
-----------
* topk_accuracy  : Top-k 분류 정확도 (k=1 → Top-1 ACC)
* auroc          : (멀티)라벨 AUROC
* f1_score_macro : 다중 클래스/라벨 macro-F1
* CLMatrix       : R_(t, i) 행렬 기반 지표
    - final_acc          : 마지막 시점 전체 평균 정확도 (ACC)
    - backward_transfer  : Backward Transfer (BWT)
    - forward_transfer   : Forward Transfer  (FWT, 옵셔널 baseline)
    - forgetting         : Avg. Forgetting (delta↓)
* OnlineAUC      : 스트리밍 AUROC 계산기 (메모리 O(1))

참고 문헌
----------
Lopez-Paz & Ranzato, *“Gradient Episodic Memory for CL”*, NeurIPS 2017
Chaudhry et al., *“Efficient Lifelong Learning with A-GEM”*, ICLR 2019
"""

from __future__ import annotations

import math
import warnings
from collections import deque
from typing import Iterable, List, Optional, Sequence, Tuple

import numpy as np
import torch

try:
    from sklearn.metrics import (
        accuracy_score,
        f1_score,
        roc_auc_score,
    )
except ImportError as e:  # pragma: no cover
    raise ImportError(
        "`sklearn`가 필요합니다.  ➜  pip install scikit-learn"
    ) from e


# --------------------------------------------------------------------------- #
# 1. 배치 단위 기본 분류 지표 -------------------------------------------------- #
# --------------------------------------------------------------------------- #
def _to_numpy(x: torch.Tensor | np.ndarray | Sequence) -> np.ndarray:
    """Tensor/리스트 등을 np.ndarray(float64) 로 변환."""
    if isinstance(x, torch.Tensor):
        x = x.detach().cpu().numpy()
    return np.asarray(x)


def topk_accuracy(
    logits: torch.Tensor | np.ndarray,
    labels: torch.Tensor | np.ndarray,
    k: int = 1,
) -> float:
    """
    Top-k accuracy (k=1 → Top-1 ACC).

    Parameters
    ----------
    logits : [..., C]
        모델 raw logit 또는 확률. 마지막 dim = #classes.
    labels : [...]
        정답 라벨 (int)
    k : int, default=1
        상위 k 예측 중 정답 포함 여부.

    Returns
    -------
    float
    """
    logits_np, labels_np = _to_numpy(logits), _to_numpy(labels).astype(int)
    topk = np.argpartition(logits_np, -k, axis=-1)[..., -k:]
    correct = (topk == labels_np[..., None]).any(axis=-1)
    return float(correct.mean())


def auroc(
    y_score: torch.Tensor | np.ndarray,
    y_true: torch.Tensor | np.ndarray,
    *,
    multi_label: bool = False,
    average: str = "macro",
) -> float:
    """
    AUROC (binary, multi-class → ovr, multi-label supported).

    Parameters
    ----------
    y_score : [..., C] or [..., L]
        확률/로짓.
    y_true  : [...]               (int/float/bool)
        정답. 멀티라벨의 경우 0/1 벡터.
    multi_label : bool, default=False
        True → y_true/score 둘 다 shape=(N, L) 인 multi-label.
    average : {"macro", "micro", "weighted", None}
        sklearn macro 등 averaging 방식.

    Returns
    -------
    float
    """
    y_true_np, y_score_np = _to_numpy(y_true), _to_numpy(y_score)
    if multi_label:
        return roc_auc_score(y_true_np, y_score_np, average=average)
    if y_score_np.ndim == 1 or y_score_np.shape[-1] == 1:  # Binary
        return roc_auc_score(y_true_np, y_score_np)
    # Multi-class → OVR
    return roc_auc_score(y_true_np, y_score_np, multi_class="ovr", average=average)


def f1_score_macro(
    y_pred: torch.Tensor | np.ndarray,
    y_true: torch.Tensor | np.ndarray,
) -> float:
    """Macro-averaged F1 (다중 클래스/라벨 모두 지원)."""
    return f1_score(
        _to_numpy(y_true), _to_numpy(y_pred), average="macro", zero_division=0
    )


# --------------------------------------------------------------------------- #
# 2. Task-IL 평가 행렬 R(t, i) ------------------------------------------------ #
# --------------------------------------------------------------------------- #
class CLMatrix:
    """
    Continual-/Incremental-/Task-IL 성능 행렬.

    행 t  : task t 학습 직후 evaluate 모든 task i
    열 i  : task i 데이터셋에서 측정한 metric (보통 accuracy)

    예)
    >>> R = CLMatrix(num_tasks=3)
    >>> R.update(0, [0.81])        # task0 학습 후
    >>> R.update(1, [0.79, 0.84])  # task1 학습 후
    >>> R.update(2, [0.75, 0.82, 0.90])
    >>> R.backward_transfer()      # 평균 BWT
    """

    def __init__(self, num_tasks: int):
        self.R = np.full((num_tasks, num_tasks), np.nan, dtype=np.float32)
        self._last_frozen_row = -1

    # ----- Row 업데이트 --------------------------------------------------- #
    def update(self, task_id: int, metric_vector: Sequence[float]) -> None:
        """
        task `task_id` 학습 직후 얻은 각 task별 metric 벡터를 행렬에 기록.

        `metric_vector[i]` 는 task i에 대한 metric.
        """
        if task_id < self._last_frozen_row:  # pragma: no cover
            raise ValueError(
                f"Row {task_id} already frozen. "
                "새로운 실험이면 새 CLMatrix 를 만들 것."
            )
        self.R[task_id, : len(metric_vector)] = np.asarray(metric_vector, float)
        self._last_frozen_row = task_id

    # ----- 대표 지표 ------------------------------------------------------ #
    def final_acc(self) -> float:
        """마지막 row(전체 학습 완료 후)의 평균 정확도 (ACC)."""
        last = self.R[self._last_frozen_row]
        return float(np.nanmean(last))

    def backward_transfer(self) -> float:
        """
        BWT = mean_{i < T-1} (R_{T-1, i} − R_{i, i})

        • 양수 → 학습이 이전 태스크까지 개선
        • 음수 → ‘잊힘’(catastrophic forgetting) 발생
        """
        T = self._last_frozen_row + 1
        if T < 2:
            return math.nan
        final_row = self.R[T - 1, : T - 1]
        diag_before = np.diag(self.R)[: T - 1]
        return float(np.nanmean(final_row - diag_before))

    def forgetting(self) -> float:
        """
        Average Forgetting
        ------------------
        F = mean_i max_{t < T_i} R_{t,i} − R_{T-1, i}

        개별 task별로 가장 높은 성능과 최종 성능 차이를 평균.
        """
        T = self._last_frozen_row + 1
        max_before = np.nanmax(self.R[: T - 1], axis=0)[: T]
        final = self.R[T - 1, : T]
        return float(np.nanmean(max_before - final))

    def forward_transfer(
        self, baselines: Optional[Sequence[float]] = None
    ) -> float:
        """
        FWT = mean_{i > 0} (R_{i-1, i} − b_i)

        baselines
            0-shot 성능(모델 랜덤 init, pretrain 등) 벡터.
            길이 < num_tasks이면 자동 zero-padding.
        """
        T = self._last_frozen_row + 1
        if T < 2:
            return math.nan
        prev_row_diag = np.diag(self.R, k=1)[: T - 1]  # R_{i-1, i}
        if baselines is None:
            baselines = np.zeros_like(prev_row_diag)
        else:
            baselines = np.asarray(baselines, float)
            if baselines.size < prev_row_diag.size:
                baselines = np.pad(
                    baselines, (0, prev_row_diag.size - baselines.size)
                )
        return float(np.nanmean(prev_row_diag - baselines))

    # ----- 유틸 ----------------------------------------------------------- #
    def as_numpy(self) -> np.ndarray:
        """R 행렬을 (deep-copy) 반환."""
        return self.R.copy()

    def __repr__(self) -> str:  # pragma: no cover
        with np.printoptions(precision=3, suppress=True):
            return f"CLMatrix(R=\n{self.R}\n)"


# --------------------------------------------------------------------------- #
# 3. 온라인 스트리밍 AUROC --------------------------------------------------- #
# --------------------------------------------------------------------------- #
class OnlineAUC:
    """
    O(1) 메모리 & 업데이트 비용으로 AUROC 근사.

    Hand & Till(2001) incremental U-statistic 이용
    (binary, 확률 점수 1-차원 한정).

    >>> auc_meter = OnlineAUC()
    >>> auc_meter.update(scores, labels)
    >>> auc_meter.compute()
    """

    __slots__ = ("n_pos", "n_neg", "rank_sum")

    def __init__(self) -> None:
        self.n_pos = 0
        self.n_neg = 0
        self.rank_sum = 0.0  # ∑ rank(pos)

    def update(
        self,
        scores: torch.Tensor | np.ndarray | Sequence[float],
        labels: torch.Tensor | np.ndarray | Sequence[int],
    ) -> None:
        s, y = _to_numpy(scores), _to_numpy(labels).astype(int)
        if s.shape != y.shape:
            raise ValueError("scores, labels shape mismatch")
        # 순위 계산 (작을수록 낮은 점수)
        order = np.argsort(s)
        ranks = np.empty_like(order, dtype=float)
        ranks[order] = np.arange(1, s.size + 1)
        # pos 샘플 rank 합산
        pos_mask = y == 1
        self.rank_sum += float(ranks[pos_mask].sum())
        self.n_pos += int(pos_mask.sum())
        self.n_neg += int((~pos_mask).sum())

    def compute(self) -> float:
        """현재까지 누적 AUROC (WMW-U 통계)."""
        if self.n_pos == 0 or self.n_neg == 0:
            warnings.warn("Positive/negative 샘플이 부족하여 AUROC=N/A")
            return math.nan
        u = self.rank_sum - self.n_pos * (self.n_pos + 1) / 2
        return u / (self.n_pos * self.n_neg)
