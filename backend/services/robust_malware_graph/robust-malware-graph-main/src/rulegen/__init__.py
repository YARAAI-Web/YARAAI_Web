#  ──────────────────────────────────────────────────────────────
#  robust-malware-graph / src / rulegen / __init__.py
#  ──────────────────────────────────────────────────────────────
"""
rulegen
=======

YARA / CAPA **자동 룰 생성** 파이프라인 모듈.

하위 서브패키지
--------------
• **feature_miner**  : 노드 saliency → 룰 후보 특성 추출
• **rl_env**         : Gym-style 환경 (PPO 학습용)
• **rl_agent**       : Pure-PyTorch PPO-Clip 에이전트
• **yara_builder**   : 토큰 시퀀스 → YARA 룰 문자열
• **capa_builder**   : 토큰 시퀀스 → CAPA YAML 룰

전역 헬퍼
---------
`make_env(rule_type="yara", **kwargs)` – 즉시 학습/테스트 환경 생성
`load_agent(path, env=None)` – 저장된 PPO 정책 불러오기

참고 문서
---------
프로젝트 **docs/rulegen/** 하위 `quick_start.md`, `agent_tuning.md` 참조
"""

from __future__ import annotations

import logging
from importlib import metadata
from typing import Any, Dict, Optional

try:
    from transformers import PreTrainedTokenizer  # type: ignore
except Exception:  # pragma: no cover - optional dep
    PreTrainedTokenizer = Any  # type: ignore
from pathlib import Path
import importlib
import sys

try:
    import gymnasium as gym
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    gym = None

# ───────────────────────── internal re-exports
try:
    from .feature_miner import FeatureMiner
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    class FeatureMiner:  # type: ignore[dead-code]
        """Fallback stub when optional deps are missing."""
        pass

try:
    from .rl_env import RuleGenEnv
    from .rl_agent import PPORuleAgent
    from .yara_builder import YaraBuilder, tokens_to_yara
    from .capa_builder import CapaBuilder, tokens_to_capa
except ModuleNotFoundError:  # pragma: no cover - optional deps
    RuleGenEnv = PPORuleAgent = YaraBuilder = CapaBuilder = None  # type: ignore
    def tokens_to_yara(*args, **kwargs):
        raise ModuleNotFoundError("rulegen optional dependencies are missing")

    def tokens_to_capa(*args, **kwargs):
        raise ModuleNotFoundError("rulegen optional dependencies are missing")

# ───────────────────────── public API surface
__all__ = [
    "FeatureMiner",
    "RuleGenEnv",
    "PPORuleAgent",
    "YaraBuilder",
    "CapaBuilder",
    "tokens_to_yara",
    "tokens_to_capa",
    "make_env",
    "load_agent",
]


def __dir__():
    """Return a sorted list of accessible attributes for autocomplete."""
    return sorted(set(globals()) | set(__all__))

# ───────────────────────── version info
try:
    __version__: str = metadata.version("robust-malware-graph")
except metadata.PackageNotFoundError:  # dev/CLI 실행 시
    __version__ = "0.0.0.dev"

# ───────────────────────── logging config (package-level default)
_LOG = logging.getLogger(__name__)
if not _LOG.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )

# ───────────────────────── gymnasium env registration
_ENV_ID = "RuleGenEnv-v0"
if gym is not None and _ENV_ID not in gym.registry:  # type: ignore[attr-defined]
    gym.register(
        id=_ENV_ID,
        entry_point="rulegen.rl_env:RuleGenEnv",
        max_episode_steps=512,
    )
    _LOG.debug("Gym env '%s' registered", _ENV_ID)

# ───────────────────────── lazy import helper
_LAZY_ATTRS = {
    "FeatureMiner": (".feature_miner", "FeatureMiner"),
    "RuleGenEnv": (".rl_env", "RuleGenEnv"),
    "PPORuleAgent": (".rl_agent", "PPORuleAgent"),
    "YaraBuilder": (".yara_builder", "YaraBuilder"),
    "tokens_to_yara": (".yara_builder", "tokens_to_yara"),
    "CapaBuilder": (".capa_builder", "CapaBuilder"),
    "tokens_to_capa": (".capa_builder", "tokens_to_capa"),
}

_LAZY_MODULES = {
    "feature_miner": ".feature_miner",
    "rl_env": ".rl_env",
    "rl_agent": ".rl_agent",
    "yara_builder": ".yara_builder",
    "capa_builder": ".capa_builder",
}


def __getattr__(name: str) -> Any:
    """Lazily import heavy submodules or objects."""
    if name in globals():
        return globals()[name]

    if name in _LAZY_MODULES:
        module = importlib.import_module(_LAZY_MODULES[name], __name__)
        sys.modules[f"{__name__}.{name}"] = module
        globals()[name] = module
        return module

    if name in _LAZY_ATTRS:
        module_path, attr_name = _LAZY_ATTRS[name]
        module = importlib.import_module(module_path, __name__)
        obj = getattr(module, attr_name)
        globals()[name] = obj
        return obj

    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# ╔══════════════════════════════════════════════════════════════╗
