"""
src.graphs.builders.hetero_builder
==================================

HeteroGraphBuilder
------------------
1) add_view(view_data, view_name)
   └─ 정규화된 HeteroData/ Data(노멀라이저 적용済) 추가
2) build() → torch_geometric.data.HeteroData
   └─ 노드 global offset 재배치 & cross-view edge 연결

지원 뷰
~~~~~~~
• 'ast'      : ('token',  'child',  'token')
• 'cfg'      : ('bb',     'cfg',    'bb')
• 'fcg'      : ('function','calls', 'function')
• 'syscall'  : ('syscall','seq',    'syscall')
"""

from __future__ import annotations

import warnings

import itertools
import logging
from collections import defaultdict
from enum import Enum
from typing import Dict, List, Tuple, Sequence

import torch
from torch_geometric.data import Data, HeteroData

from ..normalizers.schema import EDGE_REL_ID, NodeType
from ..utils import get_logger

# ────────────────────────────────────────────────────────────────
# 타입
# ────────────────────────────────────────────────────────────────
_ViewT = Data | HeteroData
_NodeKey = Tuple[str, int]  # (node_type, local_id)


class OverLengthPolicy(Enum):
    """Behaviour when feature rows exceed ``num_nodes``."""

    ERROR = "ERROR"
    TRIM = "TRIM"
    EXPAND = "EXPAND"
    MASKPAD = "MASKPAD"


