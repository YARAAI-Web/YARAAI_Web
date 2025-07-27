from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Dict, List, Sequence, Tuple, Union

from .common_token_utils import TOKEN_RE, MAX_TOKENS

import torch
from torch_geometric.data import Data

from .base import GraphLoaderBase, register_loader

# ──────────────────────────────────────────────────────────────────────────────
#  공통 상수
# ──────────────────────────────────────────────────────────────────────────────
_EDGE_KIND_CONTAINS = "contains"          # file → section / section → entry
_EDGE_KIND_LINEAR   = "cfg"                 # 섹션 내 BB 선형 연결


def _extract_tokens(line: str) -> List[str]:
    """Return identifier-like tokens from a code line."""
    return TOKEN_RE.findall(line)


@register_loader("cfg")
class CFGLoader(GraphLoaderBase):
    """
    두 가지 입력 스키마를 모두 지원한다.

    ① 기존 CFG‑JSON
       ─ {"nodes": [...], "edges": [...], "entry": id?}

    ② PE‑메타데이터(JSON)  :  :contentReference[oaicite:0]{index=0}, :contentReference[oaicite:1]{index=1} 등
       ─ 역공학 도구 출력 그대로
         → on‑the‑fly로 (①) 스키마로 변환 후 기존 로직 재사용
    """

    # ========================================================= #
    # 1. 메인 파서
    # ========================================================= #
    def _parse(self, src: str | Path | bytes, **kwargs) -> Data:  # noqa: N802
        js = self._read_json(src)

        # -------- A) 스키마 감지 & 필요 시 변환 ---------------- #
        if "nodes" not in js:           # ⇒ PE 메타 형식
            js = self._convert_pejson_to_cfg(js)

        # -------- B) 기존 CFG 로직 ---------------------------- #
        nodes: Sequence[dict] = js["nodes"]
        id2idx: Dict[int, int] = {n["id"]: i for i, n in enumerate(nodes)}
        addrs: List[int] = []
        for n in nodes:
            raw = n.get("addr", f"BB_{n['id']}")
            try:
                addrs.append(_hex_to_int(raw))
            except Exception:  # noqa: BLE001 -- fallback for non numeric addr
                addrs.append(0)

        # ---- (1) 노드 feature 행렬 --------------------------- #
        if any("feat" in n and n["feat"] for n in nodes):
            feat_dim = max(len(n.get("feat", [])) for n in nodes)
            x = torch.zeros((len(nodes), feat_dim), dtype=torch.float)
            for i, n in enumerate(nodes):
                if n.get("feat"):
                    v = torch.as_tensor(n["feat"], dtype=torch.float)
                    x[i, : v.numel()] = v
        else:
            x = None

        # ---- (2) edge_index & edge_type ---------------------- #
        raw_edges = js.get("edges", [])
        if raw_edges:
            src_idx, dst_idx, type_str = [], [], []
            for e in raw_edges:
                try:
                    src_idx.append(id2idx[e["src"]])
                    dst_idx.append(id2idx[e["dst"]])
                except KeyError as err:
                    raise ValueError(f"edge references unknown node id: {err}") from None
                type_str.append(e.get("type", "unknown"))
            edge_index = torch.tensor([src_idx, dst_idx], dtype=torch.long)
            type2id = {t: i for i, t in enumerate(sorted(set(type_str)))}
            edge_type = torch.tensor([type2id[t] for t in type_str], dtype=torch.long)
        else:
            edge_index = torch.empty((2, 0), dtype=torch.long)
            edge_type = torch.empty((0,), dtype=torch.long)

        # ---- (3) PyG Data ------------------------------------ #
        data = Data(edge_index=edge_index, edge_type=edge_type)
        if x is not None:
            data.x = x
        data.addr = addrs
        data.node_id = torch.tensor(list(id2idx.keys()), dtype=torch.long)
        data.kind_str = [n.get("kind", "") for n in nodes]
        texts = [n.get("text") for n in nodes]
        if any(t is not None for t in texts):
            data.text = texts
        if "entry" in js:                                 # 기존 엔트리 필드
            data.entry_id = torch.tensor([id2idx[js["entry"]]], dtype=torch.long)
        elif "entry_id" in js:                             # 변환 시 추가한 필드
            data.entry_id = torch.tensor([id2idx[js["entry_id"]]], dtype=torch.long)
        return data

    # ========================================================= #
    # 2. PE‑JSON → CFG 변환기
    # ========================================================= #
    @staticmethod
    def _convert_pejson_to_cfg(js: dict) -> dict:
        """
        간단 CFG 생성 규칙 (정적 분석 없이 ‘거친’ 그래프이므로 downstream에서
        ‘파일 단위 통계’ 특성 생성용으로 주로 사용):

          • root(node kind=file) → section 노드(edge=contains)
          • 각 section 내부에 1개의 BB 노드(fake BB) 생성
         • section BB들을 cfg로 연결 (PE 섹션 순서)
          • entry_point address가 해당 section BB라면 entry 지정
        """
        nodes: List[dict] = []
        edges: List[Dict[str, Union[int, str]]] = []

        next_id = 0
        root_id = next_id
        root_base = js.get("get_metadata", {}).get("base", 0)
        nodes.append({"id": root_id, "addr": _hex_to_int(root_base), "kind": "file", "feat": []})
        next_id += 1

        # 1) 섹션 순서 보존
        sections = js.get("pe_headers", {}).get("sections", [])
        sec_nodes: List[Tuple[int, dict]] = []
        for sec in sections:
            sid = next_id
            next_id += 1
            vsize = _hex_to_int(sec.get("virtual_size", 0))
            rsize = _hex_to_int(sec.get("raw_size",    0))
            addr  = _hex_to_int(sec.get("virtual_address", "0x0"))
            name = sec.get("name", "").strip()
            nodes.append({
                "id": sid,
                "addr": addr,
                "kind": "section",
                "name": name,
                "feat": [vsize, rsize],
            })
            edges.append({"src": root_id, "dst": sid, "type": _EDGE_KIND_CONTAINS})
            sec_nodes.append((sid, sec))

        # 2) 섹션마다 ‘대표 BB’ 노드(fake basic block)
        bb_nodes: List[int] = []
        total_tokens = 0
        for sid, sec in sec_nodes:
            bid = next_id
            next_id += 1
            # 이 BB 주소는 section VA + 0 (섹션 시작)
            bb_addr = _hex_to_int(sec.get("virtual_address", "0x0"))
            nodes.append({"id": bid,
                          "addr": bb_addr,
                          "kind": "bb",
                          "feat": []})
            # section → BB (포함) edge
            edges.append({"src": sid, "dst": bid, "type": _EDGE_KIND_CONTAINS})
            bb_nodes.append(bid)

            tok_count = 0
            for field in ("asm_code", "code"):
                for line in sec.get(field, []):
                    for tok in _extract_tokens(line):
                        if tok_count >= 64 or total_tokens >= MAX_TOKENS:
                            break
                        nodes.append({"id": next_id, "kind": "token", "text": tok})
                        edges.append({"src": bid, "dst": next_id, "type": _EDGE_KIND_CONTAINS})
                        next_id += 1
                        tok_count += 1
                        total_tokens += 1
                    if tok_count >= 64 or total_tokens >= MAX_TOKENS:
                        break
                if tok_count >= 64 or total_tokens >= MAX_TOKENS:
                    break

        # 3) BB 사이 연속 edge (섹션 순서대로 fall‑through 가정)
        for a, b in zip(bb_nodes, bb_nodes[1:]):
            edges.append({"src": a, "dst": b, "type": _EDGE_KIND_LINEAR})

        # 4) entry_point 지정 (가능할 때만)
        entry_va = js.get("pe_headers", {}).get("entry_point")
        if entry_va:
            # entry_va 가 속한 섹션 BB 찾아서 저장
            entry_id = None
            for bid, sec in zip(bb_nodes, sections):
                start = _hex_to_int(sec.get("virtual_address", 0))
                size  = _hex_to_int(sec.get("virtual_size", 0))
                if start <= _hex_to_int(entry_va) < start + size:
                    entry_id = bid
                    break
            if entry_id is not None:
                # downstream 호환을 위해 json 최상단에 별도로 기록
                return {"nodes": nodes, "edges": edges, "entry_id": entry_id}
        return {"nodes": nodes, "edges": edges}

    # ========================================================= #
    # 3. JSON 로더 (gzip 자동 감지) – 기존과 동일
    # ========================================================= #
    @staticmethod
    def _read_json(src: Union[str, Path, bytes]) -> dict:
        if isinstance(src, bytes):
            raw = gzip.decompress(src) if src[:2] == b"\x1f\x8b" else src
            return json.loads(raw.decode("utf-8", errors="replace"))
        path = Path(src)
        if path.suffix == ".gz":
            with gzip.open(path, "rt", encoding="utf-8") as f:
                return json.load(f)
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)


# ──────────────────────────────────────────────────────────────────────────────
#  헬퍼
# ──────────────────────────────────────────────────────────────────────────────
def _hex_to_int(v: Union[str, int]) -> int:
    """16진/10진/정수 모두 안전하게 변환"""
    if isinstance(v, int):
        return v
    try:
        return int(v, 16)
    except ValueError:
        return int(v)
