#  ──────────────────────────────────────────────────────────────
#  robust-malware-graph / src / rulegen / feature_miner.py
#  ──────────────────────────────────────────────────────────────
"""
FeatureMiner
============

• 목적
    - XAI / Grad-CAM 단계에서 얻은 **노드 saliency 벡터**를 활용해
      YARA · CAPA 룰에 투입할 “후보 특성 문자열”을 추출한다.
    - 그래프 표현은 **torch_geometric.data.HeteroData**만을 사용한다
      (프로젝트 전반에서 요구하는 ‘torch_geometric 필수’ 조건 충족).

• 입 / 출력
    - 입력
        data     : HeteroData             ‒ AST/CFG/FCG/SysCall 통합 그래프
        saliency : Tensor | dict[str,Tensor]
                   (∑_B N, ) or {node_type: (N_t, )}
    - 출력
        List[str] (YARA·CAPA가 해석 가능한 패턴 문자열)
          예) 'call:kernel32!CreateFileW', '"%TEMP%" wide ascii',
              'import:WS2_32.dll', 'byte[4]:4D 5A 90 00'

• 작동 흐름
      1. saliency ≥ min_saliency, 또는 Top‑k 노드 선정
      2. 노드별 메타필드( `name`, `value`, `bytes`, `api`, … ) 점검
      3. YARA  ↔  CAPA 포맷용 문자열 정규화
      4. 빈도·saliency 기준 정렬 후 dedup → list 반환
"""

from __future__ import annotations

import re
import string
from collections import Counter
from pathlib import Path
from typing import Callable, Dict, List, Sequence, Tuple
import math

import torch
from torch_geometric.data import HeteroData

# 프로젝트 공통 유틸
try:  # logger는 선택적 의존성으로 두어 rulegen 단독 실행도 가능하게
    from common.logger import get_logger  # type: ignore
except ModuleNotFoundError:  # fallback
    import logging

    def get_logger(name: str):
        logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
        return logging.getLogger(name)


_LOG = get_logger(__name__)


