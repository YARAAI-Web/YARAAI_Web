"""
src.graphs.transforms.augment_bridge
====================================

GraphAugmentTransform
---------------------
‣ 학습 파이프라인에서 ``Dataset(transform=GraphAugmentTransform(cfg))`` 처럼
  손쉽게 **그래프 증강**(GraphCL·AutoAug·도메인 증강 등)을 삽입할 수 있도록
  중간 어댑터 계층을 제공한다.

작동 흐름
~~~~~~~~~
1. __init__(policy_cfg)
   └─ augment.registry.build(policy_cfg) 로 증강 파이프라인 인스턴스화
2. __call__(graph)  (PyG Data/HeteroData)
   └─ self.policy(graph) 로 실제 증강 수행
3. to/device()/cpu()/cuda() 등 PyTorch API pass-through 지원
"""

from __future__ import annotations

import inspect
from typing import Any, Dict, Protocol, runtime_checkable

import torch
from torch_geometric.data import Data, HeteroData

from ..utils import get_logger

# augment 패키지 레지스트리를 import
try:
    from augment import registry as aug_registry
except ModuleNotFoundError as e:  # pragma: no cover
    raise ImportError(
        "Cannot import 'augment.registry'. "
        "Ensure src/augment/__init__.py exposes `registry`."
    ) from e

GraphT = Data | HeteroData
_LOG = get_logger("transforms.aug_bridge")

# --------------------------------------------------------------------------- #
# (optional) runtime 타입 힌트
# --------------------------------------------------------------------------- #
@runtime_checkable
class _AugPolicyProto(Protocol):  # noqa: D401
    """augment.registry 가 반환해야 하는 최소 인터페이스."""

    def __call__(self, g: GraphT) -> GraphT: ...
    def train(self, mode: bool = True) -> None: ...
    def eval(self) -> None: ...
    def to(self, device: torch.device | str) -> "_AugPolicyProto": ...
    def cuda(self, device: int | None = None): ...
    def cpu(self): ...


# --------------------------------------------------------------------------- #
# Transform 래퍼
# --------------------------------------------------------------------------- #
class GraphAugmentTransform(torch.nn.Module):
    """
    Parameters
    ----------
    policy_cfg : dict | str
        * dict : registry.build(cfg) 에 그대로 전달
        * str  : YAML/JSON 경로면 읽어서 dict 로 파싱
    """

    def __init__(self, policy_cfg: Dict[str, Any] | str):
        super().__init__()
        if isinstance(policy_cfg, (str, bytes)):
            import yaml, json, pathlib

            path = pathlib.Path(policy_cfg)
            if path.suffix in {".yml", ".yaml"}:
                policy_cfg = yaml.safe_load(path.read_text())
            elif path.suffix == ".json":
                policy_cfg = json.loads(path.read_text())
            else:  # pragma: no cover
                raise ValueError("policy_cfg str must be YAML/JSON file path")

        self.policy: _AugPolicyProto = aug_registry.build(policy_cfg)  # type: ignore[assignment]
        _LOG.info("GraphAugmentTransform – policy=%s", self.policy.__class__.__name__)

    # -------------------------------------------------------------- #
    # transform 호출
    # -------------------------------------------------------------- #
    def forward(self, g: GraphT) -> GraphT:  # noqa: D401
        return self.policy(g)

    __call__ = forward  # alias for torchvision-style use

    # -------------------------------------------------------------- #
    # PyTorch helper – policy도 함께 device 이동
    # -------------------------------------------------------------- #
    def to(self, *args, **kwargs):  # type: ignore[override]
        self.policy = self.policy.to(*args, **kwargs)  # type: ignore[attr-defined]
        return super().to(*args, **kwargs)

    def cuda(self, device: int | None = None):  # type: ignore[override]
        self.policy = self.policy.cuda(device)  # type: ignore[attr-defined]
        return super().cuda(device)

    def cpu(self):  # type: ignore[override]
        self.policy = self.policy.cpu()  # type: ignore[attr-defined]
        return super().cpu()

    # -------------------------------------------------------------- #
    # state_dict / load_state_dict – policy 내부 파라미터 연동
    # -------------------------------------------------------------- #
    def state_dict(self, *args, **kwargs):
        state = super().state_dict(*args, **kwargs)
        # 내부 policy 가 nn.Module 이면 함께 저장
        if isinstance(self.policy, torch.nn.Module):
            state["policy"] = self.policy.state_dict()
        return state

    def load_state_dict(self, state_dict: Dict[str, Any], strict: bool = True):
        if "policy" in state_dict and isinstance(self.policy, torch.nn.Module):
            self.policy.load_state_dict(state_dict.pop("policy"), strict=strict)
        super().load_state_dict(state_dict, strict=strict)


# --------------------------------------------------------------------------- #
# 빠른 테스트
# --------------------------------------------------------------------------- #
if __name__ == "__main__":  # pragma: no cover
    import inspect
    import json
    from pathlib import Path
    from graphs.loaders.factory import get_loader
    from graphs.normalizers import get_normalizer

    # 예시 그래프 로드
    g_raw = get_loader("cfg").load("example.cfg.json.gz")
    g     = get_normalizer("cfg").normalize(g_raw)

    # 샘플 증강 정책
    dummy_cfg = {"type": "EdgeDrop", "p": 0.2}
    aug = GraphAugmentTransform(dummy_cfg)

    g_aug = aug(g)
    print("original:", g.num_nodes, g.num_edges)
    print("aug     :", g_aug.num_nodes, g_aug.num_edges)
