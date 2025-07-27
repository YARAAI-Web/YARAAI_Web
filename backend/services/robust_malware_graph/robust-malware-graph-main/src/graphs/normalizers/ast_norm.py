"""
src.graphs.normalizers.ast_norm
===============================

⟦ASTNormalizer⟧
----------------
• 입력 : ASTLoader 가 만든 Data
          - edge_index
          - kind_id          : [N]
          - (opt) x          : [N, D]
• 출력 : HeteroData
          node type  : 'token'
          edge rel   : ('token', 'child', 'token')
          node attrs : {'tok_id', 'pos', 'feat'}  (schema.NODE_ATTRS 기준)

이후 NormalizerBase 가 _validate_node_attrs / _validate_edge_types 를 호출해
속성 화이트리스트·edge_type 등 최종 검증·보강을 수행.
"""

from __future__ import annotations

import torch
from torch_geometric.data import Data, HeteroData

from .base import NormalizerBase, register_normalizer
from .schema import EDGE_REL_ID, EdgeRel, NodeType

# --------------------------------------------------------------------------- #
# Normalizer
# --------------------------------------------------------------------------- #
@register_normalizer("ast")
class ASTNormalizer(NormalizerBase):
    """AST ➜ schema‐compatible HeteroData."""

    # -------------------------------------------------------------- #
    # 핵심 로직 : Data ➜ HeteroData 변환
    # -------------------------------------------------------------- #
    def _normalize_graph(self, g: Data, **kwargs) -> HeteroData:  # noqa: N802
        if isinstance(g, HeteroData):  # 이미 정규화된 경우 패스
            return g

        new_g = HeteroData()

        # ── 1) 노드 영역 ────────────────────────────────────────────
        n = g.kind_id.size(0) if hasattr(g, "kind_id") else g.num_nodes
        tok_store = new_g[NodeType.TOKEN.value]
        tok_store.num_nodes = n  # set first to avoid PyG warnings

        if hasattr(g, "text"):
            tok_store.text = list(g.text)

        tok_store.tok_id = g.kind_id.clone()
        # address 정보가 제공되는 경우에만 보존
        addr = getattr(g, "addr", None)
        if addr is not None:
            tok_store.addr = torch.as_tensor(addr).clone()

        # 위치(pos) : 0 … N-1
        tok_store.pos = torch.arange(n, dtype=torch.long)

        # 노드 임베딩(x) → 'feat'
        if hasattr(g, "x") and g.x is not None:
            tok_store.feat = g.x.clone()

        # ── 2) edge 영역 ────────────────────────────────────────────
        rel_key = (NodeType.TOKEN.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)
        new_g[rel_key].edge_index = g.edge_index.clone()

        # edge_type (정수) 자동 주입 – Base 검증 단계에서도 다시 확인
        new_g[rel_key].edge_type = torch.full(
            (g.edge_index.shape[1],),
            EDGE_REL_ID[EdgeRel.CHILD.value],
            dtype=torch.long,
        )

        return new_g
