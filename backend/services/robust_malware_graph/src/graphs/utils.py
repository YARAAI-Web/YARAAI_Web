"""
src.graphs.utils (PyG 전용)
===========================
그래프 전처리·학습 파이프라인 전역 헬퍼.

• set_random_seed   : NumPy / PyTorch / PyG / Python RNG 통합 시드 고정
• get_logger        : 싱글턴 Logger
• tqdm_wrap         : tqdm absent 시 no-op
• timer             : with 문 성능 계측
• ensure_dir        : mkdir -p
• graph_size_bytes  : PyG Data/HeteroData 대략적 메모리 사용량(B)
• hash_graph_structure : edge_index를 해시해 고유 ID 생성
"""

from __future__ import annotations

import hashlib
import logging
import os
import random
from contextlib import contextmanager
from pathlib import Path
from time import perf_counter
from typing import Iterator, Optional, Sequence

import numpy as np
try:  # optional torch dependency
    import torch
except Exception:  # pragma: no cover - optional heavy dep
    torch = None  # type: ignore
try:  # optional dependency
    from torch_geometric.data import Data, HeteroData
except Exception:  # pragma: no cover - optional heavy dep
    Data = HeteroData = object  # type: ignore

# --------------------------------------------------------------------------- #
# 1. 시드 고정
# --------------------------------------------------------------------------- #
def set_random_seed(seed: int = 42, *, deterministic: bool = False) -> None:
    """
    Python·NumPy·PyTorch(+CUDA)·PyTorch Geometric RNG 동기화.

    deterministic=True 로 두면 CuDNN 완전 결정론 설정(속도↓).
    """
    if seed < 0:
        return

    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    if torch is not None:
        torch.manual_seed(seed)
        if hasattr(torch.cuda, "manual_seed_all"):
            torch.cuda.manual_seed_all(seed)

    # PyG helper (≥2.3)
    try:
        from torch_geometric.seed import seed_everything as _pyg_seed

        _pyg_seed(seed)
    except Exception:  # pragma: no cover
        pass

    if deterministic and torch is not None:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


