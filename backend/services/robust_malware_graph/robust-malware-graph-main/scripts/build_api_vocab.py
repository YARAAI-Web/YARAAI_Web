# scripts/build_api_vocab.py

import json
from pathlib import Path
import torch
from tqdm import tqdm
import logging

# 로거 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

# --- 설정 ---
# 원본 그래프 파일이 저장된 경로
GRAPH_DIR = Path("data/splits/train/graphs") 
OUTPUT_PATH = Path("data/api_vocab.json")
# ----------------

def build_vocab():
    """
    그래프 데이터셋을 스캔하여 고유한 API 이름의 사전을 만듭니다.
    """
    if not GRAPH_DIR.is_dir():
        LOGGER.error(f"오류: 그래프 디렉토리 '{GRAPH_DIR}'를 찾을 수 없습니다.")
        return

    LOGGER.info(f"'{GRAPH_DIR}'에서 그래프를 스캔하여 API 사전을 생성합니다...")
    
    unique_api_names = set()

    graph_paths = list(GRAPH_DIR.glob("*.pt"))
    if not graph_paths:
        LOGGER.error(f"오류: '{GRAPH_DIR}'에서 그래프 파일(.pt)을 찾을 수 없습니다.")
        return

    for gp in tqdm(graph_paths, desc="Scanning Graphs for API names"):
        try:
            # weights_only=False를 사용하여 모든 데이터를 로드합니다.
            g = torch.load(gp, map_location="cpu", weights_only=False)
            if "api" in g.node_types and hasattr(g["api"], "name"):
                # 'api' 노드의 'name' 속성에서 API 이름들을 가져옵니다.
                unique_api_names.update(g["api"].name)
        except Exception as e:
            LOGGER.warning(f"{gp.name} 처리 중 오류 발생: {e}")

    if not unique_api_names:
        LOGGER.warning("경고: 'api' 노드 또는 'name' 속성을 가진 그래프를 찾지 못했습니다.")
        return

    # 정렬된 리스트로 변환하여 일관된 순서 보장
    sorted_names = sorted(list(unique_api_names))
    
    # <UNK>: 사전에 없는 API를 위한 특수 토큰 (0번 인덱스)
    vocab = {"<UNK>": 0}
    for i, name in enumerate(sorted_names):
        vocab[name] = i + 1

    LOGGER.info(f"총 {len(vocab)}개의 고유한 API를 찾았습니다 ('<UNK>' 포함).")

    # JSON 파일로 저장
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(vocab, f, indent=2, ensure_ascii=False)

    LOGGER.info(f"API 사전이 '{OUTPUT_PATH}'에 성공적으로 저장되었습니다.")

if __name__ == "__main__":
    build_vocab()
