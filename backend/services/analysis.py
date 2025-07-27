# backend/services/analysis.py

import os
import json
import subprocess
import time
import psutil
import hashlib
from typing import Any, Dict

from .mcp_collector import mcp_run
from .c_h_run import analyze_file as run_analysis, OUTPUT_DIR
from .extract_pe_headers import extract_headers
from .CAPA import map_mitre
from .CWE.map_CWE import analyze_code_with_cwe
# Virustotal 연동
from services.virustotal import get_vt_data

# IDA 및 MCP 설정
IDA_PATH   = r"C:\Program Files\IDA Professional 9.1\ida.exe"

# CAPA JSON 덤프 디렉터리
SERVICES_DIR   = os.path.dirname(os.path.abspath(__file__))
CAPA_JSON_DIR  = os.path.join(SERVICES_DIR, "CAPA", "capa_json")
os.makedirs(CAPA_JSON_DIR, exist_ok=True)


def kill_process_using_port(port: int):
    for conn in psutil.net_connections(kind="tcp"):
        if conn.status == psutil.CONN_LISTEN and conn.laddr.port == port and conn.pid and conn.pid != 0:
            try:
                p = psutil.Process(conn.pid)
                print(f"👉 PID={conn.pid} ({p.name()}) on port {port} → killing")
                p.kill()
            except Exception as e:
                print(f"❌ Failed to kill PID={conn.pid}: {e}")
            return
    print(f"⚠️ No process listening on port {port} found.")


def analyze_file(file_path: str) -> Dict[str, Any]:
    # 0) IDA + MCP 자동 실행
    subprocess.Popen(f'"{IDA_PATH}" -A "{file_path}"', shell=True)
    time.sleep(10)
    mcp = mcp_run()
    kill_process_using_port(13337)
    time.sleep(5)

    # 1) PE 헤더 추출
    try:
        pe_hdr = extract_headers(file_path)
    except Exception:
        pe_hdr = {}
    print("➤ PE headers extracted")

    # 2) C/H + VT 분석
    run_analysis(file_path)
    base_uuid = os.path.splitext(os.path.basename(file_path))[0]
    ch_json   = os.path.join(OUTPUT_DIR, f"{base_uuid}.json")
    if not os.path.exists(ch_json):
        raise FileNotFoundError(f"C/H JSON not found: {ch_json}")
    with open(ch_json, "r", encoding="utf-8") as f:
        ch_data = json.load(f)
    print("➤ C/H + VT analysis done")

    summary    = ch_data.get("summary", [])
    yara_rules = ch_data.get("yara_rules", "")
    print("➤ YARA rules extracted")

    # 3) CAPA 룰 매핑
    capa_output    = map_mitre.map_mitre(file_path)
    capa_json_path = capa_output[0]
    mitre_mapping  = capa_output[1]

    with open(capa_json_path, 'r', encoding='utf-8') as f:
        capa_rules = json.load(f)
    print("➤ CAPA rules loaded")

    # 4) SHA-256 해시 기반으로 덤프 파일명 변경
    sha256 = mcp['get_metadata']['sha256']
    target_capa_dump = os.path.join(CAPA_JSON_DIR, f"{sha256}.json")
    with open(target_capa_dump, 'w', encoding='utf-8') as f:
        json.dump(capa_rules, f, ensure_ascii=False, indent=2)
    print(f"➤ Dumped CAPA JSON to {target_capa_dump}")

    # CWE 분석
    CWE = analyze_code_with_cwe(ch_data)

    # 5) Virustotal API 호출
    try:
        vt_data = get_vt_data(sha256)
        print("➤ Virustotal data fetched")
    except Exception as e:
        print(f"❌ Virustotal API error: {e}")
        vt_data = {}

    # 6) 최종 리포트 조립
    report: Dict[str, Any] = {
        "get_metadata":         mcp['get_metadata'],
        "get_current_address":  mcp['get_current_address'],
        "get_current_function": mcp['get_current_address'],
        "get_entry_points":     mcp['get_entry_points'],
        "file_entropy":         mcp['file_entropy'],
        "string_stats":         mcp['string_stats'],
        "pe_headers":           pe_hdr,
        "virustotal":           vt_data,
        "c_code":               ch_data.get("c_code", []),
        "h_code":               ch_data.get("h_code", []),
        "summary":              summary,
        "yara_rules":           yara_rules,
        "capa_rules":           capa_rules,
        "MITRE":                mitre_mapping,
        "CWE":                  CWE
    }
    
    return report