# --------------------------------------------------------------------------- #
# 2. 로거
# --------------------------------------------------------------------------- #
def get_logger(name: str = "graphs", level: int = logging.INFO) -> logging.Logger:
    """스트림 핸들러 하나만 붙이고 재사용하는 싱글턴 Logger."""
    logger = logging.getLogger(name)
    if logger.handlers:  # 이미 초기화됨
        return logger

    logger.setLevel(level)
    fmt = "%(asctime)s | %(levelname)-7s | %(name)s: %(message)s"
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(fmt, "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(handler)
    return logger


# --------------------------------------------------------------------------- #
# 3. tqdm 래퍼
# --------------------------------------------------------------------------- #
try:
    from tqdm.auto import tqdm as _tqdm
except ModuleNotFoundError:  # pragma: no cover
    def _tqdm(iterable, *_, **__):  # type: ignore
        return iterable

def tqdm_wrap(iterable, desc: str = "", total: Optional[int] = None, **kwargs):
    return _tqdm(iterable, desc=desc, total=total, dynamic_ncols=True, **kwargs)


# --------------------------------------------------------------------------- #
# 4. 타이머 컨텍스트
# --------------------------------------------------------------------------- #
@contextmanager
def timer(
    msg: str = "elapsed",
    *,
    logger: Optional[logging.Logger] = None,
    use_tqdm: bool = False,
) -> Iterator[None]:
    """Measure wall time of a ``with`` block."""
    start = perf_counter()
    yield
    elapsed = perf_counter() - start
    if use_tqdm:
        try:
            from tqdm.auto import tqdm
        except ModuleNotFoundError:  # pragma: no cover - optional dep
            print(f"{msg}: {elapsed:.2f}s")
        else:
            tqdm.write(f"{msg}: {elapsed:.2f}s")
    else:
        if logger:
            logger.info(f"{msg}: {elapsed:.2f}s")
        else:
            print(f"{msg}: {elapsed:.2f}s")


# --------------------------------------------------------------------------- #
# 5. 파일·디렉터리
# --------------------------------------------------------------------------- #
def ensure_dir(path: str | Path) -> None:
    Path(path).expanduser().mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------------------------- #
# 6. 그래프 유틸 (PyG)
# --------------------------------------------------------------------------- #
def _tensor_mem_bytes(t: torch.Tensor) -> int:
    return t.numel() * t.element_size()


def graph_size_bytes(g: Data | HeteroData) -> int:
    """
    노드·엣지 feature 텐서 메모리 사용량(바이트) 추정.

    구조 인덱스(edge_index 등)는 제외.
    """
    size = 0
    if isinstance(g, Data):
        for key, tensor in g.items():
            if isinstance(tensor, torch.Tensor):
                size += _tensor_mem_bytes(tensor)
    else:  # HeteroData
        for store in g.node_stores + g.edge_stores:
            for tensor in store.values():
                if isinstance(tensor, torch.Tensor):
                    size += _tensor_mem_bytes(tensor)
    return size


def _flatten_edge_index(edge_index: torch.Tensor) -> bytes:
    """edge_index[2,E] → 바이트 직렬화(행 우선)."""
    return edge_index.cpu().numpy().astype(np.int64, copy=False).tobytes()


def hash_graph_structure(
    g: Data | HeteroData,
    algo: str = "sha256",
    edge_types: Sequence[str] | None = None,
) -> str:
    """
    edge_index(들)를 직렬화해 해시 → topology 전용 고유 ID.

    edge_types : HeteroData 선택적 필터, None ⇒ 모든 edge_store 사용.
    """
    hasher = hashlib.new(algo)

    if isinstance(g, Data):
        hasher.update(_flatten_edge_index(g.edge_index))
    else:
        for etype, store in g.edge_items():
            if edge_types and etype not in edge_types:
                continue
            hasher.update(_flatten_edge_index(store.edge_index))

    return hasher.hexdigest()


def sanitize_edge_index(
    store: Data | HeteroData,
    *,
    src_nodes: int,
    dst_nodes: int,
) -> Data | HeteroData:
    """Remove edges with invalid node indices.

    Edges whose source or destination IDs fall outside
    ``[0, num_nodes - 1]`` will be dropped along with any edge
    attributes of matching length. The input ``store`` is modified in
    place and also returned for convenience.
    """

    edge_index = getattr(store, "edge_index", None)
    if not isinstance(edge_index, torch.Tensor) or edge_index.numel() == 0:
        return store

    num_e = edge_index.size(1)
    src, dst = edge_index
    valid = (
        (src >= 0)
        & (src < src_nodes)
        & (dst >= 0)
        & (dst < dst_nodes)
    )
    if valid.all():
        return store

    store.edge_index = edge_index[:, valid]
    for key, val in list(store.items()):
        if key == "edge_index":
            continue
        if torch.is_tensor(val) and val.size(0) == num_e:
            store[key] = val[valid]

    return store


__all__ = [
    "set_random_seed",
    "get_logger",
    "tqdm_wrap",
    "timer",
    "ensure_dir",
    "graph_size_bytes",
    "hash_graph_structure",
    "sanitize_edge_index",
    "prune_graph_by_selection",
]

def prune_graph_by_selection(graph: HeteroData, selection_mask: torch.Tensor, threshold: float = 0.5) -> HeteroData:
    """Prunes a heterogeneous graph based on an edge selection mask.

    Args:
        graph: The input heterogeneous graph.
        selection_mask: A 1D tensor representing the importance of each edge.
        threshold: The threshold above which to keep an edge.

    Returns:
        A new graph with edges pruned based on the selection mask.
    """
    new_graph = graph.clone()
    
    # A global pointer to traverse the selection_mask
    mask_ptr = 0

    for edge_type in graph.edge_types:
        edge_store = graph[edge_type]
        num_edges = edge_store.num_edges

        if num_edges == 0:
            continue

        # Slice the relevant part of the mask for the current edge type
        current_mask = selection_mask[mask_ptr : mask_ptr + num_edges]
        
        # Create a boolean mask for edges to keep
        keep_mask = current_mask >= threshold

        # Prune the attributes of the edge store
        for key, value in edge_store.items():
            if torch.is_tensor(value) and value.size(0) == num_edges:
                new_graph[edge_type][key] = value[keep_mask]

        mask_ptr += num_edges

    return new_graph
