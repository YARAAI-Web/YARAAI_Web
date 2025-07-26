import openai
import os
import json

# 🔐 OpenAI API 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# 📌 GPT 프롬프트 템플릿
PROMPT_TEMPLATE = """
📌 [당신의 역할]
당신은 보안 전문 악성코드 분석 AI이며, 사용자는 웹 기반 시스템을 통해 동적 분석 요약 보고서를 확인하고자 함.
이 보고서는 전문가가 빠르게 판단할 수 있도록 JSON 포맷으로 구조화되어야 하며,
모든 설명은 문장 단위로 충분히 길고 풍부하게 작성해야 함.

📌 [분석 대상]
분석 대상은 Cuckoo Sandbox에서 생성된 동적 분석 결과인 report.json이며, 사용자는 이를 이해하기 쉬운 요약으로 보고자 함.
입력은 JSON이고, 출력 또한 **엄격한 JSON 구조**로 고정되어야 함.

📌 [반드시 지킬 출력 형식]
출력은 반드시 아래 구조를 따라야 함. 모든 항목은 list[str] 형태로 출력하며, 각 문장은 반드시 종결 어미 "~함"으로 끝날 것:

{
  "Summary": [...],
  "TargetInfo": [...],
  "Behavior": [...],
  "Network": [...],
  "Suspicious": [...],
  "Threat": [...],
  "Screenshots": [...],
  "Artifacts": [...]
}

📌 [출력 지침]
- 마크다운, 강조표시, 이모지 절대 사용 금지
- 항목 누락, key 이름 오탈자 절대 금지
- 출력은 JSON 문자열로 시작해야 하며, JSON 구조가 깨지면 안됨
- 항목이 존재하지 않거나 비어 있으면 "정보 없음"이라는 하나의 문자열로 리스트 안에 넣을 것
- 출력이 JSON이 아닐 경우 사용자가 시스템 오류로 판단하므로 절대 발생하지 않도록 할 것

📌 [각 항목별 내용 설명]

1. "Summary":
- 분석 전체를 요약하는 항목임
- 악성코드의 전반적 행위, 위험도, 감염 확률, 감지 여부 요약
- 주요 분석 시점, 사용된 분석 시스템 정보 포함

2. "TargetInfo":
- 분석 대상 파일 이름, SHA256 해시, 크기, PE 여부 등 파일 메타데이터
- 실행된 OS, 분석 시작 시간, 분석 시스템 IP 주소
- 패킹 여부, 언패킹 여부 명시

3. "Behavior":
- 실행된 프로세스 수 및 주요 프로세스 이름
- 생성/수정/삭제된 파일 수 및 경로 예시
- 조작된 레지스트리 키 목록
- 부모-자식 프로세스 관계 분석
- 행위 시간 흐름상 순서 요약 (예: 10:15 → 레지스트리 생성, 10:20 → 파일 삭제)

4. "Network":
- 접속한 IP, 포트, 도메인, DNS 요청
- HTTP 요청 경로 및 Header 정보 (User-Agent, URL 등)
- 통신한 대상의 국가 등 GeoIP 정보
- 연결 실패나 탐지 회피 시도 언급

5. "Suspicious":
- 사용된 악성 API 목록 (예: VirtualAllocEx, CreateRemoteThread 등)
- 악성 문자열, 명령어, 쉘 명령, 실행 경로 등 포함
- API 호출 횟수가 비정상적으로 많은 경우 강조

6. "Threat":
- 예측되는 악성코드 유형 (RAT, 드로퍼, 백도어, 스틸러 등)
- VirusTotal 탐지 결과 요약 (탐지된 경우 이름과 백신 제품 수 포함)
- 예상 공격 목적 (정보 수집, 원격 제어, 감염 확산 등)

7. "Screenshots":
- 스크린샷 개수
- 캡처된 창 이름 및 특이점 여부 (GUI 프로그램인지 여부 포함)
- 화면 상에 악성 행위 정황이 있는지 여부

8. "Artifacts":
- 드롭된 파일 수, 확장자, 경로
- 실행 가능성 여부, 시스템에 미친 영향
- 분석 도중 발견된 파일 흔적들 요약

📌 [예외 처리]
- 보고서에 해당 항목이 없거나 빈 리스트일 경우: 해당 키에 ["정보 없음"] 만 삽입
- 출력은 반드시 JSON 시작 구조로 시작하며, GPT의 설명을 붙이지 말 것
"""


# ✅ 스크린샷 정보 추가 함수
def attach_screenshot_info(report_json: dict, screenshot_dir: str) -> dict:
    try:
        screenshot_files = [
            f for f in os.listdir(screenshot_dir)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
        ]
        report_json["screenshots"] = screenshot_files
    except Exception:
        report_json["screenshots"] = []
    return report_json

# ✅ GPT 요약 생성
def generate_summary_from_dynamic_report(report_json: dict) -> dict:
    input_json = json.dumps(report_json, ensure_ascii=False, indent=2)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 악성코드 분석 요약 전문가입니다."},
            {"role": "user", "content": PROMPT_TEMPLATE + input_json}
        ],
        temperature=0.3,
    )
    result = response["choices"][0]["message"]["content"]

    try:
        parsed = json.loads(result)
        if not isinstance(parsed, dict) or "Summary" not in parsed:
            raise ValueError("응답 JSON 구조 오류")
        return parsed
    except Exception:
        return {
            "Summary": ["⚠️ GPT 응답을 JSON으로 파싱할 수 없습니다. 현재 결과는 다음과 같습니다."],
            "Raw": result.split("\n")
        }

# ✅ JSON 구조 보정
def prepare_report_json_for_prompt(report_json: dict) -> dict:
    report_json.setdefault("behavior", {"processes": [], "summary": {}})
    report_json.setdefault("network", {
        "hosts": [], "dns": [], "http": [], "tcp": [], "udp": [],
        "icmp": [], "tls": [], "smtp": [], "irc": [], "domains": [],
        "http_ex": [], "https_ex": [], "smtp_ex": [], "mitm": [],
        "dns_servers": [], "dead_hosts": [], "pcap_sha256": ""
    })
    report_json.setdefault("static", {"pe_exports": [], "digital_signers": []})
    report_json.setdefault("signatures", [])
    report_json.setdefault("target", {"file": {}})
    report_json.setdefault("screenshots", [])  # 초기화만, 이후 attach 함수에서 덮어씀
    report_json.setdefault("dropped", [])
    return report_json

# ✅ 고급 요약 (프로세스가 너무 많을 때 분할)
def generate_full_summary_with_split(report_json: dict, screenshot_dir: str) -> dict:
    report_json = prepare_report_json_for_prompt(report_json)
    report_json = attach_screenshot_info(report_json, screenshot_dir)
    processes = report_json.get("behavior", {}).get("processes", [])

    if len(processes) > 20:
        chunk_size = 10
        chunks = [processes[i:i + chunk_size] for i in range(0, len(processes), chunk_size)]
        merged_summary = {
            "Summary": [], "TargetInfo": [], "Behavior": [], "Network": [],
            "Suspicious": [], "Threat": [], "Screenshots": [], "Artifacts": []
        }

        for chunk in chunks:
            temp_json = report_json.copy()
            temp_json["behavior"]["processes"] = chunk
            partial = generate_summary_from_dynamic_report(temp_json)
            if "Raw" in partial:
                continue
            for key in merged_summary:
                merged_summary[key].extend(partial.get(key, []))
                merged_summary[key].append("")  # 줄바꿈

        return merged_summary
    else:
        return generate_summary_from_dynamic_report(report_json)
