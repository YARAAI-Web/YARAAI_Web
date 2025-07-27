# robust-malware-graph / src / explain / cfg_explainer / __init__.py
# --------------------------------------------------------------------------- #
#  🧩  Public API for CFGExplainer sub-package
#
#  • Re-exports key building blocks
#      – CFGASTMapper        : CFG ↔ AST 토큰 매퍼
#      – GumbelMaskSelector  : 노드 마스크 학습기
#      – CFGPathAggregator   : 선택 노드 → 경로/컴포넌트 단위 집계
#      – ShapleyNodeRanker   : 중요도(Shapley) 추정 & 랭킹
#
#  • Convenience helpers
#      – train_selector(...) : 짧은 코드로 Selector 학습
#      – explain_cfg(...)    : 〈Selector → Aggregator → Ranker → Mapper〉
#                              풀 파이프라인 한 번에 실행
#
#  사용 예
#  --------------------------------------------------------------------------
#  >>> from robust_malware_graph.explain.cfg_explainer import explain_cfg
#  >>> result = explain_cfg(cfg_g, ast_g, model,
#  ...                      selector_kwargs=dict(epochs=1500, lr=3e-3),
#  ...                      ranker_kwargs=dict(num_permutations=512),
#  ...                      top_k=30)
#  >>> result["tokens"]           # AST 토큰 인덱스 (Top-k 노드 매핑)
#  >>> result["paths"][0]["subgraph"].edge_index
# --------------------------------------------------------------------------- #
from __future__ import annotations

from typing import Dict, List, Sequence

from torch_geometric.loader import DataLoader

import torch
import torch.nn as nn
from torch_geometric.data import Data, HeteroData
from pathlib import Path

from .aggregator import CFGPathAggregator, aggregate_paths, iter_edge_types
from .mapper import CFGASTMapper
from .ranker import ShapleyNodeRanker, quick_rank
from .selector import GumbelMaskSelector
from ..utils import ensure_edgeaware_selector

__all__ = [
    # core classes
    "CFGASTMapper",
    "GumbelMaskSelector",
    "CFGPathAggregator",
    "ShapleyNodeRanker",
    # helpers
    "aggregate_paths",
    "quick_rank",
    "train_selector",
    "explain_cfg",
]

__version__: str = "0.1.0"


# --------------------------------------------------------------------------- #
#                       High-level convenience wrappers                       #
# --------------------------------------------------------------------------- #
def train_selector(
    cfg_graph: Data | Sequence[Data] | Sequence[HeteroData],
    model,
    *,
    view: str = "cfg",
    device: str | torch.device = "cpu",
    epochs: int = 1_000,
    lr: float = 2e-3,
    alpha: float = 1.0,
    beta: float = 2e-2,
    plot_path: Path | str | None = None,
    score_fn=None,
    amp: bool = False,
    selector: GumbelMaskSelector | None = None,
    batch: bool = False,
    batch_size: int = 1,
    **selector_kwargs,
) -> GumbelMaskSelector:
    """
    One-shot training helper that returns a fitted `GumbelMaskSelector`.

    Parameters
    ----------
    cfg_graph : Data | Sequence[Data]
        Single CFG graph or sequence of graphs.
    model : nn.Module or callable
        Frozen classifier that returns a single logit/score.
    view : str
        Edge relation view to train on (e.g., "cfg", "ast").
    device : str or torch.device
        Compute device for selector parameters.
    epochs, lr, alpha, beta
        Hyper-parameters forwarded to `selector.train_loop`.
    plot_path : Path | str | None
        If given, save training curves (fidelity/sparsity/deletion) as PNG.
    selector
        Pre-initialized selector. When provided, its ``_init_params``
        method is invoked for each graph before training instead of
        creating a new instance.
    batch, batch_size
        If ``batch`` is ``True`` a ``DataLoader`` is used with the given
        ``batch_size`` to train on multiple graphs per step.
    selector_kwargs
        Extra args → ``GumbelMaskSelector`` (e.g., init_bias, tau_start …).
    score_fn : callable, optional
        Custom graph scoring function. If ``None``, it is built from ``model``
        assuming ``Data`` inputs with ``x`` and ``edge_index`` or ``HeteroData``
        inputs for heterogeneous graphs.
    amp : bool, default=False
        Enable mixed precision (CUDA) via ``torch.amp.autocast`` and
        halve feature precision.

    Returns
    -------
    GumbelMaskSelector (trained)
    """
    if score_fn is None:
        if isinstance(cfg_graph, HeteroData):
            score_fn = lambda g: model(g.to(device)).squeeze()
        else:
            score_fn = lambda g: model(
                g.x.to(device), g.edge_index.to(device)
            ).squeeze()

    if amp and torch.cuda.is_available():
        base_fn = score_fn

        def score_fn(graph):
            with torch.amp.autocast(device_type="cuda"):
                return base_fn(graph)

    if not isinstance(cfg_graph, Sequence) or isinstance(cfg_graph, (Data, HeteroData)):
        graphs = [cfg_graph]
    else:
        graphs = list(cfg_graph)

    if selector is None:
        selector = GumbelMaskSelector(view=view, device=device, **selector_kwargs)
    selector.to(device)

    def train_on_graph(g):
        ensure_edgeaware_selector(selector, g)
        selector.train_loop(
            g.to(device),
            score_fn,
            epochs=epochs,
            lr=lr,
            alpha=alpha,
            beta=beta,
            show_progress=len(graphs) == 1,
            plot_path=plot_path if len(graphs) == 1 else None,
        )

    if batch and len(graphs) > 1:
        loader = DataLoader(graphs, batch_size=batch_size, shuffle=False)
        for epoch in range(epochs):
            for batch_graph in loader:
                ensure_edgeaware_selector(selector, batch_graph)
                selector.train_loop(
                    batch_graph.to(device),
                    score_fn,
                    epochs=1,
                    lr=lr,
                    alpha=alpha,
                    beta=beta,
                    show_progress=False,
                )
    else:
        for g in graphs:
            train_on_graph(g)

    return selector