# ║                      Convenience helpers                     ║
# ╚══════════════════════════════════════════════════════════════╝
def make_env(
    rule_type: str = "yara",
    *,
    classifier_checkpoint: str | Path = "models/gnn/res_gcl.pt",
    seed: int | None = None,
    tokenizer: Optional[PreTrainedTokenizer] = None,
    meta_path: Optional[Path] = None,
    use_domain_rand: bool = False,
    edge_drop_range: tuple[float, float] = (0.0, 0.1),
    use_adv_perturb: bool = False,
    use_lookahead: bool = False,
    single_target_mode: bool = False,
    **kwargs: Any,
) -> RuleGenEnv:
    """
    PPO 학습·추론용 환경 생성 헬퍼.

    Example
    -------
    >>> env = rulegen.make_env(rule_type="capa", max_len=128)

    Parameters
    ----------
    tokenizer : Optional transformers tokenizer
        If provided, custom rule tokens are added to this tokenizer and used
        by the environment.
    meta_path : optional Path
        Encoder meta snapshot used to reinitialize classifier input layers.
    use_lookahead : bool, default ``False``
        When ``True``, classifier probabilities are used as interim rewards to
        mitigate reward sparsity.
    """
    # Legacy argument mapping
    if "classifier_ckpt" in kwargs:
        classifier_checkpoint = kwargs.pop("classifier_ckpt")

    if isinstance(tokenizer, str):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(tokenizer)

    env = RuleGenEnv(
        rule_type=rule_type,
        classifier_checkpoint=classifier_checkpoint,
        seed=seed if seed is not None else 2024,
        tokenizer=tokenizer,
        meta_path=meta_path,
        use_lookahead=use_lookahead,
        single_target_mode=single_target_mode,
        **kwargs,
    )

    env.use_adv_perturb = bool(use_adv_perturb)

    if use_domain_rand:
        from augment.ops.drop_edge import EdgeDrop
        import random

        low, high = edge_drop_range
        rng = random.Random(seed)
        for ds in (env.clean_set, env.dummy_set):
            for i, g in enumerate(ds):
                drop_p = rng.uniform(low, high)
                keep_p = 1.0 - drop_p
                ds[i] = EdgeDrop(keep_p)(g)
        _LOG.info(
            "Applied EdgeDrop domain randomization p=[%.2f, %.2f]", low, high
        )

    _LOG.info("Created RuleGenEnv(rule_type=%s)", rule_type)
    return env


def load_agent(
    ckpt_path: str | None = None,
    env: Optional[RuleGenEnv] = None,
    policy_net: str = "gru",
    schedule_type: str | None = None,
    total_updates: int | None = None,
    seed: int | None = None,
    constraint_thresh: float = 0.5,
    lagrange_lr: float = 0.05,
    agent_kwargs: Optional[Dict[str, Any]] = None,
    **env_kwargs: Any,
) -> PPORuleAgent:
    """
    저장��� **PPO 정책**을 쉽게 불러오는 헬퍼.

    Parameters
    ----------
    ckpt_path  : `.pt` 파일 경로; None 이면 *새 에이전트* 초기화
    env        : 미리 생성한 RuleGenEnv; 없으면 자동 `make_env()`
    policy_net : "gru" 또는 사용할 GPT 모델명
    schedule_type : 학습률 스케줄러 종류 (예: "linear", "cosine")
    total_updates : 스케줄 총 스텝 수
    env_kwargs : env 미생성 시 전달할 파라미터
    agent_kwargs : PPORuleAgent 초기화 시 추가 하이퍼파라미터

    Returns
    -------
    PPORuleAgent  (policy weights 로드 완료 상태)
    """
    if env is None:
        env = make_env(seed=seed, **env_kwargs)
    agent = PPORuleAgent(
        env,
        policy_net=policy_net,
        schedule_type=schedule_type,
        total_updates=total_updates,
        seed=seed if seed is not None else 2024,
        constraint_thresh=constraint_thresh,
        lagrange_lr=lagrange_lr,
        **(agent_kwargs or {}),
    )

    def _ensure_vocab_size() -> None:
        if hasattr(agent.policy, "gpt"):
            vocab_size = env.vocab_size
            emb_size = agent.policy.gpt.get_input_embeddings().num_embeddings
            if vocab_size != emb_size:
                _LOG.warning(
                    "Resized GPT embeddings: env vocab=%d, model=%d",
                    vocab_size,
                    emb_size,
                )
                agent.policy.gpt.resize_token_embeddings(vocab_size)

    _ensure_vocab_size()
    if ckpt_path:
        agent.load(ckpt_path)
        _LOG.info("Loaded PPO agent weights from '%s'", ckpt_path)
        _ensure_vocab_size()
    else:
        _LOG.info("Initialized fresh PPO agent (no checkpoint)")
    return agent
