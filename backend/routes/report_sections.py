from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os
import json
import sys

# backend 디렉토리 경로를 명시적으로 추가
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# ✅ 정상 import
from services.dynamic.gpt_summary import generate_full_summary_with_split


router = APIRouter()

AFTER_DIR = r"C:\Users\hyunj\analysis_yaraai\after"

@router.get("/api/report/{uuid}/{section}")
def get_report_section(uuid: str, section: str):
    if section.startswith("behavior/part/"):
        part_num = section.split("/")[-1]
        path = os.path.join(AFTER_DIR, f"{uuid}_behavior_part_{part_num}.json")
    else:
        path = os.path.join(AFTER_DIR, f"{uuid}_{section}.json")

    # 🔄 summary 자동 생성
    if section == "summary" and not os.path.exists(path):
        generate_full_summary_with_split(uuid, AFTER_DIR)

    if not os.path.exists(path):
        return JSONResponse(status_code=404, content={"error": "Not found"})
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(content=data)
