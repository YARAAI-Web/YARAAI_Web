import http.client
import json
import os
import math
import re
import time
from collections import Counter

# ——————————————————————————————————————————————————
# 이 부림 양 조절
MAX_FUNCTIONS = 0  # 가능한 모든 함수를 가져옵니다
MAX_STRINGS   = 0  # 가능한 모든 문자열을 가져옵니다
OUTPUT_JSON   = "full_metadata_with_features.json"

class ID:
    def __init__(self):
        self._ = 0

conn = http.client.HTTPConnection("localhost", 13337)
headers = {"Content-type": "application/json"}
id_value = ID()

def clean_pseudocode_line(line: str) -> str:
    line = re.sub(r"/\*.*?\*/", "", line)
    line = re.sub(r"//.*$", "", line)
    return line.strip()

def call_mcp(method, params=None):
    req_id = id_value._
    payload = {
        "jsonrpc": "2.0",
        "id": req_id,
        "method": method,
        "params": params or {}
    }
    try:
        conn.request("POST", "/mcp", body=json.dumps(payload), headers=headers)
        response = conn.getresponse()
        raw = response.read().decode()
        data = json.loads(raw)
    except Exception as e:
        print(f"⚠️ [MCP] 요청 실패: method={method}, id={req_id} → {e}")
        return None

    id_value._ += 1
    if data is None or "error" in data:
        if data and "error" in data:
            print(f"⚠️ [MCP] 에러 응답: {data['error']}")
        return None
    return data.get("result", None)

def shannon_entropy(blob: bytes) -> float:
    if not blob:
        return 0.0
    cnt = Counter(blob)
    total = len(blob)
    return -sum((v / total) * math.log2(v / total) for v in cnt.values())

def is_dummy_function(name: str, size: int, xref_count: int, instr_count: int, pseudocode: list) -> bool:
    entry_names = {
        "main", "WinMain", "start", "DllMain",
        "__tmainCRTStartup", "WinMainCRTStartup",
        "pre_c_init", "pre_cpp_init",
        "__mingw_invalidParameterHandler"
    }

    # 무조건 살아남는 함수
    if name in entry_names or name.startswith("loc_"):
        return False

    # 디컴파일 실패
    if not pseudocode or pseudocode == ["⚠️ pseudocode 실패"]:
        return True

    # 조건 완화 (xref 적고, 명령도 적고, 사이즈도 작고, return밖에 없음)
    if xref_count == 0 and instr_count <= 3 and size <= 32:
        if all("return" in line or line.strip() == "" for line in pseudocode):
            return True

    # 이름으로 더미 의심되는 함수
    dummy_keywords = ["default", "invalid", "unused", "junk", "_null", "dead", "_empty", "_pad"]
    if any(kw in name.lower() for kw in dummy_keywords):
        return True

    return False

def mcp_run():
    results = {}

    print("[*] get_metadata 호출 중...")
    meta = call_mcp("get_metadata") or {}
    results["get_metadata"] = meta

    for m in ["get_current_address", "get_current_function", "get_entry_points"]:
        print(f"[*] {m} 호출 중...")
        results[m] = call_mcp(m) or {}

    file_path = meta.get("path")
    file_entropy = None
    string_stats = {}
    if file_path and os.path.isfile(file_path):
        with open(file_path, "rb") as f:
            blob = f.read()
        file_entropy = shannon_entropy(blob)

        print(f"[*] list_strings 호출 중 (filter='', count={MAX_STRINGS})...")
        strs = call_mcp("list_strings", {"filter": "", "offset": 0, "count": MAX_STRINGS}) or {}
        data = strs.get("data", [])
        lengths = [len(item.get("text", "")) for item in data]
        string_stats = {
            "string_count": len(lengths),
            "avg_str_len": sum(lengths) / len(lengths) if lengths else 0,
            "max_str_len": max(lengths) if lengths else 0
        }
    else:
        print("⚠️ get_metadata에서 파일 경로를 모험 가지오거나, 해당 파일이 없습니다.")

    results["file_entropy"] = file_entropy
    results["string_stats"] = string_stats
    return results

if __name__ == "__main__":
    mcp_run()
