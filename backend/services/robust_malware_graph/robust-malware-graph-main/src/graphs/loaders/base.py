"""
src.graphs.loaders.base  (PyG 버전)
==================================
GraphLoaderBase ‣ 원시 파일 또는 바이너리를
torch_geometric.data.(Data|HeteroData) 로 변환하는 추상 클래스.

• 공통 기능
  ├─ 글로벌 레지스트리  (register_loader / get_loader)
  ├─ 캐싱(*.pyg.pkl)   – SHA256(src) 로 key 생성
  ├─ 로깅 / 진행률 / 타이머
  └─ after_parse() 훅  – 선택적 후처리

서브클래스 작성 예
-----------------
@register_loader("cfg")
class CFGLoader(GraphLoaderBase):
    def _parse(self, src, **kw) -> Data:
        js = json.loads(Path(src).read_text())
        edge_index = torch.tensor(js["edges"]).t().contiguous()   # shape [2, E]
        x          = torch.tensor(js["node_feat"], dtype=torch.float)
        return Data(x=x, edge_index=edge_index)
"""

from __future__ import annotations

import abc
import hashlib
import logging
import pickle
import random
from pathlib import Path
from typing import Any, Dict, Optional, Type, Union

import numpy as np
import torch
from torch_geometric.data import Data, HeteroData

from contextlib import nullcontext

from ..utils import ensure_dir, get_logger, timer

# 타입 별칭 (Python ≥3.10)
GraphT = Union[Data, HeteroData]

# --------------------------------------------------------------------------- #
# 1. 글로벌 레지스트리
# --------------------------------------------------------------------------- #
_LOADER_REGISTRY: Dict[str, Type["GraphLoaderBase"]] = {}


def register_loader(name: str):
    """`@register_loader("cfg")` 식으로 로더 등록."""
    def _decorator(cls: Type["GraphLoaderBase"]):
        if name in _LOADER_REGISTRY:
            raise KeyError(f"Loader '{name}' already exists")
        _LOADER_REGISTRY[name] = cls
        cls.LOADER_NAME = name
        return cls
    return _decorator


def _lookup_loader(name: str) -> Type["GraphLoaderBase"]:
    try:
        return _LOADER_REGISTRY[name]
    except KeyError as e:
        raise ValueError(f"Unknown loader '{name}'") from e


# --------------------------------------------------------------------------- #
# 2. Base Loader (PyG)
# --------------------------------------------------------------------------- #
class GraphLoaderBase(abc.ABC):
    """
    Parameters
    ----------
    cache_dir : Path | None
        캐시 경로 (None ⇒ 캐시 비활성화)
    force_reload : bool, default False
        True 이면 캐시 무시
    """

    LOADER_NAME: str = "base"

    def __init__(
        self,
        cache_dir: Optional[Path] = None,
        *,
        force_reload: bool = False,
        log_level: int = logging.INFO,
    ) -> None:
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.force_reload = force_reload
        self.log = get_logger(f"loader.{self.LOADER_NAME}", log_level)
        if self.cache_dir:
            ensure_dir(self.cache_dir)

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    def load(self, src: str | Path | bytes, **kwargs) -> GraphT:
        """
        Returns
        -------
        torch_geometric.data.Data | HeteroData
        """
        cache_path = self._cache_path(src) if self.cache_dir else None

        # (1) 캐시 Hit
        if cache_path and cache_path.is_file() and not self.force_reload:
            self.log.debug("→ cache %s", cache_path.name)
            with cache_path.open("rb") as f:
                return pickle.load(f)

        # (2) 새로 파싱
        parse_ctx = (
            timer(
                f"{self.LOADER_NAME} parse",
                logger=self.log,
                use_tqdm=False,
            )
            if self.log.isEnabledFor(logging.DEBUG)
            else nullcontext()
        )
        with parse_ctx:
            g = self._parse(src, **kwargs)

        # (3) post-process
        g = self.after_parse(g)

        # (4) 캐시 저장
        if cache_path:
            with cache_path.open("wb") as f:
                pickle.dump(g, f, protocol=pickle.HIGHEST_PROTOCOL)

        return g

    # ------------------------------------------------------------------ #
    # Hooks
    # ------------------------------------------------------------------ #
    @abc.abstractmethod
    def _parse(self, src: str | Path | bytes, **kwargs) -> GraphT:  # noqa: N802
        """**MUST** → raw → PyG Graph(Data/HeteroData)."""
        raise NotImplementedError

    def after_parse(self, g: GraphT) -> GraphT:  # noqa: D401
        """필요하면 서브클래스에서 오버라이드."""
        return g

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #
    def _cache_path(self, src: str | Path | bytes) -> Path:
        """파일·바이트 SHA256 → `<hash>.pyg.pkl`"""
        if isinstance(src, (str, Path)):
            key = hashlib.sha256(str(Path(src).absolute()).encode()).hexdigest()
        else:
            key = hashlib.sha256(src).hexdigest()
        return self.cache_dir / f"{key}.pyg.pkl"  # type: ignore[operator]


# --------------------------------------------------------------------------- #
# 3. public factory (import-friendly)
# --------------------------------------------------------------------------- #
def get_loader(name: str, **kwargs) -> GraphLoaderBase:
    """
    Examples
    --------
    >>> loader = get_loader("ast", cache_dir=Path('~/.cache/ast').expanduser())
    >>> graph  = loader.load("/path/code.json")
    """
    cls = _lookup_loader(name)
    return cls(**kwargs)  # type: ignore[return-value]
