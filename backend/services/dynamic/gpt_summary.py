import os
import json
from typing import List
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

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


def generate_summary_from_split_json(uuid: str, base_dir: str) -> List[str]:
    results = []

    # [1] Summary
    summary_path = os.path.join(base_dir, f"{uuid}_summary.json")
    if os.path.exists(summary_path):
        with open(summary_path, encoding="utf-8") as f:
            summary_data = json.load(f)
        prompt = """
📄 [1] Summary – Basic Static Information

Summarize the following fields into a clean Korean table:
- File name, file size, file type (PE32, EXE, DLL, etc.)
- Hash values: MD5, SHA1, SHA256
- Compile timestamp, original filename, debugger path
- Any matched YARA rules

Output in Korean. Use a plain-text table. No markdown.
"""
        results.append(query_gpt(summary_data, prompt, "[1] Summary"))

    # [2] Signatures
    sig_path = os.path.join(base_dir, f"{uuid}_signatures.json")
    if os.path.exists(sig_path):
        with open(sig_path, encoding="utf-8") as f:
            sig_data = json.load(f)
        prompt = """
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
        results.append(query_gpt(sig_data, prompt, "[2] Signatures"))

    # [3] Behavior (multi-part 지원)
    part_num = 1
    while True:
        part_path = os.path.join(base_dir, f"{uuid}_behavior_part_{part_num}.json")
        if not os.path.exists(part_path):
            break
        with open(part_path, encoding="utf-8") as f:
            behavior_data = json.load(f)
        prompt = """
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
        results.append(query_gpt(behavior_data, prompt, f"[3] Behavior (Part {part_num})"))
        part_num += 1

    # [4] Network
    network_path = os.path.join(base_dir, f"{uuid}_network.json")
    if os.path.exists(network_path):
        with open(network_path, encoding="utf-8") as f:
            net_data = json.load(f)
        prompt = """
🌐 [4] Network – Network Behavior Summary

From the 'network' section, summarize in Korean:
- Contacted domains and IPs
- Protocols used (DNS, TCP, HTTP)
- GET/POST requests, full URLs
- Indicators of C2 or suspicious activity

Respond only in Korean. Use bullet points.
"""
        results.append(query_gpt(net_data, prompt, "[4] Network"))

    # [5] Screenshots
    shot_path = os.path.join(base_dir, f"{uuid}_screenshots.json")
    if os.path.exists(shot_path):
        with open(shot_path, encoding="utf-8") as f:
            shot_data = json.load(f)
        prompt = """
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
        results.append(query_gpt(shot_data, prompt, "[5] Screenshots"))

    # [6] Final Summary
    try:
        with open(summary_path, encoding="utf-8") as f:
            all_data = json.load(f)
        prompt = """
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
        results.append(query_gpt(all_data, prompt, "[6] Final Summary"))
    except:
        results.append("[6] Final Summary: 요약 불가 (summary.json 없음)")

    return results


# 🔄 외부에서 호출
def generate_full_summary_with_split(uuid: str, after_dir: str) -> list:
    return generate_summary_from_split_json(uuid, after_dir)
