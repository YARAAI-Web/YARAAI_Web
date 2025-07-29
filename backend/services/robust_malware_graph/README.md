# robust-malware-graph

> Python 3.10 이상과 **PyTorch 2.6** 이상의 환경에서 동작합니다.

```mermaid
flowchart TD
    %% ─────────────── 노드 정의 ───────────────
    A["① data/raw<br/>(PE · ELF · VT&nbsp;JSON)"]:::file
    B["① data/views<br/>(AST · CFG · FCG · SysCall)"]
    C["① data/hetero<br/>(멀티뷰 통합&nbsp;Parquet)"]
    D["augment/<br/>(GraphCL · AutoAug)"]
    E["① data/embeds<br/>(노드·그래프 임베딩 캐시)"]
    F["② models/gnn<br/>(encoder.pt, res_gcl.pt)"]
    H["evaluation<br/>(Accuracy · MacroF1 · AUROC)"]
    I["explain<br/>(중요 서브그래프)"]
    J["continual<br/>(CIL · DIL)"]
    K["rulegen<br/>(YARA · Graph Pattern)"]
    L["② models/rulebank<br/>(YARA / CAPA)"]
    M["SOC·보안 분석가<br/>(explain/report.py)"]

    %% ─────────────── 데이터 & 프로세스 흐름 ───────────────
    A -->|"collect/ – P1. 샘플 수집·중복 제거<br/>Loss: —  •  Metric: —"| B
    B -->|"extract/ – P2. 각 뷰 생성<br/>Loss: —  •  Metric: —"| C
    C -->|"graphs/hetero_builder – P3. 이질 그래프 구축<br/>Loss: —  •  Metric: —"| D
    D -->|"P4. 그래프 증강<br/>Loss: —  •  Metric: —"| E

    %% P5 학습
    E -->|"models/gnn·contrast·distill – P5. 모델 학습<br/>• Self-GCL Loss: InfoNCE<br/>• Sup-Con Loss: NT-Xent<br/>• RES-GCL Loss: BCE + Edge-Drop<br/>Metric: Val AUROC · MacroF1 · Certified r"| F

    %% P6 평가
    F -->|"logits<br/>Loss: —  •  Metric: Accuracy · MacroF1 · AUROC"| H

    %% P7 설명
    F -->|"중요 서브그래프<br/>Loss: IB-RL Selector<br/>Metric: Fidelity · Sparsity"| I

    %% P8 지속학습
    F -->|"Online Sup-Con<br/>Loss: NT-Xent<br/>Metric: ACC · BWT · AUROC"| J

    %% P9 룰 생성
    I -->|"saliency → rule draft<br/>Loss: PPO-Clip (Reward 기반)<br/>Metric: F1_clean · FP@1M · 룰 길이"| K
    K --> L
    L --> M

    %% ─────────────── 스타일 ───────────────
    classDef file fill:#f9f,stroke:#333,stroke-width:1px,color:#000;

```

