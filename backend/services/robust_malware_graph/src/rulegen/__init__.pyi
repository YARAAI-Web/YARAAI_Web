from typing import Any, Dict, Optional
from pathlib import Path
from .rl_env import RuleGenEnv
from .rl_agent import PPORuleAgent
from .feature_miner import FeatureMiner
from .yara_builder import YaraBuilder, tokens_to_yara
from .capa_builder import CapaBuilder, tokens_to_capa

__all__: list[str]
__version__: str


def make_env(
    rule_type: str = "yara",
    *,
    classifier_ckpt: str | Path = "models/gnn/res_gcl.pt",
    seed: int | None = None,
    **kwargs: Any,
) -> RuleGenEnv: ...

def load_agent(
    ckpt_path: str | None = None,
    env: Optional[RuleGenEnv] = ...,
    policy_net: str = ...,  # maintain param for completeness
    schedule_type: str | None = ...,
    total_updates: int | None = ...,
    seed: int | None = None,
    constraint_thresh: float = ...,
    lagrange_lr: float = ...,
    agent_kwargs: Optional[Dict[str, Any]] = ...,
    **env_kwargs: Dict[str, Any],
) -> PPORuleAgent: ...

