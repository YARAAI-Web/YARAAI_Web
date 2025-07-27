"""
src.graphs.normalizers.cfg_norm
===============================

⟦CFGNormalizer⟧
----------------
• 입력 : CFGLoader → Data
          - edge_index          : [2, E]
          - edge_type (opt)     : [E]   – fallthrough/jump/cond … 정수
          - x        (opt)      : [N, D]
          - addr     (opt)      : list[str]
          - entry_id (opt)      : Tensor([bb_id])
• 출력 : HeteroData
          node type  : 'bb'
          edge rel   : ('bb', 'cfg', 'bb')
          node attrs : {'feat', 'addr', 'inst_cnt'}   (schema 기준)

`NormalizerBase` 의 후처리 루틴이 호출되어
속성 화이트리스트·edge_type 검증이 한 번 더 이루어집니다.
"""

from __future__ import annotations

import torch
from torch_geometric.data import Data, HeteroData

from .base import NormalizerBase, register_normalizer
from .schema import EDGE_REL_ID, EdgeRel, NodeType

# --------------------------------------------------------------------------- #
# Normalizer
# --------------------------------------------------------------------------- #
@register_normalizer("cfg")
class CFGNormalizer(NormalizerBase):
    """CFG 데이터 → 스키마 호환 HeteroData."""

    def _normalize_graph(self, g: Data, **kwargs) -> HeteroData:  # noqa: N802
        # 이미 정규화가 끝난 경우 pass-through
        if isinstance(g, HeteroData):
            return g

        new_g = HeteroData()

        kinds = getattr(g, "kind_str", None)
        if kinds:
            kinds = ["bb" if (k is None or k == "") else k for k in kinds]
        texts = getattr(g, "text", None)

        bb_idx = [i for i, k in enumerate(kinds) if k == "bb"] if kinds else list(range(g.num_nodes))
        tok_idx = [i for i, k in enumerate(kinds) if k == "token"] if kinds else []
        str_idx = [i for i, k in enumerate(kinds) if k == "string"] if kinds else []

        bb_map = {old: i for i, old in enumerate(bb_idx)}
        tok_map = {old: i for i, old in enumerate(tok_idx)}
        str_map = {old: i for i, old in enumerate(str_idx)}

        # ────────────────────────────────────────────────────────────
        # 1) 노드 - BasicBlock
        # ────────────────────────────────────────────────────────────
        bb_store = new_g[NodeType.BB.value]

        n_nodes = len(bb_idx)
        bb_store.num_nodes = n_nodes  # set early

        if hasattr(g, "x") and g.x is not None:
            bb_store.feat = g.x[bb_idx].clone()

        if hasattr(g, "addr"):
            bb_store.addr = [g.addr[i] for i in bb_idx]
        else:
            bb_store.addr = torch.zeros(n_nodes, dtype=torch.long)
        inst_cnt = getattr(g, "inst_cnt", None)
        if inst_cnt is not None:
            bb_store.inst_cnt = torch.as_tensor(inst_cnt)[bb_idx]
        else:
            bb_store.inst_cnt = torch.full((n_nodes,), -1, dtype=torch.long)

        # ────────────────────────────────────────────────────────────
        # 2) 토큰 노드 (선택)
        # ────────────────────────────────────────────────────────────
        if tok_idx:
            tok_store = new_g[NodeType.TOKEN.value]
            tok_store.num_nodes = len(tok_idx)
            if texts:
                tok_store.text = [texts[i] for i in tok_idx]

        # ────────────────────────────────────────────────────────────
        # 3) 문자열 노드 (선택)
        # ────────────────────────────────────────────────────────────
        if str_idx:
            str_store = new_g[NodeType.STRING.value]
            str_store.num_nodes = len(str_idx)
            if texts:
                slen = [len(texts[i]) if texts[i] is not None else 0 for i in str_idx]
                str_store.slen = torch.tensor(slen, dtype=torch.long)

        # ────────────────────────────────────────────────────────────
        # 4) 엣지 – ('bb', 'cfg', 'bb') + ('bb','child','token') + ('bb','ref','string')
        # ────────────────────────────────────────────────────────────
        rel_key = (NodeType.BB.value, EdgeRel.CFG.value, NodeType.BB.value)
        edge_store = new_g[rel_key]

        cfg_edges = []
        child_edges = []
        ref_edges = []
        for src, dst in g.edge_index.t().tolist():
            if src in bb_map and dst in bb_map:
                cfg_edges.append([bb_map[src], bb_map[dst]])
            elif src in bb_map and dst in tok_map:
                child_edges.append([bb_map[src], tok_map[dst]])
            elif src in bb_map and dst in str_map:
                ref_edges.append([bb_map[src], str_map[dst]])

        if cfg_edges:
            edge_store.edge_index = torch.tensor(cfg_edges, dtype=torch.long).t().contiguous()
        else:
            edge_store.edge_index = torch.empty((2, 0), dtype=torch.long)

        edge_store.edge_type = torch.full(
            (edge_store.edge_index.size(1),),
            EDGE_REL_ID[EdgeRel.CFG.value],
            dtype=torch.long,
        )


        if child_edges:
            rel_key_tok = (NodeType.BB.value, EdgeRel.CHILD.value, NodeType.TOKEN.value)
            tok_edge_store = new_g[rel_key_tok]
            tok_edge_store.edge_index = (
                torch.tensor(child_edges, dtype=torch.long).t().contiguous()
            )
            tok_edge_store.edge_type = torch.full(
                (tok_edge_store.edge_index.size(1),),
                EDGE_REL_ID[EdgeRel.CHILD.value],
                dtype=torch.long,
            )

            # Create reverse edges: token -> bb
            rev_edges = [[dst, src] for [src, dst] in child_edges]
            rev_rel_key = (NodeType.TOKEN.value, EdgeRel.CHILD.value, NodeType.BB.value)
            rev_edge_store = new_g[rev_rel_key]
            rev_edge_store.edge_index = (
                torch.tensor(rev_edges, dtype=torch.long).t().contiguous()
            )
            rev_edge_store.edge_type = torch.full(
                (rev_edge_store.edge_index.size(1),),
                EDGE_REL_ID[EdgeRel.CHILD.value],
                dtype=torch.long,
            )

        if ref_edges:
            ref_rel_key = (
                NodeType.BB.value,
                EdgeRel.REF.value,
                NodeType.STRING.value,
            )
            ref_edge_store = new_g[ref_rel_key]
            ref_edge_store.edge_index = (
                torch.tensor(ref_edges, dtype=torch.long).t().contiguous()
            )
            ref_edge_store.edge_type = torch.full(
                (ref_edge_store.edge_index.size(1),),
                EDGE_REL_ID[EdgeRel.REF.value],
                dtype=torch.long,
            )

        # ────────────────────────────────────────────────────────────
        # 5) 그래프-레벨 메타
        # ────────────────────────────────────────────────────────────
        if hasattr(g, "entry_id") and int(g.entry_id[0]) in bb_map:
            new_g.entry_bb = torch.tensor([bb_map[int(g.entry_id[0])]], dtype=torch.long)

        return new_g
