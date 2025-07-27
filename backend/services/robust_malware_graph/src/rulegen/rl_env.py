#  ───────────────────────────────────────────────────────────────
#  robust-malware-graph / src / rulegen / rl_env.py
#  ───────────────────────────────────────────────────────────────
"""
PPO 학습용 RuleGenEnv
=====================

• 목적
    - 에이전트(`PPORuleAgent`)가 YARA/CAPA 룰을 **토큰 단위로 생성**하도록
      OpenAI Gym‑style(=Gymnasium) 환경을 제공한다.
    - **보상 함수**는 논문/스펙에 명시된 식을 1:1 그대로 구현.

          R = 0.5 · F1_clean
            + 0.4 · F1_dummy
            – 0.05 · rule_len_tokens
            + 0.05 · 𝟙{certified_r≥2}

• 핵심 의존
    - `torch_geometric.data.HeteroData` : 그래프 형태 데이터셋 로딩
    - `models.gnn.res_wrapper.RESGCLClassifier` : 인증 반경 r 평가
    - `evaluation.metrics.*` : AUROC / F1 / confusion matrix 등
    - `rulegen.feature_miner.FeatureMiner` : 어휘(토큰) 사전 제공
    - `rulegen.yara_builder`, `rulegen.capa_builder` : 토큰 → 룰 문자열

• 학습·추론 흐름
      reset()     → 초기 state (obs = EMPTY)
      step(a_t)   → 토큰 a_t append
        ├─ 룰 완성? (END 토큰 or max_len) ──┐
        └─────────── NO ───────────────────┘
        ┌────────── YES ────────────────────┐
        │ build_rule()  → evaluator()       │
        │ reward, done = True, obs = NULL   │
        └───────────────────────────────────┘
"""
from __future__ import annotations

import json
import logging
import random
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union

try:
    from transformers import PreTrainedTokenizer  # type: ignore
except Exception:  # pragma: no cover - optional dep
    PreTrainedTokenizer = None  # type: ignore
import re
import subprocess
import tempfile

try:
    import yara  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    yara = None

import gymnasium as gym
import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader  # use PyTorch loader to allow custom collate_fn
from torch_geometric.data import HeteroData

# ───────────────────────────── 프로젝트 모듈
try:
    from common.logger import get_logger  # type: ignore
except ModuleNotFoundError:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")

    def get_logger(name: str):
        return logging.getLogger(name)


from evaluation.rule_evaluator import RuleEvaluator  # type: ignore
from models.gnn.res_wrapper import RESGCLClassifier  # type: ignore
from models.gnn.encoder import RGCNEncoder  # type: ignore
from .feature_miner import FeatureMiner  # 단어 사전

_LOG = get_logger(__name__)


