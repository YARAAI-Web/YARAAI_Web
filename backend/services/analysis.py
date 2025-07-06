# backend/services/analysis.py

import os
import json
from typing import Any, Dict
import subprocess
import time

from .mcp_collector import mcp_run
# (1) C/H + VT → c_h_run 모듈
from .c_h_run import analyze_file as run_analysis, OUTPUT_DIR
# (2) PE 헤더 파싱
from .extract_pe_headers import extract_headers
from .CAPA import map_mitre
import psutil

IDA_PATH = r"C:\Program Files\IDA Professional 9.1\ida.exe"
IDA_SCRIPT = os.path.abspath("ida_mcp_launcher.py")

def kill_process_using_port(port: int):
    """
    TCP 포트(port)를 실제로 LISTEN 상태로 점유 중인 프로세스를 찾아 강제 종료합니다.
    pid=0(System Idle Process) 등은 무시합니다.
    """
    for conn in psutil.net_connections(kind="tcp"):
        # 리슨 중이면서 로컬 포트가 일치하고, pid가 0이 아닌 경우
        if conn.status == psutil.CONN_LISTEN and conn.laddr.port == port and conn.pid and conn.pid != 0:
            pid = conn.pid
            try:
                p = psutil.Process(pid)
                print(f"👉 PID={pid} ({p.name()}) 가 포트 {port}를 LISTEN 중 → 강제로 종료합니다.")
                p.kill()
            except Exception as e:
                print(f"❌ PID={pid} 강제 종료 중 오류: {e}")
            return

    print(f"⚠️ 포트 {port}를 LISTEN 상태에서 사용 중인 PID를 찾지 못했습니다.")

def analyze_file(file_path: str) -> Dict[str, Any]:
    ida_cmd = f'"{IDA_PATH}" -A "{file_path}"'
    subprocess.Popen(ida_cmd, shell=True)

    mcp = mcp_run()
    kill_process_using_port(13337)
    time.sleep(5)

    # 3) PE 헤더
    try:    pe_hdr      = extract_headers(file_path)
    except: pe_hdr      = {}
    print("meta 완료")
    
    # 1) IDA → .c/.h + VT 결과 생성
    run_analysis(file_path)

    base = os.path.splitext(os.path.basename(file_path))[0]
    ch_json = os.path.join(OUTPUT_DIR, f"{base}.json")
    if not os.path.exists(ch_json):
        raise FileNotFoundError(f"C/H JSON not found: {ch_json}")
    
    with open(ch_json, "r", encoding="utf-8") as f:
        ch_data = json.load(f)
    print("c,h생성 완료")

    # 4) Summary & YARA rule (ch_data 안에 들어 있다고 가정)
    summary     = ch_data.get("summary", [])        # e.g. ["(1) 프로세스 행위: …", "(2) 레지스트리 조작: …", …]
    yara_rules  = ch_data.get("yara_rules", "")     # e.g. "rule suspicious_behavior { ... }"
    print("YARA 완료")

    capa = map_mitre.map_mitre(file_path)
    with open(capa[0], 'r', encoding='utf-8') as f:
        capa_rules = json.load(f)
    MITRE = capa[1]

    # 5) 최종 리포트 조립
    report: Dict[str, Any] = {
        # 메타데이터
        "get_metadata":         mcp['get_metadata'],
        "get_current_address":  mcp['get_current_address'],
        "get_current_function": mcp['get_current_address'],
        "get_entry_points":     mcp['get_entry_points'],
        "file_entropy":         mcp['file_entropy'],
        "string_stats":         mcp['string_stats'],

        # PE 헤더 & MCP 문자열
        "pe_headers":           pe_hdr,

        # C/H + VT
        "virustotal":           ch_data.get("virustotal", {}),
        "c_code":               ch_data.get("c_code", []),
        "h_code":               ch_data.get("h_code", []),

        # 추가: summary & yara_rules
        "summary":              summary,
        "yara_rules":           yara_rules,
        "capa_rules":           capa_rules,
        "MITRE ATT&CK":         MITRE
    }

    return report
