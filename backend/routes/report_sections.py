# 📁 backend/routes/report_sections.py

from fastapi import APIRouter
from fastapi.responses import JSONResponse, FileResponse
import os
import json

# ✅ GPT 요약 함수 가져오기
from backend.services.dynamic.split_summary import generate_full_summary_with_split

router = APIRouter()

AFTER_DIR = r"C:\Users\hyunj\analysis_yaraai\after"


@router.get("/api/report/{uuid}/{section}")
def get_report_section(uuid: str, section: str):
    # ✅ [1] behavior part 처리
    if section.startswith("behavior/part/"):
        part_num = section.split("/")[-1]
        path = os.path.join(AFTER_DIR, f"{uuid}_behavior_part_{part_num}.json")

    # ✅ [2] AI 요약 요청 처리
    elif section == "summary-ai":
        summary_list = generate_full_summary_with_split(uuid, AFTER_DIR)
        return JSONResponse(content={"uuid": uuid, "summary": summary_list})

    # ✅ [3] 일반 JSON 반환 처리
    else:
        path = os.path.join(AFTER_DIR, f"{uuid}_{section}.json")

    # ✅ [공통] 존재 여부 확인 후 응답
    if not os.path.exists(path):
        return JSONResponse(status_code=404, content={"error": "Not found"})
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(content=data)
