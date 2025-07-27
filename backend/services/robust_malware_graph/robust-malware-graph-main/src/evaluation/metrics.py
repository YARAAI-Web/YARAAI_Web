# src/evaluation/metrics.py
"""
공통 메트릭 유틸리티

▪ Classification  : Accuracy, F1, AUROC, AUPRC, ConfusionMatrix
▪ Contrastive     : Alignment, Uniformity
▪ Robustness/Time : LatencyMeter
모든 Metric 클래스는
    m = Accuracy(topk=(1,))   # 생성
    m.update(logits, target)  # 반복
    score = m.compute()       # 최종 값
형태로 사용하며, DDP 상황에서도 자동 합산·평균됩니다.
"""

from __future__ import annotations

import math
import time
from collections import defaultdict
from typing import List, Sequence, Tuple, Union

import torch
import torch.distributed as dist

# ────────────────────────────── helper ──────────────────────────────────────
def _to_cpu(t: Union[torch.Tensor, Sequence]) -> torch.Tensor:
    return t.detach().cpu() if isinstance(t, torch.Tensor) else torch.as_tensor(t)


def _ddp_reduce(t: torch.Tensor, op: str = "sum") -> torch.Tensor:
    """DDP all-reduce; non-DDP 환경에서는 no-op."""
    if dist.is_available() and dist.is_initialized():
        t = t.clone()
        dist.all_reduce(t, dist.ReduceOp.SUM)
        if op == "mean":
            t /= dist.get_world_size()
    return t


