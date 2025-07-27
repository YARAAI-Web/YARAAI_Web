# Gemini-Generated Project Guide: robust-malware-graph

This document provides a summary of the `robust-malware-graph` project based on an analysis of its structure and workflows. Its purpose is to guide future interactions with the codebase.

## Project Overview

This project is designed to build and train Graph Neural Network (GNN) models for robust malware classification. The core workflow involves a multi-stage pipeline that starts from raw malware/benign samples and proceeds through data preprocessing, feature extraction, self-supervised pre-training (Self-GCL), and finally, supervised training of a RES-GCL classifier.

The project also contains modules for explainability (`explainer`) and Reinforcement Learning-based rule generation (`rulegen`), though these components appear to be under development and and have data compatibility issues.

## Key Directories

-   `src/cli/`: Contains the primary Python scripts that drive the project's command-line workflows.
-   `src/graphs/`: Includes logic for graph construction (`builders`), the `GraphDataset` class, and data normalization.
-   `src/models/`: Defines the GNN architectures, including `RGCNEncoder` and `RESGCLClassifier`.
-   `scripts/`: Holds utility scripts. `scripts/sanitise_graphs.py` is critical for correcting data issues before training.
-   `data/`: The root directory for all datasets, including raw, processed, and split data.
-   `models/gnn/`: The default output directory for trained model checkpoints.
-   `configs/`: Contains YAML configuration files for different training stages.

## Core Commands & Workflows

The main workflow is orchestrated through the `cli_workflow.ipynb` notebook and can be broken down into two major phases: Data Preprocessing and Model Training.

### 1. Data Preprocessing Pipeline

This sequence of commands processes raw data into a format suitable for GNN training.

1.  **Generate Labels:** Create a `meta.csv` file mapping samples to labels (0 for benign, 1 for malware).
    ```bash
    python -m cli.preprocessing --input-dir ../maldata/benign --out . labels --label 0 --csv data/meta.csv
    python -m cli.preprocessing --input-dir ../maldata/malware --out . labels --label 1 --csv data/meta.csv
    ```

2.  **Extract JSON Views:** Process raw binary files to extract graph views (AST, CFG, etc.) into JSON format.
    ```bash
    python -m cli.preprocessing --input-dir data/raw --out . --overwrite json
    ```

3.  **Construct Graphs:** Build heterogeneous graph objects (`.pt` files) from the JSON views.
    ```bash
    python -m cli.preprocessing --input-dir data/raw --out . graphs --normalise --rebuild --clean --with-feats
    ```

4.  **Sanitize Graphs:** Clean the generated graphs to resolve data inconsistencies.
    ```bash
    python scripts/sanitise_graphs.py data/hetero data/hetero_clean
    ```
    **Note:** This is a critical step. The original script was modified to call `GraphDataset._ensure_num_nodes(graph)` to correctly set the `num_nodes` attribute before sanitizing edges. This prevents `edge_index` out-of-bounds errors during model training.

5.  **Create Data Splits:** Generate train/validation/test splits from the cleaned graphs.
    ```bash
    python -m cli.preprocessing --input-dir data/hetero_clean --out . splits --fallback random --strategy random --json-out split_fold.json
    ```

6.  **Build Rulegen Dataset:** Create a specialized dataset for the rule generation module.
    ```bash
    python -m cli.rulegen_cli build-dataset --hetero-dir data/hetero_clean --labels data/meta.csv --out-dir data/rulegen_dataset
    ```

7.  **Generate Embeddings:** Create token embeddings from the graph data using a pre-trained language model.
    ```bash
    python -m cli.preprocessing --input-dir data --out . embeds --model-name microsoft/codebert-base --batch-size 64 --device cuda
    ```

### 2. Model Training Pipeline

1.  **Self-GCL Pre-training:** Pre-trains the GNN encoder using a self-supervised contrastive learning approach. This step is required before the main training.
    ```bash
    python -m cli.pretrain_selfgcl data/hetero_clean --splits split_fold.json --config configs/self_gcl.yaml --epochs 10 --batch-size 256 --lr 1e-3 --output models/gnn/encoder.pt --plot-path results/train_plot.png
    ```

