"""
src.graphs.features.pe_header_feat
==================================

PEHeaderFeatureExtractor
------------------------
• 입력 : PE 파일(*.exe, *.dll …) 경로 또는 이미 로드된 pefile.PE 객체
• 출력 : 1-D torch.Tensor (float32) — DOS/COFF/OptionalHeader 핵심 필드 벡터
• 정규화 : 'log' - log1p, 'minmax' - [0,1], 'raw' - 그대로
• 캐싱 : FeatureCache(Feather) — SHA-256 키 기반

필드
~~~~
DOS  : e_cblp, e_cp, e_cparhdr
COFF : NumberOfSections, TimeDateStamp, SizeOfOptionalHeader, Characteristics
OPT  : AddressOfEntryPoint, ImageBase, SectionAlignment, FileAlignment,
       SizeOfImage, Subsystem, DllCharacteristics
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Dict, Literal, Sequence

import numpy as np
import pefile
import torch

from ..utils import get_logger
from .cache import FeatureCache

# ──────────────────── 전역 설정 ────────────────────
_LOG = get_logger("features.pe_hdr")
_CACHE = FeatureCache(Path("~/.cache/pe_header"))
_NORM_MODE = Literal["log", "minmax", "raw"]

# min-max 범위(필요하면 데이터셋에 맞게 수정)
_MINMAX: Dict[str, tuple[int, int]] = {
    # DOS
    "e_cblp": (0, 2**16 - 1),
    "e_cp": (0, 2**16 - 1),
    "e_cparhdr": (0, 2**16 - 1),
    # COFF
    "NumberOfSections": (0, 255),
    "TimeDateStamp": (0, 0xFFFFFFFF),
    "SizeOfOptionalHeader": (0, 2**16 - 1),
    "Characteristics": (0, 0xFFFF),
    # OPT
    "AddressOfEntryPoint": (0, 0xFFFFFFFF),
    "ImageBase": (0, 0xFFFFFFFFFFFFFFFF),
    "SectionAlignment": (0, 0x10000),
    "FileAlignment": (0, 0x10000),
    "SizeOfImage": (0, 0x10000000),
    "Subsystem": (0, 0xFFFF),
    "DllCharacteristics": (0, 0xFFFF),
}
_FIELDS: Sequence[str] = tuple(_MINMAX.keys())


def _sha256_file(p: Path, chunk: int = 1 << 16) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for buf in iter(lambda: f.read(chunk), b""):
            h.update(buf)
    return h.hexdigest()


class PEHeaderFeatureExtractor:
    """
    Parameters
    ----------
    norm  : {'log','minmax','raw'}, default 'log'
    cache : bool, default True
    """

    def __init__(self, *, norm: _NORM_MODE = "log", cache: bool = True):
        self.norm = norm
        self.use_cache = cache
        self.log = _LOG

    # ──────────────────── Public ────────────────────
    def featurize(self, src: str | Path | pefile.PE) -> torch.Tensor:
        """PE 헤더 → Tensor[len(FIELDS)]."""
        pe_obj: pefile.PE
        cache_key: str | None

        # (1) 캐시 확인
        if isinstance(src, pefile.PE):
            pe_obj = src
            cache_key = None
        else:
            path = Path(src)
            cache_key = _sha256_file(path) if self.use_cache else None
            if cache_key and self.use_cache:
                try:
                    return _CACHE.load(cache_key).squeeze(0)
                except FileNotFoundError:
                    pass
            pe_obj = pefile.PE(str(path), fast_load=True)

        # (2) 필드 추출
        vals = [self._get_field(pe_obj, f) for f in _FIELDS]
        vec = torch.tensor(vals, dtype=torch.float32)

        # (3) 정규화
        vec = self._normalize(vec)

        # (4) 캐시 저장
        if cache_key and self.use_cache:
            _CACHE.save(cache_key, vec.unsqueeze(0))
        return vec

    # ──────────────────── 내부 ────────────────────
    @staticmethod
    def _get_field(pe: pefile.PE, name: str) -> int:
        try:
            if name in ("e_cblp", "e_cp", "e_cparhdr"):
                return int(getattr(pe.DOS_HEADER, name))
            if name in (
                "NumberOfSections",
                "TimeDateStamp",
                "SizeOfOptionalHeader",
                "Characteristics",
            ):
                return int(getattr(pe.FILE_HEADER, name))
            return int(getattr(pe.OPTIONAL_HEADER, name))
        except AttributeError:
            return 0

    def _normalize(self, v: torch.Tensor) -> torch.Tensor:
        if self.norm == "raw":
            return v
        if self.norm == "log":
            return torch.log1p(v)
        mins = torch.tensor([_MINMAX[f][0] for f in _FIELDS], dtype=torch.float32)
        maxs = torch.tensor([_MINMAX[f][1] for f in _FIELDS], dtype=torch.float32)
        v = torch.clamp(v, min=mins, max=maxs)
        return (v - mins) / (maxs - mins + 1e-6)
