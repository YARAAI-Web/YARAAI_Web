# robust-malware-graph / src / explain / cfg_explainer / mapper.py
# --------------------------------------------------------------------------- #
#  🗺️  CFG-to-AST Token Mapper
#
#  • 역할
#    ├─ CFG 기본블록(bb) 노드 ↔ AST 토큰 span(시작-끝) 간 다대다 매핑 구축
#    ├─ 설명(Explainer) 단계에서 CFG 마스크를 AST 토큰 하이라이트로 변환
#    └─ 추후 HTML/텍스트 리포트-생성기(explain/report.py)와 직접 연동
#
#  • 가정
#    ├─ `cfg_g`       : torch_geometric.data.Data – bb 노드 단위 CFG
#       ◦ cfg_g.x     : (N_cfg, feat_dim)          – 임베딩/속성
#       ◦ cfg_g.addr  : (N_cfg, 2) torch.LongTensor – [start_addr, end_addr]
#    ├─ `ast_g`       : torch_geometric.data.Data – AST
#       ◦ ast_g.token : (N_ast,)  torch.LongTensor – 토큰 ID
#       ◦ ast_g.span  : (N_ast, 2) torch.LongTensor – [start_addr, end_addr]
#
#         ※ PE/ELF 주소가 없는 소스-코드 레벨 AST(예: C source)라면
#           `span` 은 [line, column] 또는 토큰 인덱스여도 무방.
#
#  • 매핑 규칙 (기본)
#      bb ∈ CFG   ↔   {tok ∈ AST | overlap(bb.addr, tok.span)}
#
#  • Public API
#    ├─ mapper = CFGASTMapper(cfg_g, ast_g)      # 빌드 & 인덱싱
#    ├─ mapper.cfg_nodes_to_tokens(bb_idx_list)  # → List[int]
#    ├─ mapper.tokens_to_cfg_nodes(tok_idx_list) # → List[int]
#    ├─ mapper.save_json(path) / load_json(path)
#    └─ mapper.visualize(bb_idx_list, html_path) # optional helper
#
#  • 의존
#    torch_geometric ≥ 2.x, networkx, tqdm (optional)
# --------------------------------------------------------------------------- #
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Sequence, Set

import torch
from torch_geometric.data import Data


