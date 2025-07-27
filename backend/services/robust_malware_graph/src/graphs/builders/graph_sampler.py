"""
src.graphs.builders.graph_sampler
=================================

GraphSampler
------------
학습·XAI·디버깅에서 큰 그래프를 **부분 그래프(mini-batch)** 로 잘라내기 위한 유틸.

내장 샘플러
~~~~~~~~~~~
• sample_k_hop(seed_nodes, k)        : k-hop 근접 이웃
• sample_random_walk(start, walklen) : 다중 Random-Walk union
• sample_edge_drop(p=0.8)            : 엣지 확률 삭제(aug)

PyG 내장 래퍼
~~~~~~~~~~~~
• GraphSAINTNodeSampler
• GraphSAINTEdgeSampler
• ClusterData / ClusterLoader

설계 포인트
-----------
1. **Data·HeteroData 모두 지원**  (edge_type 보존)
2. 샘플링 결과는 원본 `Data` **view** 를 공유해 메모리 절약
3. `return_induced = True` 옵션 시 (subgraph, node_mask, edge_mask) 튜플 반환
"""

from __future__ import annotations

import random
from pathlib import Path
from typing import Iterable, List, Tuple

import torch
import numpy as np
from torch_geometric.data import Data, HeteroData
from torch_geometric.loader import (
    ClusterData,
    ClusterLoader,
    GraphSAINTEdgeSampler,
    GraphSAINTNodeSampler,
)
from torch_geometric.loader.cluster import Partition
from torch_geometric.utils import k_hop_subgraph, subgraph

###############################################################################
# base helpers
###############################################################################
def _to_tensor(idx: Iterable[int]) -> torch.Tensor:
    return torch.tensor(list(idx), dtype=torch.long)


def _edge_mask_from_subset(ei: torch.Tensor, subset: torch.Tensor) -> torch.Tensor:
    return (subset[ei[0]] & subset[ei[1]]).bool()


###############################################################################
# 1) k-hop 서브그래프
###############################################################################
def sample_k_hop(
    g: Data | HeteroData,
    seed_nodes: Iterable[int],
    k: int = 2,
    *,
    return_induced: bool = False,
) -> Data | Tuple[Data, torch.Tensor, torch.Tensor]:
    """단일 타입 Data 전용."""
    if isinstance(g, HeteroData):
        raise TypeError("HeteroData는 builders.view_merger 이후 단일 relation에 대해 사용하세요")

    seed = _to_tensor(seed_nodes)
    nodes, ei, mask = k_hop_subgraph(seed, k, g.edge_index, relabel_nodes=True)
    sub = Data(
        edge_index=ei,
        num_nodes=int(nodes.size(0)),
    )
    for k, v in g.items():
        if isinstance(v, torch.Tensor) and v.size(0) == g.num_nodes:
            sub[k] = v[nodes]
    if return_induced:
        node_mask = torch.zeros(g.num_nodes, dtype=torch.bool)
        node_mask[nodes] = True
        edge_mask = _edge_mask_from_subset(g.edge_index, node_mask)
        return sub, node_mask, edge_mask
    return sub


###############################################################################
# 2) Random-Walk 여러 번 → union
###############################################################################
def sample_random_walk(
    g: Data,
    start_nodes: Iterable[int],
    walk_length: int = 8,
    num_walks: int = 16,
    *,
    return_induced: bool = False,
) -> Data | Tuple[Data, torch.Tensor, torch.Tensor]:
    idx = [int(i) for i in start_nodes]
    for _ in range(num_walks):
        cur = random.choice(idx)
        for _ in range(walk_length):
            neigh = g.edge_index[1][g.edge_index[0] == cur]
            if len(neigh) == 0:
                break
            nxt = int(neigh[random.randrange(len(neigh))])
            idx.append(nxt)
            cur = nxt
    idx_u = torch.unique(_to_tensor(idx))
    ei, _ = subgraph(idx_u, g.edge_index, relabel_nodes=True)
    sub = Data(edge_index=ei, num_nodes=int(idx_u.size(0)))
    for k, v in g.items():
        if isinstance(v, torch.Tensor) and v.size(0) == g.num_nodes:
            sub[k] = v[idx_u]
    if return_induced:
        node_mask = torch.zeros(g.num_nodes, dtype=torch.bool)
        node_mask[idx_u] = True
        edge_mask = _edge_mask_from_subset(g.edge_index, node_mask)
        return sub, node_mask, edge_mask
    return sub


###############################################################################
# 3) Edge-Drop 증강
###############################################################################
def sample_edge_drop(
    g: Data,
    p: float = 0.8,
    *,
    return_induced: bool = False,
) -> Data | Tuple[Data, torch.Tensor]:
    keep = torch.rand(g.edge_index.size(1)) > p
    ei = g.edge_index[:, keep]
    sub = Data(edge_index=ei, num_nodes=g.num_nodes)
    for k, v in g.items():
        sub[k] = v
    if return_induced:
        return sub, keep
    return sub


###############################################################################
# 4) PyG GraphSAINT / ClusterGCN 래퍼
###############################################################################
def sainth_loader(
    g: Data,
    mode: str = "node",
    batch_size: int = 6000,
    walk_length: int = 2,
    *,
    num_steps: int = 1,
    sample_coverage: int = 0,
    save_dir: str | None = None,
    log: bool = True,
    num_workers: int = 0,
) -> GraphSAINTNodeSampler | GraphSAINTEdgeSampler:
    common = dict(
        batch_size=batch_size,
        walk_length=walk_length,
        num_steps=num_steps,
        sample_coverage=sample_coverage,
        save_dir=save_dir,
        log=log,
        num_workers=num_workers,
    )
    if mode == "node":
        common.pop("walk_length", None)
        return GraphSAINTNodeSampler(g, **common)
    if mode == "edge":
        return GraphSAINTEdgeSampler(g, **common)
    raise ValueError("mode must be 'node' or 'edge'")


