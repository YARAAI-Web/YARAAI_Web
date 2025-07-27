"""
src.graphs.features.token_embedder
==================================

TokenEmbedder
-------------
BPE(SentencePiece) + Word2Vec(옵션) 기반 토큰 임베딩 유틸리티.

기능 요약
---------
• train_bpe(corpus, vocab_size)           : *.model / *.vocab 학습
• encode(tokens|string)  → List[int]      : BPE 토큰 ID 시퀀스
• embed(tokens|string)   → Tensor[N, D]   : Word2Vec or 학습가능 nn.Embedding
• cache 와 연동          → Feather/Parquet 로 ∑ 토큰 임베딩 저장/로드

외부 종속
---------
pip install sentencepiece gensim pyarrow
"""

from __future__ import annotations

import functools
import logging
import re
import subprocess
from pathlib import Path
from typing import Iterable, List, Optional, Sequence

import gensim.downloader as api
import numpy as np
import sentencepiece as spm
import torch
import torch.nn as nn

from ..utils import ensure_dir, get_logger
from .cache import FeatureCache

# --------------------------------------------------------------------------- #
# 설정 / 상수
# --------------------------------------------------------------------------- #
_LOG = get_logger("features.token")
_TOKEN_PAT = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")  # C-style identifier
_DEFAULT_VEC = "glove-wiki-gigaword-100"            # gensim 모델 이름
_CACHE = FeatureCache(Path("~/.cache/token_embed"))


# --------------------------------------------------------------------------- #
# 메인 클래스
# --------------------------------------------------------------------------- #
class TokenEmbedder:
    """
    Parameters
    ----------
    bpe_model : Path | None
        .model 경로. None → BPE 를 사용하지 않고 whitespace split 만.
    w2v_name_or_path : str | Path | None
        Gensim key-vector 이름 or 로컬 경로(bin/vec). None → 학습가능 Embedding.
    trainable_dim : int, default 64
        w2v 가 없을 때 nn.Embedding(in_vocab, dim) 초기화용.
    """

    def __init__(
        self,
        *,
        bpe_model: Optional[Path] = None,
        w2v_name_or_path: Optional[str | Path] = _DEFAULT_VEC,
        trainable_dim: int = 64,
    ) -> None:
        self.log = _LOG
        self.sp: Optional[spm.SentencePieceProcessor] = None
        if bpe_model is not None:
            self.sp = spm.SentencePieceProcessor(model_file=str(bpe_model))
            self.pad_id = self.sp.pad_id()
        else:
            self.pad_id = 0  # whitespace split → BOS padding 없음

        # ---- Word2Vec or nn.Embedding --------------------------------
        if w2v_name_or_path is None:
            self._vec = None
            self._trainable = nn.Embedding(512, trainable_dim)  # 작은 디폴트 vocab
            self.dim = trainable_dim
        else:
            self._trainable = None
            self._vec = self._load_word2vec(w2v_name_or_path)
            self.dim = self._vec.vector_size  # type: ignore[attr-defined]

    # ================================================================= #
    # BPE 학습 & 인코딩
    # ================================================================= #
    @staticmethod
    def train_bpe(
        corpus_files: Sequence[Path],
        model_prefix: Path,
        *,
        vocab_size: int = 8_000,
        character_coverage: float = 0.9995,
    ) -> Path:
        """
        SentencePiece BPE 모델 학습. 결과: <prefix>.model / .vocab.

        Returns
        -------
        Path : 학습된 .model 파일 경로
        """
        input_arg = ",".join(str(p) for p in corpus_files)
        cmd = [
            "spm_train",
            f"--input={input_arg}",
            f"--model_prefix={model_prefix}",
            f"--vocab_size={vocab_size}",
            f"--character_coverage={character_coverage}",
            "--model_type=bpe",
            "--unk_id=1",
            "--pad_id=0",
            "--bos_id=-1",
            "--eos_id=-1",
        ]
        _LOG.info("Training BPE: %s", " ".join(cmd))
        subprocess.run(cmd, check=True)  # noqa: S603,S607
        return model_prefix.with_suffix(".model")

    # ----------------------------------------------------------------- #
    def encode(self, tokens: str | Sequence[str]) -> List[int]:
        """
        토큰/문자열 → BPE(or whitespace) ID 시퀀스. (PAD=0)
        """
        if isinstance(tokens, str):
            toks = _TOKEN_PAT.findall(tokens)
        else:
            toks = list(tokens)

        if self.sp is not None:
            # flatten sequence-of-strings to ids
            ids: List[int] = []
            for t in toks:
                ids.extend(self.sp.encode(t, out_type=int, add_bos=False, add_eos=False))
            return ids or [self.pad_id]

        # whitespace fallback
        return [hash(t) % 50_000 + 2 for t in toks] or [self.pad_id]

    # ================================================================= #
    # 임베딩 룩업
    # ================================================================= #
    def embed(self, tokens: str | Sequence[str]) -> torch.Tensor:
        """
        토큰/문자열 → 임베딩 Tensor [len(ids), dim].
        """
        ids = self.encode(tokens)

        # ---------- Word2Vec (정적) -------------------
        if self._vec is not None:
            vecs = [self._vec.get_vector(str(i)) if str(i) in self._vec else np.zeros(self.dim) for i in ids]  # type: ignore[attr-defined]
            return torch.tensor(vecs, dtype=torch.float32)

        # ---------- Trainable -------------------------
        ids_t = torch.tensor(ids, dtype=torch.long)
        # grow embedding table if needed
        if ids_t.max().item() >= self._trainable.num_embeddings:  # type: ignore[arg-type]
            new_size = int(ids_t.max().item() * 1.2)
            self._expand_trainable(new_size)
        return self._trainable(ids_t)

    # ================================================================= #
    # 캐시 I/O (옵션)
    # ================================================================= #
    def cache_embeddings(self, key: str, tokens: Sequence[str]) -> torch.Tensor:
        """
        • FeatureCache 에 (key) 저장 / 이미 있으면 로드.
        • Feather 포맷(default) 사용.
        """
        try:
            return _CACHE.load(key)
        except FileNotFoundError:
            emb = self.embed(tokens)
            _CACHE.save(key, emb)
            return emb

    # ================================================================= #
    # 내부 헬퍼
    # ================================================================= #
    @staticmethod
    def _load_word2vec(name_or_path: str | Path):
        """
        • gensim-data tag(glove-wiki-gigaword-100 등) or
        • 로컬 .bin / .vec / .kv path 지원.
        """
        p = Path(name_or_path)
        if p.exists():
            _LOG.info("Loading local w2v: %s", p)
            return api.load(str(p)) if p.is_dir() else api.load(str(p))
        _LOG.info("Downloading gensim model: %s", name_or_path)
        return api.load(name_or_path)

    def _expand_trainable(self, new_size: int) -> None:
        """
        임베딩 테이블 단순 확장 (random normal init).
        """
        old_weight = self._trainable.weight.data  # type: ignore[attr-defined]
        dim = self._trainable.embedding_dim      # type: ignore[attr-defined]
        self._trainable = nn.Embedding(new_size, dim)
        self._trainable.weight.data[: old_weight.size(0)] = old_weight
        nn.init.normal_(self._trainable.weight.data[old_weight.size(0) :], std=0.02)
        self.log.info("Expanded trainable embedding → %d rows", new_size)