| #  | 논문 (첫 저자 · 연도)                                                                              | 학회 / 저널   | 링크                            | 파이프라인 적용 포인트                             |
| -- | ------------------------------------------------------------------------------------------- | --------- | ----------------------------- | ---------------------------------------- |
| 1  | **Yamaguchi 2014**<br/>“Modeling and Discovering Vulnerabilities with Code Property Graphs” | IEEE S\&P | ([sec.cs.tu-bs.de][1])        | 멀티뷰 → 이기종 그래프 통합 원형                      |
| 2  | **Zeng 2020**<br/>“GraphSAINT: Graph Sampling Based Inductive Learning”                     | ICLR      | ([arxiv.org][2])              | 대형 이기종 그래프 미니배치 학습                       |
| 3  | **You 2020**<br/>“Graph Contrastive Learning via Augmentations” (GraphCL)                   | ICML      | ([proceedings.nips.cc][3])    | Self-GCL (InfoNCE) 표현 학습                 |
| 4  | **Cubuk 2019**<br/>“AutoAugment: Learning Augmentation Policies”                            | CVPR      | ([arxiv.org][4])              | 증강 조합·강도 자동 탐색                           |
| 5  | **Khosla 2020**<br/>“Supervised Contrastive Learning”                                       | NeurIPS   | ([proceedings.neurips.cc][5]) | Sup-Contrast 파인튜닝 (NT-Xent)              |
| 6  | **Lin 2023**<br/>“Certifiably Robust Graph Contrastive Learning (RES-GCL)”                  | NeurIPS   | ([arxiv.org][6])              | Edge-Drop Smoothing → radius *r* 보증      |
| 7  | **Devlin 2019**<br/>“BERT: Pre-training of Deep Bidirectional Transformers”                 | NAACL     | ([arxiv.org][7])              | LLM 노드-임베딩 동기화 (Masked-Node CE)          |
| 8  | **Hinton 2015**<br/>“Distilling the Knowledge in a Neural Network”                          | arXiv     | ([arxiv.org][8])              | Teacher → Student SGCN 지식 증류             |
| 9  | **Herath 2022**<br/>“CFGExplainer: Path-Level Explanation for Program Graphs”               | DSN       | ([dinalherath.com][9])        | 경로-기반 XAI (Selector·Ranker)              |
| 10 | **Tishby 2015**<br/>“Deep Learning and the Information Bottleneck Principle”                | arXiv     | ([arxiv.org][10])             | Selector Loss (Fidelity vs. Sparsity) 이론 |
| 11 | **Schulman 2017**<br/>“Proximal Policy Optimization Algorithms”                             | arXiv     | ([arxiv.org][11])             | PPO-Clip 기반 룰(RL) 최적화                    |
| 12 | **Derakhshani 2024**<br/>“Continual Learning on Graphs: Challenges, …”                      | arXiv     | ([arxiv.org][12])             | Continual Sup-Contrast (CIL / DIL)       |

[1]: https://www.sec.cs.tu-bs.de/pubs/2014-ieeesp.pdf?utm_source=chatgpt.com "[PDF] Modeling and Discovering Vulnerabilities with Code Property Graphs"
[2]: https://arxiv.org/abs/1907.04931?utm_source=chatgpt.com "GraphSAINT: Graph Sampling Based Inductive Learning Method"
[3]: https://proceedings.nips.cc/paper_files/paper/2020/file/3fe230348e9a12c13120749e3f9fa4cd-Paper.pdf?utm_source=chatgpt.com "[PDF] Graph Contrastive Learning with Augmentations - NIPS papers"
[4]: https://arxiv.org/abs/1805.09501?utm_source=chatgpt.com "AutoAugment: Learning Augmentation Policies from Data - arXiv"
[5]: https://proceedings.neurips.cc/paper/2020/file/d89a66c7c80a29b1bdbab0f2a1a94af8-Paper.pdf?utm_source=chatgpt.com "[PDF] Supervised Contrastive Learning"
[6]: https://arxiv.org/abs/2310.03312?utm_source=chatgpt.com "Certifiably Robust Graph Contrastive Learning"
[7]: https://arxiv.org/abs/1810.04805?utm_source=chatgpt.com "BERT: Pre-training of Deep Bidirectional Transformers for Language ..."
[8]: https://arxiv.org/abs/1503.02531?utm_source=chatgpt.com "[1503.02531] Distilling the Knowledge in a Neural Network - arXiv"
[9]: https://www.dinalherath.com/papers/2022dsn.pdf?utm_source=chatgpt.com "[PDF] CFGExplainer: Explaining Graph Neural Network-Based Malware ..."
[10]: https://arxiv.org/abs/1503.02406?utm_source=chatgpt.com "Deep Learning and the Information Bottleneck Principle"
[11]: https://arxiv.org/abs/1707.06347?utm_source=chatgpt.com "Proximal Policy Optimization Algorithms"
[12]: https://arxiv.org/pdf/2402.11565?utm_source=chatgpt.com "[PDF] Continual Learning on Graphs: Challenges, Solutions, and ... - arXiv"

## 학습 절차

1. `embeds`
2. `pretrain_selfgcl`
3. `finetune_supcon`
4. `train_res_gcl`

