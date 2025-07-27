"""
src.graphs.normalizers.syscall_norm
===================================

⟦SysCallNormalizer⟧
-------------------
입력 : SysCallLoader → Data
        - edge_index          : [2, E]
        - sc_id               : [N]  (syscall 이름 정수)
        - x         (opt)     : [N, D]  (노드 특성)
        - sc_name   (list)    : N개 문자열
        - start_time, puid …  (opt)  그래프-레벨 메타
출력 : HeteroData
        node type  : 'syscall'
          • feat  : [N, D] 또는 [N, 1]   (스키마 허용)
          • name  : list[str]
        edge rel   : ('syscall', 'seq', 'syscall')
          • edge_index
          • edge_type : 정수(SEQUENCE)
        graph attrs: start_time / puid  (있으면 보존)
"""

from __future__ import annotations

import torch
from torch_geometric.data import Data, HeteroData

from .base import NormalizerBase, register_normalizer
from .schema import EDGE_REL_ID, EdgeRel, NodeType

# --------------------------------------------------------------------------- #
# Normalizer
# --------------------------------------------------------------------------- #
@register_normalizer("syscall")
class SysCallNormalizer(NormalizerBase):
    """Syscall trace → 스키마 호환 HeteroData."""

    # -------------------------------------------------------------- #
    # Data  ➜  HeteroData
    # -------------------------------------------------------------- #
    def _normalize_graph(self, g: Data, **kwargs) -> HeteroData:  # noqa: N802
        if isinstance(g, HeteroData):        # 이미 정규화된 경우 pass-through
            return g

        new_g = HeteroData()

        token_texts = getattr(g, "token_text", None)
        n_tokens = len(token_texts) if token_texts else 0
        n_syscalls = g.num_nodes - n_tokens

        syscall_map = {i: i for i in range(n_syscalls)}
        token_map = {n_syscalls + i: i for i in range(n_tokens)}

        # ──────────────────────────────────────────────────────────
        # 1) 노드 – 'syscall'
        # ──────────────────────────────────────────────────────────
        sc_store = new_g[NodeType.SYSCALL.value]

        sc_store.num_nodes = n_syscalls  # set early
        sc_store.addr = torch.zeros(n_syscalls, dtype=torch.long)

        if hasattr(g, "x") and g.x is not None:
            sc_store.feat = g.x[:n_syscalls].clone()
        else:
            sc_store.feat = g.sc_id[:n_syscalls].view(-1, 1).to(torch.float32)

        if hasattr(g, "sc_name"):
            sc_store.name = list(g.sc_name)

        # ──────────────────────────────────────────────────────────
        # 2) 토큰 노드 (선택)
        # ──────────────────────────────────────────────────────────
        if n_tokens > 0:
            tok_store = new_g[NodeType.TOKEN.value]
            tok_store.num_nodes = n_tokens
            tok_store.text = list(token_texts)
            tok_store.addr = torch.zeros(n_tokens, dtype=torch.long)

        # ──────────────────────────────────────────────────────────
        # 3) 엣지 – seq + child(token)
        # ──────────────────────────────────────────────────────────
        rel_key = (
            NodeType.SYSCALL.value,
            EdgeRel.SEQ.value,
            NodeType.SYSCALL.value,
        )
        edge_store = new_g[rel_key]

        seq_edges = []
        child_edges = []
        for src, dst in g.edge_index.t().tolist():
            if src < n_syscalls and dst < n_syscalls:
                seq_edges.append([syscall_map[src], syscall_map[dst]])
            elif src < n_syscalls and dst >= n_syscalls:
                child_edges.append([syscall_map[src], token_map[dst]])

        if seq_edges:
            edge_store.edge_index = torch.tensor(seq_edges, dtype=torch.long).t().contiguous()
        else:
            edge_store.edge_index = torch.empty((2, 0), dtype=torch.long)

        edge_store.edge_type = torch.full(
            (edge_store.edge_index.size(1),),
            EDGE_REL_ID[EdgeRel.SEQ.value],
            dtype=torch.long,
        )

        if child_edges:
            rel_key_tok = (NodeType.SYSCALL.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)
            tok_edge_store = new_g[rel_key_tok]
            tok_edge_store.edge_index = (
                torch.tensor(child_edges, dtype=torch.long).t().contiguous()
            )
            tok_edge_store.edge_type = torch.full(
                (tok_edge_store.edge_index.size(1),),
                EDGE_REL_ID[EdgeRel.CHILD.value],
                dtype=torch.long,
            )

        # ──────────────────────────────────────────────────────────
        # 4) 그래프-레벨 메타 데이터
        # ──────────────────────────────────────────────────────────
        if hasattr(g, "start_time"):
            new_g.start_time = float(g.start_time)
        if hasattr(g, "puid"):
            new_g.puid = int(g.puid)

        return new_g
