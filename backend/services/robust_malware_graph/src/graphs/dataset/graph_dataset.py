"""
src.graphs.dataset.graph_dataset
================================

GraphDataset
------------
디렉터리 구조
~~~~~~~~~~~~~
<root>/
 ├─ train/
 │   ├─ graphs/
 │   │    ├─ a1b2c3.pt        # pickled Data/HeteroData
 │   │    ├─ d4e5f6.pyg.pkl
 │   │    └─ ...
 │   └─ labels.csv            # sha256,label
 ├─ val/
 └─ test/

파일 포맷
~~~~~~~~~
• torch.save(Data/HeteroData, *.pt)         (권장)
• pickle.dump(..., *.pyg.pkl)               (loader에서 저장)
• *.json(.gz) → loader.get_loader().load()  (마지막 fallback)

Notes
-----
• 메타(라벨·split)는 CSV/TSV/JSON 어떤 것이든 `id_col`/`label_col` 지정해 읽을 수 있음
• 로딩 시 transform(g) 적용 → 예: 증강·정규화 등
"""

from __future__ import annotations

import csv
import gzip
import json
import pickle
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple, Sequence
import warnings
from collections import defaultdict
import logging
import copy

import torch.nn.functional as F

import torch
from torch.utils.data import Dataset
from torch_geometric.data import Batch, Data, HeteroData
from tqdm import tqdm

from ..builders.hetero_builder import (
    ensure_num_nodes as hetero_ensure_num_nodes,
    _guess_num_nodes,
    OverLengthPolicy,
)
from ..normalizers.schema import EDGE_REL_ID, EDGE_TYPES, NodeType

try:  # optional dependency (pyarrow, pandas)
    from ..features.cache import load_tensor
except Exception:  # pragma: no cover - optional heavy deps
    load_tensor = None  # type: ignore

from ..loaders.factory import get_loader  # fallback json 로드용
from ..utils import get_logger

GraphT = Data | HeteroData
PathLike = str | Path

_LOG = get_logger("dataset.graph")
_META_LOG = get_logger("dataset.metadata")


def _guess_graph_path(graph_dir: Path, sha: str) -> Path:
    """Return an existing graph file path for *sha* under *graph_dir*."""
    candidates = [graph_dir / f"{sha}.pt", graph_dir / f"{sha}.pyg.pkl"]
    for view in ("ast", "cfg", "fcg", "sys"):
        for ext in (".json", ".json.gz"):
            candidates.append(graph_dir / f"{sha}.{view}{ext}")
    for path in candidates:
        if path.is_file():
            return path
    return graph_dir / f"{sha}"


