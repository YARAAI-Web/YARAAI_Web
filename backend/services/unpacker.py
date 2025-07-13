# services/packer.py

import os
import subprocess
import pefile
from typing import List, Dict

# ─── 1) 패커 탐지용 섹션 이름 키워드 ───────────────────────────────────────
PACKER_SIGNATURES: Dict[str, List[str]] = {
    "UPX":    ["UPX0", "UPX1"],
}

# ─── 2) 패커별 언패킹 커맨드 템플릿 ────────────────────────────────────
#    리스트 형식으로 [exe, args…, "-o"] 까지, 뒤에 (dest, src)를 붙여 실행
UNPACK_COMMANDS: Dict[str, List[str]] = {
    "UPX":    ["upx", "-d", "-o"],
}

def detect_packers(path: str) -> List[str]:
    """
    path 파일의 PE 섹션을 스캔해서 PACKER_SIGNATURES에 매칭되는
    패커 이름 리스트를 반환합니다.
    """
    try:
        pe = pefile.PE(path)
    except pefile.PEFormatError:
        return []
    found: List[str] = []
    for sec in pe.sections:
        name = sec.Name.decode(errors="ignore").rstrip("\x00").upper()
        for packer, sigs in PACKER_SIGNATURES.items():
            if any(name.startswith(sig) for sig in sigs):
                if packer not in found:
                    found.append(packer)
    return found

def unpack_file(path: str, dest_dir: str, packers: List[str]=None) -> Dict[str, bool]:
    """
    detect_packers(path) 또는 인자로 받은 packers 리스트 중
    UNPACK_COMMANDS에 정의된 것만 언패킹 시도하며,
    성공 여부를 {packer: True/False} 형태로 반환합니다.
    """
    if packers is None:
        packers = detect_packers(path)

    results: Dict[str, bool] = {}
    base = os.path.basename(path)
    for p in packers:
        cmd = UNPACK_COMMANDS.get(p)
        if not cmd:
            results[p] = False
            continue
        dst = os.path.join(dest_dir, base)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        full_cmd = cmd + [dst, path]
        try:
            subprocess.run(full_cmd,
                           check=True,
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            results[p] = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            results[p] = False
    return results
