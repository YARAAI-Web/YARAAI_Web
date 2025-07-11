# backend/services/suricata/run_convert.py

import sys
import os
import hashlib

# 같은 디렉터리의 yara_to_suricata 모듈을 import 할 수 있도록 경로 추가
sys.path.append(os.path.dirname(__file__))
from yara_to_suricata import yara_to_suricata

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_convert.py <yara_file_path>", file=sys.stderr)
        sys.exit(1)

    yara_file_path = sys.argv[1]
    # 1) YARA 룰 읽기
    with open(yara_file_path, "r", encoding="utf-8") as f:
        yara_text = f.read()

    # 2) sid 생성 (md5 기반)
    sid = int(hashlib.md5(yara_text.encode()).hexdigest()[:6], 16) % 1000000 + 1000000

    # 3) Suricata 룰 변환
    suricata_rule = yara_to_suricata(yara_text, sid)

    # 4) 결과 출력
    print(suricata_rule)

if __name__ == "__main__":
    main()
