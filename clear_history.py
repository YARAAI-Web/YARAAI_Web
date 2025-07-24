#!/usr/bin/env python3
# clear_history.py
import shutil
from pathlib import Path

# 프로젝트 루트 경로 (이 스크립트가 위치한 디렉터리)
ROOT = Path(__file__).resolve().parent

# 백엔드 폴더 경로
BACKEND = ROOT / 'backend'

# 초기화할 디렉터리 목록
TARGET_DIRS = [
    BACKEND / 'uploads',
    BACKEND / 'meta_json',
    BACKEND / 'static' / 'callgraphs',
    BACKEND / 'gpt_cache',
]

def clear_and_recreate(path: Path):
    if path.exists():
        shutil.rmtree(path)
        print(f"Deleted: {path}")
    path.mkdir(parents=True, exist_ok=True)
    print(f"Recreated: {path}")

def main():
    for d in TARGET_DIRS:
        clear_and_recreate(d)
    print("\n✅ 히스토리(캐시) 폴더 초기화 완료!")

if __name__ == '__main__':
    main()
