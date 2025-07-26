# main.py

from dotenv import load_dotenv  # test
import os
import uuid
import json
import subprocess
import shutil

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
from services.dynamic.gpt_summary import generate_summary_from_dynamic_report
from services.virustotal.vt_service import get_vt_data
from routes import dynamic_summary, check_report

# 🔐 환경 변수 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 📁 디렉터리 경로 설정
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR    = os.path.join(BASE_DIR, "uploads")
UNPACK_DIR    = os.path.join(BASE_DIR, "services", "unpacked")
META_DIR      = os.path.join(BASE_DIR, "meta_json")
STATIC_DIR    = os.path.join(BASE_DIR, "static", "callgraphs")
CAPA_JSON_DIR = os.path.join(BASE_DIR, "services", "CAPA", "capa_json")
BEFORE_DIR    = r"C:\Users\hyunj\analysis_yaraai\before"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

def format_cwe(data_cwe: list) -> str:
    formatted = []
    for name, code, description in data_cwe:
        summary = description.split("::")[0].strip() if description else ""
        formatted.append(f"- [{code}] {name}: {summary}")
    return "\n".join(formatted)

# 🚀 FastAPI 앱 설정
app = FastAPI(title="YARAAI Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(check_report.router)
app.include_router(dynamic_summary.router)

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

    # 언패킹 여부에 따른 분석 대상 결정
    if packers:
        unpack_results = unpack_file(dest_path, UNPACK_DIR, packers)
        if any(unpack_results.values()):
            analyze_path = os.path.join(UNPACK_DIR, os.path.basename(dest_path))
        else:
            analyze_path = dest_path
    else:
        analyze_path = dest_path

    # ✅ 동적 분석용 디렉토리에 복사
    try:
        before_path = os.path.join(BEFORE_DIR, os.path.basename(analyze_path))
        shutil.copy2(analyze_path, before_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"before/ 복사 실패: {e}")

    # 2) 정적/동적 분석
    try:
        report = analyze_file(analyze_path)
        report["virustotal"] = get_vt_data(report["get_metadata"]["sha256"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")

    # 3) YARA 룰 자동 생성
    tmp_meta = os.path.join(UPLOAD_DIR, f"{base_uuid}.json")
    with open(tmp_meta, "w", encoding="utf-8") as mf:
        json.dump(report, mf, ensure_ascii=False, indent=2)

    try:
        yara_txt = generate_yara_rule(tmp_meta)
    except Exception:
        yara_txt = ""

    # 4) Suricata 룰 변환
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
    except subprocess.CalledProcessError:
        report["suricata_rule"] = ""

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
    files = [
        f for f in os.listdir(UPLOAD_DIR)
        if os.path.isfile(os.path.join(UPLOAD_DIR, f))
    ]
    return JSONResponse(content={"reports": files})

# 📄 특정 리포트 조회
@app.get("/reports/{filename}")
def get_report(filename: str):
    base_uuid = os.path.splitext(filename)[0]
    meta_path = os.path.join(META_DIR, f"{base_uuid}.json")
    if not os.path.exists(meta_path):
        raise HTTPException(status_code=404, detail="Report not found")
    with open(meta_path, "r", encoding="utf-8") as mf:
        data = json.load(mf)
    return JSONResponse(content=data)

# 🔄 History용 저장된 JSON 조회
@app.get("/api/history/{file_id}")
async def get_history(file_id: str):
    json_path = os.path.join(META_DIR, f"{file_id}.json")
    if not os.path.isfile(json_path):
        raise HTTPException(status_code=404, detail=f"No history for {file_id}")
    return FileResponse(json_path, media_type="application/json")

# 🧠 GPT 분석 섹션 API (1~7)
class SectionRequest(BaseModel):
    sectionId: int
    filename: str

@app.options("/api/section")
def options_handler():
    return JSONResponse(content={"status": "OK"})

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
        1: f"""
① Information
- 다음 정보를 포함한 요약 리포트를 5줄 이상으로 자연어 처리
  • MITRE ATT&CK 기술 (처음 3개): {data['MITRE'][:3]}
  • 모듈명: {data['get_metadata'].get('module', '')}
  • SHA-256: {data['get_metadata'].get('sha256', '')}

<VirusTotal 상세 정보>
- MD5: {data['virustotal']['hashes']['md5']}
- SHA-1: {data['virustotal']['hashes'].get('sha1', '—')}
- SHA-256: {data['virustotal']['hashes']['sha256']}
- Vhash: {data['virustotal']['hashes'].get('vhash', '—')}
- File type: {data['virustotal']['file_type']}
- Magic: {data['virustotal']['magic']}
- File size: {data['virustotal']['file_size']} bytes
- TrID 상위 3개: {', '.join(f"{t['file_type']} ({t['probability']}%)" for t in data['virustotal'].get('trid', [])[:3])}
- Detect It Easy: {data['virustotal']['analysis'].get('detectiteasy', {}).get('result', '—')}
- Magika: {data['virustotal']['analysis'].get('magika', {}).get('result', '—')}
- Packer: {data['virustotal'].get('packer', '—')}

위 정보를 참고하여 **파일의 기본 속성(해시·파일타입·매직·크기)과  
백신 엔진별 탐지 결과**를 자연어로 요약해 설명해주세요.
""",
        2: f"""
② 정적 분석

(1) PE 헤더 정보
- 형식: {data['pe_headers'].get('file_type', '')} {data['pe_headers'].get('machine', '')}
- 크기: {data['get_metadata'].get('size', '')} bytes
- 섹션 목록: {', '.join([s.get('name', '') for s in data['pe_headers'].get('sections', [])])}

(2) 문자열 (Strings)
- 총 문자열 수: {data["string_stats"].get('string_count', '')}
- 탐지된 C&C 문자열(도메인/URL 포함): 추후 정제 필요

(3) Entry Point 지점
- Entry Point Address: {data.get('get_entry_points')[0].get('address', '') if data.get('get_entry_points') else ''}
- Entry Point Name: {data.get('get_entry_points')[0].get('name', '') if data.get('get_entry_points') else ''}

(4) 난독화 및 패킹 여부
- 섹션 엔트로피 평균: {data['file_entropy']}
- 패커 탐지 결과: 추후 반영 필요

(5) YARA 룰 매칭
- 탐지된 룰 수: {len(data['yara_rules']) if isinstance(data['yara_rules'], list) else 1}
""",
        3: """
③ 동적 분석
- 악성코드 실행 시 생성된 프로세스 정보 확인
- 레지스트리 키 조작 여부 확인
- 파일 생성/수정/삭제 이벤트 확인
- 위 행위들의 로그를 시간대별로 정리
""",
        4: """
④ Call Graph
- 함수 호출 관계를 시각적으로 표현한 HTML 파일 생성됨
- 분석가가 내부 로직 흐름을 빠르게 파악할 수 있음
""",
        5: """
⑤ 클러스터링
- 유사한 악성코드 샘플들을 클러스터링하여 그룹화
""",
        6: f"""
⑥ MITRE ATT&CK 매핑
- 감지된 기술: {data['MITRE']}
- 각 기술 설명: 예) [T1082] "System Information Discovery": 시스템 정보를 수집하는 기술
- 전체 동작 과정을 자세히 설명
""",
        7: f"""
⑦ CWE 매핑
- 매핑된 CWE ID 설명 및 매핑 기준: {format_cwe(data['CWE'])}
- 전체 동작 과정을 자세히 설명
"""
    }

    title = section_map.get(req.sectionId)
    body  = SECTION_PROMPTS.get(req.sectionId)
    if not title or not body:
        raise HTTPException(status_code=400, detail="Invalid sectionId")

    prompt = f"""
당신은 악성코드 분석 전문가입니다. 아래 요구사항에 따라 한글로 작성해주세요.

<분석 대상 개요>
- 파일명: {data['get_metadata'].get('module')}
- SHA-256: {data['get_metadata'].get('sha256')}
- 형식: {data['get_metadata'].get('fileType')}
- 크기: {data['get_metadata'].get('fileSize')}

<{title}>
{body}
"""

    try:
        resp = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
            temperature=0.7
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT 요청 실패: {e}")

    text = resp.choices[0].message.content.strip()
    if req.sectionId == 1:
        return JSONResponse(content={"text": text, "virustotal": data["virustotal"]})
    if req.sectionId == 4:
        base = data["get_metadata"]["module"].rsplit(".", 1)[0]
        return JSONResponse(content={"text": text, "callgraph_html": f"/static/callgraphs/{base}.html"})
    return JSONResponse(content={"text": text})

# 🧠 CAPA 기반 자연어 분석 보고서 (8)
class CapaRequest(BaseModel):
    sha256: str

@app.post("/api/capa-report")
def get_capa_report(req: CapaRequest = Body(...)):
    capa_path = os.path.join(CAPA_JSON_DIR, f"{req.sha256}.json")
    if not os.path.exists(capa_path):
        raise HTTPException(status_code=404, detail="CAPA 결과를 찾을 수 없습니다")
    with open(capa_path, "r", encoding="utf-8") as f:
        capa_json = json.load(f)

    prompt = "아래는 CAPA 분석 도구가 출력한 JSON 결과입니다...\n"
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 숙련된 악성코드 분석가입니다。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.2
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT 요청 실패: {e}")

    return JSONResponse(content={"report": resp.choices[0].message.content.strip()})

# 동적 분석 자동 실행
@app.on_event("startup")
def start_run_monitor():
    try:
        subprocess.Popen(["python", "run_monitor.py"])
    except Exception as e:
        print(f"run_monitor 자동 실행 실패: {e}")
