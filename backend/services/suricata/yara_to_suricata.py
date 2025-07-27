# backend/services/suricata/yara_to_suricata.py

import re

# 제외 키워드 (보강됨)
EXCLUDE_KEYWORDS = [
    # PE entry point / SEH / CRT
    "DllMain", "DllEntryPoint", "dllmain_crt_", "dllmain_dispatch", "dllmain_raw",
    "_SEH_", "_EH_", "SEH_", "ExceptionList", "ValidateLocalCookies",
    # 디버깅/주소 심볼
    "unk_", "dword_", "off_", "LABEL_", "JUMPOUT", "loc_", "sub_",
    "retaddr", "savedregs", "fdwReason", "lpReserved", "lpvReserved",
    # 컴파일러 특수 함수 및 보호 루틴
    "__security_", "__guard_", "__fastfail", "__get_entropy",
    "__DestructExceptionObject", "__return_address", "__vcrt_", "__scrt_",
    "__except_", "__vcrt_thread_", "__scrt_dllmain", "__except_validate_context_record",
    # 수학 함수 및 타입 관련
    "fabs", "frndint", "_BYTE", "_WORD", "_DWORD", "uintptr_t", "void", "double", "long", "char", "int32_t", "bool",
    "BOOL", "BYTE4", "PVOID", "LPVOID", "HINSTANCE", "DWORD",
    # 시스템 구조체 및 환경
    "StackLimit", "StackBase", "StackCookie", "_TEB", "NtCurrentTeb", "_NLG_", "_IsNonwritableInCurrentImage",
    # 호출 규약 및 연산자
    "__cdecl", "__stdcall", "__fastcall", "__thiscall", "__usercall",
    # 기타 컴파일러 속성 및 정의
    "attributes", "entropy", "default", "struct", "switch", "const", "unsigned",
    # 추가 보편 시스템 API 및 헬퍼
    "IsProcessorFeaturePresent", "LOBYTE", "BYREF"
]

# 정규표현식 기반 제외 패턴
EXCLUDE_PATTERNS = [
    r"^__.*$",
    r"^loc_[0-9A-Fa-f]+$",
    r"^sub_[0-9A-Fa-f]+$",
    r"^off_[0-9A-Fa-f]+$",
    r"^unk_[0-9A-Fa-f]+$",
    r"^dword_[0-9A-Fa-f]+$",
    r"^LABEL_[0-9]+$",
    r"^_EH\d+_.*$",
    r"^_unwind_.*$",
    r"^_ff.*$",
    r"^_UNKNOWN$",
    r"^_ST\d+$",
    r"^[a-fA-F0-9]{4,8}$"
]

def should_exclude(string: str) -> bool:
    sl = string.lower()
    # 키워드 기반 제외
    for kw in EXCLUDE_KEYWORDS:
        if kw.lower() in sl:
            return True
    # 길이 제한
    if len(string) < 4:
        return True
    # 패턴 기반 제외
    for pat in EXCLUDE_PATTERNS:
        if re.match(pat, string):
            return True
    return False

def yara_to_suricata(yara_rule: str, sid: int) -> str:
    # strings: ~ condition: 블록 추출
    m = re.search(r"strings:\s*(.*?)\s*condition:", yara_rule, re.DOTALL)
    if not m:
        raise ValueError("유효한 YARA rule 형식이 아닙니다.")
    lines = m.group(1).splitlines()

    content_rules = []
    for line in lines:
        ms = re.search(r'=\s*"(.*?)"', line)
        mh = re.search(r'=\s*\{(.*?)\}', line)
        if ms:
            s = ms.group(1).strip()
            if not should_exclude(s):
                content_rules.append(f'content:"{s}"; nocase;')
        elif mh:
            hx = mh.group(1).replace(" ", "")
            content_rules.append(f'content:"|{hx}|";')

    if not content_rules:
        return "// No valid content strings after filtering."

    body = "\n    ".join(content_rules)
    return f'''alert tcp any any -> any any (
    msg:"Auto-generated Suricata rule from YARA";
    flow:established,to_server;
    {body}
    threshold:type limit, track by_src, count 1, seconds 60;
    sid:{sid}; rev:1;
)'''