class HeteroGraphBuilder:
    """
    여러 정규화된 뷰 그래프를 추가 → 최종 HeteroData 로 병합.

    Parameters
    ----------
    log_level : int, default logging.INFO
    """

    def __init__(self, log_level: int = logging.INFO) -> None:
        self.log = get_logger("builder.hetero", log_level)
        self._views: Dict[str, _ViewT] = {}
        # global node id 매핑 : (view, ntype, local_id) → global_id
        self._id_maps: Dict[Tuple[str, _NodeKey], int] = {}
        # next global id per node type
        self._global_counters: Dict[str, int] = defaultdict(int)

    # ===========================================================
    # public
    # ===========================================================
    def add_view(self, g: _ViewT, view: str) -> None:
        """
        정규화된 (Hetero)Data 를 뷰 이름과 함께 저장.
        """
        if view in self._views:
            raise ValueError(f"view '{view}' already added")
        self._views[view] = g
        self.log.debug("Added view '%s'  node_types=%s", view, list(g.node_types))

    def build(self) -> HeteroData:
        """
        모든 add_view() 후 호출 → 병합된 HeteroData 반환.
        """
        if not self._views:
            raise RuntimeError("No views added")

        out = HeteroData()
        self._assign_global_ids()
        self._merge_node_stores(out)
        for ntype, count in self._global_counters.items():
            out[ntype].num_nodes = count
        self._merge_edge_stores(out)
        return out

    # ===========================================================
    # internals
    # ===========================================================
    def _assign_global_ids(self) -> None:
        """Assign contiguous global IDs for nodes across views.

        Raises
        ------
        ValueError
            If a node store does not define ``num_nodes``.
        """
        for view_name, g in self._views.items():
            for ntype in g.node_types:
                store = g[ntype]
                if "num_nodes" not in store:
                    raise ValueError(
                        f"view '{view_name}' node type '{ntype}' lacks num_nodes"
                    )
                num = store.num_nodes
                start = self._global_counters[ntype]
                self._global_counters[ntype] += num
                for lid in range(num):
                    self._id_maps[(view_name, (ntype, lid))] = start + lid
            self.log.debug(
                "[%s] assigned global ids — %s",
                view_name,
                {nt: g[nt].num_nodes for nt in g.node_types},
            )

    # -----------------------------------------------------------
    def _merge_node_stores(self, out: HeteroData) -> None:
        """
        노드 속성 병합: 동일 node_type 에 대해 concat (row-wise).
        """
        for ntype in self._global_counters:
            # gather tensors/attrs across views
            stores = [g[ntype] for g in self._views.values() if ntype in g.node_types]
            if not stores:
                continue

            # 모든 속성 키 집계
            keys = set(itertools.chain.from_iterable(s.keys() for s in stores))
            # keys.discard("num_nodes")  # keep num_nodes for later assignment
            merged_store = out[ntype]

            for k in keys:
                cols = []
                ref_store = next((s for s in stores if k in s), None)
                for s in stores:
                    if k in s:
                        val = s[k]
                        if isinstance(val, torch.Tensor):
                            cols.append(val)
                        elif isinstance(val, Sequence):
                            cols.extend(list(val))
                        else:
                            cols.extend([val] * s.num_nodes)
                    else:  # 없는 view → padding 값
                        if isinstance(ref_store[k], torch.Tensor):
                            shape = list(ref_store[k].shape)
                            shape[0] = s.num_nodes
                            cols.append(torch.zeros(shape, dtype=ref_store[k].dtype))
                        else:  # list[str] 같은 python obj
                            cols.extend([None] * s.num_nodes)
                if not cols:
                    ref_val = ref_store[k]
                    if isinstance(ref_val, torch.Tensor):
                        shape = list(ref_val.shape)
                        shape[0] = 0
                        merged_store[k] = torch.zeros(shape, dtype=ref_val.dtype)
                    else:
                        merged_store[k] = []
                else:
                    merged_store[k] = (
                        torch.cat(cols)
                        if isinstance(cols[0], torch.Tensor)
                        else list(cols)
                    )

    # -----------------------------------------------------------
    def _merge_edge_stores(self, out: HeteroData) -> None:
        """
        edge_index global remap + concat per (src,rel,dst) 키.
        """
        tmp_edges: Dict[Tuple[str, str, str], List[torch.Tensor]] = defaultdict(list)
        tmp_attrs: Dict[Tuple[str, str, str], Dict[str, List[torch.Tensor]]] = (
            defaultdict(lambda: defaultdict(list))
        )

        for view_name, g in self._views.items():
            for src_t, rel_t, dst_t in g.edge_types:
                store = g[(src_t, rel_t, dst_t)]
                # 로컬 -> 글로벌 id 변환
                src, dst = store.edge_index
                src_g = torch.tensor(
                    [self._id_maps[(view_name, (src_t, int(i)))] for i in src],
                    dtype=torch.long,
                )
                dst_g = torch.tensor(
                    [self._id_maps[(view_name, (dst_t, int(i)))] for i in dst],
                    dtype=torch.long,
                )
                tmp_edges[(src_t, rel_t, dst_t)].append(torch.stack([src_g, dst_g]))

                # 나머지 edge 속성도 합치기
                for k, v in store.items():
                    if k == "edge_index":
                        continue
                    tmp_attrs[(src_t, rel_t, dst_t)][k].append(v)

        # concat & dedup
        for key, edge_list in tmp_edges.items():
            edges = torch.cat(edge_list, dim=1)
            # deduplication
            ei, inverse = torch.unique(edges, dim=1, return_inverse=True)
            out[key].edge_index = ei

            # aggregate edge attributes using the same mapping
            for k, tensors in tmp_attrs[key].items():
                attr = torch.cat(tensors)
                if attr.size(0) != edges.size(1):
                    raise ValueError(
                        f"edge attribute '{k}' count {attr.size(0)} does not match"
                        f" edge count {edges.size(1)}"
                    )
                first_idx = torch.full((ei.size(1),), -1, dtype=torch.long)
                for idx, uid in enumerate(inverse.tolist()):
                    if first_idx[uid] == -1:
                        first_idx[uid] = idx
                out[key][k] = attr[first_idx]

            # edge_type auto fill if missing
            if "edge_type" not in out[key]:
                out[key].edge_type = torch.full(
                    (ei.shape[1],),
                    EDGE_REL_ID[key[1]],
                    dtype=torch.long,
                )


# ────────────────────────────────────────────────────────────────
# 4. Convenience – batch-builder (views → hetero/*.pt)
# ────────────────────────────────────────────────────────────────
from pathlib import Path
import multiprocessing as mp
from functools import partial

from ..loaders.factory import get_loader  # view JSON → (Hetero)Data
from ..normalizers.base import get_normalizer  # optional schema normaliser
from ..utils import tqdm_wrap, ensure_dir, set_random_seed


