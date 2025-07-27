from __future__ import annotations

import gzip
import json
import re
from pathlib import Path
from typing import Dict, List, Sequence, Union

# --------------------------------------------------------------------------- #
#  Token leaf kinds to be collapsed into a single 'token' category
# --------------------------------------------------------------------------- #
_TOKEN_LEAF_KINDS = {
    "identifier",
    "string_literal",
    "number_literal",
    "char_literal",
    "comment",
    "token",
}

from .common_token_utils import TOKEN_RE, MAX_TOKENS


def _normalise_ast(nodes: Sequence[dict], edges: Sequence) -> None:
    """Normalize AST nodes in-place."""
    for n in nodes:
        if n.get("kind") in _TOKEN_LEAF_KINDS:
            n["kind"] = "token"

import torch
from torch_geometric.data import Data

from .base import GraphLoaderBase, register_loader


@register_loader("ast")  # 기존 이름 유지
class ASTLoader(GraphLoaderBase):
    """
    (1) 일반 AST  JSON  → PyG Data
    (2) PE 메타데이터 JSON → (1)의 스키마로 on‑the‑fly 변환 후 PyG Data

    ──────────────────────────────────────────────────────────────────
    * PE JSON  노드 매핑 ••• 간단 요약
      root(file) ─▶ section
                 ├▶ entry_point
                 ├▶ current_function
                 └▶ entropy
      노드 feat 예시
        section        : [virtual_size, raw_size]
        entry_point    : [size]
        current_func   : [size]
        entropy        : [entropy]            (실수 1‑개)
    """

    # ============================================================= #
    # 1. 메인 파서
    # ============================================================= #
    def _parse(self, src: str | Path | bytes, **kwargs) -> Data:  # noqa: N802
        js = self._read_json(src)

        # -------- A) 스키마 감지 & 필요 시 변환 -------------------- #
        if "nodes" not in js:  # = PE 메타 형식
            js = self._convert_pejson_to_ast(js)

        _normalise_ast(js["nodes"], js.get("edges", []))

        # -------- B) 공통 AST 처리(기존 코드) ---------------------- #
        nodes: Sequence[dict] = js["nodes"]

        # Check for missing 'kind'
        src_path = str(src) if isinstance(src, (str, Path)) else "<bytes>"
        for n in nodes:
            if "kind" not in n:
                self.log.warning("node missing 'kind' in %s: %s", src_path, n)
                n["kind"] = "unknown"

        id2idx: Dict[int, int] = {n["id"]: i for i, n in enumerate(nodes)}
        node_kinds: List[str] = [n["kind"] for n in nodes]

        kind2id: Dict[str, int] = {k: i for i, k in enumerate(sorted(set(node_kinds)))}
        kind_id = torch.tensor([kind2id[k] for k in node_kinds], dtype=torch.long)

        # ---- 노드 특성 행렬 (있을 때만) --------------------------- #
        if any("feat" in n and n["feat"] for n in nodes):
            feat_dim = max(len(n.get("feat", [])) for n in nodes)
            x = torch.zeros((len(nodes), feat_dim), dtype=torch.float)
            for i, n in enumerate(nodes):
                if n.get("feat"):
                    v = torch.as_tensor(n["feat"], dtype=torch.float)
                    x[i, : v.numel()] = v
        else:
            x = None

        # ---- edge_index ---------------------------------------- #
        raw_edges = js.get("edges", [])
        if raw_edges:
            mapped = []
            try:
                for src, tgt in raw_edges:
                    mapped.append([id2idx[src], id2idx[tgt]])
                    mapped.append([id2idx[tgt], id2idx[src]])
            except KeyError as e:
                raise ValueError(f"edge references unknown node id: {e}") from None
            edge_index = torch.tensor(mapped, dtype=torch.long).t().contiguous()
        else:
            edge_index = torch.empty((2, 0), dtype=torch.long)

        # ---- PyG Data ----------------------------------------- #
        data = Data(edge_index=edge_index, kind_id=kind_id)
        if x is not None:
            data.x = x

        node_texts: List[str] = []
        for n in nodes:
            if n.get("kind") == "token":
                node_text = n.get("text") or " ".join(n.get("tokens", []))
            else:
                node_text = str(n.get("kind", "")).lower()
            node_texts.append(node_text)

        data.text = node_texts
        data.kind_str = node_kinds
        data.node_id = torch.tensor(list(id2idx.keys()), dtype=torch.long)
        return data

    # ============================================================= #
    # 2. PE‑메타 → AST 변환기
    # ============================================================= #
    @staticmethod
    def _convert_pejson_to_ast(js: dict) -> dict:
        """
        PE 분석 JSON(역‑공학 도구 출력)을 간이 AST 스키마로 변환
        또한 c_code/asm_code/llvm_ir 필드에서 토큰을 추출하여
        file 노드의 자식으로 연결한다.
        """
        nodes: List[dict] = []
        edges: List[List[int]] = []

        next_id = 0
        # 1) root node (파일 자체)
        nodes.append({"id": next_id, "kind": "file", "feat": []})
        root = next_id
        next_id += 1

        # 2) 섹션들
        for sec in js.get("pe_headers", {}).get("sections", []):
            nid = next_id
            next_id += 1
            try:
                vsize = int(sec.get("virtual_size", "0"), 16)
                rsize = int(sec.get("raw_size", "0"), 16)
            except ValueError:  # 혹시 10진수 문자열/정수일 때
                vsize = int(sec.get("virtual_size", 0))
                rsize = int(sec.get("raw_size", 0))
            name = sec.get("name", "").strip()
            nodes.append({
                "id": nid,
                "kind": "section",
                "name": name,
                "feat": [vsize, rsize],
            })
            edges.append([root, nid])

        # 3) 엔트리포인트
        for ep in js.get("get_entry_points", []):
            nid = next_id
            next_id += 1
            size = _hex_to_int(ep.get("size", 0))
            nodes.append({"id": nid, "kind": "entry_point", "feat": [size]})
            edges.append([root, nid])

        # 4) 현재 함수
        if cf := js.get("get_current_function"):
            nid = next_id
            next_id += 1
            size = _hex_to_int(cf.get("size", 0))
            nodes.append({"id": nid, "kind": "current_function", "feat": [size]})
            edges.append([root, nid])


        # 5) 파일 엔트로피
        if js.get("file_entropy") is not None:
            nid = next_id
            next_id += 1
            nodes.append({"id": nid, "kind": "entropy", "feat": [float(js["file_entropy"])]})
            edges.append([root, nid])

        # 6) 코드 문자열에서 토큰 추출
        code_fields = ("c_code", "asm_code", "llvm_ir")
        lines: List[str] = []
        for field in code_fields:
            lines.extend(js.get(field, []))

        if lines:
            seen: set[str] = set()
            for line in lines:
                for tok in TOKEN_RE.findall(line):
                    if tok in seen:
                        continue
                    seen.add(tok)
                    nodes.append({"id": next_id, "kind": "token", "text": tok, "feat": []})
                    edges.append([root, next_id])
                    next_id += 1
                    if len(seen) >= MAX_TOKENS:
                        break
                if len(seen) >= MAX_TOKENS:
                    break

        return {"nodes": nodes, "edges": edges}

    # ============================================================= #
    # 3. JSON/JSON‑GZ 로더 (변경 없음)
    # ============================================================= #
    @staticmethod
    def _read_json(src: Union[str, Path, bytes]) -> dict:
        """
        • bytes   : gzip 여부 자동 감지
        • str/Path: *.json | *.json.gz
        """
        if isinstance(src, bytes):
            raw = gzip.decompress(src) if src[:2] == b"\x1f\x8b" else src
            return json.loads(raw.decode("utf-8", errors="replace"))

        path = Path(src)
        if path.suffix == ".gz":
            with gzip.open(path, "rt", encoding="utf-8") as f:
                return json.load(f)
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)


# ------------------------------------------------------------------ #
# 4. 내부 헬퍼
# ------------------------------------------------------------------ #
def _hex_to_int(v: Union[str, int]) -> int:
    if isinstance(v, int):
        return v
    try:
        return int(v, 16)
    except ValueError:
        return int(v)
