"""Unified registry and single entry point for graph utilities.

src.graphs
==========

보물 프로젝트의 **그래프 전처리·저장·증강·학습 파이프라인**을 한데 모은
통합 패키지입니다. 하위 모듈의 가장 자주 쓰이는 심벌을 재-export 하여
간결한 임포트 체계를 제공합니다.

빠른 예시
~~~~~~~~
>>> from graphs import (
...     get_loader, get_normalizer, HeteroGraphBuilder,
...     GraphDataset, GraphAugmentTransform,
... )
>>> ast_raw  = get_loader('ast').load('foo.ast.json.gz')
>>> ast_norm = get_normalizer('ast').normalize(ast_raw)
>>> builder  = HeteroGraphBuilder(); builder.add_view(ast_norm, 'ast')
>>> g_hetero = builder.build()
"""
from __future__ import annotations

from typing import List

# ────────────────────────────────────────────────────────────────
# Sub-package 핵심 심벌 re-export
# ────────────────────────────────────────────────────────────────
# loaders
try:  # optional dependency on torch_geometric/torch
    import torch
    if getattr(torch, "Tensor", None) is None:
        raise ImportError("invalid torch stub")
    from .loaders import get_loader, available as loaders_available
    from .dataset import GraphDataset, split_by_time, split_random
    from .normalizers import get_normalizer, available as norms_available
except Exception:  # pragma: no cover - optional heavy deps
    def get_loader(*_args, **_kw):  # type: ignore
        raise ImportError("torch_geometric is required")

    loaders_available = lambda: []  # type: ignore

    class GraphDataset:  # type: ignore
        pass

    def split_by_time(*_args, **_kw):  # type: ignore
        raise ImportError("torch_geometric is required")

    def split_random(*_args, **_kw):  # type: ignore
        raise ImportError("torch_geometric is required")

    def get_normalizer(*_a, **_kw):  # type: ignore
        raise ImportError("torch_geometric is required")

    norms_available = lambda: []  # type: ignore

# builders
from .builders import (
    HeteroGraphBuilder,
    ViewMerger,
    relabel,
    sample_k_hop,
    sample_random_walk,
    sample_edge_drop,
    sainth_loader,
    sainth_loader_hetero,
    cluster_loader,
)

# features (optional dependencies)
try:  # pragma: no cover - optional heavy deps
    from .features import (
        TokenEmbedder,
        OpcodeEmbedder,
        PEHeaderFeatureExtractor,
        CallGraphStatExtractor,
        available as feats_available,
    )
except Exception:  # noqa: BLE001 - broad for optional import
    feats_available = lambda: []  # type: ignore

# dataset (placeholder when optional deps missing handled above)

# transforms (optional augment dependency)
try:  # pragma: no cover - optional heavy deps
    from .transforms import (
        GraphAugmentTransform,
        GraphPruner,
        AttributeScaler,
        available as transforms_available,
    )
except Exception:  # noqa: BLE001 - broad for optional import
    transforms_available = lambda: []  # type: ignore

# ────────────────────────────────────────────────────────────────
# 편의 함수: 전체 가용 심벌 카탈로그
# ────────────────────────────────────────────────────────────────
def catalog() -> dict[str, List[str]]:
    """서브패키지별 ‘available()’ 목록을 딕셔너리로 반환."""
    return {
        "loaders": loaders_available(),
        "normalizers": norms_available(),
        "features": feats_available(),
        "transforms": transforms_available(),
    }

# ────────────────────────────────────────────────────────────────
# __all__ 지정 – 와일드카드 import 최소 공개 범위
# ────────────────────────────────────────────────────────────────
__all__: List[str] = [
    # loaders / normalizers
    "get_loader",
    "get_normalizer",
    # builders
    "HeteroGraphBuilder",
    "ViewMerger",
    "relabel",
    "sample_k_hop",
    "sample_random_walk",
    "sample_edge_drop",
    "sainth_loader",
    "sainth_loader_hetero",
    "cluster_loader",
    # dataset
    "GraphDataset",
    "split_by_time",
    "split_random",
    # util
    "catalog",
]

if "TokenEmbedder" in globals():
    __all__.extend([
        "TokenEmbedder",
        "OpcodeEmbedder",
        "PEHeaderFeatureExtractor",
        "CallGraphStatExtractor",
    ])

if "GraphAugmentTransform" in globals():
    __all__.extend([
        "GraphAugmentTransform",
        "GraphPruner",
        "AttributeScaler",
    ])

# 선택: 패키지 버전 문자열 (pyproject.toml에 정의돼 있을 때 자동)
try:
    from importlib.metadata import version as _ver

    __version__ = _ver("robust-malware-graph")
except Exception:  # pragma: no cover
    __version__ = "0.0.0"
