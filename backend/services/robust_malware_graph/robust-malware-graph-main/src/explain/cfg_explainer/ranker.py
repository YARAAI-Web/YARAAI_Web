# robust-malware-graph / src / explain / cfg_explainer / ranker.py
# --------------------------------------------------------------------------- #
#  🔢  Shapley-like Node Importance Ranker
#
#  Path-/node-level explanation 단계에서 선택(Selector)·집계(Aggregator)된
#  후보 노드 세트에 대해 **Shapley value**(marginal contribution) 기반
#  중요도를 추정해 최종 “Top-k 중요 노드/경로”를 리턴한다.
#
#  • 사용 예
#    ------------------------------------------------------------------
#    >>> from torch_geometric.utils import k_hop_subgraph
#    >>> ranker = ShapleyNodeRanker(
#    ...     graph      = cfg_subgraph,          # torch_geometric.data.Data
#    ...     score_fn   = lambda g: model(g.x, g.edge_index).sigmoid().item(),
#    ...     background = 0.10,                  # baseline prob for empty set
#    ... )
#    >>> top10 = ranker.rank(k=10, num_permutations=256)
#
#  • 핵심 아이디어
#      φ_i ≈ 1/M Σ_m [ f(S_m ∪ {i}) − f(S_m) ]
#      (S_m 은 무작위 순열 기준, i 이전에 등장한 노드 서브셋)
#
#    – M: num_permutations          (Monte-Carlo)
#    – f(·): `score_fn`             (모델 예측 score)
#    – background: 빈 그래프(or 마스킹) 점수
#
#  • 의존
#      torch ≥ 2.0, torch_geometric ≥ 2.x, tqdm(optional)
# --------------------------------------------------------------------------- #
from __future__ import annotations

import itertools
import random
from collections import defaultdict
from typing import Callable, Dict, Iterable, List, Sequence

import torch
from torch_geometric.data import Data
from torch_geometric.utils import subgraph

try:
    from tqdm.auto import tqdm  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    tqdm = lambda x, **kwargs: x  # type: ignore


# --------------------------------------------------------------------------- #
#                            Helper: node dropping                            #
# --------------------------------------------------------------------------- #
def default_drop_fn(g: Data, drop_nodes: Sequence[int]) -> Data:
    """
    Subgraph excluding `drop_nodes`.
    텐서 복사 비용 최소화를 위해 edge-mask 방식 대신 PyG `subgraph`.
    """
    keep_nodes = torch.ones(g.num_nodes, dtype=torch.bool)
    keep_nodes[torch.as_tensor(drop_nodes, dtype=torch.long)] = False
    edge_index, _ = subgraph(keep_nodes.nonzero(as_tuple=False).view(-1), g.edge_index, relabel_nodes=True)
    # 노드 feature 재인덱싱
    new_x = g.x[keep_nodes]
    new_data = Data(x=new_x, edge_index=edge_index)

    #  추가 field 복사(주소, 타입 등) → 필요한 경우만
    for key in g.keys:
        if key in {"x", "edge_index"}:
            continue
        attr = g[key]
        if torch.is_tensor(attr) and attr.size(0) == g.num_nodes:
            new_data[key] = attr[keep_nodes]
        else:
            new_data[key] = attr
    return new_data


