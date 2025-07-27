from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Dict, List, Sequence, Tuple, Union

import torch
from torch_geometric.data import Data

from .base import GraphLoaderBase, register_loader
from .common_token_utils import TOKEN_RE, MAX_TOKENS, split_name

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #
_EDGE_KIND_CONTAINS = "contains"


@register_loader("fcg")
class FCGLoader(GraphLoaderBase):
    """
    (1) 기존 Function‑Call‑Graph JSON
        ─ {"functions": [...], "calls": [...], "entry": id?}

    (2) PE 메타데이터 JSON            ◆NEW
        ─ "functions" 키가 없으면 본 형식으로 간주하여
          entry_start → section_i …  가상 FCG를 동적으로 생성
    """

    # ========================================================= #
    # 1. 메인 파서
    # ========================================================= #
    def _parse(self, src: str | Path | bytes, **kwargs) -> Data:  # noqa: N802
        js = self._read_json(src)

        # -------- A) 스키마 감지 & 필요 시 변환 ---------------- #
        if "functions" not in js:          # ⇒ PE 메타 형식
            js = self._convert_pejson_to_fcg(js)

        funcs: Sequence[dict] = js["functions"]

        # -------- B) 함수 이름을 토큰 노드로 변환 -------------- #
        next_id = max((f["id"] for f in funcs), default=-1) + 1
        token_cnt = 0
        for fn in list(funcs):
            for tok in split_name(fn.get("name", "")):
                if token_cnt >= MAX_TOKENS:
                    break
                funcs.append({"id": next_id, "kind": "token", "text": tok})
                js.setdefault("calls", []).append(
                    {"src": fn["id"], "dst": next_id, "type": _EDGE_KIND_CONTAINS}
                )
                next_id += 1
                token_cnt += 1
            if token_cnt >= MAX_TOKENS:
                break

        id2idx: Dict[int, int] = {f["id"]: i for i, f in enumerate(funcs)}
        n_nodes = len(funcs)

        # -------- 1) 노드 메타 & feat ------------------------- #
        names: List[str] = [f.get("name", f"fn_{f['id']}") for f in funcs]
        addrs: List[int] = []
        for f in funcs:
            try:
                addrs.append(_hex_to_int(f.get("addr", 0)))
            except Exception:  # noqa: BLE001 -- non-numeric addr
                addrs.append(0)
        is_ext = torch.tensor([bool(f.get("external", False)) for f in funcs])

        # --- feat 행렬 (있을 때만) ---------------------------- #
        if any("feat" in f and f["feat"] for f in funcs):
            feat_dim = max(len(f.get("feat", [])) for f in funcs)
            x = torch.zeros((n_nodes, feat_dim), dtype=torch.float)
            for i, f in enumerate(funcs):
                if f.get("feat"):
                    v = torch.as_tensor(f["feat"], dtype=torch.float)
                    x[i, : v.numel()] = v
        else:
            x = None

        # -------- 2) edge_index & edge_type ------------------- #
        raw_calls = js.get("calls", [])
        if raw_calls:
            src_idx, dst_idx, etype_str = [], [], []
            for c in raw_calls:
                try:
                    src_idx.append(id2idx[c["src"]])
                    dst_idx.append(id2idx[c["dst"]])
                except KeyError as err:
                    raise ValueError(
                        f"call references unknown function id: {err}"
                    ) from None
                etype_str.append(c.get("type", "unknown"))

            edge_index = torch.tensor([src_idx, dst_idx], dtype=torch.long)
            type2id = {t: i for i, t in enumerate(sorted(set(etype_str)))}
            edge_type = torch.tensor([type2id[t] for t in etype_str], dtype=torch.long)
        else:
            edge_index = torch.empty((2, 0), dtype=torch.long)
            edge_type = torch.empty((0,), dtype=torch.long)

        # -------- 3) PyG Data --------------------------------- #
        data = Data(edge_index=edge_index, edge_type=edge_type)
        if x is not None:
            data.x = x
        data.name = names
        data.addr = addrs
        data.is_external = is_ext.bool()
        data.node_id = torch.tensor(list(id2idx.keys()), dtype=torch.long)
        data.kind_str = [f.get("kind", "function") for f in funcs]
        texts = [f.get("text") for f in funcs]
        if any(t is not None for t in texts):
            data.text = texts

        # 엔트리 필드
        if "entry" in js:
            data.entry_id = torch.tensor([id2idx[js["entry"]]], dtype=torch.long)
        elif "entry_id" in js:            # 변환 시 추가 필드
            data.entry_id = torch.tensor([id2idx[js["entry_id"]]], dtype=torch.long)

        return data

    # ========================================================= #
    # 2. PE‑JSON → FCG 변환기
    # ========================================================= #
    @staticmethod
    def _convert_pejson_to_fcg(js: dict) -> dict:
        """
        PE 메타 ➜ {functions, calls, entry} 간단 변환
          • id 0 : entry_start (PE entry_point)
          • id 1..N : section_i  (각 섹션을 ‘함수’로 모델링)
          • calls : entry_start → section_i
        """
        functions: List[dict] = []
        calls: List[Dict[str, Union[int, str]]] = []

        # 1) entry_start
        ep = _hex_to_int(js.get("pe_headers", {}).get("entry_point", "0x0"))
        ep_size = _hex_to_int(js.get("get_current_function", {}).get("size", 0))
        functions.append(
            {"id": 0, "name": "entry_start", "addr": ep, "feat": [ep_size]}
        )

        # 2) 섹션 가상 함수
        sections = js.get("pe_headers", {}).get("sections", [])
        for idx, sec in enumerate(sections, start=1):
            name = sec.get("name", "").strip() or f"sec_{idx}"
            addr = _hex_to_int(sec.get("virtual_address", "0x0"))
            vsize = _hex_to_int(sec.get("virtual_size", 0))
            functions.append(
                {
                    "id": idx,
                    "name": f"sec_{idx}_{name}",
                    "section_name": name,
                    "addr": addr,
                    "feat": [vsize],
                }
            )
            calls.append({"src": 0, "dst": idx, "type": "calls"})

        # 3) 함수 이름 토큰 노드
        next_id = len(functions)
        token_cnt = 0
        for fn in list(functions):
            for tok in split_name(fn["name"]):
                if token_cnt >= MAX_TOKENS:
                    break
                functions.append({"id": next_id, "kind": "token", "text": tok})
                calls.append({"src": fn["id"], "dst": next_id, "type": _EDGE_KIND_CONTAINS})
                next_id += 1
                token_cnt += 1
            if token_cnt >= MAX_TOKENS:
                break

        return {"functions": functions, "calls": calls, "entry_id": 0}

    # ========================================================= #
    # 3. JSON / JSON.GZ 로더
    # ========================================================= #
    @staticmethod
    def _read_json(src: Union[str, Path, bytes]) -> dict:
        """bytes · .json · .json.gz 모두 지원"""
        if isinstance(src, bytes):
            raw = gzip.decompress(src) if src[:2] == b"\x1f\x8b" else src
            return json.loads(raw.decode("utf‑8", errors="replace"))
        path = Path(src)
        if path.suffix == ".gz":
            with gzip.open(path, "rt", encoding="utf‑8") as f:
                return json.load(f)
        with path.open("r", encoding="utf‑8") as f:
            return json.load(f)


# ───────────────────────────────────────────────────────────────── #
#  헬퍼
# ───────────────────────────────────────────────────────────────── #
def _hex_to_int(v: Union[str, int]) -> int:
    """16진/10진/정수 모두 안전 변환"""
    if isinstance(v, int):
        return v
    try:
        return int(v, 16)
    except ValueError:
        return int(v)
