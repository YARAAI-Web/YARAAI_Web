# backend/services/mcp_collector.py

import os
import json
import subprocess

MAX_STRINGS = 500
# IDA 스크립트가 full_metadata_with_features.json 을 생성하는 위치
# → 여기에 절대 경로로 출력되도록 IDA 스크립트 내에서 세팅하거나, cwd 를 지정합니다.
OUTPUT_JSON = "full_metadata_with_features.json"
IDA_PATH    = r"C:\Program Files\IDA Professional 9.1\ida.exe"
IDA_SCRIPT  = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "ida_mcp_launcher.py")
)

def collect_mcp_strings(file_path: str) -> dict:
    # 1) MCP 플러그인 + 스크립트 실행
    cmd = [
        IDA_PATH,
        "-A",
        f"-S{IDA_SCRIPT}",
        file_path
    ]
    try:
        # cwd 를 프로젝트 루트(혹은 백엔드 working-dir) 로 지정
        subprocess.run(cmd, check=True, cwd=os.path.dirname(__file__) + "/..")
    except Exception as e:
        print(f"⚠️ MCP subprocess 실패: {e}")
        return {}

    # 2) JSON 로드 (cwd 지정한 곳에 생성되어 있을 겁니다)
    if not os.path.isfile(OUTPUT_JSON):
        print(f"⚠️ MCP JSON not found in cwd: {os.getcwd()} → {OUTPUT_JSON}")
        return {}

    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("string_stats", {})