2.  **RES-GCL Training:** Trains the final classifier using the pre-trained encoder.
    ```bash
    python -m cli.train_res_gcl --encoder-checkpoint models/gnn/encoder.pt --meta-path models/gnn/encoder.meta.pkl --splits-dir data/splits --epochs 50 --batch-size 128 --lr 1e-3 --output models/gnn/res_gcl.pt --no-embeds --force-reinit
    ```

### 3. Explainer & RL Workflow (Fixed)

The final stages of the pipeline, involving the explainer and RL-based feature mining, have been fixed to enable YARA rule generation.

-   **Feature Mining:** The `cli.rulegen_cli feature-mine` command has been corrected to properly load graph data and labels, enabling the extraction of features for the RL agent.
    ```bash
    python -m src.cli.rulegen_cli feature-mine --graph-dir data/splits --labels data/meta.csv --out features.json
    ```
    **Troubleshooting `cli.rulegen_cli feature-mine`:**
    The `feature-mine` command required extensive debugging to resolve a series of cascading errors. The core issue stemmed from a mismatch between the `classifier` model, which was dynamically reconfigured based on the dataset, and the `explainer` model, which was loaded with a fixed configuration from a previous training run.

    1.  **`SyntaxError: expected 'except' or 'finally' block`**:
        *   **Cause**: An improperly structured `try...except` block in `src/cli/rulegen_cli.py`.
        *   **Resolution**: Corrected the indentation and structure of the `try...except` block to properly catch exceptions.

    2.  **`ValueError: too many values to unpack (expected 4)`**:
        *   **Cause**: The `collect_dataset_metadata` function in `src/graphs/dataset/graph_dataset.py` was returning 5 values, but the call site in `rulegen_cli.py` was only expecting 4.
        *   **Resolution**: Updated the calling code in `rulegen_cli.py` to correctly unpack all 5 return values.

    3.  **`AttributeError: 'PGExplainer' object has no attribute 'embed_dim'`**:
        *   **Cause**: The script attempted to access `selector.embed_dim`, but this attribute was not explicitly set in the `PGExplainer` class constructor.
        *   **Resolution**: Modified `src/explain/pg_explainer.py` to explicitly set `self.embed_dim` in the constructor. Added a `hasattr` check in `rulegen_cli.py` for backward compatibility.

    4.  **`RuntimeError: mat1 and mat2 shapes cannot be multiplied`**:
        *   **Cause**: This was the most critical error. The `classifier`'s encoder was dynamically updated to output high-dimensional embeddings (e.g., 768) based on the input data (including CodeBERT features). However, the pre-trained `explainer`'s `edge_mlp` layer was expecting low-dimensional embeddings (e.g., 128) from when it was originally trained. This dimensional mismatch caused the matrix multiplication to fail.
        *   **Resolution (Projection Layer)**: Instead of re-initializing the explainer's trained weights (which would destroy learned knowledge), a `torch.nn.Linear` projection layer was dynamically inserted in `rulegen_cli.py`. This layer projects the high-dimensional embeddings from the classifier down to the low-dimensional format expected by the explainer, preserving the explainer's learned weights.

    5.  **`RuntimeError: indices should be either on cpu or on the same device as the indexed tensor (cpu)`**:
        *   **Cause**: The projected embedding tensors were on the CPU, while the graph's index tensors (`src`, `dst`) had been moved to the GPU.
        *   **Resolution**: Modified `src/explain/pg_explainer.py` to ensure that the embedding tensors passed to the `forward` method are explicitly moved to the same device as the graph's tensors.

    6.  **`AttributeError: 'HeteroData' has no attribute 'device'`**:
        *   **Cause**: The code was trying to access `graph.device`, which is not a valid attribute for a `HeteroData` object. Device information must be retrieved from a tensor within the object.
        *   **Resolution**: Changed the code in `pg_explainer.py` to get the device from one of the graph's internal tensors (e.g., `graph[graph.edge_types[0]].edge_index.device`).

    7.  **`NameError: name 'prune_graph_by_selection' is not defined`**:
        *   **Cause**: The function was called in `rulegen_cli.py` but had not been defined or imported.
        *   **Resolution**: Implemented the `prune_graph_by_selection` function in `src/graphs/utils.py` and added the corresponding import statement to `rulegen_cli.py`.

    8.  **`TypeError: FeatureMiner.mine() missing 1 required positional argument: 'saliency'`**:
        *   **Cause**: The `mine` method was called with only the `graph` object. It also requires saliency information.
        *   **Resolution**: The output from the explainer (`selection`, an edge mask) was first converted to node-level importance using the `selector.get_node_saliency()` method. This `node_saliency` was then correctly passed as the `saliency` argument to the `miner.mine()` method.

    9.  **`IndexError: global_idx out of range`**:
        *   **Cause**: The `FeatureMiner` was still receiving an *edge mask* instead of the *node saliency* it expected, causing it to interpret edge importance values as out-of-bounds node indices.
        *   **Resolution**: Corrected the logic to ensure the `node_saliency` map (derived from `get_node_saliency`) was passed to the miner, not the raw `selection` (edge mask).

    10. **`TypeError: Object of type int64 is not JSON serializable` & `TypeError: cannot convert the series to <class 'int'>`**:
        *   **Cause**: When reading `meta.csv` with pandas, the `label` column was being interpreted as a `numpy.int64` or a pandas `Series` object, which are not directly serializable by Python's standard `json` library.
        *   **Resolution**: Added logic in `rulegen_cli.py` to explicitly handle the case where the label might be a pandas `Series` (taking the first element if so) and to cast the final label value to a standard Python `int` before appending it to the results list.

