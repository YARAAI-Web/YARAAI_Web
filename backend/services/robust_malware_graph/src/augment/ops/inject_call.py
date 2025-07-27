"""
InjectAPICall (PyG)
===================
그래프에 **더미 API-Call 노드** k 개를 주입하여
· 시퀀스 길이 증가, · 호출 그래프 분산 등으로 모델을 혼동시키는 증강 연산.

필수 edge type
--------------
canonical etype = ('bb', 'calls', 'api')
(그래프에 node type 'api' 가 없어도 동적으로 추가됩니다)
"""

from __future__ import annotations

import numbers
from typing import Any, List, Tuple

import logging
LOGGER = logging.getLogger(__name__)

import numpy as np
import torch
from torch_geometric.data import Data, HeteroData

from src.graphs.utils import sanitize_edge_index

from augment import register_op
from augment.base import SimpleAug, AugmentBase
from importlib import util as _import_util
from pathlib import Path

_schema_spec = _import_util.spec_from_file_location(
    "_schema", Path(__file__).resolve().parents[2] / "graphs" / "normalizers" / "schema.py"
)
_schema = _import_util.module_from_spec(_schema_spec)
assert _schema_spec and _schema_spec.loader
_schema_spec.loader.exec_module(_schema)
EDGE_REL_ID = _schema.EDGE_REL_ID
EdgeRel = _schema.EdgeRel


