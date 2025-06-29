import os
import idaapi
import idautils
import idc
import ida_pro

def extract_c_code():
    try:
        if not idaapi.init_hexrays_plugin():
            print("[!] Hex-Rays Decompiler 사용 불가")
            return ""

        c_code = ""
        for func_ea in idautils.Functions():
            try:
                cfunc = idaapi.decompile(func_ea)
                pseudocode = cfunc.get_pseudocode()
                c_code += "\n".join([line.line for line in pseudocode]) + "\n\n"
            except Exception as e:
                print(f"[!] 함수 0x{func_ea:x} 디컴파일 실패: {e}")
        return c_code
    except Exception as e:
        print(f"[!] 전체 디컴파일 오류: {e}")
        return ""

def write_ch_files(base_path):
    base = os.path.splitext(base_path)[0]
    c_path = base + ".c"
    h_path = base + ".h"

    c_code = extract_c_code()
    h_code = f"#ifndef {os.path.basename(base).upper()}_H\n#define {os.path.basename(base).upper()}_H\n\n// 프로토타입 생략\n\n#endif\n"

    with open(c_path, "w", encoding="utf-8") as f:
        f.write(c_code)
    with open(h_path, "w", encoding="utf-8") as f:
        f.write(h_code)

    print(f"[+] {c_path} / {h_path} 저장 완료")

# 실행
input_file = idaapi.get_input_file_path()
write_ch_files(input_file)

ida_pro.qexit(0)
