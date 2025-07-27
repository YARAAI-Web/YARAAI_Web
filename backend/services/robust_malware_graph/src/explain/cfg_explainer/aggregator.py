# robust-malware-graph / src / explain / cfg_explainer / aggregator.py
# --------------------------------------------------------------------------- #
#  🔗  Path / Component Aggregator
#
#  Selector 단계에서 얻은 “살아남은” 노드 집합(selected_nodes)을
#  • (1) **연결 컴포넌트**(weakly) 단위로 묶고,
#  • (2) 각 컴포넌트를 **선형(path) 시퀀스**로 정렬
#        ─ Topological sort (DAG) → fallback: BFS 레벨/addr 오름차순.
#
#  반환값은:
#      List[ dict ]  # ↳ {
#                       "nodes"    : List[int],          # ordered (global)
#                       "edges"    : Tensor[2, E],      # local indices
#                       "edge_ids" : Tensor[E],         # global edge ids
#                       "node_map" : List[Tuple[str,int]],
#                       "edge_map" : List[Tuple],
#                       "feat"     : Tensor | None,     # path feature
#                       "subgraph" : torch_geometric.data.Data }
#
#  Down-stream (Ranker / Report) 에서 경로별 중요도 합산, 코드 하이라이트 등에 사용.
#
#  • 의존
#      torch ≥ 2.0, torch_geometric ≥ 2.x, networkx ≥ 3.0
# --------------------------------------------------------------------------- #
from __future__ import annotations

from typing import Dict, List, Sequence, Tuple, Iterable, Optional

import networkx as nx
import torch
from torch_geometric.data import Data, HeteroData
from torch_geometric.utils import to_networkx


# --------------------------------------------------------------------------- #
#                               Helper utils                                  #
# --------------------------------------------------------------------------- #
def iter_edge_types(g: Data | HeteroData, rel: str) -> Iterable[Tuple[Tuple[str, str, str] | None, Data]]:
    """Yield edge stores whose relation matches ``rel``.

    For ``HeteroData`` this filters all ``edge_types`` where the relation part
    equals ``rel`` or, when ``rel`` is ``"cfg"``, includes the common CFG
    variants (``jump``, ``conditional``, ``fallthrough``).

    ``Data`` instances yield a single ``(None, g)`` pair.
    """

    if isinstance(g, Data):
        if rel == "cfg":
            yield None, g
        return

    cfg_alias = {"cfg", "jump", "conditional", "fallthrough"}
    for etype in g.edge_types:
        if rel == etype[1] or (rel == "cfg" and etype[1] in cfg_alias):
            yield etype, g[etype]


