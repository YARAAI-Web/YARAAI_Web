import os
import paramiko
import requests
import json
import time
import uuid
import subprocess
import psutil  # ⚠️ VM1에 설치되어 있어야 함 (pip install psutil)

# 설정
VM1_IP = "192.168.56.108"
VM1_USER = "cuckoo"
VM1_PASS = "cuckoo"
REMOTE_INPUT_DIR = "/home/cuckoo/files_input/"
CUCKOO_API = f"http://{VM1_IP}:8090"

LOCAL_RESULT_DIR = r"C:\Users\hyunj\analysis_yaraai\after"
AFTER_DIR = r"C:\Users\hyunj\analysis_yaraai\after"

def analyze_dynamically(filepath):
    print(f"[🚀] 동적 분석 시작: {filepath}")
    ensure_cuckoo_running()

    # 1. 파일명과 UUID 추출
    filename = os.path.basename(filepath)
    file_uuid = os.path.splitext(filename)[0]

    # 2. VM1에 파일 전송 (SSH/SFTP)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(VM1_IP, username=VM1_USER, password=VM1_PASS)
    sftp = ssh.open_sftp()

    remote_path = os.path.join(REMOTE_INPUT_DIR, filename)
    print(f"[📤] 파일 전송 중 → {remote_path}")
    sftp.put(filepath, remote_path)
    sftp.close()

    # 3. Cuckoo에 제출 (API)
    print(f"[📨] Cuckoo에 파일 제출 중...")
    with open(filepath, "rb") as f:
        files = {"file": (filename, f)}
        headers = {"Authorization": "Bearer j7SZCIezICZK_aBh7UYw-w"}
        response = requests.post(f"{CUCKOO_API}/tasks/create/file", files=files, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Cuckoo 제출 실패: {response.text}")

    task_id = response.json().get("task_id")
    print(f"[✅] Task ID: {task_id}")

    # 4. 리포트 대기 및 수신
    wait_for_report(ssh, task_id, file_uuid)

    ssh.close()

def wait_for_report(ssh, task_id, file_uuid, timeout=600):
    print(f"[⏳] 분석 대기 중 (task #{task_id})")
    remote_report = f"/home/cuckoo/.cuckoo/storage/analyses/{task_id}/reports/report.json"
    local_json_path = os.path.join(LOCAL_RESULT_DIR, f"{file_uuid}_dynamic.json")

    sftp = ssh.open_sftp()

    elapsed = 0
    while elapsed < timeout:
        try:
            sftp.stat(remote_report)
            sftp.get(remote_report, local_json_path)
            print(f"[📥] 분석 결과 저장 완료 → {local_json_path}")

            # ✅ 여기서 JSON 분리
            from services.dynamic.split_report import split_report_sections
            with open(local_json_path, encoding="utf-8") as f:
                report_json = json.load(f)
            split_report_sections(report_json, file_uuid, AFTER_DIR)

            break
        except FileNotFoundError:
            time.sleep(5)
            elapsed += 5
    else:
        print("[❌] 분석 시간 초과: report.json 없음")

    # 스크린샷도 다운로드
    download_screenshots(sftp, task_id, file_uuid)
    sftp.close()

def download_screenshots(sftp, task_id, file_uuid):
    remote_shots_dir = f"/home/cuckoo/.cuckoo/storage/analyses/{task_id}/shots/"
    local_shots_dir = os.path.join(LOCAL_RESULT_DIR, f"{file_uuid}_shots")
    os.makedirs(local_shots_dir, exist_ok=True)

    try:
        for fname in sftp.listdir(remote_shots_dir):
            if fname.endswith(".jpg"):
                sftp.get(
                    os.path.join(remote_shots_dir, fname),
                    os.path.join(local_shots_dir, fname)
                )
        print(f"[🖼️] 스크린샷 다운로드 완료 → {local_shots_dir}")
    except Exception as e:
        print(f"[⚠️] 스크린샷 다운로드 실패: {e}")

def ensure_cuckoo_running():
    cuckoo_running = False
    for p in psutil.process_iter(['name', 'cmdline']):
        try:
            name = p.info['name']
            cmdline = " ".join(p.info['cmdline']) if p.info['cmdline'] else ""
            if "cuckoo" in name.lower() or "cuckoo" in cmdline.lower():
                cuckoo_running = True
                break
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue

    if not cuckoo_running:
        print("[⚙️] Cuckoo 실행 안 됨 → 자동 실행 시도 중...")
        subprocess.Popen(["cuckoo"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.Popen(
            ["cuckoo", "web", "runserver", "0.0.0.0:8090"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(10)  # 대기
    else:
        print("[✅] Cuckoo 이미 실행 중.")

from services.dynamic.split_report import split_report_sections

# # ✅ 분석 완료 후 report.json 경로
# report_path = os.path.join(AFTER_DIR, f"{file_uuid}_dynamic.json")
# with open(report_path, encoding="utf-8") as f:
#     report_json = json.load(f)

# # ✅ 섹션별 JSON으로 분리 저장
# split_report_sections(report_json, file_uuid, AFTER_DIR)