# ───────────────────────────── base class ───────────────────────────────────
class Metric:
    def __init__(self):  # noqa: D401
        self.reset()

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def compute(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    __call__ = lambda self: self.compute()  # type: ignore


# ─────────────────────────── classification ────────────────────────────────
class Accuracy(Metric):
    """Top-k Accuracy"""

    def __init__(self, topk: Tuple[int, ...] = (1,)):
        super().__init__()
        self.topk = tuple(sorted(set(topk)))

    def reset(self):
        self.correct = torch.zeros(len(self.topk), dtype=torch.long)
        self.total = torch.tensor(0, dtype=torch.long)

    @torch.no_grad()
    def update(self, logits: torch.Tensor, target: torch.Tensor):
        maxk = max(self.topk)
        bsz = target.size(0)

        _, pred = logits.topk(maxk, dim=1)
        pred = pred.t()  # (maxk, B)
        correct_mat = pred.eq(target.view(1, -1).expand_as(pred))

        for i, k in enumerate(self.topk):
            self.correct[i] += correct_mat[:k].flatten().sum().cpu()
        self.total += bsz

    def compute(self):
        acc = self.correct.float() * 100.0 / self.total.clamp(min=1)
        acc = _ddp_reduce(acc, "mean")
        return tuple(acc.tolist()) if len(self.topk) > 1 else acc.item()


class F1(Metric):
    """(Macro)-F1.  multi-label→threshold, multi-class→argmax"""

    def __init__(self, average: str = "macro", threshold: float = 0.5):
        from sklearn.metrics import f1_score

        super().__init__()
        self.average, self.threshold = average, threshold
        self._f1 = f1_score

    def reset(self):
        self.preds, self.targets = [], []

    @torch.no_grad()
    def update(self, logits: torch.Tensor, target: torch.Tensor):
        self.preds.append(_to_cpu(logits))
        self.targets.append(_to_cpu(target))

    def compute(self):
        y_pred = torch.cat(self.preds).numpy()
        y_true = torch.cat(self.targets).numpy()
        if y_true.ndim == 2:  # multi-label
            y_pred = (y_pred > self.threshold).astype(int)
        else:                 # single-label
            y_pred = y_pred.argmax(1)
        return float(self._f1(y_true, y_pred, average=self.average))


class AUROC(Metric):
    def __init__(self, average: str = "macro"):
        from sklearn.metrics import roc_auc_score

        super().__init__()
        self.average, self._roc = average, roc_auc_score

    def reset(self):
        self.preds, self.targets = [], []

    @torch.no_grad()
    def update(self, probs: torch.Tensor, target: torch.Tensor):
        self.preds.append(_to_cpu(probs))
        self.targets.append(_to_cpu(target))

    def compute(self):
        y_pred = torch.cat(self.preds).numpy()
        y_true = torch.cat(self.targets).numpy()
        try:
            score = self._roc(
                y_true,
                y_pred,
                average=self.average,
                multi_class="ovr" if y_pred.shape[-1] > 1 and y_true.ndim == 1 else "raise",
            )
        except ValueError:  # 클래스 편향 등
            score = float("nan")
        return float(score)


class AUPRC(Metric):
    def __init__(self, average: str = "macro"):
        from sklearn.metrics import average_precision_score

        super().__init__()
        self.average, self._ap = average, average_precision_score

    def reset(self):
        self.preds, self.targets = [], []

    @torch.no_grad()
    def update(self, probs: torch.Tensor, target: torch.Tensor):
        self.preds.append(_to_cpu(probs))
        self.targets.append(_to_cpu(target))

    def compute(self):
        y_pred = torch.cat(self.preds).numpy()
        y_true = torch.cat(self.targets).numpy()
        return float(self._ap(y_true, y_pred, average=self.average))


class ConfusionMatrix(Metric):
    def __init__(self, num_classes: int):
        super().__init__()
        self.num_classes = num_classes

    def reset(self):
        self.mat = torch.zeros((self.num_classes, self.num_classes), dtype=torch.long)

    @torch.no_grad()
    def update(self, logits: torch.Tensor, target: torch.Tensor):
        pred = logits.argmax(1)
        cm = torch.zeros_like(self.mat)
        for t, p in zip(target.view(-1), pred.view(-1)):
            cm[t, p] += 1
        self.mat += cm.cpu()

    def compute(self):
        return _ddp_reduce(self.mat, "sum")


# ─────────────────────── contrastive representation ────────────────────────
def _sq_pairwise(x, y):
    return (x - y).pow(2).sum(1)


class Alignment(Metric):
    """GraphCL Alignment:  mean ||z1 − z2||₂"""

    def reset(self):
        self.sum, self.cnt = torch.tensor(0.0), torch.tensor(0)

    @torch.no_grad()
    def update(self, z1: torch.Tensor, z2: torch.Tensor):
        self.sum += _sq_pairwise(z1, z2).sqrt().sum().cpu()
        self.cnt += z1.size(0)

    def compute(self):
        val = self.sum / self.cnt.clamp(min=1)
        return _ddp_reduce(val, "mean").item()


class Uniformity(Metric):
    """Uniformity: log( mean exp(-2 ||zi − zj||²) )"""

    def reset(self):
        self.sum_exp, self.cnt = torch.tensor(0.0), torch.tensor(0)

    @torch.no_grad()
    def update(self, z: torch.Tensor):
        z = torch.nn.functional.normalize(z, dim=1)
        cos = z @ z.t()
        sqd = 2 - 2 * cos
        mask = ~torch.eye(z.size(0), dtype=torch.bool, device=z.device)
        self.sum_exp += torch.exp(-sqd[mask]).sum().cpu()
        self.cnt += z.size(0) * (z.size(0) - 1)

    def compute(self):
        val = torch.log(self.sum_exp / self.cnt.clamp(min=1))
        return _ddp_reduce(val, "mean").item()


# ───────────────────────────── latency ─────────────────────────────────────
class LatencyMeter(Metric):
    """평균 추론 시간 (ms / 샘플)"""

    def reset(self):
        self.total_ms, self.samples = 0.0, 0
        self._tic = None

    def start(self):
        torch.cuda.synchronize() if torch.cuda.is_available() else None
        self._tic = time.perf_counter()

    def stop(self, n: int = 1):
        if self._tic is None:
            raise RuntimeError("LatencyMeter.stop() before start()")
        torch.cuda.synchronize() if torch.cuda.is_available() else None
        self.total_ms += (time.perf_counter() - self._tic) * 1e3
        self.samples += n
        self._tic = None

    def update(self, *args, **kwargs):
        """dummy: 사용 안 함"""

    def compute(self):
        avg = self.total_ms / max(1, self.samples)
        return _ddp_reduce(torch.tensor(avg), "mean").item()


# ──────────────────────────── pretty print ─────────────────────────────────
def format_metrics(metrics: dict[str, Metric]) -> str:
    """로그용 문자열 """
    outs = []
    for k, m in metrics.items():
        v = m.compute()
        if isinstance(v, (tuple, list)):
            outs.append(f"{k}: {', '.join(f'{x:.3f}' for x in v)}")
        elif isinstance(v, torch.Tensor):
            outs.append(f"{k}: {v.tolist()}")
        else:
            outs.append(f"{k}: {v:.4f}")
    return " | ".join(outs)