@register_op
class InjectAPICall(SimpleAug, AugmentBase):
    """Random API-Call injection operator for PyG graphs."""

    _DEFAULT_API_VOCAB: List[str] = [
        # Windows API 예시
        "CreateFileA",
        "ReadFile",
        "WriteFile",
        "VirtualAlloc",
        "LoadLibraryA",
        "GetProcAddress",
        "WinExec",
        "InternetOpenUrlA",
        "Socket",
        "Connect",
    ]

    DEFAULT_FEAT_DIM: int = 32

    def __init__(
        self,
        api_vocab: List[str] | None = None,
        k: int = 2,
        attach_strategy: str = "random_bb",
        feat_dim: int = DEFAULT_FEAT_DIM,
        seed: int | None = None,
        **kwargs: Any,
    ) -> None:
        # ── 인자 검증 ────────────────────────────────────────────────────
        if not isinstance(k, numbers.Integral) or k <= 0:
            raise ValueError("k must be a positive integer")
        if attach_strategy not in {"random_bb", "first_bb"}:
            raise ValueError("attach_strategy must be 'random_bb' or 'first_bb'")

        if not isinstance(feat_dim, numbers.Integral) or feat_dim <= 0:
            raise ValueError("feat_dim must be a positive integer")

        self.api_vocab = api_vocab or self._DEFAULT_API_VOCAB
        self.k = int(k)
        self.attach_strategy = attach_strategy
        self._rng = (
            np.random.RandomState(seed)
            if seed is not None
            else np.random.RandomState()
        )
        self.feat_dim = int(feat_dim)

        super().__init__(
            api_vocab=self.api_vocab,
            k=self.k,
            attach_strategy=self.attach_strategy,
            seed=seed,
            feat_dim=self.feat_dim,
            **kwargs,
        )

    # ------------------------------------------------------------------ #
    # AugmentBase 인터페이스                                             #
    # ------------------------------------------------------------------ #
    def __call__(self, g: Data | HeteroData) -> Data | HeteroData:  # type: ignore[override]
        """
        Returns
        -------
        torch_geometric.data.Data | HeteroData
            Dummy API 노드가 주입된 **새 그래프** (원본과 동일 device).
        """
        LOGGER.debug(
            "InjectAPICall: start | k=%d attach_strategy=%s", self.k, self.attach_strategy
        )
        sg = g.clone()  # 구조 공유 + feature 딥 카피

        if isinstance(sg, Data):
            self._inject_api_homo(sg)
        elif isinstance(sg, HeteroData):
            if "bb" not in sg.node_types:
                return sg  # bb 노드가 없으면 증강 불가
            self._inject_api_hetero(sg)
        else:  # pragma: no cover
            raise TypeError(
                "InjectAPICall supports torch_geometric Data or HeteroData, "
                f"got {type(sg)}"
            )

        LOGGER.debug("InjectAPICall: end")
        return sg

    # ================================================================== #
    #                          homogeneous Data                          #
    # ================================================================== #
    def _inject_api_homo(self, data: Data) -> None:
        device = self._pick_device(data)
        before = data.num_nodes

        num_bb = data.num_nodes
        if num_bb == 0:
            return

        bb_indices = self._choose_bb_indices(num_bb, device)

        # (1) 노드 추가 ----------------------------------------------------------------
        new_api_idx = torch.arange(num_bb, num_bb + self.k, device=device)
        data.num_nodes = num_bb + self.k  # PyG 2.x : 수동 갱신

        # 노드 특성이 있으면 0-벡터로 패딩
        for key, feat in list(data.items()):
            if torch.is_tensor(feat) and feat.size(0) == num_bb:
                pad_shape = list(feat.shape)
                pad_shape[0] = self.k
                data[key] = torch.cat(
                    [feat, torch.zeros(pad_shape, dtype=feat.dtype, device=device)],
                    dim=0,
                )

        # 새 특성: api_name / dummy_feat
        api_name_feat, dummy_feat = self._make_new_node_feats(device)
        data.api_name = api_name_feat
        data.dummy_feat = dummy_feat
        if "x" in data:
            data.x = torch.cat([data.x, dummy_feat], dim=0)
        else:
            pad = torch.zeros(num_bb, dummy_feat.size(1), dtype=dummy_feat.dtype, device=device)
            data.x = torch.cat([pad, dummy_feat], dim=0)

        # (2) 엣지 추가 ----------------------------------------------------------------
        new_edges = torch.stack([bb_indices, new_api_idx], dim=0)
        if "edge_index" in data:
            data.edge_index = torch.cat([data.edge_index, new_edges], dim=1)
        else:
            data.edge_index = new_edges

        # sanitize edges and warn if any were dropped
        before_e = data.edge_index.size(1)
        sanitize_edge_index(data, src_nodes=data.num_nodes, dst_nodes=data.num_nodes)
        after_e = data.edge_index.size(1)
        if after_e < before_e:
            logging.warning(
                "InjectAPICall filtered %d out-of-range edges", before_e - after_e
            )

        LOGGER.debug(
            "InjectAPICall(homo): nodes %d -> %d", before, data.num_nodes
        )

    # ================================================================== #
    #                        heterogeneous HeteroData                     #
    # ================================================================== #
    def _inject_api_hetero(self, data: HeteroData) -> None:
        device = self._pick_device(data["bb"])

        # (1) target bb 노드 선택
        num_bb = data["bb"].num_nodes
        if not num_bb:
            return
        bb_indices = self._choose_bb_indices(num_bb, device)

        # (2) API 노드 추가 ------------------------------------------------------------
        api_store = data["api"]
        if "api" in data.node_types and api_store.num_nodes is not None:
            old_api_n = api_store.num_nodes
        else:
            old_api_n = 0
        new_api_idx = torch.arange(old_api_n, old_api_n + self.k, device=device)

        # 새 노드 수 등록 (특성이 없더라도 반드시 num_nodes 지정)
        api_store.num_nodes = old_api_n + self.k

        # 기존 특성 0-패딩
        for key, feat in list(api_store.items()):
            if torch.is_tensor(feat) and feat.size(0) == old_api_n:
                pad_shape = list(feat.shape)
                pad_shape[0] = self.k
                api_store[key] = torch.cat(
                    [feat, torch.zeros(pad_shape, dtype=feat.dtype, device=device)],
                    dim=0,
                )

        # 새 특성 저장
        api_name_feat, dummy_feat = self._make_new_node_feats(device)
        if "api_name" in api_store:
            api_store["api_name"] = torch.cat([api_store["api_name"], api_name_feat], 0)
            api_store["dummy_feat"] = torch.cat([api_store["dummy_feat"], dummy_feat], 0)
            if "x" in api_store:
                api_store["x"] = torch.cat([api_store["x"], dummy_feat], 0)
        else:
            api_store["api_name"] = api_name_feat
            api_store["dummy_feat"] = dummy_feat
            api_store["x"] = dummy_feat

        # (3) 엣지 추가 ---------------------------------------------------------------
        etype: Tuple[str, str, str] = ("bb", "calls", "api")
        edge_store = data[etype]

        new_edges = torch.stack([bb_indices, new_api_idx], dim=0)
        if "edge_index" in edge_store:
            edge_store.edge_index = torch.cat([edge_store.edge_index, new_edges], dim=1)
        else:
            edge_store.edge_index = new_edges
        # edge_type 업데이트
        new_types = torch.full(
            (new_edges.size(1),),
            EDGE_REL_ID[EdgeRel.CALLS.value],
            dtype=torch.long,
            device=device,
        )
        if "edge_type" in edge_store:
            edge_store.edge_type = torch.cat([edge_store.edge_type, new_types])
        else:
            edge_store.edge_type = new_types

        # sanitize edges and warn if any were dropped
        before_e = edge_store.edge_index.size(1)
        sanitize_edge_index(
            edge_store,
            src_nodes=data["bb"].num_nodes or 0,
            dst_nodes=api_store.num_nodes or 0,
        )
        after_e = edge_store.edge_index.size(1)
        if after_e < before_e:
            logging.warning(
                "InjectAPICall filtered %d out-of-range edges", before_e - after_e
            )
        LOGGER.debug(
            "InjectAPICall(hetero): api nodes %d -> %d", old_api_n, api_store.num_nodes
        )

    # ================================================================== #
    #                               utils                                #
    # ================================================================== #
    def _pick_device(self, store: Any) -> torch.device:
        """store(노드/엣지)의 첫 tensor device 반환 – 없으면 CPU."""
        for val in store.values():
            if torch.is_tensor(val):
                return val.device
        return torch.device("cpu")

    def _choose_bb_indices(self, num_bb: int, device: torch.device) -> torch.Tensor:
        """attach_strategy에 따라 기본 블록(bb) 노드 index 선택."""
        if self.attach_strategy == "random_bb":
            idx = self._rng.randint(0, num_bb, size=self.k)
        else:  # 'first_bb'
            idx = np.zeros(self.k, dtype=np.int64)
        return torch.as_tensor(idx, device=device, dtype=torch.long)

    def _make_new_node_feats(self, device: torch.device) -> Tuple[torch.Tensor, torch.Tensor]:
        """api_name(string 또는 long) & dummy_feat(float32) 생성."""
        api_names = self._rng.choice(self.api_vocab, size=self.k, replace=True)

        # Torch string 지원 여부 확인 (>=1.12) → 미지원 시 int index로 저장
        try:
            dummy = torch.tensor(["a"])
            is_string_supported = dummy.dtype.name == "torch.string"  # type: ignore[attr-defined]
        except Exception:
            is_string_supported = False

        if is_string_supported:
            api_name_feat = torch.tensor(list(api_names), dtype=torch.string, device=device)  # type: ignore[attr-defined]
        else:
            vocab2idx = {n: i for i, n in enumerate(self.api_vocab)}
            api_name_feat = torch.as_tensor(
                [vocab2idx[n] for n in api_names], dtype=torch.long, device=device
            )

        dummy_feat = torch.zeros(
            self.k, self.feat_dim, dtype=torch.float32, device=device
        )
        return api_name_feat, dummy_feat