# ═════════════════════════════════════════════���══════════════════════════
# Dataset
# ════════════════════════════════════════════════════════════════════════
class GraphDataset(Dataset):
    """
    Parameters
    ----------
    root : Path
        데이터셋 루트 (train/val/test 서브폴더 포함).
    split : {'train','val','test'}
    label_file : str | None
        `root/split/<label_file>` 경로의 CSV/TSV/JSON.
    id_col / label_col : str
        레이블 파일에서 ID(sha) / label 컬럼명.
    transform : Callable | None
        각 그래프 로딩 후 호출할 transform.
    require_labels : bool, default=False
        ``True`` 로 설정하면 레이블이 없는 샘플은 로드 후 즉시 제거한다.
    over_length_policy : OverLengthPolicy, default=OverLengthPolicy.TRIM
        Handling strategy when node features exceed ``num_nodes``.
    load_embeds : bool, default True
        ``root/embeds/<sha>.ftr`` 임베딩 파일을 자동 로드할지 여부.
    embed_dir : Path | None, optional
        ``load_embeds`` 가 ``True`` 일 때 임베딩을 찾을 디렉터리.
        ``None`` 이면 ``root/embeds``를 사용한다.
    """

    def __init__(
        self,
        root: PathLike,
        split: str = "train",
        *,
        label_file: Optional[str] = "labels.csv",
        id_col: str = "sha256",
        label_col: str = "label",
        transform: Optional[Callable[[GraphT], GraphT]] = None,
        require_labels: bool = False,
        over_length_policy: OverLengthPolicy = OverLengthPolicy.TRIM,
        load_embeds: bool = True,
        embed_dir: Path | None = None,
        edge_types_schema: Optional[List[Tuple[str, str, str]]] = None,
    ) -> None:
        self.root = Path(root)
        self.split = split
        self.graph_dir = self.root / split / "graphs"
        self.transform = transform
        self.id_col = id_col
        self.label_col = label_col
        self.require_labels = require_labels
        self.over_length_policy = over_length_policy
        self.load_embeds = load_embeds
        self.embed_dir = (
            Path(embed_dir) if embed_dir is not None else self.root / "embeds"
        )
        self.edge_types_schema = edge_types_schema

        # ── 파일 목록 & 레이블 로드 ───────────────────────────────
        self.samples: List[str] = sorted(
            p.stem for p in self.graph_dir.iterdir() if p.is_file()
        )
        self.labels: Dict[str, int] = {}

        if label_file:
            self._load_labels(self.root / split / label_file)

        dropped = 0
        if require_labels:
            before = len(self.samples)
            self.samples = [s for s in self.samples if s in self.labels]
            dropped = before - len(self.samples)
            if dropped:
                _LOG.info(
                    "GraphDataset [%s] dropped %d unlabeled samples", split, dropped
                )

        _LOG.info(
            "GraphDataset [%s]  total=%d  labeled=%d  remaining=%d",
            split,
            len(self.samples) + dropped,
            len(self.labels),
            len(self.samples),
        )

    # ────────────────────────────────────────────────────────────────
    # PyTorch API
    # ────────────────────────────────────────────────────────────────
    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> Tuple[GraphT, int | None, str]:
        sha = self.samples[idx]
        g = self._load_graph(sha)
        g = GraphDataset._remove_batch(g)
        g = GraphDataset._sanitize_attrs(g)

        # --- [강건성 개선 최종안] ---
        # 데이터 로딩의 가장 근본적인 지점에서 데이터 무결성을 보장합니다.
        # 1. 먼저, 그래프의 모든 정보를 바탕으로 정확한 노드 수를 계산합니다.
        g = GraphDataset._ensure_num_nodes(g)
        # 2. 다음으로, 계산된 노드 수에 맞게 피처('x')의 존재와 길이를 보장합니다.
        g = GraphDataset._ensure_x(g, policy=self.over_length_policy)
        # 3. 마지막으로, 이제 신뢰할 수 있는 num_nodes와 피처 길이를 기준으로 유효하지 않은 엣지를 제거합니다.
        g = GraphDataset._sanitize_edges(g)

        if self.transform:
            g = self.transform(g)
            # 변환 후에도 데이터 무결성을 다시 한번 보장합니다.
            g = GraphDataset._ensure_num_nodes(g)
            g = GraphDataset._ensure_x(g, policy=self.over_length_policy)
            g = GraphDataset._sanitize_edges(g)

        label = self.labels.get(sha, None)
        return g, label, sha

    # ────────────────────────────────────────────────────────────────
    # collate
    # ─────────────────────��──────────────────────────────────────────
    @staticmethod
    def collate_fn(
        batch: List[Tuple[GraphT, int | None, str]],
        *,
        attr_names: Dict[str, List[str]] | None = None,
        edge_types_schema: Optional[List[Tuple[str, str, str]]] = None,
    ) -> Dict:
        """Collate a list of graphs with possible feature size mismatch.

        ``torch_geometric.data.Batch.from_data_list`` requires matching
        feature dimensions for all graphs.  Some datasets may contain
        graphs with different node feature sizes, which would normally
        trigger a ``RuntimeError`` during collation.  To provide a more
        robust batching behaviour we inspect each graph and pad
        2‑dimensional tensors (typically ``x``/``feat``) so that every
        graph shares the maximum feature dimension found in the batch.
        """

        graphs, labels, ids = zip(*batch)
        # __getitem__에서 무결성이 보장되므로, collate에서는 더 이상 복잡한 전처리가 필요 없습니다.
        graphs = [GraphDataset._remove_batch(g) for g in graphs]
        graphs = [GraphDataset._ensure_x(g) for g in graphs]
        if attr_names:
            graphs = [GraphDataset._ensure_meta_ids(g, attr_names) for g in graphs]

        # --------------------------------------------------------------
        # Determine max feature dimension for every (node/edge_type, attr)
        # --------------------------------------------------------------
        max_dim: Dict[Tuple[Any, str], int] = defaultdict(int)
        for g in graphs:
            if isinstance(g, HeteroData):
                # node attributes
                for ntype in g.node_types:
                    store = g[ntype]
                    for attr, val in store.items():
                        if (
                            attr in {"x", "feat"}
                            and isinstance(val, torch.Tensor)
                            and val.dim() <= 2
                        ):
                            if val.dim() == 0 or val.numel() == 0:
                                dim = 0
                            else:
                                dim = 1 if val.dim() == 1 else val.size(1)
                            key = (ntype, attr)
                            max_dim[key] = max(max_dim[key], dim)
                # edge attributes
                for etype in g.edge_types:
                    store = g[etype]
                    for attr, val in store.items():
                        if (
                            attr != "edge_index"
                            and isinstance(val, torch.Tensor)
                            and val.dim() <= 2
                        ):
                            if val.dim() == 0 or val.numel() == 0:
                                dim = 0
                            else:
                                dim = 1 if val.dim() == 1 else val.size(1)
                            key = (etype, attr)
                            max_dim[key] = max(max_dim[key], dim)
            else:  # Data
                for attr, val in g.items():
                    if (
                        attr in {"x", "feat"}
                        and isinstance(val, torch.Tensor)
                        and val.dim() <= 2
                    ):
                        if val.dim() == 0 or val.numel() == 0:
                            dim = 0
                        else:
                            dim = 1 if val.dim() == 1 else val.size(1)
                        key = ("", attr)
                        max_dim[key] = max(max_dim[key], dim)
                for attr, val in g.items():
                    if (
                        attr not in {"x", "feat", "edge_index"}
                        and isinstance(val, torch.Tensor)
                        and val.dim() <= 2
                    ):
                        if val.dim() == 0 or val.numel() == 0:
                            dim = 0
                        else:
                            dim = 1 if val.dim() == 1 else val.size(1)
                        key = ("", attr)
                        max_dim[key] = max(max_dim[key], dim)

        # --------------------------------------------------------------
        # Pad features to the collected max dimension
        # --------------------------------------------------------------
        padded_graphs: List[GraphT] = []
        for g in graphs:
            # --- SEGFAULT FIX (Attempt 2) ---
            # Use copy.deepcopy() instead of g.clone(). This is a more robust
            # way to ensure a true deep copy, in case the .clone() method
            # of the custom graph object has issues with shared references.
            g_clone = copy.deepcopy(g)
            if isinstance(g_clone, HeteroData):
                for ntype in g_clone.node_types:
                    store = g_clone[ntype]
                    for attr, val in list(store.items()):
                        if attr in {"x", "feat"} and isinstance(val, torch.Tensor):
                            if val.dim() == 0 or val.numel() == 0:
                                key = (ntype, attr)
                                target = max_dim[key]
                                n = store.num_nodes or 1
                                store[attr] = val.new_zeros((n, target))
                                continue
                            if val.dim() == 1:
                                val = val.unsqueeze(-1)
                                store[attr] = val
                            if val.dim() == 2:
                                key = (ntype, attr)
                                target = max_dim[key]
                                if val.size(1) < target:
                                    pad = target - val.size(1)
                                    store[attr] = F.pad(val, (0, pad))
                for etype in g_clone.edge_types:
                    store = g_clone[etype]
                    for attr, val in list(store.items()):
                        if attr == "edge_index" or not isinstance(val, torch.Tensor):
                            continue
                        if val.dim() == 0 or val.numel() == 0:
                            key = (etype, attr)
                            target = max_dim[key]
                            n = store.num_edges or (store.edge_index.size(1) if hasattr(store, "edge_index") else 1)
                            store[attr] = val.new_zeros((n, target))
                            continue
                        if val.dim() == 1:
                            val = val.unsqueeze(-1)
                            store[attr] = val
                        if val.dim() == 2:
                            key = (etype, attr)
                            target = max_dim[key]
                            if val.size(1) < target:
                                pad = target - val.size(1)
                                store[attr] = F.pad(val, (0, pad))
            else:
                for attr, val in list(g_clone.items()):
                    if attr in {"x", "feat"} and isinstance(val, torch.Tensor):
                        if val.dim() == 0 or val.numel() == 0:
                            key = ("", attr)
                            target = max_dim[key]
                            n = g_clone.num_nodes or 1
                            g_clone[attr] = val.new_zeros((n, target))
                            continue
                        if val.dim() == 1:
                            val = val.unsqueeze(-1)
                            g_clone[attr] = val
                        if val.dim() == 2:
                            key = ("", attr)
                            target = max_dim[key]
                            if val.size(1) < target:
                                pad = target - val.size(1)
                                g_clone[attr] = F.pad(val, (0, pad))
                for attr, val in list(g_clone.items()):
                    if attr in {"x", "feat", "edge_index"} or not isinstance(val, torch.Tensor):
                        continue
                    if val.dim() == 0 or val.numel() == 0:
                        key = ("", attr)
                        target = max_dim[key]
                        n = g_clone.num_edges if hasattr(g_clone, "num_edges") else 1
                        g_clone[attr] = val.new_zeros((n, target))
                        continue
                    if val.dim() == 1:
                        val = val.unsqueeze(-1)
                        g_clone[attr] = val
                    if val.dim() == 2:
                        key = ("", attr)
                        target = max_dim[key]
                        if val.size(1) < target:
                            pad = target - val.size(1)
                            g_clone[attr] = F.pad(val, (0, pad))
            padded_graphs.append(g_clone)

        batch_graph = Batch.from_data_list(padded_graphs)

        labels_t = (
            torch.tensor(labels, dtype=torch.long) if None not in labels else None
        )
        return {"graph": batch_graph, "label": labels_t, "ids": ids}

    # ════════════════════════════════════════════════════════════════
    # internal helpers
    # ════════════════════════════════════════════════════════════════
    def _load_labels(self, path: Path) -> None:
        if not path.is_file():
            _LOG.warning(
                "label file '%s' not found, proceeding without labels", path.name
            )
            return

        if path.suffix in {".csv", ".tsv"}:
            sep = "," if path.suffix == ".csv" else "\t"
            with path.open() as f:
                reader = csv.DictReader(f, delimiter=sep)
                for row in reader:
                    self.labels[row[self.id_col]] = int(row[self.label_col])

        elif path.suffix == ".json":
            data = json.loads(path.read_text())
            for row in data:
                self.labels[row[self.id_col]] = int(row[self.label_col])

        else:
            _LOG.warning("Unsupported label file format '%s'", path.suffix)

    # --------------------------------------------------------------
    def _load_graph(self, sha: str) -> GraphT:
        """
        1) *.pt               → torch.load
        2) *.pyg.pkl          → pickle.load
        3) *.json/.json.gz    → loader fallback (AST/CFG/…)
        """
        # [A] .pt
        pt_file = self.graph_dir / f"{sha}.pt"
        if pt_file.is_file():
            g = torch.load(pt_file, weights_only=False)
            return self._attach_embeds(sha, g)

        # [B] .pyg.pkl
        pkl_file = self.graph_dir / f"{sha}.pyg.pkl"
        if pkl_file.is_file():
            with pkl_file.open("rb") as f:
                g = pickle.load(f)
            return self._attach_embeds(sha, g)

        # [C] .json / .json.gz (+ view suffix)
        for view in ("ast", "cfg", "fcg", "sys"):
            for ext in (".json", ".json.gz"):
                fp = self.graph_dir / f"{sha}.{view}{ext}"
                if fp.is_file():
                    loader = get_loader(view)
                    g = loader.load(fp)
                    return self._attach_embeds(sha, g)

        raise FileNotFoundError(f"graph file for '{sha}' not found")

    def _attach_embeds(self, sha: str, g: GraphT) -> GraphT:
        if not self.load_embeds:
            return g
        if load_tensor is None:  # optional dependency missing
            return g
        embed_file = self.embed_dir / f"{sha}.ftr"
        if not embed_file.is_file():
            if not getattr(self, "_warn_missing_embed", False):
                _LOG.warning("embed file '%s' not found for %s", embed_file.name, sha)
                self._warn_missing_embed = True
            return g
        if not isinstance(g, HeteroData) or "token" not in g.node_types:
            return g
        try:
            feat = load_tensor(sha, self.embed_dir, mmap=False)
        except Exception as exc:  # pragma: no cover - unexpected I/O errors
            warnings.warn(f"failed to load embed for {sha}: {exc}")
            return g

        store = g["token"]

        # --- [파이프라인 재설계] 임베딩을 원본 특징에 즉시 통합 ---
        if hasattr(store, "x") and store.x is not None:
            store.x = torch.cat([store.x, feat], dim=-1)
        else:
            store.x = feat

        if hasattr(store, "x_codebert"):
            del store.x_codebert

        return g

    # --------------------------------------------------------------
    @staticmethod
    def _remove_batch(g: GraphT) -> GraphT:
        """Remove ``batch`` attributes from node stores."""

        if isinstance(g, HeteroData):
            for ntype in g.node_types:
                if hasattr(g[ntype], "batch"):
                    delattr(g[ntype], "batch")
        elif isinstance(g, Data):
            if hasattr(g, "batch"):
                delattr(g, "batch")
        return g

    # --------------------------------------------------------------
    @staticmethod
    def _ensure_x(
        g: GraphT, *, policy: OverLengthPolicy = OverLengthPolicy.TRIM
    ) -> GraphT:
        """Fill missing ``x`` attributes from ``feat`` in each node store.

        Parameters
        ----------
        policy : OverLengthPolicy
            How to handle cases where ``x`` or ``feat`` has more rows than
            ``num_nodes``.
        """

        def _handle(
            store: Data | HeteroData, attr: str, n: int, node_type: str
        ) -> None:
            tensor = getattr(store, attr)
            # 1D tensors are interpreted as per-node features of shape (N, 1).
            # They are first reshaped to 2D so that padding logic can treat them
            # the same as regular feature matrices.
            if tensor.dim() == 1:
                tensor = tensor.unsqueeze(-1)
                setattr(store, attr, tensor)
            if tensor.size(0) < n:
                pad = n - tensor.size(0)
                padded = F.pad(tensor, (0, 0, 0, pad))
                setattr(store, attr, padded)
                return
            if tensor.size(0) == n:
                return
            if policy is OverLengthPolicy.ERROR:
                raise ValueError(f"{tensor.size(0)} > num_nodes({n})")
            if policy is OverLengthPolicy.TRIM:
                warnings.warn(
                    f"{node_type}: trimmed {tensor.size(0) - n} row(s) from {attr}",
                    RuntimeWarning,
                )
                setattr(store, attr, tensor[:n])
            elif policy is OverLengthPolicy.EXPAND:
                store.num_nodes = tensor.size(0)
            elif policy is OverLengthPolicy.MASKPAD:
                mask = torch.zeros(tensor.size(0), dtype=torch.bool)
                mask[:n] = True
                setattr(store, "mask", mask)
                store.num_nodes = tensor.size(0)

        if isinstance(g, HeteroData):
            for node_type in g.node_types:
                store = g[node_type]
                if "x" not in store and "feat" in store:
                    store.x = store.feat

                if "x" in store and store.num_nodes is not None:
                    _handle(store, "x", store.num_nodes, node_type)
        elif isinstance(g, Data):
            if getattr(g, "x", None) is None and hasattr(g, "feat"):
                g.x = g.feat
            if (
                getattr(g, "x", None) is not None
                and getattr(g, "num_nodes", None) is not None
            ):
                _handle(g, "x", g.num_nodes, "Data")
        return g

    @staticmethod
    def _ensure_num_nodes(g: GraphT) -> GraphT:
        """Infer ``num_nodes`` metadata when missing.

        Length is guessed from attributes such as ``x``/``feat``/``addr`` or
        ``inst_cnt`` with ``edge_index`` as a last resort.
        """
        if isinstance(g, HeteroData):
            hetero_ensure_num_nodes(g)
        elif isinstance(g, Data):
            g.num_nodes = _guess_num_nodes(g)
        return g

    # --------------------------------------------------------------
    @staticmethod
    def _ensure_meta_ids(g: GraphT, attr_names: Dict[str, List[str]]) -> GraphT:
        """Ensure metadata id tensors exist for required attributes."""
        if isinstance(g, HeteroData):
            for nt, names in attr_names.items():
                if nt not in g.node_types:
                    continue
                store = g[nt]
                n = store.num_nodes or 0
                for name in names:
                    key = f"{name}_id"
                    if not hasattr(store, key):
                        setattr(store, key, torch.zeros(n, dtype=torch.long))
        elif isinstance(g, Data):
            names = attr_names.get("", [])
            n = g.num_nodes or 0
            for name in names:
                key = f"{name}_id"
                if not hasattr(g, key):
                    setattr(g, key, torch.zeros(n, dtype=torch.long))
        return g

    # --------------------------------------------------------------
    @staticmethod
    def _sanitize_attrs(g: GraphT) -> GraphT:
        """Convert numeric lists to tensors and stash others under ``meta``."""

        def process_store(store: Data | HeteroData) -> None:
            meta = getattr(store, "meta", None)
            if not isinstance(meta, dict):
                meta = {} if meta is None else {"value": meta}

            for attr, val in list(store.items()):
                if attr == "meta":
                    continue
                if isinstance(val, list):
                    if all(isinstance(x, (int, float, bool)) for x in val) or not val:
                        store[attr] = torch.tensor(val)
                    else:
                        meta[attr] = val
                        del store[attr]
                elif isinstance(val, str):
                    meta[attr] = val
                    del store[attr]

            if meta:
                store.meta = meta

        if isinstance(g, HeteroData):
            for _, store in g.node_items():
                process_store(store)
            for _, store in g.edge_items():
                process_store(store)
        else:
            process_store(g)

        return g

    # --------------------------------------------------------------
    @staticmethod
    def _sanitize_attrs(g: GraphT) -> GraphT:
        """Convert numeric lists to tensors and stash others under ``meta``."""

        def process_store(store: Data | HeteroData) -> None:
            meta = getattr(store, "meta", None)
            if not isinstance(meta, dict):
                meta = {} if meta is None else {"value": meta}

            for attr, val in list(store.items()):
                if attr == "meta":
                    continue
                if isinstance(val, list):
                    if all(isinstance(x, (int, float, bool)) for x in val) or not val:
                        store[attr] = torch.tensor(val)
                    else:
                        meta[attr] = val
                        del store[attr]
                elif isinstance(val, str):
                    meta[attr] = val
                    del store[attr]

            if meta:
                store.meta = meta

        if isinstance(g, HeteroData):
            for _, store in g.node_items():
                process_store(store)
            for _, store in g.edge_items():
                process_store(store)
        else:
            process_store(g)

        return g

    # --------------------------------------------------------------
    @staticmethod
    def _sanitize_edge_index(
        store: Data | HeteroData,
        *,
        src_nodes: int,
        dst_nodes: int,
    ) -> None:
        """Remove edges referencing invalid node indices."""
        edge_index = getattr(store, "edge_index", None)
        if not isinstance(edge_index, torch.Tensor) or edge_index.numel() == 0:
            return
        num_e = edge_index.size(1)
        src, dst = edge_index

        if (src < 0).any() or (dst < 0).any():
            _LOG.error(
                f"Negative index found in edge_index! src_nodes={src_nodes}, dst_nodes={dst_nodes}, edge_index={edge_index}"
            )
            raise ValueError("Negative index found in edge_index. See log for details.")

        valid = (src < src_nodes) & (dst < dst_nodes)
        if not valid.all():
            _LOG.warning(
                f"Invalid edges found. Original edge_index shape: {edge_index.shape}"
            )
            _LOG.warning(f"  Invalid src indices: {src[~valid]}")
            _LOG.warning(f"  Invalid dst indices: {dst[~valid]}")
            _LOG.warning(f"  Valid mask sum: {valid.sum().item()} / {num_e}")
            store.edge_index = edge_index[:, valid]
            for key, val in list(store.items()):
                if key == "edge_index":
                    continue
                if torch.is_tensor(val) and val.size(0) == num_e:
                    store[key] = val[valid]
            _LOG.warning(f"  New edge_index shape: {store.edge_index.shape}")

    # --------------------------------------------------------------
    @staticmethod
    def _sanitize_edges(g: GraphT) -> GraphT:
        if isinstance(g, HeteroData):
            for etype in g.edge_types:
                src_t, _, dst_t = etype
                # --- [강건성 개선 최종안] ---
                # 엣지 유효성 검사의 기준이 되는 노드 수를, 선언된 num_nodes와
                # 실제 피처 텐서의 길이 중 '더 작은 값'으로 설정하여 안정성을 극대화합니다.
                # 이는 num_nodes가 피처 텐서보다 크게 잘못 설정된 경우에도 out-of-bounds 오류를 방지합니다.

                # 출발 노드의 유효한 최대 노드 수 계산
                src_n_declared = g[src_t].num_nodes or 0
                src_feat_len = (
                    g[src_t].x.size(0)
                    if hasattr(g[src_t], "x") and g[src_t].x is not None
                    else 0
                )
                src_n = (
                    min(src_n_declared, src_feat_len)
                    if src_feat_len > 0
                    else src_n_declared
                )

                # 도착 노드의 유효한 최대 노드 수 계산
                dst_n_declared = g[dst_t].num_nodes or 0
                dst_feat_len = (
                    g[dst_t].x.size(0)
                    if hasattr(g[dst_t], "x") and g[dst_t].x is not None
                    else 0
                )
                dst_n = (
                    min(dst_n_declared, dst_feat_len)
                    if dst_feat_len > 0
                    else dst_n_declared
                )

                GraphDataset._sanitize_edge_index(
                    g[etype], src_nodes=src_n, dst_nodes=dst_n
                )
        else:
            n_declared = g.num_nodes or 0
            feat_len = g.x.size(0) if hasattr(g, "x") and g.x is not None else 0
            n = min(n_declared, feat_len) if feat_len > 0 else n_declared
            GraphDataset._sanitize_edge_index(g, src_nodes=n, dst_nodes=n)
        return g