# ╔══════════════════════════════════════════════════════════════╗
# ║                       환경 정의                               ║
# ╚══════════════════════════════════════════════════════════════╝
class RuleGenEnv(gym.Env):
    """
    OpenAI Gym‑style PPO 환경.
    """

    metadata = {"render.modes": ["human"]}

    # Special token IDs will be appended to vocab at env init
    PAD, END = "<PAD>", "<END>"

    # ──────────────────────────────────────────────────────────
    def __init__(
        self,
        *,
        rule_type: str = "yara",  # or "capa"
        vocab_file: Optional[Union[str, Path]] = None,
        dataset_dir: Union[str, Path] = "data/splits",
        meta_path: Optional[Path] = None,
        attr_dim: int = 16,
        max_len: int = 180,
        batch_size_eval: int = 128,
        classifier_checkpoint: str | Path = "models/gnn/res_gcl.pt",
        device: str | torch.device = "cuda" if torch.cuda.is_available() else "cpu",
        classifier_device: str | torch.device = "cpu",
        seed: int = 2024,
        tokenizer: Optional[PreTrainedTokenizer] = None,
        hint_features: List[str] | None = None,
        max_hint_tokens: int | None = None,
        token_saliency: Dict[str, float] | None = None,
        step_penalty: float = -0.01,
        per_token_saliency: float = 0.02,
        normalize_reward: bool = False,
        core_tokens: Sequence[str] | None = None,
        use_shaping: bool = False,
        use_adv_perturb: bool = False,
        use_lookahead: bool = False,
        single_target_mode: bool = False,
        reward_weights: dict | None = None,
        fp_penalty_start: float = 0.01,
        fp_penalty_end: float = 0.5,
        fp_penalty_delay: int = 0,
        curriculum_steps: int = 20000,
        off_target_penalty: float = 0.25,
        off_target_penalty_start: float | None = None,
        off_target_penalty_end: float | None = None,
        off_target_steps: int | None = None,
        no_tp_penalty: float = 0.2,
        rule_len_penalty_start: float | None = None,
        rule_len_penalty_end: float | None = None,
        rule_len_steps: int | None = None,
        rule_len_penalty_delay: int = 0,
        improve_bonus: float = 0.1,
    ):
        """
        Parameters
        ----------
        rule_type        : "yara" | "capa"
        vocab_file       : 사전 json (토큰 → id) 경로; 없으면 FeatureMiner로 동적 생성
        dataset_dir      : time‑split train/val/test parquet 경로
        meta_path        : optional encoder meta snapshot (.meta.pkl)
        attr_dim         : metadata embedding dimension when reconfiguring encoder
        max_len          : 룰 최대 토큰 길이 (spec ≤ 512 제한 대비 여유)
        batch_size_eval  : 보상 산출 시 배치 추론 크기
        classifier_checkpoint  : 보상 계산용 분류기 체크포인트 경로
        device           : 모델/데이터 평가 디바이스
        classifier_device : 분류기 로드 및 추론에 사용할 디바이스
        seed             : reproducibility
        tokenizer        : HuggingFace tokenizer to extend with rule tokens
        hint_features    : 초기 관측에 포함할 토큰 문자열 시퀀스
        max_hint_tokens  : 힌트 토큰 최대 길이. ``None``이면 기본 힌트 길이를 사용
                          GPT 토크나이저가 주어지면 ``max_len + max_hint_tokens``
                          가 ``tokenizer.model_max_length`` (기본 1024) 을
                          넘지 않도록 자동 조정된다
        token_saliency   : 토큰별 중요도 가중치 딕셔너리
        step_penalty     : 매 스텝 적용할 패널티 (e.g. ``-0.01``)
        per_token_saliency : 선택한 토큰 saliency 가중치 배율
        normalize_reward : ``True``면 보상을 평균 0, 표준편차 1로 표준화해 반환
        core_tokens      : shaping potential 계산에 사용할 핵심 토큰 시퀀스
        use_shaping      : ``True``면 potential based reward shaping 활성화
        use_lookahead   : ``True``면 룰 미완성 시 분류기 확률을 임시 보상으로 사용
        single_target_mode : ``True``면 매 에피소드 하나의 더미 그래프를 무작위 선택해 해당 특성 토큰을 힌트로 제공
        reward_weights   : F1/길이/인증 보상 가중치 딕셔너리
        fp_penalty_start : 초기 False Positive 패널티 배율
        fp_penalty_end   : curriculum_steps 소모 후 적용할 배율
        fp_penalty_delay : 일정 스텝 동안 FP 패널티를 적용하지 않음
        curriculum_steps : 패널티 스케줄 총 스텝 수
        off_target_penalty : single_target_mode 시 비표적 매치 1건당 패널티
        off_target_penalty_start : 오프 타깃 패널티 초기 가중치
        off_target_penalty_end   : off_target_steps 소모 후 적용할 가중치
        off_target_steps : 오프 타깃 패널티 스케줄 총 스텝 수
        no_tp_penalty : TP가 0일 때 부여할 패널티 크기
        rule_len_penalty_start : rule_len 패널티 초기 가중치 (기본 reward_weights['rule_len'])
        rule_len_penalty_end   : rule_len_steps 소모 후 적용할 가중치
        rule_len_steps : rule_len 패널티 스케줄 총 스텝 수
        rule_len_penalty_delay : 일정 스텝 이후부터 rule_len 패널티 스케줄 적용
        """
        super().__init__()
        torch.manual_seed(seed)
        random.seed(seed)
        np.random.seed(seed)
        self.attr_dim = int(attr_dim)

        self.rule_type = rule_type.lower()
        assert self.rule_type in {"yara", "capa"}

        # ── Vocabulary & tokenizer ────────────────────────────
        if vocab_file is None:
            if hint_features:
                self.token2id = {
                    tok: i for i, tok in enumerate(sorted(set(hint_features)))
                }
                vocab_file = Path(dataset_dir) / "rule_vocab.json"
                with open(vocab_file, "w") as f:
                    json.dump(self.token2id, f, ensure_ascii=False, indent=2)
                _LOG.info(
                    "Saved vocab (%d tokens) from hint_features → %s",
                    len(self.token2id),
                    vocab_file,
                )
            else:
                _LOG.info("Vocab file not provided → mining from train split …")
                vocab_file = self._build_vocab(Path(dataset_dir) / "train")
                with Path(vocab_file).open() as fp:
                    self.token2id: Dict[str, int] = json.load(fp)
        else:
            with Path(vocab_file).open() as fp:
                self.token2id: Dict[str, int] = json.load(fp)

        # 특수 토큰 추가
        self.token2id.setdefault(self.PAD, len(self.token2id))
        self.token2id.setdefault(self.END, len(self.token2id))

        if tokenizer is not None:
            self.tokenizer = tokenizer
            tokenizer.add_special_tokens({"pad_token": self.PAD, "eos_token": self.END})
            existing = set(tokenizer.get_vocab().keys())
            new_tokens = [t for t in self.token2id if t not in existing]
            if new_tokens:
                tokenizer.add_tokens(new_tokens)
            self.token2id = tokenizer.get_vocab()
        else:
            self.tokenizer = None

        self.id2token = {i: t for t, i in self.token2id.items()}
        self.vocab_size = len(self.token2id)
        self.max_len = max_len
        self._orig_max_len = max_len

        # categorize tokens for action masking
        self._colon_id = self.token2id.get(":")
        self._string_token_ids = {
            tid
            for tok, tid in self.token2id.items()
            if (
                len(tok) >= 2
                and (
                    (tok[0] == '"' and tok[-1] == '"')
                    or (tok[0] == "'" and tok[-1] == "'")
                )
            )
        }
        self._number_token_ids = {
            tid
            for tok, tid in self.token2id.items()
            if re.fullmatch(r"[0-9A-Fa-f]+", tok)
        }
        _punct = {":", ".", ",", ";", "(", ")", "[", "]", "{", "}"}
        self._punct_token_ids = {
            tid for tok, tid in self.token2id.items() if tok in _punct
        }
        self._number_token_strings = {self.id2token[i] for i in self._number_token_ids}

        # token saliency weights
        self.token_saliency = token_saliency or {}
        self.step_penalty = step_penalty
        self.per_token_saliency = per_token_saliency
        self.normalize_reward = normalize_reward

        default_weights = {
            "f1_clean": 0.5,
            "f1_dummy": 0.4,
            "rule_len": -0.02,
            "certified_bonus": 0.1,
        }
        self.reward_weights = default_weights | (reward_weights or {})

        # running reward statistics
        from common.running_stats import RunningStats

        self.running_stats = RunningStats()

        # rule evaluation logging
        self.rule_eval_history: List[dict] = []
        self.rule_eval_callback: Optional[
            Callable[[str, dict], None]
        ] = None
        self._max_history = 1000

        self.core_tokens = set(core_tokens or [])
        self.use_shaping = use_shaping
        self.use_lookahead = bool(use_lookahead)
        self._phi_last = 0.0
        self._episode_steps = 0
        self.gamma = 0.99
        self.use_adv_perturb = bool(use_adv_perturb)

        self.fp_penalty_start = float(fp_penalty_start)
        self.fp_penalty_end = float(fp_penalty_end)
        self.fp_penalty_delay = int(fp_penalty_delay)
        self.curriculum_steps = max(1, int(curriculum_steps))
        self.off_target_penalty_start = (
            float(off_target_penalty)
            if off_target_penalty_start is None
            else float(off_target_penalty_start)
        )
        self.off_target_penalty_end = (
            float(off_target_penalty)
            if off_target_penalty_end is None
            else float(off_target_penalty_end)
        )
        self.off_target_steps = max(
            1,
            int(off_target_steps if off_target_steps is not None else self.curriculum_steps),
        )
        self.no_tp_penalty = float(no_tp_penalty)
        self.total_steps = 0

        self.improve_bonus = float(improve_bonus)
        self.prev_f1_dummy = 0.0

        self.rule_len_penalty_start = (
            float(self.reward_weights["rule_len"]) if rule_len_penalty_start is None else float(rule_len_penalty_start)
        )
        self.rule_len_penalty_end = (
            float(self.reward_weights["rule_len"]) if rule_len_penalty_end is None else float(rule_len_penalty_end)
        )
        self.rule_len_steps = max(1, int(rule_len_steps if rule_len_steps is not None else self.curriculum_steps))
        self.rule_len_penalty_delay = int(rule_len_penalty_delay)

        # Hint features / tokens
        self.hint_features = hint_features or []
        self._default_hint_tokens: List[int] = []
        for feat in self.hint_features:
            for tok in self._rule_tokenize(feat):
                tok_id = self.token2id.get(tok)
                if tok_id is not None:
                    self._default_hint_tokens.append(tok_id)

        # defer max_hint_tokens calculation until after target features are loaded
        self.max_hint_tokens = int(max_hint_tokens) if max_hint_tokens is not None else len(self._default_hint_tokens)

        self._hint_tokens: List[int] = []

        # Gym spaces
        self.action_space = gym.spaces.Discrete(self.vocab_size)

        # ── 모델 로드 ───────────────────────────────────────────
        self.device = torch.device(device)
        self.classifier_device = torch.device(classifier_device)
        self.classifier: RESGCLClassifier = RESGCLClassifier.load_pretrained(
            Path(classifier_checkpoint), map_location=self.classifier_device
        )

        meta_attr_names = None
        if meta_path is not None:
            try:
                from torch.serialization import add_safe_globals
                from src.graphs.normalizers.schema import NodeType

                add_safe_globals([NodeType])
                meta = torch.load(meta_path, weights_only=False)
                if isinstance(meta, dict):
                    meta_attr_names = meta.get("attr_names")
                    meta_in_dims = {k: int(v) for k, v in meta.get("in_dims", {}).items()}
                    meta_vocab = int(meta.get("vocab_size", 0))
                    self.attr_dim = int(meta.get("attr_dim", self.attr_dim))
                    if hasattr(self.classifier, "encoder"):
                        self.classifier.encoder.attr_dim = self.attr_dim
                    self.classifier.reinit_input_dims(
                        in_dims=meta_in_dims,
                        attr_names=meta_attr_names,
                        vocab_size=meta_vocab,
                    )
                    _LOG.info(
                        "Loaded encoder attributes from meta snapshot: %s",
                        self.classifier.encoder.attr_names,
                    )
            except Exception as exc:  # pragma: no cover - optional
                _LOG.warning("Failed to load meta snapshot %s: %s", meta_path, exc)

        # ── 데이터셋 로드 ───────────────────────────────────────
        self.batch_size_eval = batch_size_eval
        self._load_datasets(dataset_dir)
        self.single_target_mode = bool(single_target_mode)
        self.full_dummy_set = list(self.dummy_set)
        if hasattr(self, "_clf_probs_dummy"):
            self._clf_probs_full_dummy = list(self._clf_probs_dummy)

        # precompute target hint tokens for single target mode
        raw_target_tokens: List[List[int]] = []
        if self.single_target_mode:
            fm = FeatureMiner(top_k=50)
            for g in self.full_dummy_set:
                try:
                    sal = torch.ones(sum(g[nt].num_nodes for nt in g.node_types))
                    feats = fm(g, sal)
                except Exception:
                    feats = []
                tokens: List[int] = []
                for feat in feats:
                    for tok in self._rule_tokenize(feat):
                        tid = self.token2id.get(tok)
                        if tid is not None:
                            tokens.append(tid)
                raw_target_tokens.append(tokens)

        if max_hint_tokens is None:
            self.max_hint_tokens = max(
                self.max_hint_tokens,
                *(len(t) for t in raw_target_tokens) if raw_target_tokens else [0],
            )

        max_allowed = getattr(self.tokenizer, "model_max_length", 1024) - self.max_len
        if self.max_hint_tokens > max_allowed:
            logging.warning(
                "max_hint_tokens (%d) clipped to %d due to GPT context limit",
                self.max_hint_tokens,
                max_allowed,
            )
            self.max_hint_tokens = max_allowed

        self._default_hint_tokens = (
            self._default_hint_tokens[: self.max_hint_tokens]
            + [self.token2id[self.PAD]] * max(0, self.max_hint_tokens - len(self._default_hint_tokens))
        )

        self.target_features_list = []
        for tokens in raw_target_tokens:
            t = tokens[: self.max_hint_tokens]
            if len(t) < self.max_hint_tokens:
                t += [self.token2id[self.PAD]] * (self.max_hint_tokens - len(t))
            self.target_features_list.append(t)

        self.observation_space = gym.spaces.Box(
            low=0,
            high=self.vocab_size,
            shape=(self.max_len + self.max_hint_tokens,),
            dtype=np.int32,
        )

        # 평가지표/보상 모듈
        self.evaluator = RuleEvaluator(
            clf=self.classifier,
            device=self.device,
            batch_size=self.batch_size_eval,
        )

        meta_file = Path(dataset_dir) / "metadata_vocab.json"
        if meta_file.is_file() and meta_attr_names is None:
            try:
                self._reconfigure_encoder_for_metadata(meta_file)
            except Exception as exc:  # pragma: no cover - optional
                _LOG.warning("Failed to reconfigure encoder for metadata: %s", exc)

        # 내부 상태
        self.reset()

    def update_reward_weights(self, weights: dict | None = None, **kwargs) -> None:
        """Update :attr:`reward_weights` in-place.

        Parameters
        ----------
        weights : optional mapping of reward component names to new values.
        **kwargs : additional key-value pairs overriding the weights.
        """

        if weights:
            for k, v in weights.items():
                if k in self.reward_weights:
                    self.reward_weights[k] = float(v)
        for k, v in kwargs.items():
            if k in self.reward_weights:
                self.reward_weights[k] = float(v)

    # ───────────────────────────────────────────── rule eval logging ―
    def set_rule_eval_callback(
        self, callback: Callable[[str, dict], None] | None
    ) -> None:
        """Register a callback invoked after each rule evaluation."""

        self.rule_eval_callback = callback

    def get_rule_eval_history(self) -> List[dict]:
        """Return and clear recorded rule evaluation history."""

        hist = list(self.rule_eval_history)
        self.rule_eval_history.clear()
        return hist

    # ─────────────────────────────────────────────────── gym API —
    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,
        hint_features: List[str] | None = None,
    ) -> Tuple[np.ndarray, dict]:
        super().reset(seed=seed)
        info_extra: dict = {}
        if self.single_target_mode:
            idx = random.randrange(len(self.full_dummy_set))
            target = self.full_dummy_set[idx]
            self.dummy_set = [target]
            if hasattr(self, "_clf_probs_full_dummy"):
                self._clf_probs_dummy = [self._clf_probs_full_dummy[idx]]
            hint_tokens = list(self.target_features_list[idx])
            info_extra["target_idx"] = idx
            sha = getattr(target, "sha256", None)
            if sha is not None:
                info_extra["target_sha"] = sha
        else:
            feats = hint_features if hint_features is not None else self.hint_features
            hint_tokens = []
            for feat in feats:
                for tok in self._rule_tokenize(feat):
                    tok_id = self.token2id.get(tok)
                    if tok_id is not None:
                        hint_tokens.append(tok_id)
            hint_tokens = hint_tokens[: self.max_hint_tokens]
            if len(hint_tokens) < self.max_hint_tokens:
                hint_tokens += [self.token2id[self.PAD]] * (self.max_hint_tokens - len(hint_tokens))

        self._hint_tokens = list(hint_tokens)
        self._tokens = []
        self._phi_last = 0.0
        self._episode_steps = 0
        obs = self._pad_obs(self._tokens)
        info = {"hint": np.array(self._hint_tokens, dtype=np.int32)}
        info.update(info_extra)
        return obs, info

    def step(
        self, action: int
    ) -> Tuple[np.ndarray, float, bool, bool, dict]:  # Gymnasium step sig
        assert self.action_space.contains(action)
        done = False
        truncated = False
        reward = 0.0
        info: dict = {}
        self._episode_steps += 1
        self.total_steps += 1

        # 1) 토큰 append
        self._tokens.append(action)
        tok_str = self.id2token[action]
        reward += self.step_penalty
        reward += self.per_token_saliency * self.token_saliency.get(tok_str, 0.0)

        # 2) 종료 조건
        max_tokens = self.observation_space.shape[0]
        total_len = len(self._tokens) + len(self._hint_tokens)
        rule_text = self._tokens_to_rule(self._tokens)

        compute_reward = False
        if action == self.token2id[self.END] or total_len >= max_tokens:
            done = True
            truncated = total_len >= max_tokens
            compute_reward = True
        elif self.use_shaping and self.core_tokens:
            tokens_now = set(self._rule_tokenize(rule_text))
            if set(self.core_tokens).issubset(tokens_now):
                compute_reward = True

        shaping = 0.0
        metrics = {}
        if compute_reward:
            final_r, metrics, shaping = self._compute_reward(
                rule_text, update_stats=done
            )
            if done:
                if self.normalize_reward:
                    std = self.running_stats.std or 1.0
                    final_r = (final_r - self.running_stats.mean) / std
                reward += final_r
                info["metrics"] = metrics
        elif self.use_lookahead:
            look_p = self._lookahead_prob(self._tokens)
            reward += look_p
            info["lookahead_prob"] = look_p

        if self.use_shaping:
            reward += shaping
            info["shaping"] = shaping

        obs = self._pad_obs(self._tokens)
        if done:
            info["episode_len"] = self._episode_steps
        return obs, reward, done, truncated, info

    def render(self, mode: str = "human"):
        rule = self._tokens_to_rule(self._tokens)
        print(f"[RuleGenEnv] current rule ({len(self._tokens)} tok):\n{rule}")

    # ──────────────────────────────── internal utils ―─────────
    # Vocab build
    def _build_vocab(self, train_dir: Path) -> Path:
        """
        학습 split 그래프 + FeatureMiner를 사용해 토큰 사전 생성
        결과는 JSON 파일로 저장 후 경로 반환.
        """
        fm = FeatureMiner(top_k=80)
        token_counter: Dict[str, int] = {}

        # 그래프 폴더 순회
        graph_files = sorted(train_dir.glob("*.pt"))
        for g_path in graph_files:
            g: HeteroData = torch.load(g_path, map_location="cpu", weights_only=False)
            # saliency dummy → 모든 노드 equal (추출 다양성 ↑)
            s = torch.ones(sum(g[nt].num_nodes for nt in g.node_types))
            feats = fm(g, s)
            for f in feats:
                for tok in self._rule_tokenize(f):
                    token_counter[tok] = token_counter.get(tok, 0) + 1

        # 빈도순 + token → id
        sorted_toks = sorted(token_counter.items(), key=lambda kv: (-kv[1], kv[0]))
        vocab = {tok: idx for idx, (tok, _) in enumerate(sorted_toks)}
        # 파일 저장
        vocab_file = train_dir.parent / "rule_vocab.json"
        with vocab_file.open("w") as fp:
            json.dump(vocab, fp, ensure_ascii=False, indent=2)
        _LOG.info("Saved vocab (%d tokens) → %s", len(vocab), vocab_file)
        return vocab_file

    # 데이터셋 로딩
    def _load_datasets(self, dataset_dir: Union[str, Path]) -> None:
        """Load clean/dummy graph datasets.

        Graph objects must contain a ``file_path`` attribute pointing to the raw
        binary so that :class:`RuleEvaluator` can scan files directly.
        ``dataset_dir`` should contain ``clean.pt`` and ``dummy.pt`` saved by
        :func:`rulegen.build_dataset.build_dataset` or
        ``python -m cli.rulegen_cli build-dataset``.
        """
        ds_dir = Path(dataset_dir)
        self.clean_set: List[HeteroData] = torch.load(
            ds_dir / "clean.pt", weights_only=False
        )
        self.dummy_set: List[HeteroData] = torch.load(
            ds_dir / "dummy.pt", weights_only=False
        )
        _LOG.info(
            "Loaded dataset — clean:%d, dummy:%d",
            len(self.clean_set),
            len(self.dummy_set),
        )
        if self.use_lookahead:
            self._precompute_clf_probs()

    def _precompute_clf_probs(self) -> None:
        """Precompute classifier logits for every graph in the datasets."""
        from src.graphs.dataset import GraphDataset

        attr_names = getattr(self.classifier.encoder, "attr_names", None)

        class _ListDS(torch.utils.data.Dataset):
            def __init__(self, graphs: Sequence[HeteroData]):
                self.graphs = list(graphs)

            def __len__(self) -> int:
                return len(self.graphs)

            def __getitem__(self, idx: int):
                g = self.graphs[idx]
                sha = getattr(g, "sha256", str(idx))
                return g, 0, sha

        def _collect(ds_list: Sequence[HeteroData]) -> List[float]:
            ds = _ListDS(ds_list)
            loader = DataLoader(
                ds,
                batch_size=self.batch_size_eval,
                shuffle=False,
                collate_fn=lambda b: GraphDataset.collate_fn(b, attr_names=attr_names),
            )
            logits: List[float] = []
            self.classifier.eval()
            for batch in loader:
                g = batch["graph"].to(self.classifier_device)
                out = self.classifier(g)
                if isinstance(out, (list, tuple)):
                    out = out[0]
                out = out.view(-1)
                logits.extend(out.detach().cpu().tolist())
            return logits

        self._clf_probs_clean = _collect(self.clean_set)
        self._clf_probs_dummy = _collect(self.dummy_set)

    def _fgsm_graph(self, g: HeteroData, label: int, epsilon: float) -> HeteroData:
        g_adv = g.clone().to(self.classifier_device)
        for nt in g_adv.node_types:
            x = g_adv[nt].get("x")
            if x is not None and torch.is_floating_point(x):
                g_adv[nt].x = x.clone().detach().requires_grad_(True)

        self.classifier.eval()
        logit = self.classifier(g_adv, return_logits=True)
        target = torch.tensor([float(label)], device=self.classifier_device)
        loss = F.binary_cross_entropy_with_logits(logit.squeeze(), target)
        self.classifier.zero_grad()
        loss.backward()

        for nt in g_adv.node_types:
            x = g_adv[nt].get("x")
            if x is not None and x.grad is not None:
                adv = x + epsilon * x.grad.sign()
                g_adv[nt].x = adv.detach()
        return g_adv.cpu()

    def _perturb_set(
        self, dataset: Sequence[HeteroData], label: int, ratio: float, epsilon: float
    ) -> List[HeteroData]:
        n_adv = max(1, int(len(dataset) * ratio))
        idx = random.sample(range(len(dataset)), n_adv)
        out: List[HeteroData] = []
        for i, g in enumerate(dataset):
            if i in idx:
                out.append(self._fgsm_graph(g, label, epsilon))
            else:
                out.append(g)
        return out

    def _reconfigure_encoder_for_metadata(self, vocab_path: Path) -> None:
        """Reinitialize classifier.encoder based on dataset metadata."""
        from src.graphs.dataset import collect_dataset_metadata  # lazy import

        with vocab_path.open("r", encoding="utf-8") as fp:
            vocab = json.load(fp)

        attr_names: Dict[str, List[str]] = {}
        for nt, attrs in vocab.items():
            if isinstance(attrs, dict):
                attr_names[nt] = sorted(attrs.keys())
            elif isinstance(attrs, list):
                attr_names.setdefault("", []).append(nt)
            else:
                raise TypeError(
                    f"Unsupported value type for {nt!r}: {type(attrs).__name__}"
                )

        class _ListDS:
            def __init__(self, graphs):
                self.graphs = graphs

            def __len__(self):
                return len(self.graphs)

            def __getitem__(self, idx):
                return self.graphs[idx]

        ds = _ListDS(self.clean_set + self.dummy_set)
        metadata, in_dims, _, _, max_ids = collect_dataset_metadata(
            [ds], attr_dim=self.attr_dim
        )
        vocab_size = max(max_ids.values(), default=0) + 1

        old_enc = self.classifier.encoder
        if not hasattr(old_enc, "out_proj"):
            old_enc.attr_names = attr_names
            return
        hidden_dim = old_enc.out_proj.in_features
        out_dim = old_enc.out_proj.out_features
        num_layers = len(getattr(old_enc, "convs", []))
        target_node = getattr(old_enc, "target_node", None)
        dropout = getattr(old_enc.drop, "p", 0.0) if hasattr(old_enc, "drop") else 0.0

        new_enc = RGCNEncoder(
            metadata=metadata,
            in_dims=in_dims,
            attr_names=attr_names,
            vocab_size=vocab_size,
            attr_dim=self.attr_dim,
            hidden_dim=hidden_dim,
            num_layers=num_layers,
            out_dim=out_dim,
            dropout=dropout,
            target_node=target_node,
        )

        new_state = new_enc.state_dict()
        old_state = old_enc.state_dict()
        for k, v in old_state.items():
            if k in new_state and new_state[k].shape == v.shape:
                new_state[k] = v
        new_enc.load_state_dict(new_state, strict=False)
        new_enc.to(self.classifier_device)
        self.classifier.encoder = new_enc

    # 관측 pad
    def _pad_obs(self, toks: Sequence[int]) -> np.ndarray:
        obs_len = self.observation_space.shape[0]
        arr = np.full((obs_len,), fill_value=self.token2id[self.PAD], dtype=np.int32)
        all_toks = list(self._hint_tokens) + list(toks)
        n = min(len(all_toks), obs_len)
        if n:
            arr[:n] = all_toks[:n]
        max_id = int(arr.max())
        min_id = int(arr.min())
        assert max_id < self.vocab_size and min_id >= 0, (
            f"Observation token ids out of range: min={min_id}, max={max_id}, vocab_size={self.vocab_size}"
        )
        return arr

    def _graph_hint_tokens(self, g: HeteroData) -> List[int]:
        """Extract hint token ids from a graph's features."""
        feats = getattr(g, "features", None)
        if not isinstance(feats, list):
            try:
                fm = FeatureMiner(top_k=20)
                sal = torch.ones(sum(g[nt].num_nodes for nt in g.node_types))
                feats = fm(g, sal)
            except Exception:
                feats = []
        tokens: List[int] = []
        for feat in feats:
            for tok in self._rule_tokenize(str(feat)):
                tid = self.token2id.get(tok)
                if tid is not None:
                    tokens.append(tid)
        return tokens

    def get_action_mask(
        self,
        tokens: Optional[Sequence[int]] = None,
        hint_tokens: Optional[Sequence[int]] = None,
    ) -> np.ndarray:
        """Return a binary mask for valid next actions.

        Parameters
        ----------
        tokens : optional sequence of token ids representing the current rule.
            Defaults to the environment's internal token list.
        hint_tokens : optional sequence of hint token ids.  Defaults to the
            hint tokens from ``reset``.
        """

        toks = list(self._tokens if tokens is None else tokens)
        hints = self._hint_tokens if hint_tokens is None else list(hint_tokens)

        mask = np.ones(self.vocab_size, dtype=np.int8)

        # length constraint – reserve space for END token
        obs_len = self.observation_space.shape[0]
        total_len = len(toks) + len(hints)
        if total_len >= obs_len - 1:
            mask[:] = 0
            mask[self.token2id[self.END]] = 1
            return mask

        # basic parenthesis balance
        open_tok = self.token2id.get("(")
        close_tok = self.token2id.get(")")
        if close_tok is not None and open_tok is not None:
            opens = sum(1 for t in toks if t == open_tok)
            closes = sum(1 for t in toks if t == close_tok)
            if opens <= closes:
                mask[close_tok] = 0

        # ':' usage rules
        if self._colon_id is not None:
            if not toks:
                mask[self._colon_id] = 0
            else:
                prev = self.id2token[toks[-1]]
                if prev in {":", "(", "[", "{", ",", "."}:
                    mask[self._colon_id] = 0

        # string/number token placement
        if toks:
            prev = self.id2token[toks[-1]]
            if prev != ":":
                for tid in self._string_token_ids:
                    mask[tid] = 0
            if prev != ":" and prev not in self._number_token_strings:
                for tid in self._number_token_ids:
                    mask[tid] = 0
            if prev == ":":
                for tid in self._punct_token_ids:
                    mask[tid] = 0
        else:
            for tid in self._string_token_ids | self._number_token_ids:
                mask[tid] = 0

        return mask

    # token → string → rule
    def _tokens_to_rule(self, toks: Sequence[int]) -> str:
        all_toks = list(self._hint_tokens) + list(toks)
        raw_tokens = [
            self.id2token[i]
            for i in all_toks
            if i not in {self.token2id[self.END], self.token2id[self.PAD]}
        ]
        if self.rule_type == "yara":
            from .yara_builder import tokens_to_yara  # type: ignore

            return tokens_to_yara(raw_tokens, tokenizer=self.tokenizer)
        else:
            from .capa_builder import tokens_to_capa  # type: ignore

            return tokens_to_capa(raw_tokens, tokenizer=self.tokenizer)

    @torch.inference_mode()
    def _lookahead_prob(self, tokens: Sequence[int]) -> float:
        """Return weighted F1 of rule matches against classifier predictions."""
        if not tokens:
            return 0.0

        rule_text = self._tokens_to_rule(tokens)

        try:
            if self.rule_type == "yara":
                if yara is None:
                    return 0.0
                compiled = yara.compile(source=rule_text)

                def _match(path: Path) -> bool:
                    try:
                        return bool(compiled.match(str(path)))
                    except Exception:
                        return False

            else:  # capa rule
                with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False) as tmp:
                    tmp.write(rule_text)
                    tmp.flush()

                def _match(path: Path) -> bool:
                    try:
                        proc = subprocess.run(
                            ["capa", str(path), "-r", tmp.name, "--json"],
                            capture_output=True,
                            text=True,
                            check=False,
                        )
                    except FileNotFoundError:
                        return False
                    if proc.returncode != 0:
                        return False
                    try:
                        js = json.loads(proc.stdout)
                    except Exception:
                        return False
                    return bool(js.get("rules"))
        except Exception:
            return 0.0

        matches: List[int] = []
        for g in self.clean_set:
            p = getattr(g, "file_path", None) or getattr(g, "sha256", None)
            matches.append(int(_match(Path(str(p))) if p is not None else False))
        for g in self.dummy_set:
            p = getattr(g, "file_path", None) or getattr(g, "sha256", None)
            matches.append(int(_match(Path(str(p))) if p is not None else False))

        labels = [1 if logit >= 0 else 0 for logit in self._clf_probs_clean]
        labels += [1 if logit >= 0 else 0 for logit in self._clf_probs_dummy]

        TP = FP = FN = TN = 0
        for pred, lab in zip(matches, labels):
            if pred and lab:
                TP += 1
            elif pred and not lab:
                FP += 1
            elif not pred and lab:
                FN += 1
            else:
                TN += 1

        denom_pos = 2 * TP + FP + FN
        f1_dummy = 0.0 if denom_pos == 0 else 2 * TP / denom_pos
        denom_neg = 2 * TN + FP + FN
        f1_clean = 0.0 if denom_neg == 0 else 2 * TN / denom_neg

        w = self.reward_weights
        return float(w["f1_clean"] * f1_clean + w["f1_dummy"] * f1_dummy)

    def _compute_off_target_penalty(
        self,
        rule_text: str,
        dummy_set: Sequence[HeteroData],
        penalty_factor: float,
    ) -> Tuple[float, float]:
        """Compute penalty and match count for off-target graphs."""
        if not self.single_target_mode or len(self.full_dummy_set) <= len(dummy_set):
            return 0.0, 0.0
        off_targets = [g for g in self.full_dummy_set if g not in dummy_set]
        if not off_targets:
            return 0.0, 0.0
        _, f1_ot, _, _ = self.evaluator.evaluate_rule(rule_text, [], off_targets)
        m_off = len(off_targets)
        matches = float(f1_ot * m_off / (2 - f1_ot)) if f1_ot > 0 else 0.0
        penalty = penalty_factor * matches
        return penalty, matches

    # reward
    @torch.inference_mode()
    def _compute_reward(
        self, rule_text: str, *, update_stats: bool = True
    ) -> Tuple[float, dict, float]:
        clean_set = self.clean_set
        dummy_set = self.dummy_set
        if self.use_adv_perturb:
            clean_set = self._perturb_set(self.clean_set, 0, 0.2, 0.05)
            dummy_set = self._perturb_set(self.dummy_set, 1, 0.2, 0.05)

        f1_clean, f1_dummy, certified_r, counts = self.evaluator.evaluate_rule(
            rule_text,
            clean_set,
            dummy_set,
        )

        invalid_rule = certified_r < 0

        rule_len = len(self._rule_tokenize(rule_text))

        # dynamic FP penalty schedule
        if self.total_steps < self.fp_penalty_delay:
            curr_penalty = 0.0
        else:
            progress = min(
                self.total_steps - self.fp_penalty_delay,
                self.curriculum_steps,
            ) / self.curriculum_steps
            curr_penalty = (
                self.fp_penalty_start
                + (self.fp_penalty_end - self.fp_penalty_start) * progress
            )

        TP, FP, FN, TN = counts
        n = len(clean_set)
        fp_rate = 0.0 if n == 0 else FP / n
        false_positive = FP > 0

        w = self.reward_weights
        weighted_f1 = w["f1_clean"] * f1_clean + w["f1_dummy"] * f1_dummy

        if self.total_steps < self.rule_len_penalty_delay:
            progress_len = 0.0
        else:
            progress_len = min(
                self.total_steps - self.rule_len_penalty_delay,
                self.rule_len_steps,
            ) / self.rule_len_steps
        curr_rule_len_w = self.rule_len_penalty_start + (
            self.rule_len_penalty_end - self.rule_len_penalty_start
        ) * progress_len

        reward = weighted_f1 + curr_rule_len_w * rule_len
        if certified_r >= 2:
            reward += w["certified_bonus"]

        if invalid_rule:
            reward -= 1.0

        reward -= curr_penalty * fp_rate

        used_tokens = self._rule_tokenize(rule_text)
        if used_tokens:
            bonus = 0.02 * np.mean(
                [self.token_saliency.get(t, 0.0) for t in used_tokens]
            )
        else:
            bonus = 0.0
        reward += bonus

        # penalize off-target matches in single-target mode
        progress_off = min(self.total_steps, self.off_target_steps) / self.off_target_steps
        curr_off_penalty = self.off_target_penalty_start + (
            self.off_target_penalty_end - self.off_target_penalty_start
        ) * progress_off
        off_target_pen, off_matches = self._compute_off_target_penalty(
            rule_text,
            dummy_set,
            curr_off_penalty,
        )
        reward -= off_target_pen

        no_tp = counts[0] == 0 and len(dummy_set) > 0
        if no_tp:
            reward -= self.no_tp_penalty

        if f1_dummy > self.prev_f1_dummy:
            reward += self.improve_bonus * (f1_dummy - self.prev_f1_dummy)
        self.prev_f1_dummy = f1_dummy

        metrics = dict(
            f1_clean=f1_clean,
            f1_dummy=f1_dummy,
            rule_len=rule_len,
            rule_len_weight=curr_rule_len_w,
            certified_r=certified_r,
            invalid_rule=invalid_rule,
            fp_rate=fp_rate,
            fp_penalty=curr_penalty * fp_rate,
            fp_penalty_factor=curr_penalty,
            saliency_bonus=bonus,
            off_target_matches=off_matches,
            off_target_penalty=off_target_pen,
            off_target_penalty_factor=curr_off_penalty,
            counts=counts,
            false_positive=false_positive,
            no_tp=no_tp,
            no_tp_penalty=self.no_tp_penalty if no_tp else 0.0,
            reward=reward,
        )
        shaping = 0.0
        if self.core_tokens:
            used = set(self._rule_tokenize(rule_text))
            if set(self.core_tokens).issubset(used):
                phi = weighted_f1
                shaping = self.gamma * phi - self._phi_last
                self._phi_last = phi
        if update_stats:
            self.running_stats.update(float(reward))
        log_entry = {"rule": rule_text}
        log_entry.update(metrics)
        self.rule_eval_history.append(log_entry)
        if len(self.rule_eval_history) > self._max_history:
            self.rule_eval_history.pop(0)
        if self.rule_eval_callback:
            try:
                self.rule_eval_callback(rule_text, metrics)
            except Exception:  # pragma: no cover - logging errors shouldn't crash
                _LOG.exception("rule_eval_callback failed")
        return reward, metrics, shaping

    # rule string tokenizer (공용)
    @staticmethod
    def _rule_tokenize(text: str) -> List[str]:
        tokens = (
            text.replace("(", " ( ").replace(")", " ) ").replace(":", " : ").split()
        )
        out: List[str] = []
        for tok in tokens:
            subtokens = [tok]
            if re.search(r"[a-z][A-Z]", tok) or re.search(r"[A-Za-z]\d", tok):
                subtokens = re.findall(r"[A-Z][^A-Z]*", tok)
            if "_" in tok:
                tmp: List[str] = []
                for st in subtokens:
                    tmp.extend(st.split("_"))
                subtokens = tmp
            for st in subtokens:
                if st:
                    out.append(st)
        return out


# ──────────────────────────────── quick smoke‑test ────────────
if __name__ == "__main__":
    env = RuleGenEnv(
        rule_type="yara",
        dataset_dir="data/splits",  # 실제 경로 맞게 수정
        max_len=64,
    )
    obs, _ = env.reset()
    total_r = 0.0
    for _ in range(10):  # 무작위 10 스텝
        a = env.action_space.sample()
        obs, r, done, tr, info = env.step(a)
        total_r += r
        if done:
            env.render()
            print("Reward:", r, info)
            break
    print("Total reward acc:", total_r)
