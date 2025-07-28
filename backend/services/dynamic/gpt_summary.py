import openai
import os
import json

# 🔐 OpenAI API 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# ✅ GPT 호출 함수 (GPT-4 Turbo + Prompt 전략 반영)
def query_gpt(json_input: dict, section_prompt: str, section_title: str) -> str:
    input_str = json.dumps(json_input, ensure_ascii=False, indent=2)
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a senior malware analysis expert. Your task is to write the Korean-language report for section '{section_title}', "
                "based on the provided JSON data. Do not include any markdown or HTML. Respond only in structured, clear Korean."
            )
        },
        {
            "role": "user",
            "content": section_prompt.strip() + "\n\n[Input JSON]\n" + input_str
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=messages,
        temperature=0.3,
        max_tokens=4096
    )
    return response["choices"][0]["message"]["content"]

# ✅ 기본 필드 보정 및 스크린샷 정리
def prepare_json(report_json: dict):
    report_json.setdefault("behavior", {"processes": []})
    report_json.setdefault("network", {})
    report_json.setdefault("static", {})
    report_json.setdefault("target", {})
    report_json.setdefault("signatures", [])

    try:
        report_id = report_json.get("info", {}).get("id") or report_json.get("target", {}).get("file", {}).get("sha256")
        if report_id:
            base_dir = os.getenv("CUCKOO_AFTER_DIR", r"C:\\Users\\hyunj\\analysis_yaraai\\after")
            matched_dir = next((d for d in os.listdir(base_dir) if str(report_id) in d and d.endswith("_shots")), None)
            if matched_dir:
                screenshot_dir = os.path.join(base_dir, matched_dir)
                report_json["screenshots"] = sorted([
                    os.path.join(matched_dir, f) for f in os.listdir(screenshot_dir)
                    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
                ])
            else:
                report_json["screenshots"] = []
    except:
        report_json["screenshots"] = []

    return report_json

# ✅ 전체 요약 생성 함수
def generate_summary_from_dynamic_report(report_json: dict) -> list:
    report_json = prepare_json(report_json)
    results = []

    # [1] Summary
    prompt_1 = """
📄 [1] Summary – Basic Static Information

Summarize the following fields into a clean Korean table:
- File name, file size, file type (PE32, EXE, DLL, etc.)
- Hash values: MD5, SHA1, SHA256
- Compile timestamp, original filename, debugger path
- Any matched YARA rules

Output in Korean. Use a plain-text table. No markdown.
"""
    input_1 = { "target": report_json["target"], "static": report_json["static"] }
    results.append(query_gpt(input_1, prompt_1, "[1] Summary"))

    # [2] Signatures
    prompt_2 = """
🛑 [2] Signatures – Detected Malicious Behaviors

Categorize signatures by severity:
- 🔴 severity 3: Malicious
- 🟡 severity 2: Suspicious
- 🔵 severity 1: Informational

For each group, summarize in Korean:
- Number of events
- Signature name
- Short description of behavior

Output must be in Korean, grouped by severity level.
"""
    input_2 = { "signatures": report_json["signatures"] }
    results.append(query_gpt(input_2, prompt_2, "[2] Signatures"))

    # [3] Behavior – Process-wise
    prompt_3 = """
📂 [3] Behavior – Process-level Activity Summary

For each process, summarize the following:
- Executable path
- PID / Parent PID
- Command-line
- 2~3 key API calls
- Observed behavior (injection, file creation, registry, etc.)

Output format:
📌 Process 1:
- Image: ...
- PID/PPID: ...
- Command Line: ...
- APIs: ...
- Observed Behavior: ...

Respond only in Korean. Max 5 lines per process.
"""
    processes = report_json["behavior"]["processes"]
    for i in range(0, len(processes), 10):
        chunk = processes[i:i+10]
        input_3 = { "behavior": { "processes": chunk } }
        results.append(query_gpt(input_3, prompt_3, f"[3] Behavior (Part {i//10 + 1})"))

    # [4] Network
    prompt_4 = """
🌐 [4] Network – Network Behavior Summary

From the 'network' section, summarize in Korean:
- Contacted domains and IPs
- Protocols used (DNS, TCP, HTTP)
- GET/POST requests, full URLs
- Indicators of C2 or suspicious activity

Respond only in Korean. Use bullet points.
"""
    input_4 = { "network": report_json["network"] }
    results.append(query_gpt(input_4, prompt_4, "[4] Network"))

    # [5] Screenshots
    prompt_5 = """
📷 [5] Screenshots – Visual Behavior Summary

For each screenshot filename:
- Describe visible UI or behavior in Korean
- Mention any installation wizard, CLI traces, errors

Format example:
- screenshot1.png → 설치 마법사 창이 표시됨
- screenshot2.png → 명령 프롬프트에서 'whoami' 실행됨

If no screenshots, return: "스크린샷 없음"
Respond only in Korean. No markdown.
"""
    input_5 = { "screenshots": report_json.get("screenshots", []) }
    results.append(query_gpt(input_5, prompt_5, "[5] Screenshots"))

    # [6] Final Summary
    prompt_6 = """
🔎 [6] Expert Summary – Executive Report

Based on all sections, write a final Korean report:
1. Malware classification (e.g., RAT, Infostealer, etc.)
2. Key observed behaviors
3. Evasion or anti-analysis techniques
4. Related MITRE ATT&CK techniques (include T-numbers)
5. Possible attribution to known threat actor(s)
6. Security recommendations (blocking, detection, IOC)

Structure it like a report to a SOC team. Use numbered bullet points.
Respond in Korean. No markdown.
"""
    results.append(query_gpt(report_json, prompt_6, "[6] Final Summary"))

    return results

# ✅ 외부용 호출 함수
def generate_full_summary_with_split(report_json: dict, after_dir: str) -> list:
    report_json = prepare_json(report_json)
    return generate_summary_from_dynamic_report(report_json)