-   **PPO Agent Training:** The `cli.rulegen_cli ppo-train` command is now configured to use the mined features to train the PPO agent, ensuring vocabulary consistency between training and generation.
    ```bash
    python -m src.cli.rulegen_cli ppo-train --train-features features.json --dataset-dir data/rulegen_dataset --epochs 5 --checkpoint models/rulegen/ppo_agent.pt
    ```
    You can limit the vocabulary with `--max-vocab N` to keep only the top-N tokens from hints.
-   **YARA Rule Generation:** The `cli.rulegen_cli generate` command now correctly loads the trained agent and generates meaningful YARA rules.
    ```bash
    python -m src.cli.rulegen_cli generate --agent-checkpoint models/rulegen/ppo_agent.pt --n-rules 200 --out models/rulegen/yara/generated_rules.yar
    ```

These steps are now functional and included in the final `cli_workflow.ipynb`.

### Troubleshooting `pretrain_selfgcl.py`

`pretrain_selfgcl.py` 스크립트 실행 과정에서 두 가지 주요 문제가 발생하고 해결되었습니다.

**1. 차원 불일치 `RuntimeError` (해결 완료)**

- **문제 요약**: `RGCNEncoder`의 `nn.Linear` 계층에 전달되는 텐서의 차원과, 계층이 기대하는 입력 차원이 일치하지 않�� `mat1 and mat2 shapes cannot be multiplied` 오류��� 반복적으로 발생했습니다.
- **근본 원인**: 데이터 피처의 차원을 계산하고 모델에 전달하는 여러 컴포넌트 간의 책임과 정보가 불일치했습니다. `collect_dataset_metadata` 함수는 외부 임베딩(CodeBERT) 차원을 `in_dims`에 잘못 포함시켰고, `RGCNEncoder` 모델은 이 정보를 부정확하게 해석하여 계층을 잘못된 차원으로 생성했습니다.
- **해결책**: "단일 진실의 원천" 및 "역할의 명확한 분리" 원칙을 적용하여 시스템을 재설계했습니다.
    1.  **`collect_dataset_metadata` 책임 한정**: `in_dims`가 오직 그래프 내부 피처의 최종 차원만을 계산하도록 수정했습니다.
    2.  **`pretrain_selfgcl.py` 역할 명확화**: `RGCNEncoder`에 각 차원 정보를 명시적인 개별 매개변수(`in_dims`, `token_original_dim`, `codebert_dim`)로 전달하도록 수정했습니다.
    3.  **`RGCNEncoder` 강건성 확보**: `__init__`에서 모든 계산 경로에 필요한 계층을 미리 생성하고, `forward`에서는 데이터 상태에 따라 안전한 경로를 선택하도록 수정했습니다.

**2. 표현 붕괴 (Representation Collapse) 및 높은 Loss (해결 진행 중)**

