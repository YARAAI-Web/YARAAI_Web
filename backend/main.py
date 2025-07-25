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
        print(f"Formatted CWE: {name} ({code}) - {summary}")
        formatted.append(f"- [{code}] {name}: {summary}")
    return "\n".join(formatted)

# 🚀 FastAPI 앱 설정
app = FastAPI(title="YARAAI Analysis API")

print("[🛠️] CORS 미들웨어 설정됨")
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
    print(f"Detected packers: {packers}")

    # 언패킹 여부에 따른 분석 대상 결정
    if packers:
        unpack_results = unpack_file(dest_path, UNPACK_DIR, packers)
        print(f"Unpack results: {unpack_results}")
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
        print(f"[📥] 분석 대상 파일 복사됨 → {before_path}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"before/ 복사 실패: {e}")

    # 2) 정적/동적 분석
    try:
        report = analyze_file(analyze_path)
        report["virustotal"] = get_vt_data(report["get_metadata"]["sha256"])
        print(f"[📥] 분석 대상 파일 복사됨 → {before_path}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")

    # 3) YARA 룰 자동 생성
    tmp_meta = os.path.join(UPLOAD_DIR, f"{base_uuid}.json")
    with open(tmp_meta, "w", encoding="utf-8") as mf:
        json.dump(report, mf, ensure_ascii=False, indent=2)

    try:
        yara_txt = generate_yara_rule(tmp_meta)
        print("YARA rule generation successful")
    except Exception:
        yara_txt = ""
        print("YARA rule generation failed, using empty rule.")

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
        # ... (prompt bodies unchanged) ...
    }

    section_title = section_map.get(req.sectionId)
    prompt_body   = SECTION_PROMPTS.get(req.sectionId)
    if not section_title or not prompt_body:
        raise HTTPException(status_code=400, detail="Invalid sectionId")

    meta = data['get_metadata']
    prompt = f"""
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
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
            temperature=0.7
        )
        text = resp.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT 요청 실패: {e}")

    if req.sectionId == 1:
        return JSONResponse(content={
            "text": text,
            "virustotal": data["virustotal"]
        })
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
                {"role": "system", "content": "당신은 숙련된 악성코드 분석가입니다。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.2
        )
        report = resp.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT 요청 실패: {e}")

    return JSONResponse(content={"report": report})

# 동적 분석 자동 실행
@app.on_event("startup")
def start_run_monitor():
    try:
        subprocess.Popen(["python", "run_monitor.py"])
        print("[🚀] run_monitor.py 자동 실행됨")
    except Exception as e:
        print(f"[❌] run_monitor 자동 실행 실패: {e}")
