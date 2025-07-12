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

# 🔐 환경 변수 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 📁 디렉터리 경로 설정
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR    = os.path.join(BASE_DIR, "uploads")
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

    # 2) 정적/동적 분석
    try:
        report = analyze_file(dest_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")

    # 3) Jeongbin’s YARA 룰 자동 생성
    tmp_meta = os.path.join(UPLOAD_DIR, f"{base_uuid}.json")
    with open(tmp_meta, "w", encoding="utf-8") as mf:
        json.dump(report, mf, ensure_ascii=False, indent=2)

    try:
        yara_txt = generate_yara_rule(tmp_meta)
    except Exception:
        yara_txt = ""

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
    metadata: dict

SECTION_PROMPTS = {
    1: """① 패킹 또는 암호화 기법 사용 여부
- Entropy 분석 및 패커 명칭 확인
- .text 섹션 해시 제공

② 문자열 분석
- 악성 키워드 주제별 정리 (예: powershell, reg add 등)
- URL, 도메인, IP 주소 정리

③ YARA 룰 매칭 분석
- 룰 이름, 조건식, 탐지 문자열 정리
- 커버리지 평가""",
    2: """① 프로세스 행위 분석
- cmd.exe → powershell.exe → svchost.exe 흐름 여부
- 타임라인 기반 정렬 및 자식 PID 기록
- Process Hollowing 여부

② 레지스트리 조작 분석
- Run 키, Task Scheduler, 서비스 등록 여부""",
    3: """① 함수 호출 흐름 시각화
- 주요 함수 중심 노드/엣지 구조 정리
- 기능 단위로 군집화
- 루트 함수 강조 및 전체 노드/엣지 수 요약""",
    4: """① MITRE ATT&CK 기술 매핑
- 탐지된 행위별 TTP 코드 연결

② 근거 제공
- 명령어, 로그 등 증거 기반 설명

③ 시나리오 정리
- 공격 흐름을 시간 순으로 구성""",
    5: """① 생성 파일 덤프 요약
- 경로, 해시, 권한, 타임스탬프

② 시스템 로그 분석
- 실행 시점, 파일 경로, 행위 요약""",
    6: """① 위협 흐름 정리
- 자식 프로세스 생성 → 설정 변경 → 외부 통신 구조

② 공격 목적 유추
- 정보 탈취 vs 지속성 확보

③ 유사 샘플 비교
- 탐지된 룰 또는 행동 기반 비교""",
    7: """① CWE ID 매핑
- 탐지된 행위별 CWE 코드

② 대응책 제시
- 기술적 보안 권고사항 요약

③ 취약점 우선순위 분류
- Critical/High 등급 시각화""",
}

@app.post("/api/section")
def fetch_gpt_section(req: SectionRequest = Body(...)):
    section_map = {
        1: "❶ 정적 분석 결과 구조",
        2: "❷ 동적 분석 결과 (프로세스 및 레지스트리)",
        3: "❸ Call Graph",
        4: "❹ MITRE ATT&CK 매핑",
        5: "❺ Artifacts 덤프 파일",
        6: "❻ 위협 흐름 및 목적 요약",
        7: "❼ CWE 기반 권고",
    }
    section_title = section_map.get(req.sectionId)
    prompt_body   = SECTION_PROMPTS.get(req.sectionId)
    if not section_title or not prompt_body:
        raise HTTPException(status_code=400, detail="Invalid sectionId")

    meta = req.metadata
    prompt = f"""
당신은 악성코드 분석 전문가입니다。

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
            messages=[{"role":"user","content":prompt}],
            max_tokens=1024,
            temperature=0.7
        )
        text = resp.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT 요청 실패: {e}")

    if req.sectionId == 3:
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