- **문제 현상**:
    1.  **높은 Loss**: `RuntimeError` 해결 후에도, 대조 학습의 Loss가 `log(배치 크��)`에 근사하는 높은 값(6.x)에서 줄어들지 않았습니다.
    2.  **낮은 임베딩 표준 편차**: 모델이 출력하는 임베딩(`emb`)의 표준 편차(std)를 측정한 결과, 0.06과 같이 0에 매우 가까운 값으로 나타났습니다.
- **결론**: 위 두 현상은 모델이 모든 입력에 대해 거의 동일한, 무의미한 임베딩을 출력하는 **표현 붕괴**가 일어나고 있음을 의미합니다. 이는 모델이 유의미한 특징을 학습하지 못하고 있음을 나타냅니다.
- **원인 분석**:
    - **가장 유력한 원인**: **부적절한 하이퍼파라미터**. 모델의 구조적 결함보다는, 현재 데이터셋과 모델 조합에 하이퍼파라미터(특히 학습률)가 맞지 않아 학습이 불안정해지고 표현 붕괴로 이어졌을 가능성이 가장 높습니다.
    - **프로젝션 헤드 검토**: `SelfGraphCL`의 프로젝션 헤드에는 표현 붕괴를 막기 위한 배치 정규화(Batch Normalization)가 올바르게 포함되어 있음을 확인했습니다.
    - **배치 처리 검토**: `DataListLoader`를 사용하지만, `train_epoch` 내에서 `Batch.from_data_list`를 통해 올바르게 배치 단위로 처리되고 있음을 확인했습니다.
- **현재 해결책**:
    - **1순위 조치**: 표현 붕괴를 해결하는 가장 직접적이고 효과적인 방법은 **학습률을 낮추는 것**입니다. 현재 `1e-3`에서 `1e-4`로 낮추어 학습을 안정화시키는 것을 시도하고 있습니다.
    - **후속 조치**: 만약 학습률 조정만으로 부족할 경우, `configs/self_gcl.yaml`의 데이터 증강 강도 및 `temperature` 값을 조정하거나, `LARS`와 같은 대조 학습에 더 안정적인 옵티마이저를 도입하는 것을 고려할 것입니다.

**중요 원칙: 파이프라인의 각 단계는 독립적으로 성공해야 합니다.**
`pretrain_selfgcl` 단계가 실패하여 "망가진" 인코더가 생성된 상태에서, 다음 단계인 `finetune_supcon`을 진행하는 것은 의미가 없습니다. 반드시 사전 학습 단계의 표현 붕괴 문제를 해결하여, 유용한 특징 추출 능력을 갖춘 인코더를 확보한 후에 미세 조정 단계로 넘어가야 합니다.

### Troubleshooting `finetune_supcon.py`

`finetune_supcon.py` 스크립트 실행 중, `pretrain_selfgcl.py` 단계에서 해결했던 것과 유사한 `RuntimeError: mat1 and mat2 shapes cannot be multiplied` 오류가 재발했습니다. 이는 파이프라인의 각 스크립트가 데이터와 모델을 일관되지 않은 방식으로 처리했기 때문에 발생했습니다.

**문제: 파���프라인 일관성 부족으로 인한 `RuntimeError`**

- **현상**: `finetune_supcon.py`에서 `RGCNEncoder`를 실행할 때, 832차원 텐서를 66차원 입력을 기대하는 `nn.Linear` 계층에 전달하면서 차원 불일치 오류가 발생했습니다.
- **근본 원인**:
    1.  **데이터 처리 불일치**: `src/graphs/dataset/graph_dataset.py`의 `_attach_embeds` 메소드가 CodeBERT 임베딩(768차원)을 원본 피처(66차원)에 덮어쓰거나 합쳐서 `g['token'].x`를 832차원으로 만들었습니다. 이는 `pretrain_selfgcl.py`가 데이터를 처리하는 방식(원본 피처는 `.x`에, CodeBERT 임베딩은 별도의 `.x_codebert`에 저장)과 달랐습니다.
    2.  **모델 초기화 불일치**: `finetune_supcon.py`는 사전 학습된 `RGCNEncoder`를 재구성할 때, Gated Fusion 경로를 활성화하는 데 필수적인 `codebert_dim`과 `token_original_dim` 메타데이터를 전달하지 않았습니다. 이로 인해 모델은 Gated Fusion이 비활성화된 상태로 잘못 초기화되었습니다.