def explain_cfg(
    cfg_graph: Data,
    ast_graph: Data,
    model,
    *,
    view: str = "cfg",
    device: str | torch.device = "cpu",
    selector_kwargs: Dict | None = None,
    ranker_kwargs: Dict | None = None,
    top_k: int | None = 20,
    pretrained_explainer: nn.Module | None = None,
    score_fn=None,
) -> Dict[str, object]:
    """
    End-to-end explanation pipeline.

    Steps
    -----
    1. **Selector**  : train sparse node mask.
    2. **Aggregator**: group selected nodes into ordered paths.
    3. **Ranker**    : estimate Shapley importance & rank.
    4. **Mapper**    : convert CFG nodes → AST token indices.

    Parameters
    ----------
    pretrained_explainer : nn.Module, optional
        Pre-trained explainer providing ``get_node_saliency`` or ``hard_selection``.
        When set, selector training is skipped and this explainer is used
        to obtain ``sel_nodes`` via thresholding or top-k ranking.

    Returns
    -------
    dict
        {
          "selector" : GumbelMaskSelector,
          "sel_nodes": List[int],              # hard selection
          "paths"    : List[dict],             # Aggregator output
          "ranked"   : List[(int,float)],      # node-level rank (desc)
          "tokens"   : List[int],              # AST token indices
          "mapper"   : CFGASTMapper
        }
    """
    selector_kwargs = selector_kwargs or {}
    ranker_kwargs = ranker_kwargs or {}

    if score_fn is None:
        if isinstance(cfg_graph, HeteroData):
            score_fn = lambda g: model(g.to(device)).squeeze()
        else:
            score_fn = lambda g: model(
                g.x.to(device), g.edge_index.to(device)
            ).squeeze()

    # ── 1. Selector / Pretrained Explainer
    if pretrained_explainer is None:
        selector = train_selector(
            cfg_graph,
            model,
            view=view,
            device=device,
            score_fn=score_fn,
            **selector_kwargs,
        )
    else:
        selector = pretrained_explainer

    ensure_edgeaware_selector(selector, cfg_graph)
    selector.to(device)

    if pretrained_explainer is None:
        sel_nodes = selector.hard_selection(cfg_graph).tolist()
    else:
        if hasattr(selector, "get_node_saliency"):
            try:
                mask_prob = selector(cfg_graph)
                node_sal = selector.get_node_saliency(cfg_graph, mask_prob)
            except TypeError:
                node_sal = selector.get_node_saliency(cfg_graph)

            if isinstance(node_sal, dict):
                scores = []
                for ntype in getattr(cfg_graph, "node_types", ["node"]):
                    if ntype in node_sal:
                        scores.append(node_sal[ntype])
                    else:
                        scores.append(torch.zeros(cfg_graph[ntype].num_nodes))
                node_score = torch.cat(scores)
            else:
                node_score = node_sal

            if top_k is not None:
                sel_nodes = torch.topk(node_score, top_k).indices.tolist()
            else:
                sel_nodes = (node_score > 0.5).nonzero(as_tuple=False).view(-1).tolist()
        elif hasattr(selector, "hard_selection"):
            hs = selector.hard_selection(cfg_graph)
            if isinstance(hs, dict):
                nodes = set()
                if isinstance(cfg_graph, HeteroData):
                    for etype, store in iter_edge_types(cfg_graph, view):
                        idx = hs.get(str(etype))
                        if idx is None or len(idx) == 0:
                            continue
                        idx = torch.as_tensor(idx, dtype=torch.long)
                        ei = store.edge_index[:, idx]
                        nodes.update(ei[0].tolist())
                        nodes.update(ei[1].tolist())
                else:
                    idx = torch.as_tensor(hs, dtype=torch.long)
                    ei = cfg_graph.edge_index[:, idx]
                    nodes.update(ei[0].tolist())
                    nodes.update(ei[1].tolist())
                sel_nodes = sorted(nodes)
            else:
                sel_nodes = torch.as_tensor(hs, dtype=torch.long).tolist()
        else:
            raise ValueError(
                "pretrained_explainer must implement get_node_saliency or hard_selection"
            )

    # ── 2. Aggregator
    paths = aggregate_paths(cfg_graph, sel_nodes)

    # ── 3. Ranker
    ranked = quick_rank(
        cfg_graph.to(device),
        score_fn,
        selector_mask=sel_nodes,
        **ranker_kwargs,
    )
    ranked_top = ranked if top_k is None else ranked[:top_k]

    # ── 4. Mapper
    mapper = CFGASTMapper(cfg_graph, ast_graph)
    tokens = mapper.cfg_nodes_to_tokens([n for n, _ in ranked_top])

    return {
        "selector": selector,
        "sel_nodes": sel_nodes,
        "paths": paths,
        "ranked": ranked,
        "tokens": tokens,
        "mapper": mapper,
    }