class FeatureMiner:
    """
    YARA / CAPA 후보 특성 추출기
    """

    # ──────────────────────────────────────────────────────────
    # regex pre‑compilation (성능 ↑, 재사용 ↑)
    _WS = r"[ \t\r\n]+"  # whitespace
    _API_RX = re.compile(r"[A-Za-z0-9_#!?@\[\]\-\.+]{3,}")
    _STRING_FILTER = re.compile(r"[\x00-\x1F]")  # control chars
    _HEX_RX = re.compile(r"[0-9A-Fa-f]{2}")
    _UPPER_RX = re.compile(r"^[A-Z0-9_]+$")
    _LABEL_RX = re.compile(r"^(?:sub|loc|nullsub|unk)_[0-9A-Fa-f]+$")
    _LONG_HEX_RX = re.compile(r"^[0-9A-Fa-f]{20,}$")
    _ADDR_RX = re.compile(r"^(?:0x)?[0-9A-Fa-f]{4,}$")
    _SEC_RX = re.compile(r"^\.[A-Za-z0-9$.]{1,8}$")

    # 공통 타입·컴파일러 토큰 (자동 제외 목록)
    COMMON_TYPE_TOKENS = {
        "int",
        "char",
        "short",
        "long",
        "void",
        "float",
        "double",
        "unsigned",
        "signed",
        "size_t",
        "ptr",
        "byte",
        "word",
        "dword",
        "qword",
    }

    COMMON_COMPILER_TOKENS = {
        "memcpy",
        "memset",
        "memmove",
        "memcmp",
        "strcpy",
        "strcmp",
        "strlen",
        "sprintf",
        "printf",
        "scanf",
        "malloc",
        "free",
        "new",
        "delete",
    }

    def __init__(
        self,
        *,
        top_k: int = 50,
        top_k_percent: float | None = None,
        saliency_top_percent: float | None = None,
        dynamic_k: bool = False,
        min_saliency: float = 1e-3,
        keep_per_type: int = 20,
        max_per_prefix: int | None = None,
        benign_freqs: dict[str, int] | None = None,
        mal_freqs: dict[str, int] | None = None,
        freq_ratio: float = 1.0,
        freq_threshold: float | int = 0,
        benign_weight: float = 1.0,
        auto_relax: bool = True,
        verify_func: callable | None = None,
        restore_top_n: int = 1,
    ) -> None:
        """
        Args
        ----
        top_k         : 전체 노드 중 saliency 기준으로 상위 k개를 기본 타깃으로 삼는다.
        top_k_percent : 그래프 노드 수 비율 기반 자동 k 산출 (0~1 사이). 지정 시 ``top_k``보다 우선.
        dynamic_k     : 노드 saliency 분포(평균+표준편차)에 따라 k를 자동 조정한다.
        min_saliency  : 절대 saliency 임계값 (둘 중 하나라도 통과하면 선택).
        keep_per_type : 노드 타입마다 너무 편중되지 않도록 선정 상한.
        max_per_prefix : 정규화된 후보 토큰을 prefix별로 제한할 최대 개수.
        saliency_top_percent : 누적 saliency 기준 추가 필터 (0~1 사이).
        freq_ratio   : benign 빈도와 악성 빈도의 비율 비교시 사용.
        restore_top_n : 필터링 결과가 비어 있을 때 복원할 최대 토큰 수.
        """
        self.top_k = top_k
        self.top_k_percent = top_k_percent
        self.saliency_top_percent = saliency_top_percent
        self.dynamic_k = dynamic_k
        self.min_saliency = min_saliency
        self.keep_per_type = keep_per_type
        self.max_per_prefix = int(max_per_prefix) if max_per_prefix else None
        self.benign_freqs = benign_freqs
        self.mal_freqs = mal_freqs
        self.freq_ratio = float(freq_ratio)
        self.freq_threshold = freq_threshold
        self.benign_weight = float(benign_weight)
        self.auto_relax = bool(auto_relax)
        self.verify_func = verify_func
        self.restore_top_n = int(restore_top_n)

    # ────────────────────────────────────────── benign freq updates ―
    def update_benign_freqs(self, updates: Dict[str, int]) -> None:
        """Update :attr:`benign_freqs` with additional counts."""

        if self.benign_freqs is None:
            self.benign_freqs = {}
        for k, v in updates.items():
            self.benign_freqs[k] = self.benign_freqs.get(k, 0) + int(v)

    def set_freq_threshold(self, thresh: float) -> None:
        """Update :attr:`freq_threshold` value."""

        self.freq_threshold = float(thresh)

    # ──────────────────────────────────────────────── public ―─

    def __call__(
        self,
        data: HeteroData,
        saliency: torch.Tensor | Dict[str, torch.Tensor],
        sal_stats: Dict[str, Tuple[float, float]] | None = None,
    ) -> List[str]:
        return self.mine(data, saliency, sal_stats)

    def mine(
        self,
        data: HeteroData,
        saliency: torch.Tensor | Dict[str, torch.Tensor],
        sal_stats: Dict[str, Tuple[float, float]] | None = None,
    ) -> List[str]:
        """
        핵심 메서드: saliency 벡터와 그래프를 분석해 문자열 패턴 리스트 반환
        """
        if isinstance(saliency, dict):
            flat_sal, node_offsets = self._flatten_saliency_dict(saliency, data)
        else:
            flat_sal = saliency
            node_offsets = self._infer_offsets_from_data(data)

        flat_sal = flat_sal.detach().cpu()

        # 1) saliency 상위 노드 선택
        selected_indices = self._select_nodes(flat_sal)

        # 타입별 상한 적용을 위해 선택 노드를 그룹화한다.
        if self.keep_per_type > 0:
            grouped: Dict[str, torch.Tensor] = {}
            for ntype, (start, end) in node_offsets.items():
                mask = (selected_indices >= start) & (selected_indices < end)
                idxs = selected_indices[mask]
                if idxs.numel() == 0:
                    continue
                sal_slice = flat_sal[idxs]
                order = torch.argsort(sal_slice, descending=True)
                idxs = idxs[order]
                if idxs.numel() > self.keep_per_type:
                    _LOG.debug(
                        "FeatureMiner: trimmed %d nodes of type '%s'",
                        idxs.numel() - self.keep_per_type,
                        ntype,
                    )
                    idxs = idxs[: self.keep_per_type]
                grouped[ntype] = idxs
            if grouped:
                selected_indices = torch.cat(list(grouped.values()))
                sal_vals = flat_sal[selected_indices]
                order = torch.argsort(sal_vals, descending=True)
                selected_indices = selected_indices[order]

        selected_set = set(selected_indices.tolist())

        # 2) 노드별 메타 추출
        raw_features: List[str] = []
        feat_sal_map: Dict[str, float] = {}
        for global_idx in selected_indices:
            ntype, local_idx = self._map_global_to_local(global_idx, node_offsets)
            meta = data[ntype]
            cand = self._extract_candidates(
                data, ntype, local_idx, meta, node_offsets, selected_set
            )
            raw_features.extend(cand)
            sal_val = float(flat_sal[global_idx])
            for feat in cand:
                feat_sal_map[feat] = feat_sal_map.get(feat, 0.0) + sal_val

        # 3) 정규화 & dedup 정렬
        cleaned = self._normalize_and_rank(raw_features, feat_sal_map)
        cleaned = self._filter_by_benign_freq(cleaned, feat_sal_map)
        if sal_stats is not None:
            cleaned = self._filter_by_saliency_stats(cleaned, sal_stats)
        _LOG.debug("FeatureMiner: mined %d distinct candidates", len(cleaned))
        return cleaned

    # ─────────────────────────────────────────── helpers (saliency) ―─

    def _flatten_saliency_dict(
        self, sal_dict: Dict[str, torch.Tensor], data: HeteroData
    ) -> Tuple[torch.Tensor, Dict[str, Tuple[int, int]]]:
        """
        saliency 가 node_type별 dict 형태일 때 하나의 1‑D 텐서로 병합
        반환 값
        -------
        flat_sal   : shape (∑_t N_t, )
        offsets    : {ntype: (start, end)}
        """
        pieces: List[torch.Tensor] = []
        offsets: Dict[str, Tuple[int, int]] = {}
        cursor = 0
        for ntype in data.node_types:
            s = sal_dict.get(ntype)
            if s is None:
                s = torch.zeros(data[ntype].num_nodes, dtype=torch.float32)
            pieces.append(s)
            offsets[ntype] = (cursor, cursor + s.numel())
            cursor += s.numel()
        return torch.cat(pieces, dim=0), offsets

    def _infer_offsets_from_data(self, data: HeteroData) -> Dict[str, Tuple[int, int]]:
        """
        flat saliency가 주어졌을 때 node_type별 offset 계산
        """
        offsets: Dict[str, Tuple[int, int]] = {}
        cursor = 0
        for ntype in data.node_types:
            n_nodes = data[ntype].num_nodes
            offsets[ntype] = (cursor, cursor + n_nodes)
            cursor += n_nodes
        return offsets

    def _select_nodes(self, flat_sal: torch.Tensor) -> torch.Tensor:
        """
        top‑k · min_saliency 기준 노드 인덱스 선택 (global idx).
        """
        flat_sal = flat_sal.detach().cpu()
        # 조건 1) 절대 threshold
        mask = flat_sal >= self.min_saliency

        k = self.top_k
        n_nodes = flat_sal.numel()
        if self.top_k_percent is not None:
            k = max(int(n_nodes * self.top_k_percent), 1)

        if self.dynamic_k:
            thresh = float((flat_sal.mean() + flat_sal.std()).item())
            dyn_mask = flat_sal >= max(thresh, self.min_saliency)
            if dyn_mask.any():
                mask |= dyn_mask
                k = max(k, int(dyn_mask.sum().item()))

        if n_nodes > k:
            topk_idx = torch.topk(flat_sal, k).indices
            mask[topk_idx] = True

        selected = mask.nonzero(as_tuple=False).squeeze(1)
        if selected.numel() > k:
            topk_idx = torch.topk(flat_sal[selected], k).indices
            selected = selected[topk_idx]

        if (
            self.saliency_top_percent is not None
            and selected.numel() > 0
            and self.saliency_top_percent > 0
        ):
            order = torch.argsort(flat_sal[selected], descending=True)
            sal_slice = flat_sal[selected][order]
            cum = torch.cumsum(sal_slice, dim=0)
            total = float(cum[-1])
            if total > 0:
                ratio = cum / total
                idx = torch.searchsorted(
                    ratio, float(self.saliency_top_percent), right=False
                ).item()
                keep_len = min(int(idx) + 1, selected.numel())
                selected = selected[order][:keep_len]
            else:
                selected = selected[order[:1]]

        return selected

    def _map_global_to_local(
        self,
        global_idx: int,
        offsets: Dict[str, Tuple[int, int]],
    ) -> Tuple[str, int]:
        """
        global → (node_type, local_idx) 매핑
        """
        for ntype, (start, end) in offsets.items():
            if start <= global_idx < end:
                return ntype, global_idx - start
        raise IndexError("global_idx out of range")

    def _map_local_to_global(
        self, ntype: str, local_idx: int, offsets: Dict[str, Tuple[int, int]]
    ) -> int:
        """(node_type, local_idx) → global index"""
        start, _ = offsets[ntype]
        return start + local_idx

    # ───────────────────────────────────────── helpers (extract) ―─

    def _extract_candidates(
        self,
        data: HeteroData,
        ntype: str,
        local_idx: int,
        meta: torch_geometric.data.Data,
        offsets: Dict[str, Tuple[int, int]],
        selected_set: set[int] | None = None,
    ) -> List[str]:
        """한 노드에서 YARA·CAPA 후보 문자열을 추출한다.

        노드 메타필드는 다음 키 중 하나 이상을 가정한다.

        - ``name`` / ``api``            : 함수 호출명
        - ``value`` / ``string``        : 문자열 리터럴
        - ``import`` / ``dll``          : 의존 DLL 이름
        - ``bytes``                     : Raw byte 시퀀스
        - ``syscall`` / ``name``        : 시스템 호출명

        추가 도메인 feature 삽입을 원할 시 이 함수를 수정하여 보강
        (파일 경로, 레지스트리 키, URL, PE‑섹션 이름 등).
        """
        alias_map = {
            "name": ["name", "api"],
            "value": ["value", "string", "text"],
            "import": ["import", "import_"],
            "bytes": ["bytes"],
            "syscall": ["syscall", "syscall_name"],
            "path": ["path", "filepath"],
            "url": ["url", "uri"],
            "reg": ["reg", "key", "registry"],
        }

        def _lookup(m, key):
            x = getattr(m, key, None)
            if x is None and hasattr(m, "meta"):
                meta_dict = getattr(m, "meta")
                if isinstance(meta_dict, dict):
                    x = meta_dict.get(key)
            return x

        # One-time, very detailed debug log for the first selected node.
        if not hasattr(self, "_has_logged_detailed_meta"):
            _LOG.debug("=" * 50)
            _LOG.debug(
                f"DEBUG: Detailed inspection of first selected node (ntype='{ntype}', local_idx={local_idx})."
            )
            _LOG.debug(
                f"DEBUG: All available keys in `meta` object: {list(meta.keys())}"
            )

            meta_content = _lookup(meta, "meta")
            if (
                meta_content is not None
                and isinstance(meta_content, (list, tuple))
                and local_idx < len(meta_content)
            ):
                _LOG.debug(
                    f"DEBUG: Content of `meta.meta` field: {meta_content[local_idx]}"
                )
            else:
                _LOG.debug("DEBUG: `meta.meta` field not found or not accessible.")

            # Temporarily define _get here to test it
            def _get_for_debug(attr: str):
                keys = alias_map.get(attr, [attr])
                for key in keys:
                    x = _lookup(meta, key)
                    if x is None:
                        continue
                    if isinstance(x, (list, tuple)):
                        if local_idx < len(x):
                            return x[local_idx]
                        continue
                    if torch.is_tensor(x):
                        try:
                            arr = x[local_idx]
                            if arr.ndim == 0:
                                return str(arr.item())
                            return bytes(arr.tolist()).decode(errors="ignore")
                        except Exception:
                            continue
                    try:
                        return x[local_idx] if hasattr(x, "__getitem__") else x
                    except Exception:
                        continue
                return None

            for attr_to_test in ["name", "value", "syscall"]:
                retrieved_val = _get_for_debug(attr_to_test)
                _LOG.debug(
                    f"DEBUG: _get('{attr_to_test}') returned: {retrieved_val} (type: {type(retrieved_val)})"
                )

            self._has_logged_detailed_meta = True
            _LOG.debug("=" * 50)

        candidates: List[str] = []

        # 메타 필드 단일 접근 헬퍼
        def _get(attr: str):
            keys = alias_map.get(attr, [attr])
            for key in keys:
                # primarily rely on dict-style access
                x = meta.get(key, None)
                if x is None:
                    meta_dict = meta.get("meta", {})
                    if isinstance(meta_dict, dict):
                        x = meta_dict.get(key)
                if x is None:
                    x = _lookup(meta, key)
                if x is None:
                    continue
                # StringTensor 또는 List[str]일 수 있음
                if isinstance(x, (list, tuple)):
                    if local_idx < len(x):
                        return x[local_idx]
                    continue
                # torch 텐서 → str
                if torch.is_tensor(x):
                    # assume 1‑D tensor of ints (char codes) or encoded bytes
                    try:
                        arr = x[local_idx]
                        if arr.ndim == 0:  # scalar id
                            return str(arr.item())
                        return bytes(arr.tolist()).decode(errors="ignore")
                    except Exception:
                        continue
                # plain python object
                try:
                    if isinstance(x, str):
                        return x
                    return x[local_idx] if hasattr(x, "__getitem__") else x
                except Exception:
                    continue
            return None

        # 1) API / 함수명
        name = _get("name") or _get("api")
        if isinstance(name, str):
            n = name.lower()
            if n.startswith(("sub_", "nullsub", "loc_")) or n in {"start", "_start"}:
                name = None

        chain_label = None
        if isinstance(name, str) and self._API_RX.fullmatch(name):
            candidates.append(f"call:{name}")
            chain_label = name

        # 2) 문자열 리터럴
        string_val = _get("value") or _get("string")
        if isinstance(string_val, str):
            s = self._STRING_FILTER.sub("", string_val)
            # 짧거나 null bytes만 있으면 제외
            if len(s) >= 4 and any(c in string.printable for c in s):
                yara = f'"{s}" wide ascii nocase'
                candidates.append(yara)

        # 3) import library
        lib = _get("import") or _get("dll")
        if isinstance(lib, str) and lib.lower().endswith(".dll"):
            candidates.append(f"import:{lib}")

        # 4) raw bytes (선택적)
        byte_arr = _get("bytes")
        if isinstance(byte_arr, (bytes, bytearray)):
            hx = " ".join(f"{b:02X}" for b in byte_arr[:8])  # 처음 8B만
            if self._HEX_RX.search(hx):
                candidates.append(f"byte[{len(byte_arr)}]:{hx}")

        # 5) section 이름
        if ntype == "section":
            sec = _get("name") or _get("section_name")
            if isinstance(sec, str):
                s = sec.strip("\x00 ").strip()
                if s and s not in {".text", ".data", ".rdata"}:
                    candidates.append(f'"{s}" ascii nocase')
                    candidates.append(f"marker:{s}")

        # 6) 기타 Heuristic
        #    예) ntype == 'syscall' 등
        syscall = _get("syscall")
        if syscall is None and ntype == "syscall":
            syscall = _get("name")
        if isinstance(syscall, str):
            candidates.append(f"syscall:{syscall}")

        # 7) 파일 경로
        path_val = _get("path")
        if path_val is None and ntype == "file":
            path_val = _get("name")
        if isinstance(path_val, str):
            p = self._STRING_FILTER.sub("", path_val)
            if p:
                candidates.append(f'"{p}" wide ascii nocase')
                for seg in re.split(r"[\\\\/]+", p):
                    seg = seg.strip()
                    if seg:
                        candidates.append(f"path:{seg}")

        # 8) 레지스트리 경로
        reg_val = _get("reg")
        if reg_val is None and ntype == "registry":
            reg_val = _get("name")
        if isinstance(reg_val, str):
            r = self._STRING_FILTER.sub("", reg_val)
            if r:
                candidates.append(f'"{r}" wide ascii nocase')
                for seg in re.split(r"\\\\+", r):
                    seg = seg.strip()
                    if seg:
                        candidates.append(f"reg:{seg}")

        # 9) URL
        url_val = _get("url")
        if isinstance(url_val, str):
            u = self._STRING_FILTER.sub("", url_val)
            m = re.match(r"https?://([^/]+)(/.*)?", u, re.IGNORECASE)
            if m:
                domain = m.group(1)
                if domain:
                    candidates.append(f"url:{domain}")
                path_part = m.group(2) or ""
                for seg in path_part.split("/"):
                    seg = seg.strip()
                    if seg:
                        candidates.append(f"url:{seg}")
            elif u:
                candidates.append(f'"{u}" wide ascii nocase')

        # 이웃 노드 동시 선택 시 chain 토큰 생성
        if selected_set is not None and chain_label is not None:
            for etype in data.edge_types:
                src, _, dst = etype
                if src != ntype:
                    continue
                edges = data[etype].edge_index
                rows = (edges[0] == local_idx).nonzero(as_tuple=False).view(-1)
                for r in rows.tolist():
                    nbr_local = int(edges[1, r])
                    nbr_global = self._map_local_to_global(dst, nbr_local, offsets)
                    if nbr_global not in selected_set:
                        continue
                    nbr_meta = data[dst]
                    nbr_name = None
                    for key in ["name", "api"]:
                        val = _lookup(nbr_meta, key)
                        if val is None:
                            continue
                        if isinstance(val, (list, tuple)) and nbr_local < len(val):
                            nbr_name = val[nbr_local]
                        elif torch.is_tensor(val):
                            try:
                                arr = val[nbr_local]
                                if arr.ndim == 0:
                                    nbr_name = str(arr.item())
                                else:
                                    nbr_name = bytes(arr.tolist()).decode(
                                        errors="ignore"
                                    )
                            except Exception:
                                continue
                        else:
                            try:
                                nbr_name = (
                                    val[nbr_local]
                                    if hasattr(val, "__getitem__")
                                    else val
                                )
                            except Exception:
                                continue
                        if isinstance(nbr_name, str) and self._API_RX.fullmatch(
                            nbr_name
                        ):
                            candidates.append(f"chain:{chain_label}→{nbr_name}")
                        break

        return candidates

    # ───────────────────────────────────────── helpers (post) ―─

    def _normalize_and_rank(
        self, feats: Sequence[str], sal_map: Dict[str, float] | None = None
    ) -> List[str]:
        """
        • 중복 제거
        • 출현 빈도 + saliency 기반 단순 정렬
          (현재 saliency는 node별이므로, 동일 스트링이 여러 노드서 나오면 freq 교차 반영)
        """
        cnt = Counter(feats)
        items = []
        for feat, freq in cnt.items():
            sal = sal_map.get(feat, 0.0) if sal_map else 0.0
            items.append((feat, sal, freq))
        ranked = sorted(items, key=lambda t: (-t[1], -t[2], t[0]))
        filtered: List[str] = []
        for feat, _, _ in ranked:
            token = feat
            if token.startswith(
                ("call:", "chain:", "import:", "syscall:", "path:", "reg:", "url:")
            ):
                token = token.split(":", 1)[1]
            if token.startswith('"'):
                m = re.match(r'"([^"\n]+)', token)
                if m:
                    token = m.group(1)
            token = token.strip()
            token_l = token.lower()
            if token_l in self.COMMON_TYPE_TOKENS:
                continue
            if token_l in self.COMMON_COMPILER_TOKENS:
                continue
            if self._UPPER_RX.fullmatch(token):
                continue
            if self._LABEL_RX.fullmatch(token):
                continue
            if self._LONG_HEX_RX.fullmatch(token):
                continue
            if self._ADDR_RX.fullmatch(token):
                continue
            if self._SEC_RX.fullmatch(token):
                if token.lower() in {".text", ".data", ".rdata", ".rsrc"}:
                    continue
            filtered.append(feat)
        if self.max_per_prefix and self.max_per_prefix > 0:
            result: List[str] = []
            counts: Dict[str, int] = {}

            def _prefix(s: str) -> str:
                if s.startswith('"'):
                    return "string"
                if s.startswith("byte["):
                    return "byte"
                return s.split(":", 1)[0]

            for f in filtered:
                pfx = _prefix(f)
                cnt = counts.get(pfx, 0)
                if cnt < self.max_per_prefix:
                    result.append(f)
                    counts[pfx] = cnt + 1
            filtered = result

        return filtered

    def _filter_by_saliency_stats(
        self, feats: Sequence[str], stats: Dict[str, Tuple[float, float]]
    ) -> List[str]:
        """악성/정상 saliency 통계 기반 필터링"""
        filtered: List[str] = []
        for f in feats:
            val = stats.get(f)
            if val is None:
                filtered.append(f)
                continue
            mal_score, ben_score = val
            if mal_score > self.min_saliency and mal_score > ben_score:
                filtered.append(f)
        return filtered

    def _filter_by_benign_freq(
        self, feats: Sequence[str], sal_map: Dict[str, float] | None = None
    ) -> List[str]:
        """정상 샘플에서 자주 등장하는 토큰을 제거한다."""
        if not self.benign_freqs:
            return list(feats)

        weight = getattr(self, "benign_weight", 1.0)
        scored = []
        for f in feats:
            sal = sal_map.get(f, 0.0) if sal_map else 0.0
            freq = self.benign_freqs.get(f, 0)
            score = sal - weight * math.log(freq + 1)
            scored.append((f, score))
        scored.sort(key=lambda t: t[1], reverse=True)
        ordered = [f for f, _ in scored]

        threshold = float(self.freq_threshold)
        ratio = float(self.freq_ratio)
        filtered: List[str] = []
        while True:
            filtered.clear()
            for f in ordered:
                freq = self.benign_freqs.get(f)
                mal = self.mal_freqs.get(f) if self.mal_freqs else None
                if freq is not None:
                    if freq >= threshold:
                        continue
                    if mal is not None and freq >= mal * ratio:
                        continue
                filtered.append(f)
            if filtered or not ordered or not self.auto_relax:
                break
            if threshold > 1:
                threshold /= 2
            if self.mal_freqs and ratio > 0:
                ratio /= 2
            if threshold <= 1 and (not self.mal_freqs or ratio <= 0):
                break
        if filtered or not ordered:
            return filtered

        # 모든 후보가 제거된 경우
        cand_order: List[str] = []
        if self.mal_freqs:
            high_mal: List[str] = []
            for f in ordered:
                ben = self.benign_freqs.get(f, 0)
                mal = self.mal_freqs.get(f, 0)
                if mal > ben * 2:
                    high_mal.append(f)
            if high_mal:
                cand_order = sorted(
                    high_mal,
                    key=lambda x: sal_map.get(x, 0.0) if sal_map else 0.0,
                    reverse=True,
                )

        if not cand_order:
            if self.mal_freqs:

                def _ratio(tok: str) -> float:
                    ben = self.benign_freqs.get(tok, float("inf"))
                    mal = self.mal_freqs.get(tok, 0)
                    return ben / mal if mal > 0 else float("inf")

                cand_order = sorted(
                    ordered,
                    key=lambda x: (
                        _ratio(x),
                        self.benign_freqs.get(x, float("inf")),
                        -(sal_map.get(x, 0.0) if sal_map else 0.0),
                    ),
                )
            else:
                cand_order = ordered

        if not cand_order:
            return []

        top_n = getattr(self, "restore_top_n", len(cand_order))
        return cand_order[:top_n]

    # ──────────────────────────────────────────────────────────


# ────────────────────────── CLI 단독 실행 for quick test ──
if __name__ == "__main__":
    import argparse
    from torch_geometric.data import HeteroData

    parser = argparse.ArgumentParser(description="FeatureMiner quick‑test")
    parser.add_argument("--top_k", type=int, default=30)
    args = parser.parse_args()

    # dummy graph ‒ 단일 실행 확인용
    g = HeteroData()
    g["func"].x = torch.zeros(3, 1)
    g["func"].name = ["CreateFileW", "memcpy", "VirtualAlloc"]
    g["str"].x = torch.zeros(2, 1)
    g["str"].value = ["%TEMP%\\evil.bin", "ok"]
    g["import"].x = torch.zeros(1, 1)
    g["import"].import_ = ["WS2_32.dll"]  # 'import'는 예약어라 필드명 수정
    sal = torch.tensor([0.9, 0.1, 0.05, 0.8, 0.02, 0.6])  # global saliency

    miner = FeatureMiner(top_k=args.top_k)
    for feat in miner(g, sal):
        print(feat)
