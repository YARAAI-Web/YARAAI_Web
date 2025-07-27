"""
auto_aug.controller
===================
LSTM 기반 *policy controller* – 강화학습으로 증강 시퀀스(Policy)를 샘플링.

● 핵심 클래스
    • OperationSpace   –  검색 공간 정의 (Op 목록 · 하이퍼파라미터 bins)
    • LSTMController   –  AutoAug 논문의 RNN Controller (REINFORCE 학습 가정)

사용 예
-------
>>> from augment.auto_aug.controller import OperationSpace, LSTMController
>>> from augment import build_op
>>>
>>> op_space = OperationSpace(
...     search_space={
...         "NodeDrop":   {"keep_prob": [0.1, 0.2, 0.3, 0.4]},
...         "EdgeDrop":   {"keep_prob": [0.1, 0.2, 0.3, 0.4]},
...         "AttrMask":   {"p":         [0.05, 0.1, 0.2]},
...         "InjectAPICall": {"k":      [1, 2, 3, 4]},
...         "CodeBlockSwap": {"prob_pair": [0.1, 0.2, 0.3]},
...     },
...     max_seq_len=4,          # 한 policy 당 Op 최대 4개
... )
>>> controller = LSTMController(op_space)
>>> policy, log_prob, ent = controller.sample_policy()
>>> # policy == [build_op(...), build_op(...), ...]  리스트
"""

from __future__ import annotations

import math
import random
from typing import Dict, List, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F

from augment import OPS_REGISTRY, build_op


# ──────────────────────────────────────────────────────────────
# 1. OperationSpace – 탐색 공간 정의
# ──────────────────────────────────────────────────────────────
class OperationSpace:
    """
    증강 Op 와 각 Op 의 discrete 하이퍼파라미터 bin 을 관리.

    Parameters
    ----------
    search_space : dict[str, dict[str, list]]
        {"OpName": {"param": [v1, v2, ...], ...}, ...}
    max_seq_len : int
        한 policy(뷰 시퀀스) 최대 길이.
    """

    def __init__(self, search_space: Dict[str, Dict[str, List]], max_seq_len: int = 4):
        self.op_names: List[str] = list(search_space.keys())
        self.params_map: Dict[str, Dict[str, List]] = search_space
        self.max_seq_len = max_seq_len

        # --- Op → 토큰 id 매핑
        self.op2id: Dict[str, int] = {op: i for i, op in enumerate(self.op_names)}
        self.id2op: Dict[int, str] = {i: op for op, i in self.op2id.items()}

        # --- param bins 길이 (head 별 출력 차원)
        self.param_bins: Dict[str, int] = {
            op: math.prod(len(v) for v in search_space[op].values())
            for op in self.op_names
        }

    # ---------------------------------------------------------
    # 헬퍼 – id ↔️ kwargs 변환
    # ---------------------------------------------------------
    def param_id2kwargs(self, op_name: str, param_id: int) -> Dict:
        """정수 param_id → 실제 kwargs dict 로 변환."""
        space = self.params_map[op_name]
        keys = list(space.keys())
        bins_per_key = [len(space[k]) for k in keys]
        kwargs: Dict = {}
        # 다차원 인덱스를 1차원 id 로 flatten 했던 것 역변환
        for i, k in enumerate(reversed(keys)):
            bins = bins_per_key[-(i + 1)]
            idx = param_id % bins
            param_id //= bins
            kwargs[k] = space[k][idx]
        return kwargs

    def kwargs2param_id(self, op_name: str, kwargs: Dict) -> int:
        """kwargs dict → flatten param_id (학습 중 사용 X, 평가용)."""
        space = self.params_map[op_name]
        keys = list(space.keys())
        bins_per_key = [len(space[k]) for k in keys]
        param_id = 0
        multiplier = 1
        for k, bins in reversed(list(zip(keys, bins_per_key))):
            idx = space[k].index(kwargs[k])
            param_id += idx * multiplier
            multiplier *= bins
        return param_id


