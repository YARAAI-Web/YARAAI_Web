# services/utils/cleanup.py

import os
import shutil

def cleanup_file(file_path):
    done_dir = r"C:\Users\User\Desktop\yaraai\done"
    os.makedirs(done_dir, exist_ok=True)

    filename = os.path.basename(file_path)
    dest_path = os.path.join(done_dir, filename)

    try:
        shutil.move(file_path, dest_path)
        print(f"[📁] 분석 완료 후 이동됨 → {dest_path}")
    except Exception as e:
        print(f"[⚠️] 파일 이동 실패: {e}")