class CFGASTMapper:
    """
    빠른 역-인덱스를 구축해 O(1)-like 다대다 조회를 제공하는 헬퍼 클래스.

    Example
    -------
    >>> mapper = CFGASTMapper(cfg_g, ast_g)
    >>> toks = mapper.cfg_nodes_to_tokens([12, 27])     # bb id → 토큰
    >>> bbs  = mapper.tokens_to_cfg_nodes(toks[:10])    # 토큰 → bb id
    >>> mapper.save_json("tmp/mapping.json")
    """

    # --------------------------- constructor --------------------------------
    def __init__(
        self,
        cfg_graph: Data,
        ast_graph: Data,
        *,
        span_key_cfg: str = "addr",
        span_key_ast: str = "span",
        cfg_node_type: str = "bb",
    ) -> None:
        self.cfg_g = cfg_graph
        self.ast_g = ast_graph
        self.span_key_cfg = span_key_cfg
        self.span_key_ast = span_key_ast

        # 내부 인덱스
        self.cfg_node_type = cfg_node_type

        self._cfg_to_tok: Dict[tuple[str, int], Set[int]] = {}
        self._tok_to_cfg: Dict[int, Set[tuple[str, int]]] = {}

        self._build_index()

    # --------------------------- private utils ------------------------------
    @staticmethod
    def _overlap(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
        """Inclusive range overlap check."""
        return not (a_end < b_start or b_end < a_start)

    def _build_index(self) -> None:
        """
        cfg_bb_i  ↔  {tok_j …}  역-인덱스 구축.
        복잡도 : O(N_cfg × log N_ast) using span-start sort & binary search
        """
        # ── AST 토큰 span 시작점 기준 정렬 (Python list keeps idx)
        ast_spans = self.ast_g[self.span_key_ast]  # (N_ast, 2)
        if not isinstance(ast_spans, torch.Tensor) or ast_spans.ndim != 2:
            raise ValueError(f"`ast_g.{self.span_key_ast}` must be (N,2) Tensor")

        sorted_ast_idx = torch.argsort(ast_spans[:, 0])  # by span start
        sorted_starts = ast_spans[sorted_ast_idx, 0]

        for bb_idx, (bb_start, bb_end) in enumerate(self.cfg_g[self.span_key_cfg]):
            # ── lower-bound(binary search) for candidate token window
            left = torch.searchsorted(sorted_starts, bb_start, right=False).item()

            # iterate until start exceeds bb_end
            for pos in range(left, len(sorted_ast_idx)):
                tok_idx = sorted_ast_idx[pos].item()
                tok_start, tok_end = ast_spans[tok_idx].tolist()
                if tok_start > bb_end:
                    break  # no further overlap possible

                if self._overlap(bb_start, bb_end, tok_start, tok_end):
                    key = (self.cfg_node_type, int(bb_idx))
                    self._cfg_to_tok.setdefault(key, set()).add(tok_idx)
                    self._tok_to_cfg.setdefault(tok_idx, set()).add(key)

        # ensure empty sets for nodes with zero overlap
        for bb_idx in range(self.cfg_g.num_nodes):
            self._cfg_to_tok.setdefault((self.cfg_node_type, int(bb_idx)), set())

        for tok_idx in range(self.ast_g.num_nodes):
            self._tok_to_cfg.setdefault(tok_idx, set())

    # --------------------------- public API ---------------------------------
    def cfg_nodes_to_tokens(self, bb_indices: Sequence[tuple[str, int] | int]) -> List[int]:
        """Return a deduplicated list of AST token indices overlapped by given CFG nodes."""
        toks: Set[int] = set()
        for bb in bb_indices:
            if isinstance(bb, tuple):
                key = (bb[0], int(bb[1]))
            else:
                key = (self.cfg_node_type, int(bb))
            toks.update(self._cfg_to_tok.get(key, set()))
        return sorted(toks)

    def tokens_to_cfg_nodes(self, tok_indices: Sequence[int]) -> List[tuple[str, int]]:
        """Inverse lookup: AST token indices → related CFG nodes."""
        bbs: Set[tuple[str, int]] = set()
        for tok in tok_indices:
            bbs.update(self._tok_to_cfg.get(int(tok), set()))
        return sorted(bbs)

    # --------------------------- I/O helpers --------------------------------
    def to_dict(self) -> Dict[str, Dict[str, List[int]]]:
        """Return JSON-serialisable mapping."""
        return {
            "cfg_node_type": self.cfg_node_type,
            "cfg_to_tok": {f"{t}:{i}": sorted(v) for (t, i), v in self._cfg_to_tok.items()},
            "tok_to_cfg": {str(k): [f"{t}:{i}" for (t, i) in v] for k, v in self._tok_to_cfg.items()},
        }

    @classmethod
    def from_dict(
        cls, mapping: Dict[str, Dict[str, List[int]]], cfg_graph: Data, ast_graph: Data
    ) -> "CFGASTMapper":
        obj = cls.__new__(cls)  # bypass __init__
        obj.cfg_g = cfg_graph
        obj.ast_g = ast_graph
        obj.span_key_cfg = "addr"
        obj.span_key_ast = "span"
        obj.cfg_node_type = mapping.get("cfg_node_type", "bb")
        obj._cfg_to_tok = {}
        for k, v in mapping["cfg_to_tok"].items():
            t, idx = k.split(":")
            obj._cfg_to_tok[(t, int(idx))] = set(v)
        obj._tok_to_cfg = {}
        for k, v in mapping["tok_to_cfg"].items():
            obj._tok_to_cfg[int(k)] = {(p.split(":")[0], int(p.split(":")[1])) for p in v}
        return obj

    # file-based convenience wrappers
    def save_json(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as fp:
            json.dump(self.to_dict(), fp, indent=2, ensure_ascii=False)

    @classmethod
    def load_json(
        cls, path: str | Path, cfg_graph: Data, ast_graph: Data
    ) -> "CFGASTMapper":
        with Path(path).open("r", encoding="utf-8") as fp:
            data = json.load(fp)
        return cls.from_dict(data, cfg_graph, ast_graph)

    # ---------------------- optional visualisation --------------------------
    def visualize(self, bb_indices: Sequence[int], html_path: str | Path) -> None:
        """
        간단한 HTML snippet 생성 – 선택된 CFG bb에 매핑된 토큰을
        <span class="highlight">…</span> 로 둘러싸 하이라이트.
        """
        tokens = self.cfg_nodes_to_tokens(bb_indices)
        tok_ids = set(tokens)

        # assume ast_g has 'token_str' attr holding string form
        tok_strs = self.ast_g.get("token_str", None)
        if tok_strs is None:
            raise RuntimeError("ast_g must contain 'token_str' for visualization")

        html_tokens = [
            f'<span class="highlight">{s}</span>' if i in tok_ids else s
            for i, s in enumerate(tok_strs)
        ]
        html = (
            "<html><head><style>"
            ".highlight{background:gold;}"
            "body{font-family:monospace;white-space:pre;}"
            "</style></head><body>"
            + " ".join(html_tokens)
            + "</body></html>"
        )

        html_path = Path(html_path)
        html_path.parent.mkdir(parents=True, exist_ok=True)
        html_path.write_text(html, encoding="utf-8")

    # ----------------------- dunder convenience -----------------------------
    def __getitem__(self, bb_idx: tuple[str, int] | int) -> List[int]:
        """shorthand mapper[(type,id)] → tokens list."""
        return self.cfg_nodes_to_tokens([bb_idx])

    def __len__(self) -> int:
        return len(self._cfg_to_tok)
