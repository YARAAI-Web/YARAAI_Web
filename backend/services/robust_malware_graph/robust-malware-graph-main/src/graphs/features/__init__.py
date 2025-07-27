"""
src.graphs.features
===================

공개 API
--------
from graphs.features import (
    TokenEmbedder,
    OpcodeEmbedder,
    PEHeaderFeatureExtractor,
    CallGraphStatExtractor,
    available,            # → ['token', 'opcode', 'pe_header', 'call_graph']
)

• TokenEmbedder            : BPE + Word2Vec 기반 토큰 임베딩
• OpcodeEmbedder           : Opcode2Vec or nn.Embedding
• PEHeaderFeatureExtractor : PE 헤더 → 수치 벡터
• CallGraphStatExtractor   : FCG 통계(feature hashing)

추가 feature 모듈을 작성했다면
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. 해당 모듈을 `src/graphs/features/` 하위에 둔 뒤
2. 여기의 `_FEATURES` 딕셔너리에 키/클래스를 추가하거나
   `available()`/`get()` 로직을 수정하면 됩니다.
"""

from __future__ import annotations

from typing import Dict, List, TYPE_CHECKING, Type

from .token_embedder import TokenEmbedder
from .opcode_embedder import OpcodeEmbedder
from .pe_header_feat import PEHeaderFeatureExtractor
from .call_graph_feat import CallGraphStatExtractor

# --------------------------------------------------------------------------- #
# 내부 매핑  (간단 레지스트리)
# --------------------------------------------------------------------------- #
_FEATURES: Dict[str, Type] = {
    "token": TokenEmbedder,
    "opcode": OpcodeEmbedder,
    "pe_header": PEHeaderFeatureExtractor,
    "call_graph": CallGraphStatExtractor,
}

# --------------------------------------------------------------------------- #
# 편의 헬퍼
# --------------------------------------------------------------------------- #
def available() -> List[str]:
    """사용 가능한 feature 모듈 키 리스트를 알파벳순으로 반환합니다."""
    return sorted(_FEATURES.keys())


def get(name: str, **kwargs):
    """
    문자열 키 하나로 피처 추출/임베딩 클래스 인스턴스를 생성합니다.

    Examples
    --------
    >>> embedder = get("token", bpe_model=Path("bpe.model"))
    >>> vecs = embedder.embed("char *str;")
    """
    try:
        cls = _FEATURES[name]
    except KeyError as e:
        raise ValueError(f"Unknown feature module '{name}'. "
                         f"Use one of: {', '.join(available())}") from e
    return cls(**kwargs)  # type: ignore[return-value]

# --------------------------------------------------------------------------- #
# re-export  &  __all__
# --------------------------------------------------------------------------- #
__all__ = [
    "TokenEmbedder",
    "OpcodeEmbedder",
    "PEHeaderFeatureExtractor",
    "CallGraphStatExtractor",
    "available",
    "get",
]

# --------------------------------------------------------------------------- #
# IDE / 타입체커용 힌트 (런타임엔 실행되지 않음)
# --------------------------------------------------------------------------- #
if TYPE_CHECKING:  # pragma: no cover
    from . import cache  # noqa: F401
