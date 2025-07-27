"""
ObfuscPatch (PyG)
=================
CFG 엣지(u → v) 중 일부에 **Junk Basic-Block** 노드를 삽입하여
u → junk → v 경로로 치환(또는 추가)하는 난독화 증강.

전제
-----
* `data`는 `torch_geometric.data.HeteroData` 타입
* 노드 타입 `'bb'`, 엣지 타입 `('bb','cfg','bb')` 존재

Parameters
----------
insert_ratio : float   – 삽입할 CFG 엣지 비율(0 < r ≤ 1)
remove_original : bool – True → u→v 엣지 삭제, False → 유지
junk_feat_dim : int|None – 새 노드 `feat` 차원(None = 기존 `feat` 차원)
seed : int|None        – NumPy RNG 시드
"""
from __future__ import annotations

import math
import numbers
from typing import Any, Tuple

import numpy as np
import torch
from torch_geometric.data import HeteroData

from augment import register_op
from augment.base import SimpleAug, AugmentBase


@register_op
class ObfuscPatch(SimpleAug, AugmentBase):
    _ETYPE: Tuple[str, str, str] = ("bb", "cfg", "bb")

    # ------------------------------- init ------------------------------ #
    def __init__(
        self,
        insert_ratio: float = 0.1,
        remove_original: bool = False,
        junk_feat_dim: int | None = None,
        seed: int | None = None,
        **kwargs: Any,
    ):
        if (
            not isinstance(insert_ratio, numbers.Real)
            or not 0.0 < insert_ratio <= 1.0
        ):
            raise ValueError("insert_ratio must be in (0, 1].")
        self.insert_ratio = float(insert_ratio)
        self.remove_original = bool(remove_original)
        self.junk_feat_dim = junk_feat_dim
        self._rng = (
            np.random.RandomState(seed)
            if seed is not None
            else np.random.RandomState()
        )
        super().__init__(
            insert_ratio=self.insert_ratio,
            remove_original=self.remove_original,
            junk_feat_dim=self.junk_feat_dim,
            seed=seed,
            **kwargs,
        )

    # ----------------------------- __call__ ---------------------------- #
    def __call__(self, data: HeteroData) -> HeteroData:  # type: ignore[override]
        # 사전 조건 검사
        if (
            math.isclose(self.insert_ratio, 0.0)
            or "bb" not in data.node_types
            or self._ETYPE not in data.edge_types
        ):
            return data

        # 깊은 복사(원본 보존)
        g: HeteroData = data.clone()
        device = g.get("x_dict", {}).get("bb", torch.empty(0)).device

        # ---------- (1) 기존 CFG 엣지 ----------
        edge_index = g[self._ETYPE].edge_index  # shape (2,E)
        num_edges = edge_index.size(1)
        if num_edges == 0:
            return g

        # ---------- (2) 샘플링 ----------
        num_insert = max(1, int(num_edges * self.insert_ratio))
        sel_idx = self._rng.choice(num_edges, size=num_insert, replace=False)
        src_sel = edge_index[0, sel_idx]
        dst_sel = edge_index[1, sel_idx]

        # ---------- (3) junk 노드 feature ----------
        n_bb_orig = g["bb"].num_nodes
        feat_key = "feat" if "feat" in g["bb"] else None
        feat_dim = (
            self.junk_feat_dim
            if self.junk_feat_dim is not None
            else (g["bb"][feat_key].size(-1) if feat_key else 32)
        )

        # 기존 노드에 junk_flag 존재 여부 확인
        if "junk_flag" not in g["bb"]:
            g["bb"]["junk_flag"] = torch.zeros(
                n_bb_orig, 1, dtype=torch.bool, device=device
            )

        # 새 노드 feature / flag
        zero_feat = torch.zeros(num_insert, feat_dim, device=device)
        junk_flag = torch.ones(num_insert, 1, dtype=torch.bool, device=device)

        # (a) feat
        if feat_key:
            g["bb"][feat_key] = torch.cat([g["bb"][feat_key], zero_feat], dim=0)
        else:
            g["bb"]["feat"] = torch.cat(
                [torch.zeros(n_bb_orig, feat_dim, device=device), zero_feat], dim=0
            )
            feat_key = "feat"

        # (b) junk_flag
        g["bb"]["junk_flag"] = torch.cat([g["bb"]["junk_flag"], junk_flag], dim=0)

        # node 개수 갱신
        g["bb"].num_nodes = n_bb_orig + num_insert

        # ---------- (4) 엣지 업데이트 ----------
        # (i) 기존 edge 유지 여부
        keep_mask = torch.ones(num_edges, dtype=torch.bool, device=device)
        if self.remove_original:
            keep_mask[torch.as_tensor(sel_idx, device=device)] = False

        keep_edges = edge_index[:, keep_mask]

        # (ii) 신규 edge(u→junk, junk→v)
        new_ids = torch.arange(n_bb_orig, n_bb_orig + num_insert, device=device)
        new_src = torch.cat([src_sel, new_ids])
        new_dst = torch.cat([new_ids, dst_sel])
        new_edges = torch.stack([new_src, new_dst], dim=0)

        # (iii) 결합
        g[self._ETYPE].edge_index = torch.cat([keep_edges, new_edges], dim=1)

        # 엣지 속성(있다면) 제거 또는 맞춰주기 – 여기서는 삭제
        for key in list(g[self._ETYPE].keys()):
            if key != "edge_index":
                del g[self._ETYPE][key]

        return g