# ──────────────────────────────────────────────────────────────
# 2. LSTMController
# ──────────────────────────────────────────────────────────────
class LSTMController(nn.Module):
    """
    LSTM 기반 AutoAug Controller.

    • 토큰 시퀀스: [<START>, op₁, param₁, op₂, param₂, ...]
    • Even step  → op logits   (|op_space|)
    • Odd  step  → param logits (op-specific |param_bins|)
    """

    def __init__(
        self,
        op_space: OperationSpace,
        embed_dim: int = 32,
        hidden_dim: int = 100,
        temperature: float = 1.0,
    ):
        super().__init__()
        self.op_space = op_space
        self.temperature = temperature

        # ---- 임베딩
        n_ops = len(op_space.op_names)
        self.start_token = nn.Parameter(torch.zeros(embed_dim), requires_grad=False)
        self.op_embedding = nn.Embedding(n_ops, embed_dim)

        # ---- LSTM
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)

        # ---- Heads
        self.op_head = nn.Linear(hidden_dim, n_ops)
        # 각 op 별 param_head (크기 가변)
        self.param_heads = nn.ModuleList(
            [
                nn.Linear(hidden_dim, op_space.param_bins[op])
                for op in op_space.op_names
            ]
        )

    # ---------------------------------------------------------
    # Sampling
    # ---------------------------------------------------------
    @torch.no_grad()
    def sample_policy(
        self,
        temperature: float | None = None,
    ) -> Tuple[List, torch.Tensor, torch.Tensor]:
        """
        Returns
        -------
        policy_ops : list[AugmentBase]
            build_op 로 생성된 증강 연산 리스트
        log_prob : torch.Tensor
            샘플링 log-prob 전체 합 (스칼라)
        entropy : torch.Tensor
            시퀀스 entropy 합 (스칼라) – REINFORCE 밸류베이스 사용 가능
        """
        T = temperature or self.temperature
        device = self.start_token.device

        inputs = self.start_token.unsqueeze(0).unsqueeze(0)  # (1,1,embed)
        hx, cx = (
            torch.zeros(1, 1, self.lstm.hidden_size, device=device),
            torch.zeros(1, 1, self.lstm.hidden_size, device=device),
        )

        log_probs = []
        entropies = []
        sampled_ops = []

        for step in range(self.op_space.max_seq_len):
            out, (hx, cx) = self.lstm(inputs, (hx, cx))  # out:(1,1,H)
            h = out.squeeze(1)  # (1,H)

            # (0) Op 선택
            logits_op = self.op_head(h) / T
            probs_op = F.softmax(logits_op, dim=-1)
            op_id = torch.multinomial(probs_op, 1).item()
            log_prob_op = torch.log(probs_op[0, op_id] + 1e-8)
            entropy_op = -(probs_op * torch.log(probs_op + 1e-8)).sum()

            op_name = self.op_space.id2op[op_id]

            # (1) Param 선택 – op-specific head
            logits_param = self.param_heads[op_id](h) / T
            probs_param = F.softmax(logits_param, dim=-1)
            param_id = torch.multinomial(probs_param, 1).item()
            log_prob_param = torch.log(probs_param[0, param_id] + 1e-8)
            entropy_param = -(probs_param * torch.log(probs_param + 1e-8)).sum()

            # (2) 기록
            log_probs += [log_prob_op, log_prob_param]
            entropies += [entropy_op, entropy_param]

            kwargs = self.op_space.param_id2kwargs(op_name, param_id)
            sampled_ops.append(build_op(op_name, **kwargs))

            # (3) 다음 step 입력 = 현재 op 임베딩
            inputs = self.op_embedding(torch.tensor([[op_id]], device=device))

        # ---- 결과 (정책, 로그확률 합계, 엔트로피 합계)
        log_prob = torch.stack(log_probs).sum()
        entropy = torch.stack(entropies).sum()
        return sampled_ops, log_prob, entropy


# ──────────────────────────────────────────────────────────────
# 3. 간단 테스트
#    (python -m augment.auto_aug.controller 로 실행 가능)
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # 임시 탐색 공간 예시
    search_space_example = {
        "NodeDrop": {"keep_prob": [0.1, 0.2, 0.3, 0.4]},
        "EdgeDrop": {"keep_prob": [0.1, 0.2, 0.3, 0.4]},
        "AttrMask": {"p": [0.05, 0.1, 0.2]},
    }

    op_space = OperationSpace(search_space_example, max_seq_len=3)
    controller = LSTMController(op_space)
    pol, lp, ent = controller.sample_policy()
    print([op.name for op in pol], lp.item(), ent.item())
