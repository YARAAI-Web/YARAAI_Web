# backend/services/analysis.py

import os
import json
from typing import Any, Dict

# (1) C/H + VT → c_h_run 모듈
from .c_h_run import analyze_file as run_analysis, OUTPUT_DIR
# (2) PE 헤더 파싱
from .extract_pe_headers import extract_headers
# (3) MCP 문자열 통계
from .mcp_collector import collect_mcp_strings
# (4) 파일 메타데이터
from .meta import (
    get_metadata,
    get_current_address,
    get_current_function,
    get_entry_points,
    file_entropy,
    string_stats,
)

def analyze_file(file_path: str) -> Dict[str, Any]:
    # 1) IDA → .c/.h + VT 결과 생성
    run_analysis(file_path)

    base = os.path.splitext(os.path.basename(file_path))[0]
    ch_json = os.path.join(OUTPUT_DIR, f"{base}.json")
    if not os.path.exists(ch_json):
        raise FileNotFoundError(f"C/H JSON not found: {ch_json}")

    with open(ch_json, "r", encoding="utf-8") as f:
        ch_data = json.load(f)

    # 2) 메타데이터
    try:    meta        = get_metadata(base)
    except: meta        = {}
    try:    current_addr= get_current_address(base)
    except: current_addr= None
    try:    current_fn  = get_current_function(base)
    except: current_fn  = {}
    try:    entry_pts   = get_entry_points(base)
    except: entry_pts   = []
    try:    entropy     = file_entropy(base)
    except: entropy     = None
    try:    str_stats   = string_stats(base)
    except: str_stats   = {}

    # 3) PE 헤더
    try:    pe_hdr      = extract_headers(file_path)
    except: pe_hdr      = {}

    # 4) MCP 문자열
    try:    mcp_stats   = collect_mcp_strings(file_path)
    except: mcp_stats   = {}

    # 5) Summary & YARA rule (ch_data 안에 들어 있다고 가정)
    summary     = ch_data.get("summary", [])        # e.g. ["(1) 프로세스 행위: …", "(2) 레지스트리 조작: …", …]
    yara_rules  = ch_data.get("yara_rules", "")     # e.g. "rule suspicious_behavior { ... }"

    # 6) 최종 리포트 조립
    report: Dict[str, Any] = {
        # 메타데이터
        "get_metadata":         meta,
        "get_current_address":  current_addr,
        "get_current_function": current_fn,
        "get_entry_points":     entry_pts,
        "file_entropy":         entropy,
        "string_stats":         str_stats,

        # PE 헤더 & MCP 문자열
        "pe_headers":           pe_hdr,
        "mcp_strings":          mcp_stats,

        # C/H + VT
        "virustotal":           ch_data.get("virustotal", {}),
        "c_code":               ch_data.get("c_code", []),
        "h_code":               ch_data.get("h_code", []),

        # 추가: summary & yara_rules
        "summary":              summary,
        "yara_rules":           yara_rules,
    }

    return report