def collect_dataset_metadata(
    ds: "Dataset | Sequence[Dataset]",
    *,
    attr_dim: int = 0,
    strict: bool = False,
) -> tuple[
    tuple[list[str], list[tuple[str, str, str]]],
    dict[str, int],
    dict[str, int],  # raw_feat_dim 추가
    dict[str, list[str]],
    dict[str, int],
]:
    """Iterate over one or more datasets and gather union metadata.

    Parameters
    ----------
    ds:
        Single dataset or sequence of datasets to inspect. Each dataset must
        yield either a ``Data``/``HeteroData`` object or a tuple where the first
        element is the graph.
    attr_dim:
        Embedding dimensionality for metadata attributes. ``in_dims`` will be
        computed as ``feat_dim + len(attr_names) * attr_dim`` per node type.

    strict:
        When ``True`` raise ``ValueError`` if a graph contains an ``edge_type``
        index outside the known range.

    Returns
    -------
    metadata, in_dims, attr_names, max_ids
        ``metadata`` is the ``(node_types, edge_types)`` tuple suitable for
        :class:`RGCNEncoder`.  ``in_dims`` maps node types to the required input
        feature dimensions and ``attr_names`` lists metadata attribute names for
        each node type. ``max_ids`` records the maximum observed ``<name>_id``
        value for every metadata attribute across the dataset. The union of
        these IDs determines the minimum ``vocab_size`` required when
        constructing :class:`RGCNEncoder`.
    """

    _LOG.debug(">>> Entering collect_dataset_metadata...")
    _META_LOG.setLevel(logging.DEBUG)  # DEBUG 레벨 설정
    datasets = [ds] if isinstance(ds, GraphDataset) else list(ds)

    node_types: list[str] = []
    edge_types: list[tuple[str, str, str]] = []
    feat_dim: dict[str, int] = defaultdict(int)
    raw_feat_dim: dict[str, int] = defaultdict(int)  # 원본 차원 저장
    attr_map: dict[str, set[str]] = defaultdict(set)
    max_ids: dict[str, int] = defaultdict(int)

    total_graphs = sum(len(d) for d in datasets)
    with tqdm(total=total_graphs, desc="Collecting metadata") as pbar:
        for d in datasets:
            _LOG.debug(f"Processing dataset with {len(d)} graphs.")
            for i in range(len(d)):
                item = d[i]
                if isinstance(item, tuple):
                    g = item[0]
                else:
                    g = item
                if isinstance(g, HeteroData):
                    for nt in g.node_types:
                        if nt not in node_types:
                            node_types.append(nt)
                    for et in g.edge_types:
                        if et not in edge_types:
                            edge_types.append(et)
                    for nt in g.node_types:
                        store = g[nt]
                        current_feat_dim = 0
                        if hasattr(store, "x") and store.x is not None:
                            current_feat_dim = getattr(store, "x").size(-1)
                        # `_attach_embeds`가 .x에 모든 특징을 통합하므로, .x_codebert는 더 이상 존재하지 않습니다.
                        # 따라서 이 로직은 이제 필요 없습니다.
                        # if nt == NodeType.TOKEN.value and hasattr(store, "x_codebert") and store.x_codebert is not None:
                        #     current_feat_dim += getattr(store, "x_codebert").size(-1)
                        feat_dim[nt] = max(feat_dim[nt], current_feat_dim)
                        for key, val in store.items():
                            if key.endswith("_id") and isinstance(val, torch.Tensor):
                                name = key[:-3]
                                attr_map[nt].add(name)
                                if val.numel() > 0:
                                    max_ids[name] = max(max_ids[name], int(val.max()))
                else:  # Data
                    if "" not in node_types:
                        node_types.append("")
                    if hasattr(g, "x"):
                        feat_dim[""] = max(feat_dim.get("", 0), g.x.size(-1))
                    for key, val in g.items():
                        if key.endswith("_id") and isinstance(val, torch.Tensor):
                            name = key[:-3]
                            attr_map[""].add(name)
                            if val.numel() > 0:
                                max_ids[name] = max(max_ids[name], int(val.max()))

                pbar.update(1)

    attr_names = {nt: sorted(names) for nt, names in attr_map.items()}
    _LOG.debug(f"[collect_dataset_metadata] Final attr_names: {attr_names}")

    # --- [강건성 개선 최종안] ---
    # `in_dims`는 이제 오직 순수 피처의 차원만을 책임집니다.
    # `RGCNEncoder`가 이 순수 차원과 `attr_dim`을 받아 스스로 최종 차원을 계산하게 됩니다.
    in_dims = {}
    for nt in node_types:
        # `feat_dim`은 데이터에서 발견된 가장 큰 피처 차원을 저장하고 있습니다.
        # 이를 그대로 순수 피처 차원으로 사용합니다.
        pure_feat_dim = feat_dim.get(nt, 0)
        in_dims[nt] = pure_feat_dim
        _LOG.debug(f"  - in_dims for '{nt}': {pure_feat_dim} (pure feature dimension)")

    total_len = sum(len(d) for d in datasets)
    if total_len > 0 and edge_types:
        relation_ids: set[int] = set()
        invalid_found = False
        for d in datasets:
            for i in range(len(d)):
                item = d[i]
                g = item[0] if isinstance(item, tuple) else item
                sha = item[2] if isinstance(item, tuple) and len(item) >= 3 else None
                if isinstance(g, HeteroData):
                    for et in g.edge_types:
                        if hasattr(g[et], "edge_type"):
                            et_vals = g[et].edge_type
                            if et_vals.numel() > 0:
                                min_id = int(et_vals.min())
                                max_id = int(et_vals.max())
                                if min_id < 0 or max_id >= len(EDGE_REL_ID):
                                    invalid_found = True
                                    if sha is not None and hasattr(d, "graph_dir"):
                                        path = _guess_graph_path(d.graph_dir, sha)
                                    else:
                                        path = sha if sha is not None else str(i)
                                    msg = f"Invalid edge_type index in {path} (min={min_id} max={max_id})"
                                    _META_LOG.error(msg)
                                    if strict:
                                        raise ValueError(msg)
                                relation_ids.update(map(int, et_vals.tolist()))
        if strict and invalid_found:
            raise ValueError("invalid edge_type index")
        if relation_ids:
            num_relations = max(relation_ids) + 1
        else:
            num_relations = 0
    else:
        num_relations = 0

    num_relations = max(num_relations, len(EDGE_TYPES))

    edge_types_full = list(EDGE_TYPES)
    if num_relations > len(edge_types_full):
        edge_types_full.extend(edge_types[len(edge_types_full) : num_relations])
        if len(edge_types_full) < num_relations:
            edge_types_full.extend(
                [f"", f"r{i}", f""] for i in range(len(edge_types_full), num_relations)
            )

    metadata = (tuple(node_types), tuple(edge_types_full[:num_relations]))
    _LOG.debug("<<< Exiting collect_dataset_metadata.")
    return metadata, in_dims, raw_feat_dim, attr_names, dict(max_ids)
