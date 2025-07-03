# backend/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os, uuid, json
from services.analysis import analyze_file

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
META_DIR   = os.path.join(BASE_DIR, "meta_json")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)

app = FastAPI(title="YARAAI Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_and_analyze(file: UploadFile = File(...)):
    ext = file.filename.rsplit(".", 1)[-1].lower()
    if ext not in ("exe", "dll"):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    unique_name = f"{uuid.uuid4()}.{ext}"
    dest_path   = os.path.join(UPLOAD_DIR, unique_name)
    try:
        data = await file.read()
        with open(dest_path, "wb") as f:
            f.write(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

    try:
        report = analyze_file(dest_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")

    base      = os.path.splitext(unique_name)[0]
    meta_path = os.path.join(META_DIR, f"{base}.json")

    # ——— 이 위치로 옮겼습니다! ———
    try:
        with open(meta_path, "w", encoding="utf-8") as mf:
            json.dump(report, mf, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Warning: failed to write meta JSON:", e)

    # 쓰고 나서 확인
    print("DEBUG: META_DIR      =", META_DIR)
    print("DEBUG: computed path  =", meta_path)
    print("DEBUG: file exists?   ", os.path.exists(meta_path))

    return {"filename": unique_name}

@app.get("/reports")
def list_reports():
    files = [
        f for f in os.listdir(UPLOAD_DIR)
        if os.path.isfile(os.path.join(UPLOAD_DIR, f))
    ]
    return {"reports": files}

@app.get("/reports/{filename}")
def get_report(filename: str):
    base      = os.path.splitext(filename)[0]
    meta_path = os.path.join(META_DIR, f"{base}.json")
    if not os.path.exists(meta_path):
        raise HTTPException(status_code=404, detail="Report not found")
    try:
        with open(meta_path, "r", encoding="utf-8") as mf:
            return json.load(mf)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load report: {e}")