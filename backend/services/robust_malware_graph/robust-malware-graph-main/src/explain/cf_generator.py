# robust-malware-graph / src / explain / cf_generator.py
# --------------------------------------------------------------------------- #
#  🔄  Counter-Factual Subgraph Generator
#
#  목표
#  ────
#  • 입력 CFG `g` 와 분류기 `model`, 원하는 「반대 결과」 `target_label`
#  • 최소한의 노드/엣지 수정(drop) 으로 예측을 `target_label` 로 뒤집는
#    counter-factual 그래프 `g*` + 수정 집합 ΔV, ΔE 산출
#
#  기본 알고리즘
#  ────────────
#    1. Gradient-based importance (∂logit/∂node_feat) 산출
#    2. Greedy-beam search (width = beam_size) 로
#         ┌─ 가장 중요 노드/엣지부터 제거하고
#         └─ 예측이 flip 되면 즉시 반환 / 아니면 계속
#    3. budget (max_del_nodes / edges) 초과 시 실패
#
#  사용 예
#  -------------------------------------------------------------------------
#  >>> cf = CounterFactualGenerator(model, g, device="cuda")
#  >>> result = cf.generate(target_label=0, beam_size=4, max_steps=15)
#  >>> result["success"], result["cf_graph"].y_pred, result["delta_nodes"]
#
#  의존
#  ────
#  • torch ≥2.0
#  • torch_geometric ≥2.x
#  • networkx (optional – 연결성 체크용)
# --------------------------------------------------------------------------- #
from __future__ import annotations

import heapq
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

import torch
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.utils import subgraph as pyg_subgraph

try:
    import networkx as nx
    from torch_geometric.utils import to_networkx
except ModuleNotFoundError:  # pragma: no cover
    nx = None  # type: ignore


# --------------------------------------------------------------------------- #
#                              Helper dataclass                               #
# --------------------------------------------------------------------------- #
@dataclass
class CFResult:
    success: bool
    cf_graph: Optional[Data]
    delta_nodes: List[int]
    delta_edges: List[Tuple[int, int]]
    steps: int
    original_pred: int
    new_pred: int


