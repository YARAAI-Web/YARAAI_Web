from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

AFTER_DIR = r"C:\Users\User\Desktop\yaraai\after"

@router.get("/download-json/{uuid}")
def download_dynamic_json(uuid: str):
    json_path = os.path.join(AFTER_DIR, f"{uuid}_dynamic.json")
    if not os.path.isfile(json_path):
        return {"error": "File not found"}
    return FileResponse(
        path=json_path,
        filename=f"{uuid}_dynamic.json",
        media_type="application/json"
    )
