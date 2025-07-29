# 규칙 생성 가이드 (Quick Start)

`rulegen` 서브패키지는 XAI 단계에서 도출한 중요 노드 정보를 이용하여 YARA/CAPA 룰 초안을 생성합니다.

- **경로/레지스트리/URL 기반 특징도 추출한다.**
- CLI: `python -m cli.rulegen_cli feature-mine` 으로 후보 특성을 수집할 수 있습니다.
- `--dynamic-k`, `--top-k-percent`, `--keep-per-type` 옵션으로 후보 선별 방식을 세밀하게 조정할 수 있습니다.
- PPO 학습용 데이터셋은 `python -m cli.rulegen_cli build-dataset` 또는
  ``rulegen.build_dataset.build_dataset`` 함수로 생성합니다.
  함수 호출 시 ``binary_dir`` 인자를 지정하면 그래프의 ``file_path``가 해당 경로를
  가리키도록 저장됩니다.
- `scripts/compute_benign_freqs.py` 스크립트로 메타 CSV를 이용해 정상 그래프에서 공통 토큰의 빈도를 계산할 수 있습니다.
  ```bash
  python scripts/compute_benign_freqs.py \
      --graph-dir data/graphs \
      --meta-csv data/meta.csv \
      --out benign_freqs.json
  ```
  메타 CSV는 다음 명령으로 생성할 수 있습니다.
  ```bash
  python -m cli.preprocessing --input-dir ../maldata/benign --out . labels --label 0 --csv data/meta.csv
  ```
  계산된 JSON은 `--benign-freqs` 옵션에 전달해 자주 등장하는 토큰을 필터링합니다.

- `scripts/compute_feature_freqs.py` 스크립트로 메타 CSV의 라벨을 기준으로
  악성/정상 그래프 각각의 특징 빈도를 계산할 수 있습니다. 출력 JSON 형식은
  `{feature: [mal_count, ben_count]}` 입니다.
  ```bash
  python scripts/compute_feature_freqs.py \
      --graph-dir data/graphs \
      --meta-csv data/meta.csv \
      --out feature_freqs.json
  ```


```python
from rulegen import FeatureMiner
from torch_geometric.data import HeteroData

# data: HeteroData, saliency: Tensor
miner = FeatureMiner(
    top_k=40,
    top_k_percent=0.05,
    dynamic_k=True,
    keep_per_type=20,
    freq_threshold=10,
    # disable automatic relaxation if desired
    auto_relax=True,
)
candidates = miner(data, saliency)
print(candidates[:5])
```

`top_k_percent` 비율을 지정하면 전체 노드 수에 따라 `k`가 자동 계산됩니다.
`dynamic_k=True` 로 설정하면 saliency 분포를 이용해 `k`가 조정됩니다.
`keep_per_type` 는 노드 타입별 최대 후보 수를 제한합니다.

환경 초기화 시 보상 가중치를 조정할 수 있습니다.

```python
from rulegen import RuleGenEnv

env = RuleGenEnv(
    vocab_file="vocab.json",
    dataset_dir="data/splits",
    reward_weights={
        "f1_clean": 0.6,
        "f1_dummy": 0.3,
        "rule_len": -0.05,
        "certified_bonus": 0.1,
    },
    no_tp_penalty=0.2,
)
```

`no_tp_penalty`는 룰이 더미 그래프를 한 건도 매치하지 못했을 때 적용되는
패널티의 크기를 조절합니다. 기본값은 `0.2`이며 CLI에서는 `--no-tp-penalty`
옵션으로 설정할 수 있습니다.

오프타깃 매치에 대한 패널티 역시 스케줄을 줄 수 있습니다.

```python
env = RuleGenEnv(
    vocab_file="vocab.json",
    dataset_dir="data/splits",
    off_target_penalty_start=0.1,
    off_target_penalty_end=0.5,
    off_target_steps=10000,
)
```