```bash
python -m cli.preprocessing --input-dir data/raw/benign --out . labels --label 0  --csv data/meta.csv
python -m cli.preprocessing --input-dir data/raw/malware --out . labels --label 1 --csv data/meta.csv
# 정상, 악성에 대하여 sha256, label, 파일명을 저장하는 meta.csv를 만들기 위한 명령어

python -m cli.preprocessing --input-dir data/raw --out . --overwrite json
# --json으로 json파일 형식을 읽는것을 명시. view를 생성한다.

# hetero graph 생성 (기존 *.pt를 삭제하려면 --clean)
python -m cli.preprocessing --input-dir data/raw --out . graphs --normalise --rebuild --clean --with-feats

# 이 단계에서 각 데이터셋 디렉터리에 `processed/metadata.pkl` 파일이 생성됩니다.

python -m cli.preprocessing --input-dir data/hetero --out . splits --fallback random --strategy random --json-out split_fold.json
# 학습, 평가, 테스트 데이터 분할

python -m cli.preprocessing --input-dir data/hetero --out . embeds --model-name microsoft/codebert-base --batch-size 64 --device cuda
# graphs 단계에서 생성한 hetero 그래프(`data/hetero`)가 필요합니다.
# embeds 단계에서 토큰 임베딩 차원이 변했다면 기존 encoder 체크포인트를 그대로
# 사용하면 안 됩니다. `--force-reinit` 옵션을 주거나 처음부터 encoder를 다시
# 학습해야 합니다.

python -m cli.pretrain_selfgcl data/hetero \
    --splits split_fold.json \
    --config configs/self_gcl.yaml \
    --epochs 30 \
    --batch-size 256 \
    --embed-dir data/embeds \
    --lr 1e-3 \
    --embed-dir data/embeds \
    --output models/gnn/encoder.pt \
    --plot-path results/train_plot.png

# DataLoader 충돌이 발생한다면 --list-loader 옵션을 사용해 보세요.
# PyG의 DataListLoader를 사용하여 개별 그래프를 리스트로 처리합니다.

# 위 명령을 실행하면 encoder.pt와 함께 그래프 메타데이터가
# models/gnn/encoder.meta.pkl로 저장됩니다. 이 파일에는
# `node_types`, `edge_types`, `in_dims`, `num_relations` 외에도
# `vocab_size`와 `max_ids`가 저장됩니다.
# `vocab_size`나 `max_ids`가 빠진 스냅샷을 사용하면
# `train_res_gcl` 실행 시 오류가 발생하며, 메시지에서
# 재학습 또는 `--force-reinit` 옵션 사용을 안내합니다.

그래프 간 노드 속성 집합을 먼저 검증하며, 불일치 시 경고가 출력됩니다.
`--reprocess` 플래그를 주면 processed 데이터셋을 자동으로 다시 생성합니다.

그래프 파일에 비숫자형 리스트 속성이 있을 경우 자동으로 메타에 저장됩니다.
주소 정보가 없는 노드의 `addr` 속성은 0으로 채워집니다.
1차원 노드 피처 텐서는 로딩 시 자동으로 `(N, 1)` 형식으로 변환됩니다.

`edge_index contains invalid node id` 오류가 발생할 경우 그래프 파일을
다음 스크립트로 정제하면 해결됩니다.

```bash
python scripts/sanitise_graphs.py data/hetero data/hetero_clean
```

그래프 메타데이터의 토큰 사전 크기를 확인하려면 다음 명령을 실행합니다.

```bash
python scripts/generate_metadata_vocab.py graphs data/splits --output meta_vocab.json \
       --label-file labels.csv
