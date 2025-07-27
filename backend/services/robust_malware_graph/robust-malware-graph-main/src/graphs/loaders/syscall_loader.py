from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Dict, List, Union

import torch
from torch_geometric.data import Data

from .base import GraphLoaderBase, register_loader
from .common_token_utils import TOKEN_RE, MAX_TOKENS

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #
_EDGE_KIND_CONTAINS = "contains"


@register_loader("syscall")
class SysCallLoader(GraphLoaderBase):
    """
    (1) 기존 Syscall‑Trace JSON
        ─ {"syscalls": [...], "edges": [...], ...}

    (2) PE‑메타데이터 JSON (역공학 도구 출력)  ◆NEW
        ─ "syscalls" 키가 없으면 본 형식으로 간주하여
          open → map_section* → close 시퀀스로 on‑the‑fly 변환
    """

    # ============================================================= #
    # 1. 메인 파서
    # ============================================================= #
    def _parse(self, src: str | Path | bytes, **kwargs) -> Data:  # noqa: N802
        js = self._read_json(src)

        # -------- A) 스키마 감지 & 필요 시 변환 -------------------- #
        if "syscalls" not in js:          # ⇒ PE 메타 형식
            js = self._convert_pejson_to_syscalls(js)

        calls = js["syscalls"]
        syscall_names = [c["name"] for c in calls]
        n_nodes = len(calls)

        # -------- B) syscall 이름을 토큰 노드로 변환 ----------------- #
        token_nodes: List[dict] = []
        token_edges: List[Dict[str, Union[int, str]]] = []
        for sc in calls:
            if len(token_nodes) >= MAX_TOKENS:
                break
            tid = n_nodes + len(token_nodes)
            token_nodes.append({"id": tid, "kind": "token", "text": sc["name"]})
            token_edges.append(
                {"src": sc["id"], "dst": tid, "type": _EDGE_KIND_CONTAINS}
            )

        calls.extend(token_nodes)
        js.setdefault("edges", []).extend(token_edges)
        n_nodes = len(calls)

        # -------- 1) syscall 이름 → 정수 인코딩 -------------------- #
        names_all: List[str] = [c.get("name", c.get("text", "")) for c in calls]
        name2id: Dict[str, int] = {n: i for i, n in enumerate(sorted(set(names_all)))}
        sc_id = torch.tensor([name2id[n] for n in names_all], dtype=torch.long)

        # -------- 2) (선택) 노드 특성 행렬 ------------------------ #
        if any("feat" in c and c["feat"] for c in calls):
            feat_dim = max(len(c.get("feat", [])) for c in calls)
            x = torch.zeros((n_nodes, feat_dim), dtype=torch.float)
            for i, c in enumerate(calls):
                if c.get("feat"):
                    v = torch.as_tensor(c["feat"], dtype=torch.float)
                    x[i, : v.numel()] = v
        else:
            x = None

        # -------- 3) edge_index ---------------------------------- #
        raw_edges = js.get("edges", [])
        if raw_edges:
            first = raw_edges[0]
            if isinstance(first, dict):
                edges: List[List[int]] = []
                for e in raw_edges:
                    try:
                        edges.append([e["src"], e["dst"]])
                    except KeyError as err:
                        raise ValueError(f"edge missing key: {err}") from None
                edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
            else:
                edge_index = torch.tensor(raw_edges, dtype=torch.long).t().contiguous()
        else:
            edge_index = torch.empty((2, 0), dtype=torch.long)

        # -------- 4) PyG Data ------------------------------------ #
        data = Data(edge_index=edge_index, sc_id=sc_id)
        if x is not None:
            data.x = x
        data.sc_name = syscall_names
        data.token_text = [t["text"] for t in token_nodes]

        # -------- 5) (선택) 메타 필드 ----------------------------- #
        if "start_time" in js:
            data.start_time = float(js["start_time"])
        if "puid" in js:
            data.puid = int(js["puid"])

        return data

    # ============================================================= #
    # 2. PE‑JSON → Syscall Trace 변환기
    # ============================================================= #
    @staticmethod
    def _convert_pejson_to_syscalls(js: dict) -> dict:
        """
        PE 메타 ➜ {syscalls, edges} 스키마로 변환
          • open            (id=0)
          • map_section[i]  (id=1..N)
          • close           (id=N+1)
          • edges : {src,dst,type='seq'} 선형 시퀀스 (0→1→…→N+1)
        """
        syscalls: List[dict] = []

        # 1) open
        filesize = _hex_to_int(
            js.get("get_metadata", {}).get("filesize")
            or js.get("pe_headers", {}).get("filesize", 0)
        )
        syscalls.append({"id": 0, "name": "open", "feat": [filesize]})

        # 2) map_section per PE section
        sections = js.get("pe_headers", {}).get("sections", [])
        for i, sec in enumerate(sections, start=1):
            vsize = _hex_to_int(sec.get("virtual_size", 0))
            rsize = _hex_to_int(sec.get("raw_size", 0))
            syscalls.append(
                {"id": i, "name": "map_section", "feat": [vsize, rsize]}
            )

        # 3) close
        last_id = len(syscalls)
        syscalls.append({"id": last_id, "name": "close", "feat": []})

        # 4) linear edges
        edges = [
            {"src": i, "dst": i + 1, "type": "seq"}
            for i in range(last_id)
        ]

        # 5) start_time / puid 보존(가능 시)
        meta: Dict[str, Union[int, float]] = {}
        if "time_date_stamp" in js.get("pe_headers", {}):
            # PE TimeDateStamp를 start_time(유닉스 epoch) 필드에 임시 저장
            meta["start_time"] = _hex_to_int(js["pe_headers"]["time_date_stamp"])
        if "sha256" in js.get("get_metadata", {}):
            # SHA256 해시를 puid 해싱 대용(하위 32bit)으로 사용
            meta["puid"] = int(js["get_metadata"]["sha256"][:8], 16)

        return {"syscalls": syscalls, "edges": edges, **meta}

    # ============================================================= #
    # 3. JSON 로더 (gzip 자동 감지) – 기존
    # ============================================================= #
    @staticmethod
    def _read_json(src: Union[str, Path, bytes]) -> Dict:
        """bytes · .json · .json.gz → dict"""
        if isinstance(src, bytes):
            raw = gzip.decompress(src) if src.startswith(b"\x1f\x8b") else src
            return json.loads(raw.decode("utf‑8", errors="replace"))

        path = Path(src)
        if path.suffix == ".gz":
            with gzip.open(path, "rt", encoding="utf-8") as f:
                return json.load(f)
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)


# ------------------------------------------------------------------ #
# 4. 헬퍼
# ------------------------------------------------------------------ #
def _hex_to_int(v: Union[str, int]) -> int:
    """16진/10진/정수 모두 안전 변환"""
    if isinstance(v, int):
        return v
    try:
        return int(v, 16)
    except ValueError:
        return int(v)