# --------------------------------------------------------------------------- #
#                               Core Aggregator                               #
# --------------------------------------------------------------------------- #
class CFGPathAggregator:
    """
    연결 컴포넌트 + 루트→리프 경로 정렬 헬퍼.

    Parameters
    ----------
    graph : torch_geometric.data.Data | torch_geometric.data.HeteroData
        전체 CFG 그래프. HeteroData일 경우 ``cfg`` 연관 모든 edge store를
        합쳐 하나의 DiGraph로 변환한다.
    undirected : bool, default False
        컴포넌트 탐색 시 방향 무시 여부 (weakly vs. strongly).
    min_path_len : int, default 1
        정렬된 path 의 최소 길이(<min)면 단일 노드 path 로 유지.
    """

    def __init__(
        self,
        graph: Data | HeteroData,
        *,
        undirected: bool = False,
        min_path_len: int = 1,
        edge_emb: Optional[torch.nn.Embedding] = None,
    ) -> None:
        self.orig_graph = graph
        self.undirected = undirected
        self.min_len = min_path_len
        self.edge_emb = edge_emb

        # --------------------------------------------------------------
        # Flatten possibly multiple CFG edge stores into a single Data
        # --------------------------------------------------------------
        if isinstance(graph, HeteroData):
            node_offsets: Dict[str, int] = {}
            global2local: Dict[int, Tuple[str, int]] = {}
            cursor = 0
            for ntype in graph.node_types:
                node_offsets[ntype] = cursor
                for i in range(graph[ntype].num_nodes):
                    global2local[cursor + i] = (ntype, i)
                cursor += graph[ntype].num_nodes

            edges: List[torch.Tensor] = []
            edge_types: List[torch.Tensor] = []
            edge_map: List[Tuple[Tuple[str, str, str], int]] = []
            for etype, store in iter_edge_types(graph, "cfg"):
                src_off = node_offsets[etype[0]]
                dst_off = node_offsets[etype[2]]
                ei = store.edge_index
                edges.append(torch.stack([ei[0] + src_off, ei[1] + dst_off]))
                if "edge_type" in store:
                    edge_types.append(store.edge_type.clone())
                else:
                    from src.graphs.normalizers.schema import EDGE_REL_ID

                    edge_types.append(
                        torch.full((ei.size(1),), EDGE_REL_ID.get(etype[1], 0), dtype=torch.long)
                    )
                edge_map.extend([(etype, int(i)) for i in range(ei.size(1))])

            edge_index = torch.cat(edges, dim=1) if edges else torch.empty((2, 0), dtype=torch.long)
            edge_type = torch.cat(edge_types) if edge_types else torch.empty((0,), dtype=torch.long)

            # concatenate node features (feat or x)
            feats: List[torch.Tensor] = []
            addrs: List[torch.Tensor] = []
            for ntype in graph.node_types:
                store = graph[ntype]
                if "x" in store:
                    feats.append(store.x)
                elif "feat" in store:
                    feats.append(store.feat)
                else:
                    feats.append(torch.zeros((store.num_nodes, 1), dtype=torch.float))
                if "addr" in store:
                    addrs.append(torch.as_tensor(store.addr))

            x = torch.cat(feats, dim=0) if feats else torch.empty((cursor, 0))
            if addrs:
                addr = torch.cat(addrs, dim=0)
            else:
                addr = None

            data = Data(x=x, edge_index=edge_index, edge_type=edge_type, num_nodes=cursor)
            if addr is not None:
                data.addr = addr
            self.g = data
            self._node_map = global2local
            self._edge_map = edge_map
        else:
            self.g = graph
            self._node_map = {i: ("node", i) for i in range(graph.num_nodes)}
            self._edge_map = [("cfg", int(i)) for i in range(graph.edge_index.size(1))]

        self._addr = self.g.get("addr", None)

        self._nx_digraph = to_networkx(
            Data(edge_index=self.g.edge_index, num_nodes=self.g.num_nodes),
            to_undirected=False,
            node_attrs=[],
        )

    # ------------------------------------------------------------------ #
    #                           Public  API                               #
    # ------------------------------------------------------------------ #
    def aggregate(
        self,
        selected_nodes: Sequence[int],
    ) -> List[Dict]:
        """
        Aggregate -> ordered path list.

        Returns
        -------
        list[dict]
            Each dict::
                { "nodes": [int …],           # ordered
                  "edges": Tensor[2,E],       # local index (0…len-1)
                  "subgraph": Data }          # induced sub-DAG
        """
        sel = set(int(i) for i in selected_nodes)
        if len(sel) == 0:
            return []

        # -------- 1) Connected components (weakly/strongly) --------------
        if self.undirected:
            comps = nx.connected_components(self._nx_digraph.to_undirected())
        else:
            comps = nx.weakly_connected_components(self._nx_digraph)

        comps = [sorted(c & sel) for c in comps if len(c & sel) > 0]

        # -------- 2) Order each component into one (or many) paths -------
        paths_out: List[Dict] = []
        for comp_nodes in comps:
            sub_nx = self._nx_digraph.subgraph(comp_nodes).copy()
            ordered = self._linearize(sub_nx)

            # split if multiple roots emerge (ordered contains list[list])
            for seq in ordered:
                if len(seq) < self.min_len:
                    # keep singleton
                    seq = seq[:1]

                # build PyG subgraph (relabel for contiguous indices)
                node_idx = torch.tensor(seq, dtype=torch.long)
                from torch_geometric.utils import subgraph as pyg_subgraph

                edge_index, edge_mask = pyg_subgraph(
                    node_idx, self.g.edge_index, relabel_nodes=True, return_edge_mask=True
                )
                sub_x = self.g.x[node_idx]
                sub_data = Data(x=sub_x, edge_index=edge_index)
                # copy per-node attrs
                for k in self.g.keys:
                    if k in {"x", "edge_index"}:
                        continue
                    v = self.g[k]
                    if torch.is_tensor(v) and v.size(0) == self.g.num_nodes:
                        sub_data[k] = v[node_idx]
                    else:
                        sub_data[k] = v

                global_eids = edge_mask.nonzero(as_tuple=False).view(-1)
                node_map = [self._node_map[n] for n in seq]
                edge_map = [self._edge_map[int(i)] for i in global_eids]

                path_feat = None
                if self.edge_emb is not None and len(global_eids) > 0:
                    et = self.g.edge_type[global_eids]
                    path_feat = self.edge_emb(et).mean(dim=0)

                paths_out.append(
                    {
                        "nodes": seq,
                        "edges": edge_index,
                        "subgraph": sub_data,
                        "edge_ids": global_eids,
                        "node_map": node_map,
                        "edge_map": edge_map,
                        "feat": path_feat,
                    }
                )

        return paths_out

    # ------------------------------------------------------------------ #
    #                       Internal helpers                              #
    # ------------------------------------------------------------------ #
    def _linearize(self, sub_nx: nx.DiGraph) -> List[List[int]]:
        """
        Try to turn subgraph into one or more linear sequences.

        • DAG → topological_sort()
        • Cycles → fallback BFS + addr ascending
        """
        if nx.is_directed_acyclic_graph(sub_nx):
            topo = list(nx.topological_sort(sub_nx))
            return [topo]

        # cycle exists ⇒ pick arbitrary root(s) by minimal out-degree
        roots = [n for n, deg in sub_nx.in_degree() if deg == 0]
        if not roots:
            roots = [min(sub_nx.nodes)]

        # BFS per root, avoid duplicates
        seen = set()
        sequences: List[List[int]] = []
        for r in roots:
            seq = []
            for u in nx.bfs_tree(sub_nx, r):
                if u not in seen:
                    seq.append(u)
                    seen.add(u)
            if seq:
                # tie-break with addr(start) / node id
                seq.sort(key=lambda n: (
                    self._addr[n][0].item() if self._addr is not None else 0,
                    n,
                ))
                sequences.append(seq)

        # leftover nodes (due to cycles) → append
        remain = [n for n in sub_nx.nodes if n not in seen]
        if remain:
            remain.sort()
            sequences.append(remain)

        return sequences


# --------------------------------------------------------------------------- #
#                               Quick helper                                  #
# --------------------------------------------------------------------------- #
def aggregate_paths(
    graph: Data | HeteroData,
    selected_nodes: Sequence[int],
    *,
    undirected: bool = False,
    min_path_len: int = 1,
    ) -> List[Dict]:
    """
    Convenience wrapper :: one-shot aggregation.
    """
    agg = CFGPathAggregator(graph, undirected=undirected, min_path_len=min_path_len)
    return agg.aggregate(selected_nodes)
