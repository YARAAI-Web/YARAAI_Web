import os
import subprocess
import json
import time
import hashlib
import requests

IDA_PATH = r"C:\Program Files\IDA Professional 9.1\ida.exe"
IDA_SCRIPT = os.path.abspath("ida_mcp_launcher.py")
OUTPUT_DIR = os.path.abspath("c_h_json")

# VirusTotal API 설정
VT_API_KEY = "a77ca95701181d9b2b3578c424fdcf8e85f85723e347f4c9cbcf5a2f9f7b0d34"  # ← 직접 복붙한 API 키
VT_ENDPOINT = "https://www.virustotal.com/api/v3/files/{}"

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def query_virustotal(file_path):
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
                "tags": attrs.get("tags", [])
            }
        else:
            return {"sha256": sha256, "error": res.status_code}
    except Exception as e:
        return {"sha256": sha256, "error": str(e)}

def inject_c_and_h_to_json(file_path):
    base = os.path.splitext(os.path.basename(file_path))[0]
    parent = os.path.dirname(file_path)

    c_path = os.path.join(parent, f"{base}.c")
    h_path = os.path.join(parent, f"{base}.h")
    json_path = os.path.join(OUTPUT_DIR, f"{base}.json")

    def safe_read_lines(p):
        return open(p, encoding='utf-8').read().splitlines() if os.path.exists(p) else []

    # VirusTotal 결과 조회
    vt_result = query_virustotal(file_path)

    result = {
        "c_code": safe_read_lines(c_path),
        "h_code": safe_read_lines(h_path),
        "virustotal": vt_result
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ 저장 완료: {json_path}")

def analyze_file(file_path):
    print(f"\n[+] 분석 시작: {file_path}")
    ida_cmd = f'"{IDA_PATH}" -A -S"{IDA_SCRIPT}" "{file_path}"'
    subprocess.run(ida_cmd, shell=True)

    # IDA C/H 파일 생성 대기
    for _ in range(20):
        c_file = file_path.replace(".exe", ".c").replace(".dll", ".c")
        h_file = file_path.replace(".exe", ".h").replace(".dll", ".h")
        if os.path.exists(c_file) and os.path.exists(h_file):
            break
        time.sleep(0.5)
    
    inject_c_and_h_to_json(file_path)