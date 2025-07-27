from pathlib import Path
import json
from typing import Any, Dict
import os

def load_yar_files(dir_path) -> dict[str, str]:
    yar_dict: dict[str, str] = {}
    base = Path(dir_path)

    # .yar 파일만 순회
    for yar_file in base.glob('*.yar'):
        # 텍스트로 읽어들이되, 인코딩 오류는 무시
        content = yar_file.read_text(encoding='utf-8', errors='ignore')
        yar_dict[yar_file.name] = content

    return yar_dict

def save_dict_as_json(data: Dict[str, Any], filepath: str) -> None:
    """
    파이썬 딕셔너리 `data`를 JSON 형태로 `filepath`에 저장한다.
    
    :param data: 저장할 딕셔너리
    :param filepath: 출력할 JSON 파일 경로 (예: "output.json")
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(
            data, 
            f, 
            ensure_ascii=False,  # 한글이 깨지지 않도록
            indent=4             # 보기 좋은 들여쓰기
        )

def yara_matches(pattern):
    print('yara 추출')
    yar_rules = load_yar_files('services\yara_rules\data')
    save_dict_as_json(yar_rules, "yar_rules.json")
    
    yar_list = []
    for i in pattern:
        for j in yar_rules:
            if i in yar_rules[j]:
                yar_list.append(yar_rules[j])
    print(yar_list)
    return yar_list
    

if __name__ == "__main__":
    data_directory = "./data"
    yar_rules = load_yar_files(data_directory)
    pattern = 'FlushFileBuffers'
    # 결과 확인
    for fname, text in yar_rules.items():
        print(f"{fname} -> {len(text)} bytes")
    
    save_dict_as_json(yar_rules, "yar_rules.json")
    yar_list = []
    for i in yar_rules:
        if pattern in yar_rules[i]:
            yar_list.append(yar_rules[i])

    print(yar_list)