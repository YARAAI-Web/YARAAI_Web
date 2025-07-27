"""
src.continual.evaluation
========================
Continual / Incremental / Online 학습 실험용 평가 유틸리티 모듈.

`import src.continual.evaluation as ev` 와 같이 임포트한 뒤
다음과 같은 객체를 바로 사용 가능하게끔 노출한다.

• Metrics
    - topk_accuracy
    - auroc
    - f1_score_macro
    - CLMatrix
    - OnlineAUC

• Evaluators
    - BatchEvaluator
    - ContinualEvaluator
    - OnlineEvaluator
"""

from __future__ import annotations

# 메트릭 함수·클래스 -----------------------------------------------------------
from .metrics import (
    topk_accuracy,
    auroc,
    f1_score_macro,
    CLMatrix,
    OnlineAUC,
)

# 평가 루프 -----------------------------------------------------------
from .evaluator import (
    BatchEvaluator,
    ContinualEvaluator,
    OnlineEvaluator,
)

# 공용 공개 심볼 정의 ----------------------------------------------------------
__all__: list[str] = [
    # metrics
    "topk_accuracy",
    "auroc",
    "f1_score_macro",
    "CLMatrix",
    "OnlineAUC",
    # evaluators
    "BatchEvaluator",
    "ContinualEvaluator",
    "OnlineEvaluator",
]

# 선택적 버전 정보 (git 태그 등과 연동하려면 수정)
__version__: str = "0.1.0"
