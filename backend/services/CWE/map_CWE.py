import os
import json
import csv

# ✅ CWE CSV 로드
def load_cwe_from_local(csv_path="1000.csv") -> dict:
    cwe_map = {}
    with open(csv_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["Name"].strip().lower()
            cwe_id = f"CWE-{row['CWE-ID']}"
            mitigation = row.get("Potential Mitigations", "").strip()
            cwe_map[name] = (cwe_id, mitigation)
    return cwe_map

# ✅ 코드에 CWE 키워드 매칭
def match_keywords_to_cwe(code_lines, cwe_name_map):
    code_text = "\n".join(code_lines).lower()
    matched = []

    for name, (cwe_id, mitigation) in cwe_name_map.items():
        keywords = name.split()
        match_score = sum(1 for word in keywords if word in code_text)
        if len(keywords) > 0 and (match_score / len(keywords)) >= 0.85:
            matched.append((name, cwe_id, mitigation))
    return matched


# ✅ 메인 실행
def analyze_code_with_cwe(data, csv_path=r"services\CWE\1000.csv"):
    code_lines = data.get("c_code", []) + data.get("h_code", [])

    # CWE 매핑 및 요약
    cwe_map = load_cwe_from_local(csv_path)
    matched = match_keywords_to_cwe(code_lines, cwe_map)

    # 결과 출력
    print("=" * 60)
    return matched

# ✅ 실행 예시
if __name__ == "__main__":
    file_path = r"D:\Whitehat\web\YARRAI_Web\backend\services\c_h_json\0002a66b-387b-4748-8413-7047c2176a56.json"
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
        code_lines = data.get("c_code", []) + data.get("h_code", [])
    # 분석 대상 JSON 경로
    analyze_code_with_cwe(file_path)