# services/vt_service.py
from dotenv import load_dotenv
import os
import requests

load_dotenv()  # .env 파일 읽어오기

VT_API_KEY = os.getenv("VT_API_KEY")
VT_BASE_URL = "https://www.virustotal.com/api/v3"
HEADERS     = {"x-apikey": VT_API_KEY}


def vt_get(path: str) -> dict:
    url = f"{VT_BASE_URL}{path}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

def get_vt_data(file_hash: str) -> dict:
    data = {}
    data["details"]     = vt_get(f"/files/{file_hash}")["data"]["attributes"]
    data["analysis"]    = vt_get(f"/files/{file_hash}/analysis")["data"]
    data["sigma_rules"] = vt_get(f"/files/{file_hash}/crowdsourced_sigma_rules")["data"]
    data["relations"]   = vt_get(f"/files/{file_hash}/relations")["data"]
    data["behaviors"]   = vt_get(f"/files/{file_hash}/behaviors")["data"]
    data["comments"]    = vt_get(f"/files/{file_hash}/comments")["data"]
    return data
