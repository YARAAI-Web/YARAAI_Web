# 📁 backend/routes/report_sections.py

from fastapi import APIRouter
from fastapi.responses import JSONResponse, FileResponse
import os
import json

router = APIRouter()

AFTER_DIR = r"C:\Users\hyunj\analysis_yaraai\after"

@router.get("/api/report/{uuid}/{section}")
def get_report_section(uuid: str, section: str):
    # behavior는 별도 처리
    if section.startswith("behavior/part/"):
        part_num = section.split("/")[-1]
        path = os.path.join(AFTER_DIR, f"{uuid}_behavior_part_{part_num}.json")
    else:
        path = os.path.join(AFTER_DIR, f"{uuid}_{section}.json")

    if not os.path.exists(path):
        return JSONResponse(status_code=404, content={"error": "Not found"})
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(content=data)
