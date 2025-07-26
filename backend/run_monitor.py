# backend/run_monitor.py

import os
import time
from services.dynamic.submit_and_monitor import analyze_dynamically
from services.utils.cleanup import cleanup_file  # ✅ 추가

WATCH_DIR = r"C:\Users\hyunj\analysis_yaraai\before"
PROCESSED = set()

def watch_before_folder():
    print("[🔍] before/ 디렉토리 감시 시작...")
    while True:
        files = [f for f in os.listdir(WATCH_DIR) if f.endswith((".exe", ".dll"))]
        new_files = [f for f in files if f not in PROCESSED]

        for fname in new_files:
            full_path = os.path.join(WATCH_DIR, fname)
            print(f"[📂] 분석 대상 파일 발견: {fname}")

            analyze_dynamically(full_path)

            # ✅ 분석 완료 후 파일 이동
            cleanup_file(full_path)

            PROCESSED.add(fname)

        time.sleep(3)

if __name__ == "__main__":
    watch_before_folder()


