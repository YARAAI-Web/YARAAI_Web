# services/suricata/suricata_extractor.py

import os
import re
import tempfile
import subprocess
import sys
from typing import Optional

def convert_yara_to_suricata(yara_file: str, suricata_script: str, working_dir: Optional[str] = None) -> str:
    python_cmd = sys.executable
    cmd = [python_cmd, suricata_script, yara_file]
    result = subprocess.run(
        cmd, cwd=working_dir,
        capture_output=True, text=True, check=True
    )
    lines = result.stdout.splitlines()
    if lines and not lines[0].startswith("alert"):
        lines = lines[1:]
    return "\n".join(lines)

def simple_suricata_from_yara(yara_file: str) -> str:
    """
    YARA 룰 내의 모든 문자열 리터럴에 대해
    개별 Suricata alert 룰을 생성하되,
    흐름 및 프로토콜 등을 유추하여 향상된 룰 생성
    """
    content = open(yara_file, "r", encoding="utf-8").read()
    m = re.search(r"rule\s+(\w+)", content)
    rule_name = m.group(1) if m else os.path.splitext(os.path.basename(yara_file))[0]
    literals = list(set(re.findall(r'"([^"]+)"', content)))  # 중복 제거

    alerts = []
    for idx, lit in enumerate(literals, start=1):
        sid = abs(hash(f"{rule_name}_{idx}")) % 9000000 + 1000000

        # 옵션 추론: URI 관련이면 http_uri로
        if "/" in lit or ".php" in lit or ".asp" in lit:
            context = "http_uri"
        elif "User-Agent" in lit or "Referer" in lit:
            context = "http_header"
        elif lit.isupper() and len(lit) <= 8:
            context = "content"  # binary signature 추정
        else:
            context = "file_data"

        alert = (
            f"alert tcp any any -> any any ( "
            f"msg:\"YARA {rule_name} matched literal #{idx}\"; "
            f"flow:established,to_server; "
            f"{context}:\"{lit}\"; nocase; "
            f"detection_filter:track by_src, count 1, seconds 60; "
            f"sid:{sid}; rev:2; "
            f")"
        )
        alerts.append(alert)

    return "\n".join(alerts)

def extract_rules_from_meta(meta_json: dict) -> str:
    yara_text = meta_json.get("yara_rule", "")
    if not yara_text.strip():
        return ""

    # 임시 .yar 파일로 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=".yar", mode="w", encoding="utf-8") as tmp:
        tmp.write(yara_text)
        tmp_yar = tmp.name

    base_dir = os.path.dirname(os.path.abspath(__file__))
    script = os.path.join(base_dir, "run_convert.py")

    try:
        suri = convert_yara_to_suricata(tmp_yar, script, working_dir=base_dir)
        # 정상 변환이 없으면 fallback
        if not suri.strip():
            suri = simple_suricata_from_yara(tmp_yar)
    except Exception:
        suri = simple_suricata_from_yara(tmp_yar)
    finally:
        try:
            os.remove(tmp_yar)
        except:
            pass

    return suri