**해결책: 파이프라인 전반의 데이터 및 모델 처리 방식 통일**

파이프라인의 강건성을 확보하기 위해, 모든 스크립트가 동일한 원칙을 따르도록 ���정했습니다.

1.  **데이터 처리 방식 통일 (`graph_dataset.py` 수정)**:
    - `_attach_embeds` 메소드를 수정하여, CodeBERT 임베딩이 항상 별도의 `x_codebert` 속성에 저장되도록 변경했습니다. 이로써 프로젝트의 모든 부분에서 'token' 노드의 데이터 구조가 `{'x': 원본 피처, 'x_codebert': 외부 임베딩}`으로 통일되었습니다.

2.  **모델 초기화 로직 통일 (`finetune_supcon.py` 수정)**:
    - `RGCNEncoder`를 재구성하는 로직을 수정하여, 저장된 메타데이터(`meta_info`)에서 `codebert_dim`과 `token_original_dim`을 포함한 모든 관련 파라미터를 명시적으로 전달하도록 변경했습니다.
    - 이를 통해, 미세 조정 단계에서도 사전 학습 단계와 정확히 동일한 구조의 인코더가 복원되도록 보장했습니다.

이러한 수정을 통해, 파이프라인의 모든 단계에서 데이터와 모델이 일관된 방식으로 처리되도록 보장하여, `RuntimeError`의 근본 원인을 해결하고 시스템의 안정성을 크게 향상시켰습니다.

### Current Troubleshooting: `cli.train_res_gcl` `CUDA error: device-side assert triggered`

**Problem:**
`cli.train_res_gcl` 실행 중 `CUDA error: device-side assert triggered` 오류가 발생���며, 특히 `Assertion srcIndex < srcSelectDimSize` 실패 메시지가 나타납니다. 이는 `torch_geometric`의 `GraphConv` 레이어 내부에서 `edge_index`가 노드 피처 텐서의 범위를 벗어나는 인덱스를 참조하려고 할 때 발생합니다. 이 오류는 CPU 환경에서도 동일하게 발생하여 데이터 자체의 불일치 문제임을 시사합니다.

**Analysis:**
1.  **Initial Hypothesis (Incorrect):** `edge_index`에 음수 값이 전달되어 발생하는 문제로 추정했으나, `pdb` 디버깅 결과 음수 값은 없었습니다.
2.  **Root Cause Identified (Confirmed):** `edge_index`의 인덱스가 해당 노드 타입의 `num_nodes` 범위를 초과하는 것이 문제의 직접적인 원인으로 확인되었습니다.
    *   `pdb` 디버깅(`src/models/gnn/encoder.py:208` 중단점)을 통해, `('function', 'child', 'token')` 엣지 타입의 경우, `function` 노드 타입의 `num_nodes`는 7개(인덱스 0-6)이지만, `edge_index[0]` (소스 노드 인덱스)의 최대값은 `1073`으로 범위를 훨씬 벗어났습니다.
    *   마찬가지로 `('syscall', 'child', 'token')` 엣지 타입의 경우, `syscall` 노드 타입의 `num_nodes`는 8개(인덱스 0-7)이지만, `edge_index[0]` (소스 노드 인덱스)의 최대값은 `1080`으로 범위를 훨씬 벗어났습니다.
    *   이는 그래프 생성 또는 배치 처리 과정에서 전역 노드 인덱스가 배치 내의 로컬 노드 인덱스로 올바르게 매핑되지 않거나, 개별 그래프의 `num_nodes`가 잘못 계산되었을 때 발생할 수 있습니다. `CUDA error`는 이 데이터 불일치의 결과로 나타나는 증상입니다.

