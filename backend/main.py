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
        1: "❶ 요약",
        2: "❷ 정적 분석",
        3: "❸ 동적 분석",
        4: "❹ 인터랙티브 그래프(call graph)",
        5: "❺ MITRE ATT&CK 매핑",
        6: "❻  CWE 기반 보안 권고",
    }
    SECTION_PROMPTS = {
    1: f"""① 요약
    - 과정 설명 간단하게(1~2문장) + 악성코드가 발생함으로써 생기는 결과(결론적으로~): 목적…""",
    2: f"""(0) 파일 크기, 포맷(EXE랑 dll 구분. PE header로)

(1) 해당 악성코드 파일에서 패킹이 사용되었는지 분석

- 섹션 기반 패킹 여부 확인
- 사용된 패커 이름(예: UPX, Themida) 제공

(2) Import 함수 목록

- (.idata 섹션에서 추가 추출)

(3) YARA 룰 매칭 결과를 분석(보류-서웅이의 결과 나오고)

- 룰 이름, 조건식, meta 정보, 탐지 문자열 전체 리스트 제공
- 룰 커버리지 수준도 평가""",
    3: f"""- 악성코드 실행 시 어떤 프로세스가 생성되었는지
- 어떤 레지스트리 키가 조작되었는지
- 파일이 생성/변경/삭제되었는지 등 시스템 상의 행위(Event)를 기록
- 시스템 로그(실행 시점, 경로, 행위 등)를 정리""",
    4: f"""callgraph.html 파일을 생성하여
- 함수 호출 관계를 시각적으로 표현""",
    5: f"""(1) 각 기술에 대응하는 로그나 명령어 근거를 제공 ⇒ capa로? 
(2) CAPA 클러스터링으로 악성코드 분류 후 설명 제공
{data['MITRE']}""",
    6: f"""(1) 탐지된 행위별로 해당하는 CWE ID를 매핑한 후 각 CWE에 대한 설명과 저 1000.csv 에 어떤 기준으로 매핑한 건지 자연어 처리 
{data['CWE']}""",
}
    section_title = section_map.get(req.sectionId)
    prompt_body   = SECTION_PROMPTS.get(req.sectionId)
    if not section_title or not prompt_body:
        raise HTTPException(status_code=400, detail="Invalid sectionId")

    meta = data['get_metadata']
    prompt = f"""
당신은 악성코드 분석 전문가입니다. 한글로 아래의 요구사항을 해결해주세요. 
출력은 반드시 **마크다운 형식 없이**, 일반 텍스트만 사용하여 작성해주세요. 
제공한 정보 이외의 내용들을 출력하지 마세요. Make sure to think step-by-step when answering. 

악성코드 분석가들이 악성코드를 정적/동적 분석 툴을 사용하지 않고 악성코드에 대한 전반적인 정보를 얻을 수 있게 해주세요.

정확하고 명료한 문장으로 잘 풀어써주세요
표준 용어(IOC, TTP, MITRE ATT&CK) 사용해주세요

객관적이고 중립적인 어조를 사용해주세요

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