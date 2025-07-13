import json
import re
from datetime import datetime
import sys

def extract_api_calls(c_code_lines):
    c_code = "\n".join(c_code_lines)

    dll_call_pattern = r"[a-zA-Z0-9_]+\.(dll|DLL)!([a-zA-Z0-9_@]+)"
    generic_call_pattern = r"\b([A-Za-z_][A-Za-z0-9_]{3,})\b"

    dll_matches = re.findall(dll_call_pattern, c_code)
    generic_matches = re.findall(generic_call_pattern, c_code)

    dll_apis = [match[1] for match in dll_matches]
    skip_words = {"eax", "ebx", "ecx", "int", "goto", "char", "main"}
    filtered_generics = [
        fn for fn in generic_matches
        if fn.lower() not in skip_words and not fn.startswith("sub_")
    ]

    combined = set(dll_apis + filtered_generics)
    return sorted(combined)

def generate_yara_rule(json_path: str) -> str:
    # 1) JSON 읽기
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    md5    = data.get("get_metadata", {}).get("md5", "unknown")
    sha256 = data.get("get_metadata", {}).get("sha256", "unknown")
    c_code_lines = data.get("c_code", [])

    # 2) API 호출 추출
    apis = extract_api_calls(c_code_lines)

    # 3) 룰 이름 및 날짜 생성
    rule_name = f"AutoGen_{md5[:8]}"
    date_str  = datetime.now().strftime("%Y-%m-%d")

    # 4) strings/condition 블록 구성
    if apis:
        strings_block = "\n        ".join(
            f'$s{i} = "{api}" fullword ascii' for i, api in enumerate(apis)
        )
        condition = f"uint16(0) == 0x5A4D and {len(apis)} of them"
    else:
        strings_block = "/* no API extracted */"
        condition = "uint16(0) == 0x5A4D"

    # 5) 멀티라인 룰 템플릿
    rule = f"""
rule {rule_name} : Malware {{
    meta:
        description = "Auto-generated YARA rule based on API usage"
        author      = "YARRAI AutoGen"
        date        = "{date_str}"
        md5         = "{md5}"
        sha256      = "{sha256}"

    strings:
        {strings_block}

    condition:
        {condition}
}}
""".strip()

    # 6) 모든 개행 제거 (한 줄로 합치기)
    single_line_rule = " ".join(line.strip() for line in rule.splitlines())

    return single_line_rule

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_yara_rule.py <path_to_input_json>", file=sys.stderr)
        sys.exit(1)

    output = generate_yara_rule(sys.argv[1])
    print(output)