```

뷰 JSON 파일로부터 메타 토큰을 추출하려면 다음과 같이 실행합니다.

```bash
python scripts/generate_metadata_vocab.py views path/to/views --output view_vocab.json
```
이 스크립트는 문자열 리스트뿐만 아니라 단일 문자열 필드(예: `"text"`)도
사전에 포함합니다. 생성된 JSON은 노드별 메타 토큰 크기(`{"node": {"attr": 10}}`)
또는 필드별 토큰 목록(`{"attr": ["a", "b"]}`) 두 형식을 모두 지원합니다.

# GNN 학습

# GNN 학습

python -m cli.finetune_supcon \
       --encoder-checkpoint models/gnn/encoder.pt \
       --meta-path models/gnn/encoder_v2.meta.pkl \
       --force-reinit \
       --split "2023Q4" \
       --epochs 100 --batch-size 128 \
       --lr 1e-4 --patience 3 --monitor both \
       --embed-dir data/embeds \
       --plot-path results/finetune_supcon/train.png
# 훈련이 끝나면 새롭게 저장된 메타 스냅샷을 기존 경로에 덮어써야 합니다.
# 예) `cp runs/finetune_supcon/best_model.meta.pkl models/gnn/encoder_v2.meta.pkl`
`--force-reinit` should be used when the fine‑tuning dataset has different
node feature dimensions or metadata from the encoder pre‑training data.
Fine‑tuning requires the token embeddings generated by the `embeds` stage.
If feature dimensions are smaller than expected, re-run that preprocessing
step or provide `--embed-dir` to point to the cached embeddings.
If feature dimensions are larger than the checkpoint expects, the projection
layer will be reinitialised. Run pretraining with the same embeddings to reuse
weights.
If this simple reinitialisation does not resolve loading errors, you must
restart from `pretrain_selfgcl` and run `finetune_supcon` again.
`--meta-path` automatically handles mismatched input layers using the
saved meta snapshot without needing `--force-reinit`.
If omitted, `finetune_supcon` will look for `encoder.pt`'s sibling
`encoder.meta.pkl` and load it automatically.
`--monitor` chooses the metric used for early stopping (`f1`, `auroc`, or `both`).

# RES-GCL 분류기 학습
**임베딩 차원이 달라졌다면 반드시 `pretrain_selfgcl`과 `finetune_supcon`을 다시 실행한 뒤에 이 단계를 수행해야 합니다.**
python -m cli.train_res_gcl \
       --encoder-checkpoint models/gnn/encoder.pt \
       --meta-path models/gnn/encoder.meta.pkl \
       --head-checkpoint models/gnn/supcon_head.pt \
       --splits-dir data/splits \
       --epochs 50 --batch-size 256 \
       --lr 1e-3 \
       --embed-dir data/embeds \
       [--no-embeds] \
       --output models/gnn/res_gcl.pt \
       --force-reinit
`--meta-path`에 지정한 메타 스냅샷이 존재하지 않으면 즉시 `RuntimeError`
가 발생합니다.
`--force-reinit`는 메타 정보를 무시하고 모든 입력 계층을 새로 초기화합니다. 기존 체크포인트와 호환되지 않을 때만 사용해야 합니다.
`train_res_gcl` also checks that every `edge_type` value fits within the
dataset relation count and raises a `ValueError` with the offending file name
when an out-of-range index is found.

# 분류기 head 학습

python -m cli.rulegen_cli feature-mine \
       --graph-dir data/splits/ \
       --labels data/meta.csv \
        --embed-dir data/embeds \
        --classifier-ckpt models/gnn/res_gcl.pt \
        --freq-threshold 10 \
        --out features.json
# 경로/레지스트리/URL 기반 문자열도 함께 추출됩니다.

# 데이터셋 변환 예시
python -m cli.rulegen_cli build-dataset \
       --hetero-dir data/hetero_clean \
       --labels data/meta.csv \
       --out-dir data/rulegen_dataset \
       --meta-path models/gnn/encoder.meta.pkl

Alternatively this can be done programmatically via
``rulegen.build_dataset.build_dataset``.

If `--metadata-vocab` is omitted, the meta snapshot will be converted to
`metadata_vocab.json` under the output directory.

# 강화학습용 feature 추출

python -m cli.rulegen_cli ppo-train \
       --train-features features.json \
       --val-features val_features.json \
       --hint-features hints.json \
       --max-hint-tokens 128 \
       --max-vocab 500 \
       --config configs/rulegen/ppo.yaml \
       --checkpoint models/rulegen/ppo_agent.pt
# Use `--max-vocab` to keep only the N most frequent tokens when
# building the vocabulary from hint features.
# `--max-hint-tokens` limits how many hint tokens are prepended to each
# observation.
# `--val-features` can point to a JSONL or JSON array.  When provided,
# these features are loaded via `_read_json_lines` and used as hints when
# sampling validation rules.
# configs/rulegen/ppo.yaml 의 model.policy_net 으로
# "gru"(기본값) 또는 "gpt2-small" 등의 GPT 모델을 선택할 수 있습니다.
# RL
python -m cli.rulegen_cli ppo-train \
       --train-features features.json \
       --hint-features hints.json \
       --epochs 50000 \
       --checkpoint models/rulegen/ppo_agent.pt \
       --plot-path runs/rulegen/ppo_train.png
# GPT-2 정책 사용 예시
python -m cli.rulegen_cli ppo-train \
       --train-features features.json \
       --policy gpt2 \
       --max-hint-tokens 64 \
       --checkpoint models/rulegen/gpt2_agent.pt

python -m cli.rulegen_cli ppo-train \
       --train-features features.json \
       --dataset-dir data/splits \
       --generate-hints-from-explainer \
       --explainer-checkpoint models/explainers/selector.pt
# When using GPT-based policies, ensure that `max_len + max_hint_tokens`
# does not exceed 1024 so the prompt fits within the model context window.
# 간단한 환경 생성 예시
```python
from rulegen import make_env