def _guess_num_nodes(store: Data | HeteroData) -> int:
    """Return a best effort ``num_nodes`` guess for *store*.

    The previous logic picked the first suitable attribute, which could result
    in inconsistent metadata when attributes such as ``addr`` and
    ``inst_cnt`` had different lengths.  This implementation collects all
    candidate lengths and issues a warning on mismatch before returning the
    maximum size.  ``0`` is returned when no hint is available.
    """

    n = getattr(store, "num_nodes", None)
    if n is not None:
        return int(n)

    # Prefer explicit feature length when present
    for attr in ("x", "feat"):
        val = getattr(store, attr, None)
        if isinstance(val, torch.Tensor):
            return int(val.size(0))

    candidates = []

    for attr in ("addr", "inst_cnt", "name", "api_name"):
        val = getattr(store, attr, None)
        if val is not None:
            try:
                candidates.append(len(val))
            except TypeError:
                if isinstance(val, torch.Tensor):
                    candidates.append(int(val.size(0)))

    ei = getattr(store, "edge_index", None)
    if isinstance(ei, torch.Tensor) and ei.numel() > 0:
        candidates.append(int(ei.max()) + 1)

    if not candidates:
        _LOG.debug(f"No candidates for num_nodes. Returning 0.")
        return 0

    unique = set(candidates)
    _LOG.debug(f"Candidates: {candidates}, Unique: {unique}")
    if len(unique) > 1:
        warnings.warn(
            f"num_nodes mismatch across attributes {sorted(unique)}; using max",
            RuntimeWarning,
        )
    return max(unique)


def _ensure_num_nodes_any(g: Data | HeteroData) -> Data | HeteroData:
    """Infer ``num_nodes`` for ``Data`` or ``HeteroData`` objects.

    Values are derived using :func:`_guess_num_nodes` so that saved graphs
    missing this metadata remain usable.
    """

    if isinstance(g, HeteroData):
        for _, store in g.node_items():
            store.num_nodes = _guess_num_nodes(store)
    else:  # Data
        g.num_nodes = _guess_num_nodes(g)
    return g


def ensure_num_nodes(hetero: HeteroData) -> None:
    """Infer and set ``num_nodes`` for every node store in ``hetero``.

    Parameters
    ----------
    hetero : HeteroData
        Graph whose node stores may lack ``num_nodes`` metadata.  The value is
        guessed from attributes such as ``x``, ``feat``, ``addr`` or
        ``inst_cnt`` with ``edge_index`` used as a fallback.
    """
    for _, store in hetero.node_items():
        store.num_nodes = _guess_num_nodes(store)


def fill_missing_node_feats(
    hetero: HeteroData,
    dim: int = 128,
    *,
    policy: OverLengthPolicy = OverLengthPolicy.TRIM,
) -> None:
    """Pad missing node features with zeros after ensuring ``num_nodes``.

    Parameters
    ----------
    hetero : HeteroData
    dim : int
        Feature dimension to use when a node store lacks ``feat``.
    policy : OverLengthPolicy
        How to handle cases where existing features are longer than
        ``num_nodes``.
    """

    ensure_num_nodes(hetero)

    for node_type, store in hetero.node_items():
        if "feat" not in store:
            store.feat = torch.zeros((store.num_nodes, dim), dtype=torch.float32)
            continue

        n = store.num_nodes
        feat_len = store.feat.size(0)
        if n is not None and feat_len > n:
            if policy is OverLengthPolicy.ERROR:
                raise ValueError(
                    f"{feat_len} > num_nodes({n}) for node type; policy=ERROR"
                )
            if policy is OverLengthPolicy.TRIM:
                warnings.warn(
                    f"{node_type}: trimmed {feat_len - n} row(s) from feat",
                    RuntimeWarning,
                )
                store.feat = store.feat[:n]
            elif policy is OverLengthPolicy.EXPAND:
                store.num_nodes = feat_len
            elif policy is OverLengthPolicy.MASKPAD:
                mask = torch.zeros(feat_len, dtype=torch.bool)
                mask[:n] = True
                store.mask = mask
                store.num_nodes = feat_len


