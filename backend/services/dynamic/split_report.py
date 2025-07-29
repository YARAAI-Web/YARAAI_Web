import os
import json

# ✅ section별 JSON 파일 분리 저장 함수
def split_report_sections(report_json: dict, uuid: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    # 기본 섹션 저장
    sections = {
        "summary": {
            "target": report_json.get("target", {}),
            "static": report_json.get("static", {})
        },
        "signatures": {
            "signatures": report_json.get("signatures", [])
        },
        "network": {
            "network": report_json.get("network", {})
        },
        "screenshots": {
            "screenshots": report_json.get("screenshots", [])
        },
        "behavior_parts": []
    }

    # behavior를 10개 단위로 나눠서 저장
    processes = report_json.get("behavior", {}).get("processes", [])
    for i in range(0, len(processes), 10):
        chunk = processes[i:i + 10]
        part = {"behavior": {"processes": chunk}}
        part_path = os.path.join(output_dir, f"{uuid}_behavior_part_{i // 10 + 1}.json")
        with open(part_path, "w", encoding="utf-8") as f:
            json.dump(part, f, ensure_ascii=False, indent=2)
        sections["behavior_parts"].append(part_path)

    # 나머지 섹션 저장
    for key, value in sections.items():
        if key == "behavior_parts":
            continue
        path = os.path.join(output_dir, f"{uuid}_{key}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(value, f, ensure_ascii=False, indent=2)

    return sections