# 힌트 문구는 `_rule_tokenize`로 분할되어 토큰 사전이 만들어집니다
env = make_env(hint_features=["import", "pe", "strings", "$a"])
obs, _ = env.reset()  # `reset()` 호출 시 다른 힌트를 전달할 수도 있습니다.
```
# The YARA builder keeps at least one real feature even when token
# extraction fails. Short hint tokens such as `pe` are accepted
# without padding.

```bash
# explainer output evaluation (combo mode by default)
python -m src.cli.explainer_rule_eval \
    --graph graph.pt --sample sample.bin \
    --saliency sal.pt --classifier models/gnn/res_gcl.pt

# retry with gradual threshold adjustments
python -m src.cli.explainer_rule_eval \
    --graph graph.pt --sample sample.bin \
    --saliency sal.pt --classifier models/gnn/res_gcl.pt \
    --fp-retries 2 --freq-threshold-step 1 --comb-ratio-step 0.2

# enforce self-detection by relaxing thresholds
python -m src.cli.explainer_rule_eval \
    --graph graph.pt --sample sample.bin \
    --saliency sal.pt --classifier models/gnn/res_gcl.pt \
    --enforce-self-detect --freq-threshold-step 1 --chunk-size-step 2

# stop FP retries after 30 seconds
python -m src.cli.explainer_rule_eval \
    --graph graph.pt --sample sample.bin \
    --saliency sal.pt --classifier models/gnn/res_gcl.pt \
    --fp-timeout 30

# require at least two matches per group
python -m src.cli.explainer_rule_eval \
    --graph graph.pt --sample sample.bin \
    --saliency sal.pt --classifier models/gnn/res_gcl.pt \
    --group-min-count 2

# count condition example
python -m src.cli.explainer_rule_eval \
    --graph graph.pt --sample sample.bin \
    --saliency sal.pt --classifier models/gnn/res_gcl.pt \
    --condition-type count --min-count 3
# exclude specific tokens when generating
python -m src.cli.explainer_rule_eval \
    --graph graph.pt --sample sample.bin \
    --saliency sal.pt --classifier models/gnn/res_gcl.pt \
    --exclude-tokens foo bar
# periodically flush results to CSV during batch evaluation
python -m src.cli.explainer_rule_eval \
    --graph-dir graphs --meta-csv meta.csv \
    --classifier models/gnn/res_gcl.pt \
    --out-csv results.csv --flush-every 5