import logging
import psutil
import torch

LOGGER = logging.getLogger(__name__)

def _log_memory(stage: str):
    """Logs current CPU memory usage."""
    cpu_mem = psutil.virtual_memory()
    LOGGER.info(f"[MemoryLog] Stage: {stage} | CPU Used: {cpu_mem.used / 1024**3:.2f}GB ({cpu_mem.percent}%)")


import logging
import psutil
import torch

LOGGER = logging.getLogger(__name__)
if not LOGGER.hasHandlers():
    LOGGER.addHandler(logging.NullHandler())

def _log_memory(stage: str):
    """Logs current CPU memory usage."""
    cpu_mem = psutil.virtual_memory()
    # Use the root logger to ensure the message is displayed
    logging.info(f"[MemoryLog] Stage: {stage} | CPU Used: {cpu_mem.used / 1024**3:.2f}GB ({cpu_mem.percent}%)")


def sainth_loader_hetero(
    g: HeteroData,
    mode: str = "node",
    batch_size: int = 6000,
    walk_length: int = 2,
    *,
    num_steps: int = 1,
    sample_coverage: int = 0,
    save_dir: str | None = None,
    log: bool = True,
    num_workers: int = 0,
) -> Iterable[HeteroData]:
    """GraphSAINT sampler for :class:`HeteroData` graphs.

    The heterogeneous graph is converted to a homogeneous view for sampling and
    then reconstructed on the fly for each mini-batch.
    """


    _log_memory("sainth_loader_hetero: Start")
    
    for node_type_str in g.node_types:
        if g[node_type_str].num_nodes is None:
            g[node_type_str].num_nodes = 0
    
    logging.info("Converting HeteroData to homogeneous graph...")
    _log_memory("sainth_loader_hetero: Before to_homogeneous")
    homo = g.to_homogeneous(add_node_type=True, add_edge_type=True)
    _log_memory("sainth_loader_hetero: After to_homogeneous")
    logging.info("Homogeneous graph created.")

    logging.info("Initializing GraphSAINT loader...")
    _log_memory("sainth_loader_hetero: Before sainth_loader init")
    loader = sainth_loader(
        homo,
        mode=mode,
        batch_size=batch_size,
        walk_length=walk_length,
        num_steps=num_steps,
        sample_coverage=sample_coverage,
        save_dir=save_dir,
        log=log,
        num_workers=num_workers,
    )
    _log_memory("sainth_loader_hetero: After sainth_loader init")
    logging.info("GraphSAINT loader initialized.")

    for i, sub in enumerate(loader):
        _log_memory(f"sainth_loader_hetero: Start of iteration {i}")
        yield sub.to_heterogeneous(
            node_type=sub.node_type,
            edge_type=sub.edge_type,
            node_type_names=list(g.node_types),
            edge_type_names=list(g.edge_types),
        )
        _log_memory(f"sainth_loader_hetero: End of iteration {i}")


def cluster_loader(
    g: Data,
    num_parts: int = 1500,
    batch_size: int = 20,
    shuffle: bool = True,
) -> ClusterLoader:
    data = ClusterData(g, num_parts=num_parts, recursive=False)
    return ClusterLoader(data, batch_size=batch_size, shuffle=shuffle)


def cluster_loader_hetero(
    g: HeteroData,
    num_parts: int = 1500,
    batch_size: int = 20,
    shuffle: bool = True,
) -> ClusterLoader:
    """ClusterGCN loader for :class:`HeteroData` graphs."""
    data = ClusterData(g, num_parts=num_parts, recursive=False)
    return ClusterLoader(data, batch_size=batch_size, shuffle=shuffle)


def cluster_file_loader(
    g: Data,
    cluster_file: str | Path,
    batch_size: int = 20,
    shuffle: bool = True,
) -> ClusterLoader:
    """ClusterGCN loader from a saved ``*.npz`` partition file."""
    arr = np.load(cluster_file)
    part = Partition(
        indptr=torch.from_numpy(arr["indptr"]),
        index=torch.from_numpy(arr["index"]),
        partptr=torch.from_numpy(arr["partptr"]),
        node_perm=torch.from_numpy(arr["node_perm"]),
        edge_perm=torch.from_numpy(arr["edge_perm"]),
        sparse_format=str(arr.get("sparse_format", "csr")),
    )
    data_obj = ClusterData.__new__(ClusterData)
    data_obj.num_parts = part.partptr.numel() - 1
    data_obj.partition = part
    data_obj.recursive = False
    data_obj.keep_inter_cluster_edges = False
    data_obj.sparse_format = part.sparse_format
    data_obj.data = ClusterData._permute_data(data_obj, g, part)
    return ClusterLoader(data_obj, batch_size=batch_size, shuffle=shuffle)


def cluster_file_loader_hetero(
    g: HeteroData,
    cluster_file: str | Path,
    batch_size: int = 20,
    shuffle: bool = True,
) -> ClusterLoader:
    """ClusterGCN loader for :class:`HeteroData` from partition file."""
    return cluster_file_loader(g, cluster_file, batch_size=batch_size, shuffle=shuffle)
