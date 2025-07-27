"""
StandardPair (PyG)
==================
두 개의 증강 뷰(g₁, g₂)를 **동일 순서로** 주어진 Op 시퀀스에 적용하는
가장 전통적인 GraphCL-style 뷰 생성기.

- ops_a : g₁ 에 적용할 AugmentBase 리스트
- ops_b : g₂ 에 적용할 AugmentBase 리스트
          (동일 시퀀스를 쓰고 싶다면 ops_b=ops_a 도 가능)

Input / Output
--------------
torch_geometric.data.Data      (단일 그래프)
torch_geometric.data.HeteroData (이기종 그래프) 모두 지원

주의
----
각 Op 가 **in-place** 로 그래프를 바꿔도 안전하긴 하지만,
파이프라인 일관성을 위해 이 클래스 내부에서 `copy.deepcopy` 로
원본을 복제한 뒤 Op 를 적용합니다.
"""

from __future__ import annotations

import copy
from typing import List

from torch_geometric.data import Data, HeteroData

from augment import register_view
from augment.base import AugmentBase, ViewGenerator


import logging
LOGGER = logging.getLogger(__name__)

@register_view
class StandardPair(ViewGenerator):
    """(ops_a) + (ops_b) 두 시퀀스로 g₁, g₂ 를 만드는 기본 뷰 생성기."""

    def __init__(
        self,
        ops_a: List[AugmentBase],
        ops_b: List[AugmentBase],
    ) -> None:
        self.ops_a = ops_a
        self.ops_b = ops_b

    # ------------------------------------------------------------------ #
    # ViewGenerator 인터페이스
    # ------------------------------------------------------------------ #
    def __call__(
        self,
        g: Data | HeteroData,
    ) -> tuple[Data | HeteroData, Data | HeteroData]:
        """원본 그래프 → (augmented g₁, augmented g₂)."""
        sha = getattr(g, 'sha256', 'unknown_sha')
        LOGGER.debug(f"[{sha}] StandardPair.__call__ entered. Attempting deepcopy...")

        try:
            g1 = g.clone()
            g2 = g.clone()
            LOGGER.debug(f"[{sha}] Clone successful.")
        except Exception as e:
            LOGGER.error(f"[{sha}] CRASH during deepcopy: {e}", exc_info=True)
            raise

        LOGGER.debug(f"[{sha}] Augmenting view A...")
        for op in self.ops_a:
            op_name = op.__class__.__name__
            LOGGER.debug(f"[{sha}] Applying op {op_name} to view A.")
            try:
                g1 = op(g1)  # type: ignore[arg-type]
            except Exception:
                LOGGER.warning(f"[{sha}] Failed to apply op {op_name} to view A.", exc_info=True)
        
        LOGGER.debug(f"[{sha}] Augmenting view B...")
        for op in self.ops_b:
            op_name = op.__class__.__name__
            LOGGER.debug(f"[{sha}] Applying op {op_name} to view B.")
            try:
                g2 = op(g2)  # type: ignore[arg-type]
            except Exception:
                LOGGER.warning(f"[{sha}] Failed to apply op {op_name} to view B.", exc_info=True)

        LOGGER.debug(f"[{sha}] Augmentation finished. Sanitizing edges...")
        try:
            from graphs.dataset.graph_dataset import GraphDataset

            g1 = GraphDataset._sanitize_edges(g1)
            g2 = GraphDataset._sanitize_edges(g2)
        except Exception:  # pragma: no cover - log and proceed
            LOGGER.warning(f"[{sha}] Failed to sanitize graphs", exc_info=True)

        return g1, g2

    # ------------------------------------------------------------------ #
    # 유틸 (옵션) – 로깅/재현을 위해 하이퍼파라미터 dict 제공
    # ------------------------------------------------------------------ #
    @property
    def name(self) -> str:  # noqa: D401
        return self.__class__.__name__

    def hyperparams(self):
        return {
            "ops_a": [op.name for op in self.ops_a],
            "ops_b": [op.name for op in self.ops_b],
        }