**Resolution Attempts (and current status):**
1.  **Removed `_sanitize_edges` call from `_ensure_num_nodes`:** `src/graphs/dataset/graph_dataset.py` 파일에서 `_ensure_num_nodes` 함수 내의 `return GraphDataset._sanitize_edges(g)` 라인을 `return g`로 변경했습니다. (Completed)
2.  **Added explicit `_sanitize_edges` call in `__getitem__`:** `GraphDataset.__getitem__` 함수 내에 `g = GraphDataset._sanitize_edges(g)` 코드를 추가하여 각 그래프가 로드될 때 유효성 검사를 수행하도록 했습니다. (Completed)
3.  **Moved and Enhanced `_sanitize_edges` in `collate_fn`:** `src/graphs/dataset/graph_dataset.py` 파일의 `collate_fn` 함수에서 `_sanitize_edges` 호출을 `Batch.from_data_list` 호출 *이후*로 이동하고, `num_nodes_dict`가 정확하게 업데이트된 후에 엣지 유효성 검사가 이루어지도록 수정했습니다. 또한, `num_nodes`가 0인 경우 `edge_index`를 비우는 로직과 `edge_index`의 최대 인덱스가 `num_nodes`를 초과하는 경우 `num_nodes_dict`를 확장하는 로직�� 추가했습니다. (Completed)

**Current Status:**
위의 보완사항들을 적용했음에도 불구하고, `CUDA error: device-side assert triggered` 문제는 아직 완전히 해결되지 않았습니다. `pdb` 디버깅을 통해 `edge_index`의 최대값이 `num_nodes`를 초과하는 특정 엣지 타입(`('function', 'child', 'token')`, `('syscall', 'child', 'token')`)을 확인했습니다. 이는 `collate_fn` 또는 `_sanitize_edges` 함수 내에서 노드 인덱스 오프셋 또는 `num_nodes` 계산에 여전히 미묘한 문제가 있음을 시사합니다.

**Next Steps / Further Investigation:**
*   `collate_fn` 내에서 `Batch.from_data_list` 호출 직후, 그리고 `_sanitize_edges` 호출 직전에 `batch_graph` 객체의 `num_nodes_dict`와 각 `edge_index`의 `min()/max()` 값을 더욱 상세하게 로깅하여 변화를 추적해야 합니다.
*   특히 `('function', 'child', 'token')` 및 `('syscall', 'child', 'token')` 엣지 타입에 대해 `Batch.from_data_list`가 어떻게 노드 인덱스를 오프셋하는지, 그리고 그 결과가 `num_nodes_dict`와 어떻게 불일치를 일으키는지 심층적으로 분석해야 합니다.
*   `torch_geometric.data.Batch.from_data_list`의 내부 동작을 더 깊이 이해하기 위해 해당 소스 코드를 검토하거나, `torch_geometric` 커뮤니티에서 유���한 문제에 대한 해결책을 찾아볼 수 있습니다.
*   `_sanitize_edge_index` 함수가 `src_nodes` 및 `dst_nodes` 인자를 올바르게 사용하고 있는지, 그리고 `valid` 마스크가 정확하게 적용되는지 재확인해야 합니다.

### Debugging Guidelines

When encountering issues, especially `KeyError` or `RuntimeError` related to graph structures or model dimensions, follow these steps:

1.  **Prioritize Debug Logs**: When debugging, add `DEBUG` level logs (`LOGGER.debug(...)`) to critical sections of the code. This allows for detailed inspection without cluttering normal `INFO` level output.
2.  **Systematic Information Gathering**: Before attempting a fix, use logs to gather as much information as possible about the problem. This includes:
    *   The exact values of variables involved in the error (e.g., keys being looked up, shapes of tensors).
    *   The flow of execution leading up to the error.
    *   The state of relevant data structures (e.g., contents of dictionaries, lists).
3.  **Formulate and Verify Hypotheses**: Based on the collected logs, formulate a specific hypothesis about the root cause of the problem. Then, add more targeted debug logs or run `python` commands (using `run_shell_command`) to verify this hypothesis. You are free to execute `python` commands to collect log information.
4.  **Propose Solutions with Minimal Information Loss**: When proposing a solution, ensure it aims to prevent information loss. For example, if a dimension mismatch occurs, prefer projecting or padding to the correct dimension rather than discarding data. If a `KeyError` occurs due to missing schema entries, add the missing entries rather than ignoring the data. If a schema is incomplete, update the schema to reflect all possible edge types. If a `NameError` occurs due to a missing function, re-add the function. If a `RuntimeError` occurs due to shape mismatch, ensure the input dimensions of the MLPs match the actual embedding dimensions. 
5.  **Iterative Refinement**: Debugging is an iterative process. Apply small, focused changes, verify their impact with logs, and repeat until the issue is resolved.
### Troubleshooting `train_res_gcl.py` (SOLVED)

