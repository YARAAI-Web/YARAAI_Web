"""
src.graphs.features.call_graph_feat
===================================

CallGraphStatExtractor
----------------------
입력  : PyG `Data` 또는 `HeteroData` 형태의 Function-Call-Graph
출력  : 1-D torch.Tensor(float32) – 총 10차원 기본 통계

feature vector 구성
~~~~~~~~~~~~~~~~~~~
idx | 설명                                   | 범위·예시
----|----------------------------------------|-----------------------
 0  | #functions (노드 수)                   | 1 – 100k
 1  | #calls (edge 수)                       | 0 – 1M
 2  | avg_out_deg                            | 0 – 200
 3  | max_out_deg                            | 0 – 5k
 4  | avg_in_deg                             | 0 – 200
 5  | max_in_deg                             | 0 – 5k
 6  | %external_funcs                        | 0.0 – 1.0
 7  | SCC_ratio (|SCC|>1 노드 / 전체 함수)   | 0.0 – 1.0
 8  | call_density = E / N²                  | 0.0 – 1.0
 9  | lib_call_ratio (lib edges / E)         | 0.0 – 1.0

필요 패키지
~~~~~~~~~~
pip install networkx torch torch_geometric
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Sequence

import networkx as nx
import torch
from torch_geometric.data import Data, HeteroData

from ..utils import get_logger
from .cache import FeatureCache

_LOG = get_logger("features.call_graph")
_CACHE = FeatureCache(Path("~/.cache/call_graph_feat"))


# ──────────────────────────────────────────────────────────────────────
# 메인 클래스
# ──────────────────────────────────────────────────────────────────────
class CallGraphStatExtractor:
    """
    Parameters
    ----------
    cache : bool, default True
        SHA-256 그래프 구조 해시 기반 Feather 캐시 사용.
    """

    def __init__(self, *, cache: bool = True):
        self.cache = cache
        self.log = _LOG

    # ===============================================================
    # public
    # ===============================================================
    def featurize(
        self,
        g: Data | HeteroData,
        *,
        key: Optional[str] = None,
    ) -> torch.Tensor:
        """
        FCG → 10-dim 통계 벡터(float32).  (N=노드, E=엣지)

        Parameters
        ----------
        g   : PyG Data | HeteroData
        key : str | None
            캐시 키(예: 샘플 SHA-256). None ⇒ 캐시 비활성.
        """
        if self.cache and key is not None:
            try:
                return _CACHE.load(key).squeeze(0)
            except FileNotFoundError:
                pass

        vec = self._compute_stats(g)

        if self.cache and key is not None:
            _CACHE.save(key, vec.unsqueeze(0))

        return vec

    # ===============================================================
    # 내부
    # ===============================================================
    def _compute_stats(self, g: Data | HeteroData) -> torch.Tensor:
        # 1) PyG → networkx DiGraph
        if isinstance(g, HeteroData):
            # relation 키 ('function','calls','function') 라고 가정
            rel_key = next((k for k in g.edge_types if k[1] == "calls"), None)
            if rel_key is None:
                raise ValueError("HeteroData에 'calls' relation이 없음")
            edge_index = g[rel_key].edge_index
            num_nodes = g[rel_key].num_nodes
            ext_flag = getattr(g["function"], "is_external", None)
            raw_kind = getattr(g[rel_key], "raw_call_kind", None)
        else:
            edge_index = g.edge_index
            num_nodes = g.num_nodes
            ext_flag = getattr(g, "is_external", None)
            raw_kind = getattr(g, "raw_call_kind", None)

        # networkx 그래프 구축
        G = nx.DiGraph()
        G.add_nodes_from(range(num_nodes))
        G.add_edges_from(edge_index.t().tolist())

        N = num_nodes
        E = G.number_of_edges()
        out_deg = [d for _, d in G.out_degree()]
        in_deg = [d for _, d in G.in_degree()]

        # 2) 통계 계산
        ext_ratio = (ext_flag.sum().item() / N) if (ext_flag is not None and N) else 0.0

        scc = [c for c in nx.strongly_connected_components(G) if len(c) > 1]
        scc_ratio = sum(len(c) for c in scc) / N if N else 0.0

        # lib_call_ratio : raw_call_kind == 2 (‘lib’) 비율
        if raw_kind is not None and E:
            lib_ratio = (raw_kind == 2).sum().item() / E
        else:
            lib_ratio = 0.0

        vec = torch.tensor(
            [
                float(N),
                float(E),
                float(sum(out_deg) / N if N else 0),
                float(max(out_deg) if out_deg else 0),
                float(sum(in_deg) / N if N else 0),
                float(max(in_deg) if in_deg else 0),
                ext_ratio,
                scc_ratio,
                float(E) / (N * N) if N else 0.0,
                lib_ratio,
            ],
            dtype=torch.float32,
        )
        return vec


# ──────────────────────────────────────────────────────────────────────
# 빠른 테스트
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":  # pragma: no cover
    from graphs.loaders import get_loader

    loader = get_loader("fcg")
    sample = loader.load("sample.fcg.json.gz")
    feat = CallGraphStatExtractor().featurize(sample)
    print("feature vector:", feat)
