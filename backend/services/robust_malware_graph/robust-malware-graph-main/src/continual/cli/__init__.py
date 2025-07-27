"""
src.continual.cli
=================

패키지 단위 명령행 진입점
------------------------
$ python -m continual.cli <subcommand> [args…]

등록 서브커맨드
--------------
• online_supcon_train   : 스트리밍 그래프 SupContrast 학습
• online_eval           : 학습된 모델 평가

새로운 CLI 모듈을 추가하려면
---------------------------
1. `src/continual/cli/your_cmd.py` 작성 (def main(args: list[str]) -> None 패턴)
2. 아래 COMMAND_REGISTRY 에 ("your_cmd", your_cmd.main) 추가
"""

from __future__ import annotations

import importlib
import sys
from types import ModuleType
from typing import Callable, Dict, List

# --------------------------------------------------------------------------- #
# 1. 커맨드 레지스트리 – (name → (module_path, func_name))
#    모듈은 지연 import 해 실행 속도를 향상
# --------------------------------------------------------------------------- #
COMMAND_REGISTRY: Dict[str, tuple[str, str]] = {
    "online_supcon_train": ("continual.cli.online_supcon_train", "main"),
    "online_eval": ("continual.cli.online_eval", "main"),
}

__all__ = ["dispatch", "COMMAND_REGISTRY"]


# --------------------------------------------------------------------------- #
# 2. 디스패처
# --------------------------------------------------------------------------- #
def _load_callable(module_path: str, func_name: str) -> Callable[[List[str]], None]:
    """지연 import 뒤 엔트리 함수를 가져온다."""
    module: ModuleType = importlib.import_module(module_path)
    func: Callable = getattr(module, func_name)
    if not callable(func):
        raise AttributeError(f"{module_path}.{func_name} is not callable")
    return func


def dispatch(argv: list[str] | None = None) -> None:
    """
    argv[0] (subcommand)에 따라 레지스트리 모듈·함수 호출.

    Parameters
    ----------
    argv : list[str] | None
        None → sys.argv[1:] 사용.
    """
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        _print_help()
        sys.exit(1)

    cmd, *cmd_args = argv
    if cmd not in COMMAND_REGISTRY:
        print(f"Unknown command '{cmd}'")
        _print_help()
        sys.exit(1)

    module_path, func_name = COMMAND_REGISTRY[cmd]
    run = _load_callable(module_path, func_name)
    run(cmd_args)  # type: ignore[arg-type]


def _print_help() -> None:
    print("Usage: python -m continual.cli <command> [args]\n")
    print("Available commands:")
    for k in COMMAND_REGISTRY:
        print(f"  {k}")


# --------------------------------------------------------------------------- #
# 3. 패키지 모듈 직접 실행 시
# --------------------------------------------------------------------------- #
if __name__ == "__main__":  # pragma: no cover
    dispatch()
