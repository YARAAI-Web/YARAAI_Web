"""
src.graphs.builders
===================

공개 API
--------
from graphs.builders import (
    HeteroGraphBuilder,   # 뷰 간 cross-edge까지 스티칭
    ViewMerger,           # 뷰 합집합 + 오프셋만
    relabel,              # 0-base 재매핑 & 고아 노드 제거
    sample_k_hop,         # k-hop 이웃 서브그래프
    sample_random_walk,   # random-walk 병합 서브그래프
    sample_edge_drop,     # 엣지-드롭 증강
    sainth_loader,        # GraphSAINT Node/Edge Loader
    sainth_loader_hetero,
    cluster_loader,       # ClusterGCN Loader
)

모듈 구성
---------
hetero_builder.py · view_merger.py · relabeler.py · graph_sampler.py

필요 시 새 빌더/샘플러를 추가하고, 아래 `__all__` 목록만 확장하세요.
"""

from __future__ import annotations

from typing import List

# 핵심 빌더
try:  # optional torch_geometric dependency
    from .hetero_builder import HeteroGraphBuilder, OverLengthPolicy
    from .view_merger import ViewMerger

    from .relabeler import relabel
    from .graph_sampler import (
        sample_k_hop,
        sample_random_walk,
        sample_edge_drop,
        sainth_loader,
        sainth_loader_hetero,
        cluster_loader,
        cluster_loader_hetero,
    )
except Exception:  # pragma: no cover - missing heavy deps
    HeteroGraphBuilder = ViewMerger = None  # type: ignore
    OverLengthPolicy = None  # type: ignore
    def relabel(*_a, **_k):  # type: ignore
        raise ImportError("torch_geometric is required")

    def sample_k_hop(*_a, **_k):  # type: ignore
        raise ImportError("torch_geometric is required")

    def sample_random_walk(*_a, **_k):  # type: ignore
        raise ImportError("torch_geometric is required")

    def sample_edge_drop(*_a, **_k):  # type: ignore
        raise ImportError("torch_geometric is required")

    def sainth_loader(*_a, **_k):  # type: ignore
        raise ImportError("torch_geometric is required")

    def sainth_loader_hetero(*_a, **_k):  # type: ignore
        raise ImportError("torch_geometric is required")

    def cluster_loader(*_a, **_k):  # type: ignore
        raise ImportError("torch_geometric is required")

    def cluster_loader_hetero(*_a, **_k):  # type: ignore
        raise ImportError("torch_geometric is required")

__all__: List[str] = [
    # builders
    "HeteroGraphBuilder",
    "ViewMerger",
    # relabel
    "relabel",
    # samplers / loaders
    "sample_k_hop",
    "sample_random_walk",
    "sample_edge_drop",
    "sainth_loader",
    "sainth_loader_hetero",
    "cluster_loader",
    "cluster_loader_hetero",
    "OverLengthPolicy",
]