CLI 사용 시 `--reward-weights` 옵션을 주면 YAML 설정의 기본값 대신
외부에서 지정한 JSON 문자열이나 파일의 보상 가중치를 사용할 수 있습니다.

```bash
python -m cli.rulegen_cli ppo-train \
    --train-features feats.json \
    --dataset-dir data/splits \
    --reward-weights '{"f1_clean":0.7,"f1_dummy":0.2,"rule_len":-0.05}'
```

### 가중치 동적 조정

`configs/rulegen/ppo.yaml` 의 `env.weight_adjust` 섹션을 이용하면 학습 중
보상 가중치를 주기적으로 갱신할 수 있습니다.

```yaml
env:
  reward_weights:
    f1_clean: 0.5
    f1_dummy: 0.4
  weight_adjust:
    interval: 5000        # 5000 스텝마다
    delta_f1_dummy: 0.1   # f1_dummy 가중치 +0.1
    delta_f1_clean: -0.1  # f1_clean 가중치 -0.1
```

학습 루프에서 지정한 주기마다 `env.update_reward_weights()`가 호출되어
가중치가 갱신됩니다.

### 자동 보상 조정

`auto_adjust` 섹션을 사용하면 최근 롤아웃의 평균 `f1_dummy` 값이 임계치보다
낮을 때 보상 가중치를 자동으로 보정합니다.

```yaml
auto_adjust:
  threshold: 0.1
  delta_f1_dummy: 0.1
  delta_f1_clean: -0.1
```

PPO 하이퍼파라미터는 다음 옵션으로 조정할 수 있습니다.

```bash
python -m cli.rulegen_cli ppo-train \
    --train-features feats.json \
    --dataset-dir data/splits \
    --num-steps 2048 \
    --minibatch-size 128 \
    --ppo-epochs 8
```

```bash
python -m cli.rulegen_cli ppo-train \
    --train-features feats.json \
    --dataset-dir data/splits \
    --policy gpt2 \
    --checkpoint models/rulegen/gpt2_agent.pt
```

```bash
python -m cli.rulegen_cli ppo-train \
    --train-features feats.json \
    --dataset-dir data/splits \
    --generate-hints-from-explainer \
    --explainer-checkpoint models/explainers/selector.pt
```

## Warm-start

`PPORuleAgent`는 GNN 분류기가 예측한 규칙 시퀀스와 라벨을 이용해 사전 학습할 수 있습니다.
준비한 데이터셋을 `train()` 호출 시 인자로 전달하면 PPO 업데이트 전에 한 번 학습합니다.

```python
dataset = [([1, 2, 3], 1), ([4, 5], 0)]  # (token id list, label)
agent.train(total_timesteps=50000,
            pretrain_dataset=dataset,
            pretrain_epochs=3)
```

### Lookahead 보상

보상이 희소한 환경에서는 룰이 완성될 때까지 에이전트가 의미 있는 피드백을 받기
어렵습니다. `RuleGenEnv`를 `use_lookahead=True` 로 생성하거나 CLI에서
`--use-lookahead` 옵션을 지정하면 현재까지 생성한 토큰 시퀀스에 대한 분류기 예측
확률을 임시 보상으로 사용합니다.

```bash
python -m cli.rulegen_cli ppo-train \
    --train-features feats.json \
    --dataset-dir data/splits \
    --use-lookahead
```

이렇게 하면 룰이 완성되기 전에 얻는 보상을 통해 탐색이 촉진되어 보상 희소성을
완화할 수 있습니다.

### Reward Shaping

초기 학습 단계에서 유용한 토큰을 모두 포함한 규칙 작성을 유도하기 위해
잠재 보상 shaping 을 사용할 수 있습니다. CLI에서 `--use-shaping` 옵션을
주면 힌트 토큰이 핵심 토큰(`core_tokens`)으로 설정되어 shaping 보상이
활성화됩니다.

```bash
python -m cli.rulegen_cli ppo-train \
    --train-features feats.json \
    --dataset-dir data/splits \
    --use-shaping
```

### Rule evaluation CLI

