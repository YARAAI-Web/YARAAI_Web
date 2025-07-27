"""
auto_aug.search
===============
AutoAug RL 탐색 루프 (REINFORCE + moving baseline).

✔️ 핵심 함수
    run_search(controller, reward_fn, ...)
        → 최적 policy, history 로그, 체크포인트 저장

✔️ 의존
    - controller.sample_policy()   → (ops_list, log_prob, entropy)
    - reward_fn(ops_list)          → float (높을수록 좋음)

사용 예시
---------
>>> from augment.auto_aug.controller import OperationSpace, LSTMController
>>> from augment.auto_aug.search import run_search
>>>
>>> op_space = OperationSpace({ ... }, max_seq_len=4)
>>> controller = LSTMController(op_space).to('cuda')
>>>
>>> def reward_fn(ops):  # Contrastive val AUROC ↑
...     view_gen = build_view("StandardPair", ops_a=ops, ops_b=ops)
...     return evaluate_val_auroc(view_gen)   # 구현은 사용자 몫
>>>
>>> best_ops, log_hist = run_search(
...     controller,
...     reward_fn,
...     num_iters=1000,
...     lr=0.00035,
...     entropy_weight=0.01,
...     out_yaml="auto_aug/best_policy.yaml",
... )
"""
from __future__ import annotations

import math
import os
from pathlib import Path
from typing import Callable, Dict, List, Tuple

import torch
import torch.optim as optim
import yaml

from augment import build_view
from augment.auto_aug.controller import LSTMController


# ──────────────────────────────────────────────────────────────
# 1. 보조: policy → YAML 직렬화
# ──────────────────────────────────────────────────────────────
def policy_to_yaml(ops: List, path: str | os.PathLike) -> None:
    """
    AugmentBase 리스트를 YAML(dict) 형식으로 저장 (StandardPair 기준).

    저장 예:
        view: StandardPair
        ops_a:
          - {name: NodeDrop, keep_prob: 0.3}
        ops_b:  # 동일
          - {name: NodeDrop, keep_prob: 0.3}
    """
    def _op2dict(op):
        cfg = {"name": op.name}
        cfg.update(op.hyperparams())
        return cfg

    cfg_yaml = {
        "view": "StandardPair",
        "ops_a": [_op2dict(o) for o in ops],
        "ops_b": [_op2dict(o) for o in ops],
    }

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open("w", encoding="utf-8") as f:
        yaml.safe_dump(cfg_yaml, f, sort_keys=False)


# ──────────────────────────────────────────────────────────────
# 2. 메인: REINFORCE 학습 루프
# ──────────────────────────────────────────────────────────────
def run_search(
    controller: LSTMController,
    reward_fn: Callable[[List], float],
    num_iters: int = 1000,
    baseline_momentum: float = 0.9,
    lr: float = 3.5e-4,
    entropy_weight: float = 0.01,
    grad_clip: float | None = 5.0,
    device: str | torch.device = "cpu",
    out_yaml: str | os.PathLike | None = None,
    verbose: int = 100,
) -> Tuple[List, List[Dict[str, float]]]:
    """
    Parameters
    ----------
    controller : LSTMController
        Policy 샘플러 (nn.Module)
    reward_fn : callable(policy_ops) -> float
        높을수록 좋은 scalar reward 반환
    num_iters : int
        REINFORCE 업데이트 횟수
    baseline_momentum : float
        이동 평균 baseline β (0=no baseline)
    lr : float
        Adam learning rate
    entropy_weight : float
        탐색 다양성 유도를 위한 -entropy 계수
    grad_clip : float | None
        total grad L2 clip (None=미사용)
    device : torch.device
        controller 파라미터 및 연산 디바이스
    out_yaml : str | None
        최선(policy) YAML 저장 경로 (None=미저장)
    verbose : int
        iteration logging 주기

    Returns
    -------
    best_policy_ops : list[AugmentBase]
    log_history : list[dict] (iter, reward, baseline, loss, best_reward)
    """
    controller = controller.to(device)
    opt = optim.Adam(controller.parameters(), lr=lr)

    baseline = 0.0
    best_reward = -math.inf
    best_policy: List = []
    history: List[Dict[str, float]] = []

    for it in range(1, num_iters + 1):
        # -- 1. Policy 샘플링
        ops_list, log_prob, entropy = controller.sample_policy()
        reward = reward_fn(ops_list)

        # -- 2. Baseline 업데이트 (moving avg)
        if baseline_momentum > 0.0:
            baseline = baseline_momentum * baseline + (1 - baseline_momentum) * reward

        # -- 3. REINFORCE loss
        advantage = reward - baseline
        loss = -log_prob * advantage - entropy_weight * entropy

        # -- 4. Backprop
        opt.zero_grad()
        loss.backward()
        if grad_clip is not None:
            torch.nn.utils.clip_grad_norm_(controller.parameters(), grad_clip)
        opt.step()

        # -- 5. 기록
        if reward > best_reward:
            best_reward = reward
            best_policy = [p for p in ops_list]  # deepcopy X – 이미 새 인스턴스
            if out_yaml:
                policy_to_yaml(best_policy, out_yaml)

        if it % verbose == 0 or it == 1:
            print(
                f"[Iter {it:04d}] reward={reward:.4f} "
                f"baseline={baseline:.4f} best={best_reward:.4f} "
                f"loss={loss.item():.4f}"
            )

        history.append(
            {
                "iter": it,
                "reward": reward,
                "baseline": baseline,
                "loss": loss.item(),
                "best_reward": best_reward,
            }
        )

    if out_yaml:
        print(f"[AutoAug] Best policy saved → {out_yaml}")

    return best_policy, history
