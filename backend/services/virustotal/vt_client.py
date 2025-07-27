# backend/services/virustotal/vt_client.py
from dotenv import load_dotenv
import os
import requests

# 1) .env 파일 로드
load_dotenv()

# 2) .env 에 적은 이름(VT_API_KEY) 과 동일하게 읽기
VT_API_KEY = os.getenv("VT_API_KEY")
if not VT_API_KEY:
    raise RuntimeError("Virustotal API 키가 VT_API_KEY에 설정되어 있지 않습니다")

BASE_URL = "https://www.virustotal.com/api/v3"

def vt_get(endpoint: str) -> dict:
    """
    Virustotal v3 GET wrapper.
    endpoint 예: "/files/{sha256}"
    """
    url = BASE_URL + endpoint
    headers = {
        "x-apikey": VT_API_KEY
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()  # 잘못된 키면 여기서 401 발생
    return resp.json()
