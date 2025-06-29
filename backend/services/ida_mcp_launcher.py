import os
import json
import idaapi
import idautils
import ida_hexrays
import ida_pro

INPUT_PATH = idaapi.get_input_file_path()
BASE_NAME = os.path.splitext(os.path.basename(INPUT_PATH))[0]
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ch_file")
os.makedirs(OUTPUT_DIR, exist_ok=True)

C_PATH = os.path.join(OUTPUT_DIR, BASE_NAME + ".c")
H_PATH = os.path.join(OUTPUT_DIR, BASE_NAME + ".h")

pe_api_funcs = [ ... ]  # 그대로 생략 가능 (본문 유지)
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
        print("Failed to initialize Hex-Rays plugin")
        ida_pro.qexit(1)

    c_file = open(C_PATH, 'w', encoding='utf-8')
    h_file = open(H_PATH, 'w', encoding='utf-8')
    h_file.write(header)
    c_file.write(f'#include "{BASE_NAME}.h"\n\n')

    for ea in idautils.Functions():
        f = idaapi.get_func(ea)
        if f is None:
            continue

        try:
            cfunc = ida_hexrays.decompile(f)
        except:
            continue

        if cfunc is None:
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

        c_file.write(ff + '\n\n')

    c_file.close()
    h_file.close()

    print(f"✅ C/H 파일 저장 완료: {C_PATH}, {H_PATH}")

def save_as_json():
    json_path = os.path.join(OUTPUT_DIR, BASE_NAME + ".json")

    def safe_read_lines(p):
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                return f.read().splitlines()
        return []

    result = {
        "c_code": safe_read_lines(C_PATH),
        "h_code": safe_read_lines(H_PATH)
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ JSON 저장 완료: {json_path}")


idaapi.auto_wait()
decompile_to_c()
save_as_json()
ida_pro.qexit(0)
