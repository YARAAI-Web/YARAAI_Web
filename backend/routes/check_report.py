# backend/routes/check_report.py
from fastapi import APIRouter
import os

router = APIRouter()
AFTER_DIR = r"C:\Users\hyunj\analysis_yaraai\after"

@router.get("/api/check-report/{uuid}")
async def check_report(uuid: str):
    report_path = os.path.join(AFTER_DIR, f"{uuid}_dynamic.json")
    return {"exists": os.path.exists(report_path)}
