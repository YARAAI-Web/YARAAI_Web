"""
Centralised settings for the Robust‑Malware‑Graph project.

• 기본값 → configs/default.yaml → 환경변수(BMG_*) → 코드 수정(update_config)
• 싱글턴 `settings` 객체만 import 해서 사용:
    from src.common.config import settings
    log_dir = settings.LOG_DIR
• Torch/CUDA, RNG 시드 고정, 프로젝트 경로 탐색까지 포함
"""

from __future__ import annotations

import os
import random
from dataclasses import dataclass, field, asdict, replace, fields
from pathlib import Path
from typing import Any, Dict

import torch
import yaml
import numpy as np

# --------------------------------------------------------------------------- #
# 1. Project root auto‑detect  (…/robust‑malware‑graph/)
# --------------------------------------------------------------------------- #
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_YAML = _PROJECT_ROOT / "configs" / "default.yaml"

# --------------------------------------------------------------------------- #
# 2. Helpers
# --------------------------------------------------------------------------- #

def _load_yaml(path: Path) -> Dict[str, Any]:
    if path.is_file():
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


def _env_override(key: str, default: Any) -> Any:
    """환경 변수(`BMG_<KEY>`)가 있으면 캐스팅 후 반환."""
    env_key = f"BMG_{key.upper()}"
    if env_key not in os.environ:
        return default
    val = os.environ[env_key]

    # 간단 캐스팅
    if isinstance(default, bool):
        return val.lower() in {"1", "true", "yes"}
    if isinstance(default, int):
        return int(val)
    if isinstance(default, float):
        return float(val)
    return val  # str or 기타

# --------------------------------------------------------------------------- #
# 3. Dataclass definition
# --------------------------------------------------------------------------- #

@dataclass(slots=True)
class _Config:
    # --- Paths -------------------------------------------------------------- #
    PROJECT_ROOT: Path = field(default=_PROJECT_ROOT)
    DATA_DIR: Path = field(default=_PROJECT_ROOT / "data")
    MODELS_DIR: Path = field(default=_PROJECT_ROOT / "models")
    LOG_DIR: Path = field(default=_PROJECT_ROOT / "logs")

    # --- Training / Runtime ------------------------------------------------- #
    SEED: int = 42
    NUM_WORKERS: int = 8
    FORCE_CPU: bool = False
    GPU_ID: int = 0  # 첫 번째 GPU 기본

    # --- Misc --------------------------------------------------------------- #
    PRINT_CONFIG: bool = False  # 시작 시 config 로그 출력 여부
    EXP_NAME: str = "debug"   # 실험 폴더 이름(logs/EXP_NAME)

    # Derived attributes (set in __post_init__)
    EXP_DIR: Path = field(init=False)
    DEVICE: torch.device = field(init=False)

    # --------------------------------------------------------------------- #
    #              Derived / helper properties (not editable)              #
    # --------------------------------------------------------------------- #

    def __post_init__(self) -> None:
        # 파생 경로
        object.__setattr__(self, "EXP_DIR", self.LOG_DIR / self.EXP_NAME)
        self.EXP_DIR.mkdir(parents=True, exist_ok=True)

        # 디바이스 설정
        if not self.FORCE_CPU and torch.cuda.is_available():
            object.__setattr__(self, "DEVICE", torch.device(f"cuda:{self.GPU_ID}"))
            torch.cuda.set_device(self.DEVICE)
        else:
            object.__setattr__(self, "DEVICE", torch.device("cpu"))

        # 시드 고정
        random.seed(self.SEED)
        np.random.seed(self.SEED)
        torch.manual_seed(self.SEED)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.SEED)

    # --- helper ------------------------------------------------------------ #

    def to_dict(self) -> Dict[str, Any]:
        """슬롯 사용 여부와 관계없이 안전하게 dict 변환."""
        return asdict(self, dict_factory=dict)

    def __repr__(self) -> str:  # 깔끔한 출력용
        nested = "\n".join(f"  {k:<12}: {v}" for k, v in self.to_dict().items())
        return f"Config(\n{nested}\n)"

# --------------------------------------------------------------------------- #
# 4. Singleton instance (yaml → env override)
# --------------------------------------------------------------------------- #

def _build_settings() -> _Config:
    """YAML → ENV → 기본값 순으로 설정을 로드하여 단일 `_Config` 인스턴스 생성."""

    yaml_cfg = _load_yaml(_DEFAULT_YAML)

    # 1) 기본값 인스턴스 하나 생성 (post_init 실행됨)
    defaults = _Config()

    # 2) dataclasses.fields 로 필드 iterate (init=True 만 사용)
    kwargs: Dict[str, Any] = {}
    for f in fields(_Config):
        if not f.init:  # EXP_DIR, DEVICE 등 파생 필드는 제외
            continue
        value = getattr(defaults, f.name)
        # YAML 우선 적용
        if f.name in yaml_cfg:
            value = yaml_cfg[f.name]
        # 환경 변수 최종 덮어쓰기
        kwargs[f.name] = _env_override(f.name, value)

    cfg = _Config(**kwargs)  # 최종 설정 인스턴스 (post_init 다시 호출)

    if cfg.PRINT_CONFIG:
        from src.common.logger import get_logger  # 지연 import로 순환 참조 회피
        get_logger(__name__).info("Loaded config:\n%s", cfg)

    return cfg

settings: _Config = _build_settings()

# --------------------------------------------------------------------------- #
# 5. Public runtime override
# --------------------------------------------------------------------------- #

def update_config(**kwargs: Any) -> None:
    """코드 내부에서 동적으로 설정값을 덮어쓰기 위한 헬퍼.

    예) `update_config(SEED=99, EXP_NAME="trial-02")`
    새 settings 객체를 만들어 `settings` 전역에 주입한 뒤, 파생 필드를 재계산한다.
    """
    global settings
    settings = replace(settings, **kwargs)
    settings.__post_init__()  # 파생 필드 및 시드 재설정
