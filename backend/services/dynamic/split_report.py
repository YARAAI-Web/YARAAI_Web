import os
import json

# ✅ section별 JSON 파일 분리 저장 함수
def split_report_sections(report_json: dict, uuid: str, output_dir: str, chunk_size: int = 10):
    os.makedirs(output_dir, exist_ok=True)

    # 📁 저장할 각 섹션 정의
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
        "behavior_parts": []  # 나중에 part 번호만 저장
    }

    # 🔪 behavior.processes 분할 저장
    processes = report_json.get("behavior", {}).get("processes", [])
    for i in range(0, len(processes), chunk_size):
        chunk = processes[i:i + chunk_size]
        part_num = i // chunk_size + 1
        part = {"behavior": {"processes": chunk}}
        part_filename = f"{uuid}_behavior_part_{part_num}.json"
        part_path = os.path.join(output_dir, part_filename)

        with open(part_path, "w", encoding="utf-8") as f:
            json.dump(part, f, ensure_ascii=False, indent=2)

        # 경로 대신 part 번호 저장
        sections["behavior_parts"].append(part_num)

    # 💾 나머지 섹션 저장
    for key, value in sections.items():
        if key == "behavior_parts":
            continue
        path = os.path.join(output_dir, f"{uuid}_{key}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(value, f, ensure_ascii=False, indent=2)

    # 💾 metadata.output 저장
    metadata_output = report_json.get("metadata", {}).get("output", {})
    output_path = os.path.join(output_dir, f"{uuid}_metadata_output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metadata_output, f, ensure_ascii=False, indent=2)


    return sections