`src.cli.explainer_rule_eval`는 그래프와 샘플을 입력으로 중요 노드를 기반한
YARA 룰을 생성해 탐지 여부를 확인합니다. 기본 `--condition-type`은 `combo`
이며 각 그룹의 70% 이상이 매치되어야 합니다. 그룹이 하나이거나 특징이
2개 이하일 경우 별도 설정이 없으면 자동으로 `any` 조건을 사용하지만,
`--group-min-count`나 `--group-percentage`가 지정된 경우 해당 값에 맞춰
최소 매치 수가 계산됩니다.

```bash
python -m src.cli.explainer_rule_eval \
    --graph graph.pt --sample sample.bin \
    --saliency sal.pt --classifier models/gnn/res_gcl.pt
```

`--freq-threshold-step`과 `--comb-ratio-step`을 사용하면 재시도 과정에서
빈도 임계값을 낮추거나 병합 비율을 높여가며 규칙을 조정할 수 있습니다.
`--min-freq-threshold` 옵션을 지정하면 임계값 하한을 음수로도 설정할 수 있으며,
`--freq-threshold-step` 값을 0.1 등으로 두어 0.1 단위로 완화하는 것도 가능합니다.
`--enforce-self-detect` 옵션을 주면 현재 샘플이 탐지될 때까지 조건을 단계적으로 완화합니다.
`--fp-timeout` 옵션을 지정하면 FP 재시도를 해당 시간(초) 이후 중단합니다.
`--persist-fp-exclude` 옵션에 JSON 파일을 지정하면 재시도 과정에서
제외된 토큰을 누적 저장하며, 다음 실행에서도 동일 파일을 지정하면
자동으로 로드되어 동일 토큰을 계속 제외합니다.
배치 모드에서는 이렇게 수집한 FP 토큰을 전역으로 합산하여 가장 빈도가 높은 토큰을 다음 그래프 평가 시 `exclude_tokens` 인자에 자동 추가합니다. `--max-exclude-tokens` 옵션으로 최대 수를 조정하고, 필요하면 `--freq-threshold` 값을 함께 낮춰 더 엄격하게 필터링할 수 있습니다.
`--optimize` 플래그를 사용하면 재시도 과정에서 하이퍼파라미터를 온라인으로
조정합니다. `--optimizer-pkl` 옵션의 기본값은 `optimizer_state.pkl`이며 실행이
끝나면 이 위치에 상태가 자동 저장되고, 다음 실행 시 존재하면 기본으로 로드됩니다. 다른 경로에 저장하려면 `--save-optimizer` 를 사용합니다.

배치 모드에서도 `--save-optimizer` 를 지정하면 종료 시점에 상태가 해당 경로에 추가 저장됩니다.

`freq_threshold` 와 `group_min_count` 값 역시 옵티마이저에서 학습하며 기본값은 각각 `10`과 `0(None)` 입니다. 값의 범위는 `-1~100`, `0~10` 사이로 제한되고 상태 파일에 함께 저장되어 다음 실행 시 자동 복원됩니다.

`--group-min-count`나 `--group-percentage`로 조건을 조정할 수 있으며,
`--adjust-group-percentage` 옵션을 주면 특징 수가 많을 때 비율이 자동으로
낮춰집니다.
`--group-min-ratio`를 지정하면 그룹 후보 수에 비례하여 최소 매치 수가 자동으로 계산됩니다.
배치 모드에서 `--flush-every`를 지정하면 중간 결과를 주기적으로 CSV에 저장할 수 있습니다.

### Building YARA rules

채굴한 특징으로 YARA 룰을 만들 때 모든 토큰이 일치해야 한다면
`YaraBuilder`의 `condition_type`을 "all"로 지정합니다.

```python
from rulegen import FeatureMiner
from rulegen.yara_builder import YaraBuilder

tokens = FeatureMiner(top_k=10, restore_top_n=3)(data, saliency)
rule_text = YaraBuilder(condition_type="all").build(tokens)
```