# --------------------------------------------------------------------------- #
#                         Counter-Factual main class                          #
# --------------------------------------------------------------------------- #
class CounterFactualGenerator:
    """
    Counter-factual graph generator by greedy beam-search.

    Parameters
    ----------
    model : nn.Module or callable
        Frozen binary classifier returning raw logit.
    graph : Data
        Original CFG (x, edge_index [, y]).
    device : str | torch.device
        Compute device for gradient & inference.
    keep_connected : bool, default True
        제거 후 서브그래프가 연결 그래프로 남도록 강제.
    """

    def __init__(
        self,
        model,
        graph: Data,
        *,
        device: str | torch.device = "cpu",
        keep_connected: bool = True,
    ) -> None:
        self.model = model.to(device)
        self.g = graph.clone().to(device)
        self.device = device
        self.keep_connected = keep_connected

        if keep_connected and nx is None:
            raise ImportError("networkx required for `keep_connected=True`")

        self._full_logit = self._forward(self.g).item()
        self._full_pred = int(self._full_logit > 0)

    # ------------------------------------------------------------------ #
    #                       public generation API                         #
    # ------------------------------------------------------------------ #
    def generate(
        self,
        *,
        target_label: int,
        beam_size: int = 3,
        max_steps: int = 20,
        max_del_nodes: int = 15,
        max_del_edges: int = 20,
    ) -> CFResult:
        """
        Produce counter-factual subgraph if possible.

        Returns
        -------
        CFResult
            success            – bool
            cf_graph           – torch_geometric.data.Data or None
            delta_nodes/edges  – removed idx list
            steps              – #beam iterations
        """
        assert target_label in {0, 1}, "binary classifier assumed"

        # quick exit
        if self._full_pred == target_label:
            return CFResult(
                success=True,
                cf_graph=self.g,
                delta_nodes=[],
                delta_edges=[],
                steps=0,
                original_pred=self._full_pred,
                new_pred=self._full_pred,
            )

        # ---------------- grad-based importance ranking ----------------
        node_imp = self._node_importance()
        edge_imp = self._edge_importance()

        node_rank = [n for n, _ in sorted(node_imp.items(), key=lambda t: -t[1])]
        edge_rank = [e for e, _ in sorted(edge_imp.items(), key=lambda t: -t[1])]

        # beam elements: (score, del_nodes, del_edges)
        Beam = Tuple[float, Tuple[int, ...], Tuple[int, ...]]
        frontier: List[Beam] = [(0.0, tuple(), tuple())]  # score=del_count

        visited = set()
        best_cf: Optional[CFResult] = None

        for step in range(1, max_steps + 1):
            new_frontier: List[Beam] = []

            # explore child states
            for _, del_nodes, del_edges in heapq.nsmallest(beam_size, frontier):
                # choose next candidate removals
                nxt_node = self._next_item(node_rank, del_nodes)
                nxt_edge = self._next_item(edge_rank, del_edges)

                # branch 1: remove node
                if nxt_node is not None and len(del_nodes) < max_del_nodes:
                    cand_nodes = tuple(sorted((*del_nodes, nxt_node)))
                    state = (cand_nodes, del_edges)
                    if state not in visited:
                        visited.add(state)
                        score = len(cand_nodes) + len(del_edges)
                        new_frontier.append((score, cand_nodes, del_edges))

                # branch 2: remove edge
                if nxt_edge is not None and len(del_edges) < max_del_edges:
                    cand_edges = tuple(sorted((*del_edges, nxt_edge)))
                    state = (del_nodes, cand_edges)
                    if state not in visited:
                        visited.add(state)
                        score = len(del_nodes) + len(cand_edges)
                        new_frontier.append((score, del_nodes, cand_edges))

            # evaluate frontier & check flip
            evaluated: List[Beam] = []
            for score, del_nodes, del_edges in new_frontier:
                sub_g = self._subgraph(del_nodes, del_edges)
                if sub_g is None:  # disconnected constraint
                    continue
                logit = self._forward(sub_g).item()
                pred = int(logit > 0)
                if pred == target_label:
                    best_cf = CFResult(
                        success=True,
                        cf_graph=sub_g.cpu(),
                        delta_nodes=list(del_nodes),
                        delta_edges=[self._id2edge(e) for e in del_edges],
                        steps=step,
                        original_pred=self._full_pred,
                        new_pred=pred,
                    )
                    break  # return immediate – minimal by beam order
                evaluated.append((score, del_nodes, del_edges))

            if best_cf:
                break
            # next loop
            frontier = evaluated

        if best_cf:
            return best_cf

        # failure result
        return CFResult(
            success=False,
            cf_graph=None,
            delta_nodes=[],
            delta_edges=[],
            steps=max_steps,
            original_pred=self._full_pred,
            new_pred=self._full_pred,
        )

    # ------------------------------------------------------------------ #
    #                           importance rank                          #
    # ------------------------------------------------------------------ #
    def _node_importance(self) -> Dict[int, float]:
        self.model.zero_grad()
        g = self.g
        g.x.requires_grad_(True)
        logit = self._forward(g)
        logit.backward(torch.ones_like(logit))
        grad = g.x.grad  # (N, feat)
        imp = grad.norm(dim=-1).detach().cpu()  # L2
        return {i: imp[i].item() for i in range(g.num_nodes)}

    def _edge_importance(self) -> Dict[int, float]:
        ei = self.g.edge_index
        # simple heuristic: sum importance of both incident nodes
        node_imp = self._node_importance()
        imp = {}
        for idx in range(ei.size(1)):
            u, v = ei[:, idx].tolist()
            imp[idx] = node_imp[u] + node_imp[v]
        return imp

    # ------------------------------------------------------------------ #
    #                            utils                                   #
    # ------------------------------------------------------------------ #
    @torch.no_grad()
    def _forward(self, g: Data) -> torch.Tensor:
        return self.model(g.x, g.edge_index).squeeze()

    def _next_item(self, ranked: List[int], deleted: Tuple[int, ...]) -> Optional[int]:
        for x in ranked:
            if x not in deleted:
                return x
        return None

    def _id2edge(self, edge_id: int) -> Tuple[int, int]:
        u, v = self.g.edge_index[:, edge_id].tolist()
        return (u, v)

    def _subgraph(
        self, del_nodes: Sequence[int], del_edges: Sequence[int]
    ) -> Optional[Data]:
        g = self.g
        # node mask
        keep_nodes = torch.ones(g.num_nodes, dtype=torch.bool, device=g.x.device)
        keep_nodes[list(del_nodes)] = False

        # edge mask
        keep_edges = torch.ones(g.edge_index.size(1), dtype=torch.bool, device=g.x.device)
        keep_edges[list(del_edges)] = False

        # apply masks
        kept_node_idx = keep_nodes.nonzero(as_tuple=False).view(-1)
        kept_edge_idx = keep_edges.nonzero(as_tuple=False).view(-1)

        edge_index = g.edge_index[:, kept_edge_idx]
        # filter out edges pointing to deleted nodes
        mask_valid = keep_nodes[edge_index[0]] & keep_nodes[edge_index[1]]
        edge_index = edge_index[:, mask_valid]

        if self.keep_connected and nx is not None:
            if kept_node_idx.numel() == 0:
                return None
            sub_nx = to_networkx(
                Data(x=g.x[kept_node_idx], edge_index=edge_index), to_undirected=True
            )
            if not nx.is_connected(sub_nx):
                return None

        sub_x = g.x[kept_node_idx]
        # relabel nodes
        mapping = {old.item(): new for new, old in enumerate(kept_node_idx)}
        edge_index = torch.tensor(
            [[mapping[u.item()] for u in edge_index[0]],
             [mapping[v.item()] for v in edge_index[1]]],
            dtype=torch.long,
            device=edge_index.device,
        )

        sub_g = Data(x=sub_x, edge_index=edge_index)
        # copy attrs
        for k in g.keys:
            if k in {"x", "edge_index"}:
                continue
            v = g[k]
            if torch.is_tensor(v) and v.size(0) == g.num_nodes:
                sub_g[k] = v[kept_node_idx]
            else:
                sub_g[k] = v
        return sub_g