# --------------------------------------------------------------------------- #
#                                Main Ranker                                  #
# --------------------------------------------------------------------------- #
class ShapleyNodeRanker:
    """
    Monte-Carlo Shapley value estimator for node-level importance.

    Parameters
    ----------
    graph : torch_geometric.data.Data
        대상 그래프 (CFG under explain).
    score_fn : Callable[[Data], float]
        그래프 → 스칼라(score) 함수. e.g., `model(g).sigmoid()[0].item()`.
    drop_fn : Callable[[Data, Sequence[int]], Data], optional
        노드 제거 전략. 기본 == `default_drop_fn`.
    background : float, default 0.0
        빈 집합 S=∅ 에 대한 점수(f(∅)). 모델이 bias만 존재할 때 ≈ 0.5.
    seed : int | None
        RNG 고정용.
    """

    def __init__(
        self,
        graph: Data,
        score_fn: Callable[[Data], float],
        *,
        drop_fn: Callable[[Data, Sequence[int]], Data] | None = None,
        background: float = 0.0,
        seed: int | None = None,
        edge_types: torch.Tensor | None = None,
    ) -> None:
        self.g = graph
        self.score_fn = score_fn
        self.drop_fn = drop_fn or default_drop_fn
        self.background = background
        if seed is not None:
            random.seed(seed)

        # cache: f(G) (full graph) ← 불변이므로 한 번만
        self.full_score = score_fn(graph)
        self.edge_types = edge_types if edge_types is not None else graph.get("edge_type", None)

    # --------------------------------------------------------------------- #
    #                           Shapley estimation                           #
    # --------------------------------------------------------------------- #
    def _marginal_contribution(
        self,
        node: int,
        preceding_set: Sequence[int],
        cache: Dict[frozenset[int], float],
    ) -> float:
        """
        f(S ∪ {i}) − f(S) with memoisation.
        """
        S = frozenset(preceding_set)
        S_plus = frozenset((*preceding_set, node))

        if S not in cache:
            cache[S] = self._score_with_nodes(list(S))
        if S_plus not in cache:
            cache[S_plus] = self._score_with_nodes(list(S_plus))

        return cache[S_plus] - cache[S]

    def _score_with_nodes(self, nodes: Sequence[int]) -> float:
        """
        점수 f(G[nodes]) – *남길* 노드 집합을 받는다.
        빈 집합 → background score.
        """
        if len(nodes) == 0:
            return self.background
        drop = list(set(range(self.g.num_nodes)) - set(nodes))
        sub_g = self.drop_fn(self.g, drop)
        return self.score_fn(sub_g)

    # --------------------------------------------------------------------- #
    #                               Public API                               #
    # --------------------------------------------------------------------- #
    def shapley_values(
        self,
        candidates: Sequence[int] | None = None,
        *,
        num_permutations: int = 256,
        progress: bool = True,
        edge_mask: torch.Tensor | None = None,
        edge_types: torch.Tensor | None = None,
        sparsity_beta: float = 0.0,
    ) -> Dict[int, float]:
        """
        Shapley value φ_i for each node in `candidates` (or all nodes).

        Returns
        -------
        dict : { node_idx: φ_i }
        """
        cand = list(candidates) if candidates is not None else list(range(self.g.num_nodes))
        n = len(cand)
        φ = defaultdict(float)
        cache: Dict[frozenset[int], float] = {}

        iterator: Iterable[int] = tqdm(range(num_permutations), disable=not progress, desc="Permutations")

        for _ in iterator:
            ordering = cand.copy()
            random.shuffle(ordering)

            # running prefix set
            prefix: list[int] = []
            for node in ordering:
                mc = self._marginal_contribution(node, prefix, cache)
                φ[node] += mc
                prefix.append(node)

        # 평균
        for node in φ:
            φ[node] /= num_permutations

        if edge_mask is not None:
            et = edge_types if edge_types is not None else self.edge_types
            if et is not None:
                uniq = torch.unique(et)
                reg = 0.0
                for t in uniq:
                    reg += edge_mask[et == t].float().mean().item()
                reg /= len(uniq) if len(uniq) > 0 else 1
            else:
                reg = edge_mask.float().mean().item()
            for node in φ:
                φ[node] -= sparsity_beta * reg

        return dict(φ)

    def rank(
        self,
        *,
        k: int | None = None,
        num_permutations: int = 256,
        candidates: Sequence[int] | None = None,
        progress: bool = True,
        edge_mask: torch.Tensor | None = None,
        edge_types: torch.Tensor | None = None,
        sparsity_beta: float = 0.0,
    ) -> List[tuple[int, float]]:
        """
        Top-k 랭킹 반환.

        Returns
        -------
        list[ (node_idx, score) ] – 내림차순.
        """
        φ = self.shapley_values(
            candidates,
            num_permutations=num_permutations,
            progress=progress,
            edge_mask=edge_mask,
            edge_types=edge_types,
            sparsity_beta=sparsity_beta,
        )
        ranked = sorted(φ.items(), key=lambda x: x[1], reverse=True)
        return ranked if k is None else ranked[:k]


# --------------------------------------------------------------------------- #
#                         Convenience: quick utility                          #
# --------------------------------------------------------------------------- #
def quick_rank(
    graph: Data,
    score_fn: Callable[[Data], float],
    *,
    selector_mask: Sequence[int] | None = None,
    k: int = 20,
    num_permutations: int = 256,
    edge_mask: torch.Tensor | None = None,
    edge_types: torch.Tensor | None = None,
    sparsity_beta: float = 0.0,
) -> List[tuple[int, float]]:
    """
    One-liner helper often used in notebooks / pipelines.

    Parameters
    ----------
    selector_mask : Sequence[int] | None
        Prior stage(Selector) 가 반환한 “관심 노드 인덱스”. None ⇒ 전체 노드.
    """
    ranker = ShapleyNodeRanker(graph, score_fn)
    return ranker.rank(
        k=k,
        num_permutations=num_permutations,
        candidates=selector_mask,
        edge_mask=edge_mask,
        edge_types=edge_types,
        sparsity_beta=sparsity_beta,
    )
