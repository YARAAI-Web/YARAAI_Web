"""
src.graphs.features.opcode_embedder
===================================

OpcodeEmbedder
--------------
• Opcode2Vec(gensim Word2Vec)  또는  nn.Embedding(trainable) 기반
• train(corpus)   →  *.bin 임베딩 모델 학습 & 저장
• embed(seq)      →  Tensor[N, D] (opcode-level) or Tensor[D] (sequence pool)
• FeatureCache 연동 (Feather/Parquet)

권장 전처리
-----------
▸ objdump / radare2 / Ghidra 로 disasm → 공백 기준 opcode 토큰 시퀀스 생성
▸ push, mov, xor 등 **mnemonic 단위**  (피연산자 제외)
"""

from __future__ import annotations

import itertools
import logging
import subprocess
from pathlib import Path
from typing import Iterable, List, Optional, Sequence

import gensim
import numpy as np
import torch
import torch.nn as nn
from gensim.models import Word2Vec

from ..utils import ensure_dir, get_logger
from .cache import FeatureCache

# --------------------------------------------------------------------------- #
# 설정 / 전역
# --------------------------------------------------------------------------- #
_LOG = get_logger("features.opcode")
_CACHE = FeatureCache(Path("~/.cache/opcode_embed"))

# --------------------------------------------------------------------------- #
# 학습 유틸
# --------------------------------------------------------------------------- #
def train_opcode2vec(
    corpus_paths: Sequence[Path],
    out_path: Path,
    *,
    vector_size: int = 128,
    window: int = 5,
    min_count: int = 3,
    workers: int = 4,
    epochs: int = 10,
) -> Path:
    """
    opcode 뉴럴 임베딩 모델 학습(Gensim Word2Vec + SG).

    Parameters
    ----------
    corpus_paths : list[Path]
        줄당 opcode 토큰 시퀀스로 이뤄진 *.txt 파일들.
    out_path : Path
        *.bin 저장 경로 (디렉터리면 <dir>/opcode2vec.bin 자동).
    """
    out_path = Path(out_path)
    if out_path.is_dir():
        out_path = out_path / "opcode2vec.bin"
    ensure_dir(out_path.parent)

    def _sentences() -> Iterable[List[str]]:
        for p in corpus_paths:
            with p.open() as f:
                for line in f:
                    yield line.strip().split()

    _LOG.info("Training Opcode2Vec on %d corpus file(s)…", len(corpus_paths))
    model = Word2Vec(
        sentences=_sentences(),
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=1,  # Skip-gram
        workers=workers,
        epochs=epochs,
    )
    model.wv.save_word2vec_format(out_path, binary=True)
    _LOG.info("Saved Opcode2Vec → %s (vocab=%d)", out_path.name, len(model.wv))
    return out_path


# --------------------------------------------------------------------------- #
# 메인 클래스
# --------------------------------------------------------------------------- #
class OpcodeEmbedder:
    """
    Parameters
    ----------
    model_bin : Path | None
        Word2Vec binary 파일(*.bin).  None → 학습가능 Embedding 사용.
    trainable_dim : int, default 64
        Word2Vec 모델이 없을 때 nn.Embedding 초기화 크기.
    """

    def __init__(self, *, model_bin: Optional[Path] = None, trainable_dim: int = 64):
        self.log = _LOG

        if model_bin is None:
            self.w2v = None
            self.dim = trainable_dim
            self._trainable = nn.Embedding(1024, trainable_dim)  # 초기 1k opcode
        else:
            self.log.info("Loading Opcode2Vec: %s", model_bin)
            self.w2v = gensim.models.KeyedVectors.load_word2vec_format(str(model_bin), binary=True)
            self.dim = self.w2v.vector_size
            self._trainable = None

        # UNK / PAD 처리
        self.pad_tok = "<pad>"
        self.unk_tok = "<unk>"

        if self.w2v is not None and self.pad_tok not in self.w2v:
            pad_vec = np.zeros(self.dim, dtype=np.float32)
            self.w2v.add_vectors([self.pad_tok], [pad_vec])

    # ====================================================================== #
    # 인코딩 & 임베딩
    # ====================================================================== #
    def encode(self, opcodes: Sequence[str]) -> List[int]:
        """
        opcode 문자열 리스트 → 정수 시퀀스 (Word2Vec index or running hash).
        """
        if self.w2v is not None:
            idxs = []
            for op in opcodes:
                if op in self.w2v:
                    idxs.append(self.w2v.key_to_index[op])
                else:
                    idxs.append(self.w2v.key_to_index.get(self.unk_tok, 0))
            return idxs or [self.w2v.key_to_index[self.pad_tok]]
        # trainable path – simple hash bucket
        return [hash(op) % (self._trainable.num_embeddings - 2) + 2 for op in opcodes] or [0]

    def embed(self, opcodes: Sequence[str]) -> torch.Tensor:
        """
        입력 opcode 시퀀스를 임베딩 행렬 `[len(seq), dim]` 로 변환.
        """
        if self.w2v is not None:
            vecs = [self.w2v[op] if op in self.w2v else np.zeros(self.dim) for op in opcodes]
            return torch.tensor(vecs or [np.zeros(self.dim)], dtype=torch.float32)

        idx = torch.tensor(self.encode(opcodes), dtype=torch.long)
        # grow table on demand
        if idx.max().item() >= self._trainable.num_embeddings:  # type: ignore[arg-type]
            self._expand_trainable(int(idx.max().item() * 1.2))
        return self._trainable(idx)  # type: ignore[operator]

    # 시퀀스 풀링 편의
    def embed_pool(self, opcodes: Sequence[str], *, mode: str = "mean") -> torch.Tensor:
        """
        opcode 시퀀스 → 고정 크기 [dim] 벡터. mode={'mean','sum','max'}.
        """
        mat = self.embed(opcodes)
        if mode == "mean":
            return mat.mean(dim=0)
        if mode == "sum":
            return mat.sum(dim=0)
        if mode == "max":
            return mat.max(dim=0).values
        raise ValueError(f"Unknown pool mode '{mode}'")

    # ====================================================================== #
    # 캐시 I/O
    # ====================================================================== #
    def cache_embed_pool(self, key: str, opcodes: Sequence[str], *, mode: str = "mean"):
        """FeatureCache 기반 디스크 캐시."""
        try:
            return _CACHE.load(key)
        except FileNotFoundError:
            vec = self.embed_pool(opcodes, mode=mode)
            _CACHE.save(key, vec.unsqueeze(0))  # Feather 2-D 필요
            return vec

    # ====================================================================== #
    # 내부
    # ====================================================================== #
    def _expand_trainable(self, new_size: int) -> None:
        old_w = self._trainable.weight.data  # type: ignore[attr-defined]
        dim = old_w.shape[1]
        self._trainable = nn.Embedding(new_size, dim)
        self._trainable.weight.data[: old_w.size(0)] = old_w
        nn.init.normal_(self._trainable.weight.data[old_w.size(0) :], std=0.02)
        self.log.info("Expand trainable opcode table → %d", new_size)
