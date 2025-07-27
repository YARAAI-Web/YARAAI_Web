# generate_callgraph.py

import os
import re
import json
import time
from pyvis.network import Network
from dotenv import load_dotenv
from openai import OpenAI

# .env에서 OPENAI_API_KEY 불러오기
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("❌ OPENAI_API_KEY가 설정되어 있지 않습니다.")

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_call_graph(input_json_path: str, output_html_path: str) -> str:
    """
    메타 JSON에서 함수 호출 그래프를 생성하고 HTML 파일로 저장합니다.
    디버깅 출력을 통해 파싱된 함수와 호출 관계를 확인할 수 있습니다.

    Args:
        input_json_path (str): 분석 리포트 JSON 파일 경로
        output_html_path (str): 생성할 HTML 파일 경로

    Returns:
        str: 저장된 HTML 파일 경로

    Raises:
        RuntimeError: 생성 실패 시 예외를 발생시킵니다.
    """
    try:
        # 1. JSON 로드
        with open(input_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        code_lines = data.get("c_code", []) + data.get("h_code", [])
        if not code_lines:
            raise RuntimeError("JSON에 'c_code' 또는 'h_code'가 없습니다.")

        # 2. 함수 파싱 (범용 패턴)
        func_pattern = re.compile(r"^\s*[A-Za-z_]\w*\s+([A-Za-z_]\w*)\s*\(")
        call_pattern = re.compile(r"\b([A-Za-z_]\w*)\s*\(")
        functions = {}
        func_bodies = {}
        current_func = None

        for line in code_lines:
            # 함수 정의 시작
            m = func_pattern.match(line)
            if m:
                current_func = m.group(1)
                functions[current_func] = set()
                func_bodies[current_func] = []
                continue
            # 함수 본문 및 호출 수집
            if current_func:
                func_bodies[current_func].append(line)
                for callee in call_pattern.findall(line):
                    if callee != current_func:
                        functions[current_func].add(callee)

        # 디버깅 정보 출력
        print(f"[DEBUG] Detected {len(functions)} functions: {list(functions.keys())}")
        for fn, callees in functions.items():
            print(f"[DEBUG] {fn} calls -> {callees}")

        # 3. GPT 툴팁 생성
        tooltip_map = {}
        for name, body in func_bodies.items():
            snippet = "\n".join(body[:20])
            prompt = (
                f"아래 C 함수가 무슨 일을 하는지 한국어로 한 문장으로 설명해줘.\n\n"
                f"함수 이름: {name}\n\n"
                f"{snippet}\n"
            )
            try:
                resp = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt.strip()}],
                    temperature=0.3,
                    max_tokens=150
                )
                tooltip_map[name] = resp.choices[0].message.content.strip()
            except Exception as e:
                print(f"[WARN] GPT 요약 실패 for {name}: {e}")
                tooltip_map[name] = "(요약 실패)"
            time.sleep(1)

        # 4. 네트워크 그래프 생성 (모든 리소스 인라인)
        net = Network(
            height="800px", width="100%", directed=True,
            cdn_resources="in_line"
        )
        net.force_atlas_2based(gravity=-50, spring_length=100)

        for caller, callees in functions.items():
            net.add_node(caller, label=caller, title=tooltip_map.get(caller, ""))
            for callee in callees:
                net.add_node(callee, label=callee, title=tooltip_map.get(callee, ""))
                net.add_edge(caller, callee)

        # 5. HTML 생성 및 UTF-8로 저장
        html_str = net.generate_html()
        os.makedirs(os.path.dirname(output_html_path), exist_ok=True)
        with open(output_html_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(html_str)

        if not os.path.exists(output_html_path):
            raise RuntimeError(f"HTML 생성 실패: {output_html_path}가 없습니다.")

        print(f"[INFO] Call graph saved at {output_html_path}")
        return output_html_path

    except Exception as e:
        print(f"[ERROR] Call graph generation error: {e}")
        raise RuntimeError(f"Call graph 생성 실패: {e}")