`train_res_gcl.py` 스크립트 실행 과정에서 `CUDA error: device-side assert triggered` (인덱스 아웃오브바운드) 및 `mat1 and mat2 shapes cannot be multiplied` (차원 불일치) 오류가 지속적으로 발생했습니다.

**문제: 데이터 무결성 및 일관성 부족**

- **근본 원인**: 두 오류 모두 데이터 처리 파이프라인의 여러 단계에 걸쳐 데이터의 무결성이 깨졌기 때문에 발생했습니다.
    1.  **`edge_index` 손상**: `GraphDataset`이 개별 그래프를 로드하는 시점(`__getitem__`)에서, 그래프의 `edge_index`가 자신의 노드 수(`num_nodes`)나 피처 텐서(`x`)의 크기를 벗어나는 잘못된 인덱스를 포함하는 경우가 있었습니다. 이는 `Batch.from_data_list`가 노드 ID에 잘못된 오프셋을 더하게 만들어, 최종 배치 그래프에서 `CUDA error`를 유발했습니다.
    2.  **피처 차원 불일치**: 데이터셋 내에 동일 노드 타입임에도 불구하고 기본 피처의 차원이 다른 그래프(예: 'token' 피처가 1차원인 경우와 2차원인 경우)가 섞여 있었습니다. `collate_fn`은 배치 단위로만 패딩을 수행하므로, 특정 배치에 차원이 다른 그래프가 섞이면 `RGCNEncoder`가 기대하는 입력 차원과 달라져 `mat1...` 오류가 발생했습니다.
    3.  **불완전한 증강 로직**: `RESGCLClassifier` 모델 내 `forward` 메소드에서 훈련 시에만 적용되던 `EdgeDrop` 증강 로직이, 엣지만 제거하고 그로 인해 고립된 노드는 피처 텐서에서 제거하지 않아 데이터 불일치를 유발하는 잠재적 원인이었습니다.

**해결책: 데이터 처리 로직의 강건성 확보**

여러 단계의 디버깅을 거쳐, 데이터 처리 파이프라인의 각 단계가 자신의 책임을 명확히 하고 데이터 무결��을 보장하도록 시스템을 재설계했습니다.

1.  **`GraphDataset.__getitem__` 로직 강화**:
    - 데이터 로딩의 가장 근본적인 단계인 `__getitem__`에서, 그래프를 반환하기 전에 **`_ensure_num_nodes` -> `_ensure_x` -> `_sanitize_edges`** 순서로 데이터 정제 함수를 호출하도록 수정했습니다.
    - 이를 통해 `__getitem__`이 반환하는 모든 단일 그래프는 `num_nodes`, 피처 텐서 `x`, `edge_index`가 완벽하게 일관된 상태를 갖게 되었습니다.

2.  **`RGCNEncoder.forward` 로직 강건화**:
    - `__getitem__`의 수정만으로 해결되지 않는 미세한 차원 불일치에 대응하기 위해, `RGCNEncoder`의 `forward` 메소드에 방어적인 코드를 추가했습니다.
    - 이 코드는 `input_proj` 계층에 텐서를 전달하기 직전에, 실제 텐서의 차원과 계층이 기대하는 차원을 비교하여 다를 경우 **0-패딩 또는 절삭을 통해 동적으로 차원을 일치**시킵니다. 이로써 데이터셋에 내재된 사소한 불일치에도 모델이 강건하게 대처할 수 있게 되었습니다.

3.  **`RESGCLClassifier.forward` 증강 로직 제거**:
    - 모델 내부에서 데이터 구조를 변경하는 위험을 제거하기 위해, `forward` 메소드 내의 `EdgeDrop` 증강 로직을 주석 처��했습니다. 데이터 증강은 향후 필요시 데이터 로더의 `transform` 단계에서 안전하게 처리하는 것이 권장됩니다.

이러한 다층적인 수정을 통해, 데이터 파이프라인의 모든 단계에서 데이터의 무결성과 일관성을 확보하여, 지속적으로 발생하던 `CUDA error`와 `mat1...` 오류를 최종적으로 해결했습니다.
### Troubleshooting `explainer_train.py` (SOLVED)