```
# XAI selector 학습
# 분류기가 HeteroData 그래프를 입력으로 받아도 동일하게 사용할 수 있습니다.

# 단일 그래프 학습
python -m cli.explainer_train single cfg.pt \
       --model models/gnn/res_gcl.pt \
       --output models/selector.pt \
       --epochs 500 \
       --amp \
       # halves feature precision when enabled
       --full-mini-batch \
       [--no-embeds] [--no-full-score]

# AST 뷰 그래프 학습 예시
python -m cli.explainer_train single cfg.pt \
       --model models/gnn/res_gcl.pt \
       --output models/selector.pt \
       --epochs 500 \
       --ast --view data/views

# 데이터셋 전체 학습 및 특징 추출 예시
python -m cli.explainer_train batch \
        --graph-dir data/splits/train/graphs \
        --meta-csv data/meta.csv \
        --output-dir models/explainers \
        --model models/gnn/res_gcl.pt \
        --amp \
        # halves feature precision when enabled
        --full-cpu \
        [--no-embeds] [--no-full-score]
# PGExplainer global 학습 예시
python -m cli.explainer_train global \
       --graph-dir data/splits/train/graphs \
       --model models/gnn/res_gcl.pt \
       --output models/pgexplainer.pt \
       --epochs 200 \
       --gamma 0.01 \
       --tau-start 1.0 \
       --init-bias 1.0  # entropy weight and bias init
       --beta 0.1  # target sparsity weight
       # beta will increase from 1e-4 to this value during training
       --soft-mask-epochs 5  # train with soft masks for the first N epochs
       --hard-mask-mode weight  # use straight-through weighted masking
       --stability-weight 0.1 --stability-start 10 \
       --necessity-weight 0.05 --necessity-start 20 \
       --necessity-schedule  # weight increases from 1e-4 after start
       --necessity-drop-ratio 0.2 \
#
# `gamma`는 마스크 확률의 엔트로피에 곱해지는 가중치로, 0보다 크게 설정하면
# 탐색을 유도하는 항이 손실 함수에 추가됩니다. 기본값은 0.01이며 값이 너무
# 크면 희소성 학습이 어려워질 수 있습니다.
# 특징 추출만 별도로 실행할 경우
python -m cli.explainer_train feature-mine \
       --model-path models/gnn/res_gcl.pt \
       --dataset-path data/splits/train/graphs \
       --output-path mined.json \
       --embed-dir data/embeds
# 큰 그래프에서 GPU 메모리 부족이 발생할 경우
# `--full-cpu` 또는 `--full-mini-batch` 옵션을 활용해 전체 점수 계산을 조절할 수 있습니다.
# `--cluster-parts`와 `--cluster-batch-size` 옵션을 사용하면 ClusterLoader로 그래프를 분할해 처리할 수 있습니다.
# `--saint {node,edge}` 옵션을 사용하면 GraphSAINT 샘플러로 서브그래프 단위 학습이 가능해 GPU 메모리를 절약할 수 있습니다.
# 캐시된 점수만 사용할 경우 `--no-full-score` 옵션을 지정합니다.
# 필요한 점수는 `scripts/precompute_scores.py` 스크립트로 미리 계산할 수 있습니다.
```

### Validation for global explainer training

`global` 하위 명령에서는 검증 그래프를 지정해 학습 중 성능을 확인할 수 있습니다.
`--val-graph-dir`와 `--val-meta-csv` 옵션을 사용하며 기본값은 각각
`<graph_dir>/../val/graphs`, `<graph_dir>/../val/labels.csv` 입니다.
각 에폭이 끝나면 평균 Fidelity, Sparsity, Stability, Necessity가 다음과 같이 출력됩니다.

```
Epoch 1 Val Fidelity: 0.9123  Val Sparsity: 0.0731  Val Stability: 0.0321  Val Necessity: 0.1452
```

## 단일 샘플 자동 분류 예시

```bash
python scripts/single_sample_classify.py \
    --json-dir path/to/json_dir \
    --meta-csv data/meta.csv \
    --model models/gnn/res_gcl.pt \
    --out result.csv \
    --work-dir ./tmp_work
# JSON의 sha256 값을 읽어 <tmp_work>/data/hetero/<sha>.pt 그래프가 준비됩니다.
```

외부 파이썬 코드에서 동일한 기능을 사용하려면 다음과 같이 `classify_from_json`
함수를 호출하면 됩니다.

```python
from pathlib import Path
import json
from scripts.single_sample_classify import classify_from_json

with open("sample.json", "r", encoding="utf-8") as f:
    js = json.load(f)

label, prob, _ = classify_from_json(js, Path("models/gnn/res_gcl.pt"))
print(label, prob)
```

모델과 입력 그래프의 메타데이터 차원이 다를 경우 자동으로 재초기화 됩니다.
분류 정확도를 위해 학습 당시 사용한 임베딩 설정(`attr_dim`, `vocab_size`,
`model_name`)이 체크포인트와 함께 저장되어야 하며, `classify_from_json`이
이를 읽어 `run_embeds` 단계에 전달합니다.

`meta.csv`는 다음과 같이 생성합니다.
```bash
python -m cli.preprocessing --input-dir ../maldata/benign --out . labels --label 0 --csv data/meta.csv
python -m cli.preprocessing --input-dir ../maldata/malware --out . labels --label 1 --csv data/meta.csv
```
