"""
src.graphs.normalizers.fcg_norm
===============================

⟦FCGNormalizer⟧
---------------
입력  : FCGLoader → Data
출력  : HeteroData
        ├─ node type : 'function'
        │   • feat         (optional)
        │   • addr         (optional)
        │   • name         (list[str])
        │   • is_external  (BoolTensor[N])
        └─ edge rel  : ('function', 'calls', 'function')
            • edge_index
            • edge_type    (schema ID: calls)
            • raw_call_kind(optional) – 로더가 부여한 호출 종류 보존
"""

from __future__ import annotations

import torch
from torch_geometric.data import Data, HeteroData

from .base import NormalizerBase, register_normalizer
from .schema import EDGE_REL_ID, EdgeRel, NodeType

# --------------------------------------------------------------------------- #
# Normalizer
# --------------------------------------------------------------------------- #
@register_normalizer("fcg")
class FCGNormalizer(NormalizerBase):
    """Function-Call-Graph ➜ 스키마 호환 HeteroData."""

    # ------------------------------------------------------------------ #
    # 핵심: Data ➜ HeteroData
    # ------------------------------------------------------------------ #
    def _normalize_graph(self, g: Data, **kwargs) -> HeteroData:  # noqa: N802
        if isinstance(g, HeteroData):  # 이미 정규화된 경우 pass-through
            return g

        new_g = HeteroData()

        kinds = getattr(g, "kind_str", None)
        texts = getattr(g, "text", None)

        fn_idx = [i for i, k in enumerate(kinds) if k != "token"] if kinds else list(range(g.num_nodes))
        tok_idx = [i for i, k in enumerate(kinds) if k == "token"] if kinds else []

        fn_map = {old: i for i, old in enumerate(fn_idx)}
        tok_map = {old: i for i, old in enumerate(tok_idx)}

        # ──────────────────────────────────────────────────────────
        # 1) 노드 – 'function'
        # ──────────────────────────────────────────────────────────
        fn_store = new_g[NodeType.FUNCTION.value]

        fn_store.num_nodes = len(fn_idx)  # set early

        if hasattr(g, "x") and g.x is not None:
            fn_store.feat = g.x[fn_idx].clone()

        if hasattr(g, "addr"):
            fn_store.addr = [g.addr[i] for i in fn_idx]
        else:
            fn_store.addr = torch.zeros(len(fn_idx), dtype=torch.long)
        if hasattr(g, "name"):
            fn_store.name = [g.name[i] for i in fn_idx]

        if hasattr(g, "is_external"):
            fn_store.is_external = g.is_external[fn_idx].clone()
        else:
            fn_store.is_external = torch.zeros(len(fn_idx), dtype=torch.bool)

        # ──────────────────────────────────────────────────────────
        # 2) 토큰 노드 (선택)
        # ──────────────────────────────────────────────────────────
        if tok_idx:
            tok_store = new_g[NodeType.TOKEN.value]
            tok_store.num_nodes = len(tok_idx)
            if texts:
                tok_store.text = [texts[i] for i in tok_idx]

        # ──────────────────────────────────────────────────────────
        # 3) 엣지 – ('function','calls','function') + ('function','child','token')
        # ──────────────────────────────────────────────────────────
        rel_key = (
            NodeType.FUNCTION.value,
            EdgeRel.CALLS.value,
            NodeType.FUNCTION.value,
        )
        edge_store = new_g[rel_key]

        call_edges = []
        child_edges = []
        for src, dst in g.edge_index.t().tolist():
            if src in fn_map and dst in fn_map:
                call_edges.append([fn_map[src], fn_map[dst]])
            elif src in fn_map and dst in tok_map:
                child_edges.append([fn_map[src], tok_map[dst]])

        if call_edges:
            edge_store.edge_index = torch.tensor(call_edges, dtype=torch.long).t().contiguous()
        else:
            edge_store.edge_index = torch.empty((2, 0), dtype=torch.long)

        edge_store.edge_type = torch.full(
            (edge_store.edge_index.size(1),),
            EDGE_REL_ID[EdgeRel.CALLS.value],
            dtype=torch.long,
        )

        if child_edges:
            rel_key_tok = (NodeType.FUNCTION.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)
            tok_edge_store = new_g[rel_key_tok]
            tok_edge_store.edge_index = (
                torch.tensor(child_edges, dtype=torch.long).t().contiguous()
            )
            tok_edge_store.edge_type = torch.full(
                (tok_edge_store.edge_index.size(1),),
                EDGE_REL_ID[EdgeRel.CHILD.value],
                dtype=torch.long,
            )

            # reverse edges: token -> function
            rev_edges = [[dst, src] for src, dst in child_edges]
            rel_key_rev = (
                NodeType.TOKEN.value,
                EdgeRel.CHILD.value,
                NodeType.FUNCTION.value,
            )
            rev_edge_store = new_g[rel_key_rev]
            rev_edge_store.edge_index = (
                torch.tensor(rev_edges, dtype=torch.long).t().contiguous()
            )
            rev_edge_store.edge_type = torch.full(
                (rev_edge_store.edge_index.size(1),),
                EDGE_REL_ID[EdgeRel.CHILD.value],
                dtype=torch.long,
            )

        # ──────────────────────────────────────────────────────────
        # 4) 그래프-레벨 메타
        # ──────────────────────────────────────────────────────────
        if hasattr(g, "entry_id") and int(g.entry_id[0]) in fn_map:
            new_g.entry_func = torch.tensor([fn_map[int(g.entry_id[0])]], dtype=torch.long)

        return new_g