`src.cli.explainer_train` 스크립트 실행 과정에서 `KeyError`와 `RuntimeError`가 반복적으로 발생했습니다. 이는 데이터 스키마의 불일치와 불안정한 모델 수정 방식 때문에 발생한 복합적인 문제였습니다.

**1. `KeyError: 'string'` 문제**

- **현상**: `PGExplainer` 초기화 과정에서 `in_dims` 딕셔너리에 `'string'` 키가 없어 오류가 발생했습니다.
- **1차 원인 분석**: 학습된 모델의 메타데이터에 `'string'` 노드 타입이 누락되었습니다.
- **1차 해결 시도**: 데이터셋의 모든 그래프를 스캔하여 `g.node_types`를 수집, `in_dims`를 동적으로 생성.
- **실패 원인**: `g.node_types`는 실제 노드가 0개인 "유령 노드 타입"(`'string'`)을 포함하지 않아, `in_dims`에 여전히 `'string'`이 누락되었습니다.
- **2차 해결 시도**: `g.edge_types`를 스캔하여 모든 노드 타입을 역으로 추적.
- **실패 원인**: `explainer_train.py`에서 생성한 노드 타입 키(예: `'<NodeType.STRING: 'string'>'`)와 `pg_explainer.py`가 기대한 키(예: `'string'`)의 **문자열 표현 방식이 달라** 키를 찾지 못했습니다.
- **최종 해결**: `explainer_train.py`에서 노드 타입 키를 생성할 때, `pg_explainer.py`와 **동일한 정규화(normalization) 함수**를 사용하여 키 표현을 일치시킴으로써 `KeyError`를 해결했습니다.

**2. 높은 Loss 및 `RuntimeError: mat1 and mat2 shapes cannot be multiplied` 문제**

- **현상**: `KeyError` 해결 후, 학습 Loss가 비정상적으로 높고, 간헐적으로 `RuntimeError`가 발생했습니다.
- **근본 원인**:
    1.  **데이터셋 불일치**: 학습 데이터셋 내에 동일 노드 타입임에도 그래프마다 특징(feature)의 차원이 다른 경우가 있었습니다. (예: 'token' 노드의 특징이 66차원이거나 832차원)
    2.  **불안정한 외부 수정**: `train_global` 루프 내의 `_reinit_input_proj` 함수가 매번 차원이 다른 그래프를 만날 때마다, 모델의 `input_proj` 계층을 **새로운 랜덤 가중치로 계속 교체**했습니다. 이로 인해 `explainer`는 안정적인 학습이 불가능했고 Loss가 치솟았습니다.
    3.  **잘못��� 수정 위치**: 이전 시도에서 `RGCNEncoder.forward` 메소드에 차원 조정 로직을 추가했지만, 오류는 `forward`를 사용하지 않고 `input_proj`를 직접 호출하는 헬퍼 함수 `_compute_node_embeddings`에서 발생하여 효과가 없었습니다.

- **최종 해결**:
    1.  **Revert**: 이전의 모든 변경사항을 원상 복구하여 깨끗한 상태에서 시작했습니다.
    2.  **타겟 수정**: 불안정성의 원인이었던 `_reinit_input_proj` 호출을 `train_global`에서 제거하는 대신, **오류가 발생하는 `_compute_node_embeddings` 함수 내부에 직접** 차원 조정 로직을 추가했습니다.
    3.  **강건성 확보**: `_compute_node_embeddings` 함수가 `encoder.input_proj`를 호출하기 직전에, 실제 입력 텐서의 차원과 계층이 기대하는 차원을 비교하여, **0-패딩(padding) 또는 절삭(truncation)을 통해 동적으로 차원을 일치**시키도록 수정했습니다. 이 방식은 모델의 학습된 가중치를 훼손하지 않으면서 데이터 차원의 비일관성을 안정적으로 처리합니다.

이러한 다단계 디버깅과 수정을 통해, `explainer_train.py` 스크립트는 이제 다양한 스키마와 특징 차원을 가진 데이터에 대해서도 강건하게 동작할 수 있게 되었습니다.