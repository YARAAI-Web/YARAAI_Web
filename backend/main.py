# main.py
from dotenv import load_dotenv # test
import os
import uuid
import json
import subprocess
from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from openai import OpenAI

from services.analysis import analyze_file
from generate_callgraph import generate_call_graph
from services.suricata.yara_generator import generate_yara_rule
from services.unpacker import detect_packers, unpack_file

# 🔐 환경 변수 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 📁 디렉터리 경로 설정
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR    = os.path.join(BASE_DIR, "uploads")
UNPACK_DIR   = os.path.join(BASE_DIR, "services", "unpacked")
META_DIR      = os.path.join(BASE_DIR, "meta_json")
STATIC_DIR    = os.path.join(BASE_DIR, "static", "callgraphs")
CAPA_JSON_DIR = os.path.join(BASE_DIR, "services", "CAPA", "capa_json")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

def format_cwe(data_cwe: list) -> str:
    formatted = []
    for name, code, description in data_cwe:
        summary = description.split("::")[0].strip() if description else ""
        print(f"Formatted CWE: {name} ({code}) - {summary}")
        formatted.append(f"- [{code}] {name}: {summary}")
    return "\n".join(formatted)

# 🚀 FastAPI 앱 설정
app = FastAPI(title="YARAAI Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 서빙
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/meta_json", StaticFiles(directory=META_DIR), name="meta_json")


# 📤 파일 업로드 + 분석 + 룰 생성 파이프라인
@app.post("/upload")
async def upload_and_analyze(file: UploadFile = File(...)):
    # 1) 파일 저장
    ext = file.filename.rsplit(".", 1)[-1].lower()
    if ext not in ("exe", "dll"):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    unique_name = f"{uuid.uuid4()}.{ext}"
    dest_path   = os.path.join(UPLOAD_DIR, unique_name)
    data = await file.read()
    with open(dest_path, "wb") as f:
        f.write(data)
    base_uuid = os.path.splitext(unique_name)[0]

    # 1.5) 패커 탐지
    packers = detect_packers(dest_path)
    print(f"Detected packers: {packers}")

    # 패커가 감지되었을 때만 언패킹 시도 및 분석 대상 경로 결정
    if packers:
        unpack_results = unpack_file(dest_path, UNPACK_DIR, packers)
        print(f"Unpack results: {unpack_results}")

        # 언패킹에 성공한 패커가 하나라도 있으면 unpacked 파일을 분석
        if any(unpack_results.values()):
            analyze_path = os.path.join(UNPACK_DIR, os.path.basename(dest_path))
        else:
            analyze_path = dest_path
    else:
        # 패커가 없으면 원본 그대로 분석
        analyze_path = dest_path
    
    # 2) 정적/동적 분석
    try:
        report = analyze_file(analyze_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")

    # 3) Jeongbin’s YARA 룰 자동 생성
    tmp_meta = os.path.join(UPLOAD_DIR, f"{base_uuid}.json")
    with open(tmp_meta, "w", encoding="utf-8") as mf:
        json.dump(report, mf, ensure_ascii=False, indent=2)

    try:
        yara_txt = generate_yara_rule(tmp_meta)
        print("YARA rule generation successful")
    except Exception:
        yara_txt = ""
        print("YARA rule generation failed, using empty rule.") 

    # 4) Suricata 룰 변환 (YARA → Suricata)
    tmp_yar = os.path.join(UPLOAD_DIR, f"{base_uuid}.yar")
    with open(tmp_yar, "w", encoding="utf-8") as yf:
        yf.write(yara_txt)

    script = os.path.join(BASE_DIR, "services", "suricata", "run_convert.py")
    try:
        proc = subprocess.run(
            ["python3", script, tmp_yar],
            cwd=os.path.join(BASE_DIR, "services", "suricata"),
            capture_output=True, text=True, check=True
        )
        lines = proc.stdout.splitlines()
        if lines and not lines[0].startswith("alert"):
            lines = lines[1:]
        report["suricata_rule"] = "\n".join(lines)
        print("Suricata rule conversion successful")
    except subprocess.CalledProcessError:
        report["suricata_rule"] = ""
        print("Suricata rule conversion failed, using empty rule.")

    # 5) 결과 저장
    report["yara_rule"] = yara_txt
    meta_path = os.path.join(META_DIR, f"{base_uuid}.json")
    with open(meta_path, "w", encoding="utf-8") as mf:
        json.dump(report, mf, ensure_ascii=False, indent=2)

    suri_path = os.path.join(META_DIR, f"{base_uuid}_suricata.json")
    with open(suri_path, "w", encoding="utf-8") as sf:
        json.dump({"suricata_rule": report["suricata_rule"]}, sf, ensure_ascii=False, indent=2)

    # 6) CallGraph HTML 생성
    html_path = os.path.join(STATIC_DIR, f"{base_uuid}.html")
    try:
        generate_call_graph(meta_path, html_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CallGraph 생성 실패: {e}")

    return {"filename": unique_name, "callgraph": f"/static/callgraphs/{base_uuid}.html"}


# 📋 리포트 목록 조회
@app.get("/reports")
def list_reports():
    files = [f for f in os.listdir(UPLOAD_DIR) if os.path.isfile(os.path.join(UPLOAD_DIR, f))]
    return JSONResponse(content={"reports": files})


# 📄 특정 리포트 조회 (yara_rule, suricata_rule 포함)
@app.get("/reports/{filename}")
def get_report(filename: str):
    base_uuid = os.path.splitext(filename)[0]
    meta_path = os.path.join(META_DIR, f"{base_uuid}.json")
    if not os.path.exists(meta_path):
        raise HTTPException(status_code=404, detail="Report not found")
    with open(meta_path, "r", encoding="utf-8") as mf:
        data = json.load(mf)
    return JSONResponse(content=data)


# 🔄 History용 저장된 JSON 조회 엔드포인트 추가
@app.get("/api/history/{file_id}")
async def get_history(file_id: str):
    """
    History 페이지에서 클릭한 file_id에 해당하는
    저장된 JSON 보고서를 그대로 내려줍니다.
    """
    json_path = os.path.join(META_DIR, f"{file_id}.json")
    if not os.path.isfile(json_path):
        raise HTTPException(status_code=404, detail=f"No history for {file_id}")
    return FileResponse(json_path, media_type="application/json")


# 🧠 GPT 분석 섹션 API (1~7)
class SectionRequest(BaseModel):
    sectionId: int
    filename: str

@app.post("/api/section")
def fetch_gpt_section(req: SectionRequest = Body(...)):
    base = os.path.splitext(req.filename)[0]
    meta_path = os.path.join(META_DIR, f"{base}.json")
    if not os.path.isfile(meta_path):
        raise HTTPException(status_code=404, detail="Report not found")
    with open(meta_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    section_map = {
    1: "① Information",
    2: "② 정적 분석",
    3: "③ 동적 분석",
    4: "④ Call Graph",
    5: "⑤ 클러스터링",
    6: "⑥ MITRE ATT&CK",
    7: "⑦ CWE",
    }   
    SECTION_PROMPTS = {
    1: f"""① Information
- 다음 정보를 포함한 요약 리포트 5줄 이상으로 자연어 처리
{data['MITRE'][:3]}, {data['get_metadata'].get('module', '')}""",

    2: f"""② 정적 분석
(1) 파일 정보
- 형식: {data['get_metadata'].get('fileType', '')}
- 크기: {data['get_metadata'].get('fileSize', '')} bytes

(2) 패킹 여부
- 엔트로피: {data['file_entropy']}
- 패커 탐지 결과: 추후 반영 필요

(3) Import 함수
- 주요 예시: {', '.join(data['pe_headers'].get('imports', []))}

(4) YARA 룰 매칭
- 룰 수: {len(data['yara_rules']) if isinstance(data['yara_rules'], list) else 1}
- 커버리지 평가: 추후 반영 필요""",

    3: f"""③ 동적 분석
- 악성코드 실행 시 생성된 프로세스 정보 확인
- 레지스트리 키 조작 여부 확인
- 파일 생성/수정/삭제 이벤트 확인
- 위 행위들의 로그를 시간대별로 정리""",

    4: f"""④ Call Graph
- 함수 호출 관계를 시각적으로 표현한 HTML 파일 생성됨
- 분석가가 내부 로직 흐름을 빠르게 파악할 수 있음""",

    5: f"""⑤ 클러스터링
- 유사한 악성코드 샘플들을 클러스터링하여 그룹화""",

    6: f"""⑤ MITRE ATT&CK 매핑
- 감지된 기술: {data['MITRE']}
- 제공된 각 기술에 대한 설명을 자연어 처리해서 제공. 예를 들어 T1082 : "System Information Discovery"는 시스템 정보를 수집하는 기술로, 공격자가 시스템의 구성 요소를 이해하고 취약점을 찾는 데 사용됨." 이런 형식으로 설명해주세요.
""",

    7: f"""(1) 탐지된 행위별로 해당하는 CWE ID를 매핑한 후 각 CWE에 대한 설명과 저 1000.csv 에 어떤 기준으로 매핑한 건지 자연어 처리 
    예를 들어 CWE-785: "use of path manipulation function without maximum-sized buffer"는 경로 조작 함수 사용 시 출력 버퍼 크기를 충분히 지정하지 않아 버퍼 오버플로우 등의 취약점으로 이어질 수 있는 경우에 해당함. 이런 형식으로 작성해주세요.
{format_cwe(data['CWE'])}"""
}
    
    section_title = section_map.get(req.sectionId)
    prompt_body   = SECTION_PROMPTS.get(req.sectionId)
    if not section_title or not prompt_body:
        raise HTTPException(status_code=400, detail="Invalid sectionId")

    meta = data['get_metadata']
    prompt = f"""
당신은 악성코드 분석 전문가입니다. 한글로 아래의 요구사항을 해결해주세요. 
출력은 반드시 **마크다운 형식 없이**, 일반 텍스트만 사용하여 작성해주세요. 
제공한 정보 이외의 내용들을 출력하지 마세요. 
정확하고 구체적인 문장으로 최대한 풀어써주세요. 
초등학생들도 알 수 있게 작성해주세요.
문체를 “~함”으로 통일해주세요.
표준 용어(IOC, TTP, MITRE ATT&CK) 사용해주세요
객관적이고 중립적인 어조를 사용해주세요
Make sure to think step-by-step when answering. 

<분석 대상 개요>
- 파일명: {meta.get("module","")}
- 해시(SHA-256): {meta.get("sha256","")}
- 형식: {meta.get("fileType","")}
- 크기: {meta.get("fileSize","")}

<요약 보고서 - {section_title}>
{prompt_body}
"""
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}],
            max_tokens=1024,
            temperature=0.7
        )
        text = resp.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT 요청 실패: {e}")

    if req.sectionId == 4:
        filename_base = meta.get("module","").rsplit(".",1)[0]
        return JSONResponse(content={
            "text": text,
            "callgraph_html": f"/static/callgraphs/{filename_base}.html"
        })
    return JSONResponse(content={"text": text})


# 🧠 CAPA 기반 자연어 분석 보고서 (8)
class CapaRequest(BaseModel):
    sha256: str

@app.post("/api/capa-report")
def get_capa_report(req: CapaRequest = Body(...)):
    base      = req.sha256
    capa_path = os.path.join(CAPA_JSON_DIR, f"{base}.json")
    if not os.path.exists(capa_path):
        raise HTTPException(status_code=404, detail="CAPA 결과를 찾을 수 없습니다")
    with open(capa_path, "r", encoding="utf-8") as f:
        capa_json = json.load(f)

    prompt = f"""
아래는 CAPA 분석 도구가 출력한 JSON 결과입니다。
다음 템플릿에 맞춰 한글 자연어 보고서를 작성해주세요。
...
"""
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"당신은 숙련된 악성코드 분석가입니다。"},
                {"role":"user","content":prompt}
            ],
            max_tokens=1024,
            temperature=0.2
        )
        report = resp.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT 요청 실패: {e}")

    return JSONResponse(content={"report": report})