# backend/services/generate_callgraph.py

import os
import re
import json
import time
from pyvis.network import Network
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import HTTPException

# .env에서 OPENAI_API_KEY 불러오기
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("❌ OPENAI_API_KEY가 설정되어 있지 않습니다.")

# OpenAI 클라이언트 초기화 (v1 이상)
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_call_graph(input_json: str, output_html: str) -> str:
    try:
        print(f"[1] 📂 JSON 파일 로드 중: {input_json}")
        with open(input_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        c_code = data.get("c_code", [])
        h_code = data.get("h_code", [])
        code_lines = c_code + h_code

        if not code_lines:
            raise ValueError("❌ JSON 파일에 'c_code' 또는 'h_code'가 없습니다.")

        print(f"[2] 🔍 함수 파싱 시작: 코드 라인 수 = {len(code_lines)}")
        functions = {}
        func_bodies = {}
        current = None

        for line in code_lines:
            m = re.match(r'\w[\w\s\*]*\s+(sub_\w+)\s*\(', line)
            if m:
                current = m.group(1)
                functions[current] = set()
                func_bodies[current] = []
                continue
            if current:
                func_bodies[current].append(line)
                for callee in re.findall(r'\b(sub_\w+)\s*\(', line):
                    if callee != current:
                        functions[current].add(callee)

        print(f"[3] ✅ 함수 파싱 완료: 함수 수 = {len(functions)}")

        tooltip_map = {}
        for name, body in func_bodies.items():
            snippet = "\n".join(body[:20])
            prompt = f"""아래 C 함수가 무슨 일을 하는지 한국어로 한 문장으로 설명해줘.

함수 이름: {name}

{snippet}
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt.strip()}],
                    temperature=0.3,
                    max_tokens=150
                )
                tooltip_map[name] = response.choices[0].message.content.strip()
            except Exception as gpt_err:
                print(f"⚠️ GPT 요약 실패: {name} → {gpt_err}")
                tooltip_map[name] = "(요약 실패)"
            time.sleep(1.2)

        print(f"[4] 🧠 GPT 요약 완료: {len(tooltip_map)}개")

        net = Network(height="800px", width="100%", directed=True)
        net.force_atlas_2based(gravity=-50, spring_length=100)

        added_nodes = set()
        for caller, callees in functions.items():
            if caller not in added_nodes:
                net.add_node(caller, label=caller, title=tooltip_map.get(caller, ""))
                added_nodes.add(caller)
            for callee in callees:
                if callee not in added_nodes:
                    net.add_node(callee, label=callee, title=tooltip_map.get(callee, ""))
                    added_nodes.add(callee)
                net.add_edge(caller, callee)

        output_dir = os.path.dirname(output_html)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        print(f"[5] 💾 HTML 저장 경로 확인: {output_html}")
        net.write_html(output_html)

        if os.path.exists(output_html):
            print(f"✅ CallGraph 생성 완료 → {output_html}")
        else:
            print(f"❌ HTML 파일이 생성되지 않았습니다.")

        return output_html

    except Exception as e:
        print(f"❌ Call graph 생성 중 오류 발생: {e}")
        raise HTTPException(status_code=500, detail=f"Call graph 생성 실패: {str(e)}")