def _process_one(
    sha: str,
    *,
    views_dir: Path,
    hetero_dir: Path,
    views: Tuple[str, ...],
    normalise: bool,
    rebuild: bool,
    log_level: int,
    with_feats: bool = False,
    feat_dim: int = 1,
    feat_policy: OverLengthPolicy = OverLengthPolicy.TRIM,
) -> None:
    """Single sample processing for :func:`build_hetero_dataset`."""
    log = get_logger("builder.dataset", log_level)

    out_path = hetero_dir / f"{sha}.pt"
    if out_path.exists() and not rebuild:
        return  # skip existing

    builder = HeteroGraphBuilder(log_level=log_level)
    for v in views:
        fp_json = views_dir / v / f"{sha}.json"
        if not fp_json.exists():
            fp_json = fp_json.with_suffix(".json.gz")
        if not fp_json.exists():
            continue

        g = get_loader(v).load(fp_json)
        if normalise:
            g = get_normalizer(v).normalize(g)
        g = _ensure_num_nodes_any(g)
        builder.add_view(g, v)

    if not builder._views:
        log.warning("(%s) skipped – no view graphs found", sha)
        return

    hetero = builder.build()
    ensure_num_nodes(hetero)
    if with_feats:
        fill_missing_node_feats(hetero, feat_dim, policy=feat_policy)
    torch.save(hetero, out_path)


def build_hetero_dataset(
    *,
    views_dir: Path,
    hetero_dir: Path,
    views: Tuple[str, ...] = ("ast", "cfg", "fcg", "syscall"),
    normalise: bool = True,
    rebuild: bool = False,
    clean: bool = False,
    workers: int | None = 0,
    seed: int = 42,
    log_level: int = logging.INFO,
    with_feats: bool = False,
    feat_dim: int = 1,
    feat_policy: OverLengthPolicy = OverLengthPolicy.TRIM,
) -> None:
    """
    data/views/<view>/<sha>.json → data/hetero/<sha>.pt   일괄 변환.

    Parameters
    ----------
    views_dir   : Path   디렉터리 root (AST/CFG/… JSON 캐시)
    hetero_dir  : Path   출력 루트 (*.pt)
    views       : tuple  사용할 뷰 이름들
    normalise   : bool   view loader 뒤 schema normaliser 적용 여부
    rebuild     : bool   이미 존재하는 .pt 도 강제로 갱신할지
    clean       : bool   rebuild 시 이미 존재하는 *.pt 파일 삭제 여부
    workers     : int    0/1 ⇒ 직렬, 그 이상은 mp.Pool
    seed        : int    mp fork-safety RNG 시드
    """
    ensure_dir(hetero_dir)
    if clean and rebuild:
        for p in hetero_dir.glob("*.pt"):
            p.unlink(missing_ok=True)
    set_random_seed(seed)
    log = get_logger("builder.dataset", log_level)

    # ── 1. 샘플 id(sha256) 수집 ───────────────────────────────────────────
    id_sets = []
    for v in views:
        view_dir = views_dir / v
        if view_dir.is_dir():
            id_sets.append({p.stem for p in view_dir.glob("*.json*")})
    all_ids = sorted(set.union(*id_sets))
    log.info("▶ %d sample(s) aggregated across views=%s", len(all_ids), ",".join(views))

    process_one = partial(
        _process_one,
        views_dir=views_dir,
        hetero_dir=hetero_dir,
        views=views,
        normalise=normalise,
        rebuild=rebuild,
        log_level=log_level,
        with_feats=with_feats,
        feat_dim=feat_dim,
        feat_policy=feat_policy,
    )

    # ── 3. 실행 (병렬 or 직렬) ───────────────────────────────────────────
    iterable = all_ids  # 전체 샘플 목록
    total = len(all_ids)
    if workers and workers > 1:
        with mp.Pool(workers) as pool:
            for _ in tqdm_wrap(
                pool.imap_unordered(process_one, iterable),
                desc="[hetero]",
                total=total,
            ):
                pass
    else:
        for _ in tqdm_wrap(map(process_one, iterable), desc="[hetero]", total=total):
            pass

    log.info("✔ hetero graphs saved → %s", hetero_dir)
