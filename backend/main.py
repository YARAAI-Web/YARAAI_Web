# 그래프 성공 main.py

from dotenv import load_dotenv
import os, uuid, json
from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI

from services.analysis import analyze_file
from generate_callgraph import generate_call_graph

# 🔐 환경 변수 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 📁 디렉터리 경로 설정
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
META_DIR   = os.path.join(BASE_DIR, "meta_json")
STATIC_DIR = os.path.join(BASE_DIR, "static", "callgraphs")

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

app.mount("/static", StaticFiles(directory="static"), name="static")

# 📤 파일 업로드 API
@app.post("/upload")
async def upload_and_analyze(file: UploadFile = File(...)):
    ext = file.filename.rsplit(".", 1)[-1].lower()
    if ext not in ("exe", "dll"):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    unique_name = f"{uuid.uuid4()}.{ext}"
    dest_path   = os.path.join(UPLOAD_DIR, unique_name)
    data = await file.read()
    with open(dest_path, "wb") as f:
        f.write(data)

    try:
        report = analyze_file(dest_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")

    base      = os.path.splitext(unique_name)[0]
    meta_path = os.path.join(META_DIR, f"{base}.json")
    html_path = os.path.join(STATIC_DIR, f"{base}.html")
    
    with open(meta_path, "w", encoding="utf-8") as mf:
        json.dump(report, mf, ensure_ascii=False, indent=2)
    
    # 즉시 Call Graph 생성
    try:
        generate_call_graph(meta_path, html_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CallGraph 생성 실패: {e}")

    return {"filename": unique_name, "callgraph": f"/static/callgraphs/{base}.html"}

# 📋 리포트 목록 조회
@app.get("/reports")
def list_reports():
    files = [
        f for f in os.listdir(UPLOAD_DIR)
        if os.path.isfile(os.path.join(UPLOAD_DIR, f))
    ]
    return {"reports": files}

# 📄 특정 리포트 조회
@app.get("/reports/{filename}")
def get_report(filename: str):
    base      = os.path.splitext(filename)[0]
    meta_path = os.path.join(META_DIR, f"{base}.json")
    if not os.path.exists(meta_path):
        raise HTTPException(status_code=404, detail="Report not found")

    with open(meta_path, "r", encoding="utf-8") as mf:
        return json.load(mf)

# 🧠 GPT 분석 보고서 요청
class SectionRequest(BaseModel):
    sectionId: int
    metadata: dict

SECTION_PROMPTS = {
    1: """① 패킹 또는 암호화 기법 사용 여부
- Entropy 분석 및 패커 명칭 확인
- .text 섹션 해시 제공

② 문자열 분석
- 악성 키워드 주제별 정리 (예: powershell, reg add 등)
- URL, 도메인, IP 주소는 별도 정리

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
    8: """① 분석 점수 및 위험도 요약
- FileScan, Triage 점수

② 탐지 룰 상세 분석
- YARA 문자열 및 조건식

③ 전체 로그 타임라인 구성
- 시계열 정렬 및 필터 가능 구조"""
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
        7: "❽ CWE 기반 권고",
        8: "❾ 분석 JSON 요약",
    }

    section_title = section_map.get(req.sectionId)
    section_prompt = SECTION_PROMPTS.get(req.sectionId)

    if not section_title or not section_prompt:
        raise HTTPException(status_code=400, detail="Invalid sectionId")

    meta = req.metadata
    prompt = f"""
당신은 악성코드 분석 전문가입니다.

다음 샘플에 대한 분석 보고서를 작성해 주세요.  
보고서는 아래 형식을 따르며, **정량적이고 정리된 항목 기반 보고서**처럼 구성해 주세요:

- 각 항목은 '① 제목'으로 시작하고, 그 하위에 (1), (2), ... 형식으로 세부 내용을 나열합니다.
- 문장은 '~로 판단됨', '~가 확인됨', '~로 보임'과 같은 분석 문체를 사용합니다.

<분석 대상 개요>
- 파일명: {meta.get("module", "")}  
- 해시(SHA-256): {meta.get("sha256", "")}  
- 형식: {meta.get("fileType", "")}  
- 크기: {meta.get("fileSize", "")}  

<요약 보고서 - {section_title}>

다음 항목을 기준으로 보고서를 구성해 주세요:

{section_prompt}
"""

    # GPT 응답
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

    # 섹션 3인 경우, Call Graph 생성 및 경로 포함
    if req.sectionId == 3:
        filename = meta.get("module","").rsplit(".",1)[0]
        report_path = os.path.join(META_DIR, f"{filename}.json")
        html_path = os.path.join(STATIC_DIR, f"{filename}.html")
        try:
            generate_call_graph(report_path, html_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"CallGraph 생성 실패: {e}")
        return {"text": text, "callgraph_html": f"/static/callgraphs/{filename}.html"}

    return {"text": text}

