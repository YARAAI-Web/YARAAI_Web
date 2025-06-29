# backend/services/c_h_run.py

import os
import subprocess
import json
import time
import hashlib
import requests

# ─── 설정 ───
# IDA Pro 실행 파일 경로 (환경변수 또는 .env로 관리하는 걸 권장)
IDA_PATH = r"C:\Program Files\IDA Professional 9.1\ida.exe"

# 이 파일(c_h_run.py)이 위치한 디렉터리
SERVICE_DIR = os.path.dirname(os.path.abspath(__file__))

# IDA 스크립트 경로 (ida_mcp_launcher.py 파일을 같은 폴더에 두세요)
IDA_SCRIPT = os.path.abspath("ida_mcp_launcher.py")

# .c/.h → JSON 결과가 저장될 폴더
OUTPUT_DIR = os.path.join(SERVICE_DIR, "c_h_json")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# VirusTotal API 설정 (API 키는 안전하게 보관하세요!)
VT_API_KEY = "a77ca95701181d9b2b3578c424fdcf8e85f85723e347f4c9cbcf5a2f9f7b0d34"
VT_ENDPOINT = "https://www.virustotal.com/api/v3/files/{}"


def get_sha256(filepath: str) -> str:
    """파일의 SHA-256 해시를 계산합니다."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def query_virustotal(file_path: str) -> dict:
    """VirusTotal API에 조회 요청을 보내고, 주요 속성을 반환합니다."""
    sha256 = get_sha256(file_path)
    headers = {"x-apikey": VT_API_KEY}
    url = VT_ENDPOINT.format(sha256)
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            attrs = res.json().get("data", {}).get("attributes", {})
            return {
                "sha256": sha256,
                "type_tag": attrs.get("type_tag"),
                "popular_threat_name": attrs.get("popular_threat_name"),
                "tags": attrs.get("tags", []),
            }
        else:
            return {"sha256": sha256, "error": res.status_code}
    except Exception as e:
        return {"sha256": sha256, "error": str(e)}


def inject_c_and_h_to_json(file_path: str) -> None:
    """
    .c, .h 파일을 읽어 리스트 형태로 담고,
    VirusTotal 결과와 함께 OUTPUT_DIR에 JSON으로 저장합니다.
    """
    base = os.path.splitext(os.path.basename(file_path))[0]
    parent = os.path.dirname(file_path)
    c_path = os.path.join(parent, f"{base}.c")
    h_path = os.path.join(parent, f"{base}.h")
    json_path = os.path.join(OUTPUT_DIR, f"{base}.json")

    def safe_read_lines(path: str) -> list[str]:
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                return f.read().splitlines()
        return []

    result = {
        "c_code": safe_read_lines(c_path),
        "h_code": safe_read_lines(h_path),
        "virustotal": query_virustotal(file_path),
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


def analyze_file(file_path: str) -> None:
    """
    1) IDA Pro를 CLI로 호출해 디스어셈블 + MCP 스크립트 실행
    2) .c/.h 파일이 생성될 때까지 대기
    3) inject_c_and_h_to_json으로 JSON 결과 생성
    """
    print(f"[+] 분석 시작: {file_path}")
    ida_cmd = f'"{IDA_PATH}" -A -S"{IDA_SCRIPT}" "{file_path}"'
    subprocess.run(ida_cmd, shell=True, check=True)

    # C/H 파일 생성 대기
    base_no_ext = os.path.splitext(file_path)[0]
    for _ in range(20):
        if os.path.exists(base_no_ext + ".c") and os.path.exists(base_no_ext + ".h"):
            break
        time.sleep(0.5)

    inject_c_and_h_to_json(file_path)
