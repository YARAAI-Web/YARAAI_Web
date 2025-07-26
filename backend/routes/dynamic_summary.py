# backend/routes/dynamic_summary.py

from fastapi import APIRouter, HTTPException
import os
import json

from services.dynamic.gpt_summary import generate_full_summary_with_split
from services.utils.patch_report import prepare_report_json_for_prompt  # JSON 구조 보정 함수

router = APIRouter()

# 분석 결과 저장된 디렉터리 경로
DYNAMIC_DIR = r"C:\Users\hyunj\analysis_yaraai\after"

@router.get("/api/dynamic-summary/{filename}")
async def get_dynamic_summary(filename: str):
    # 확장자 자동 보정 (.exe → _dynamic.json)
    if not filename.endswith("_dynamic.json"):
        filename = filename.replace(".exe", "_dynamic.json")

    filepath = os.path.join(DYNAMIC_DIR, filename)

    # 파일 존재 여부 확인
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="분석 결과 파일이 존재하지 않음")

    try:
        # JSON 파일 로드
        with open(filepath, "r", encoding="utf-8") as f:
            report_json = json.load(f)

        # 예외 보정 (잘못된 process 구조, 누락된 항목 등)
        report_json = prepare_report_json_for_prompt(report_json)

        # GPT 요약 생성 (분할 대응 포함)
        summary_lines = generate_full_summary_with_split(report_json)

        return {"summary": summary_lines}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"요약 생성 실패: {str(e)}")
