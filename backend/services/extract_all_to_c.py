# extract_all_to_c.py

# pyright: reportMissingImports=false

import idaapi
import idautils
import ida_hexrays
import ida_pro
import os

pe_api_funcs = [  # 생략: 원본 그대로 유지
    # ...
]

header = '''#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
'''

def decompile_to_c():
    if not ida_hexrays.init_hexrays_plugin():
        print("❌ Hex-Rays plugin 초기화 실패")
        return

    input_path = idaapi.get_input_file_path()
    root = os.path.splitext(os.path.basename(input_path))[0]
    out_dir = os.path.dirname(input_path)
    os.makedirs(out_dir, exist_ok=True)

    c_path = os.path.join(out_dir, f"{root}.c")
    h_path = os.path.join(out_dir, f"{root}.h")

    print(f"📄 .c 파일 경로: {c_path}")
    print(f"📄 .h 파일 경로: {h_path}")

    try:
        c_file = open(c_path, 'w', encoding='utf-8')
        h_file = open(h_path, 'w', encoding='utf-8')
    except Exception as e:
        print(f"❌ 파일 열기 실패: {e}")
        return

    h_file.write(header)
    c_file.write(f'#include "{root}.h"\n\n')

    for ea in idautils.Functions():
        f = idaapi.get_func(ea)
        if not f:
            continue
        try:
            cfunc = ida_hexrays.decompile(f)
        except:
            continue

        if not cfunc:
            continue

        ff = str(cfunc)
        ff = ff.replace("__gmon_start__", "_gmon_start__")
        ff = ff.replace("__noreturn", "")
        ff = ff.replace("timer_t", "time_t")

        func_name = ff[:ff.find("(")].strip().split(' ')[-1].replace('*', '')
        if func_name in pe_api_funcs:
            continue

        off = ff.find("{")
        h_file.write(ff[:off].strip() + ';\n')

        if ff[:2] == "//":
            off = ff.find("{")
            t = ff[:off+1] + "\n}"
            c_file.write(t)
        else:
            c_file.write(ff + '\n\n')

    c_file.close()
    h_file.close()
    print("✅ C/H 코드 저장 완료")

idaapi.auto_wait()
decompile_to_c()
ida_pro.qexit(0)
