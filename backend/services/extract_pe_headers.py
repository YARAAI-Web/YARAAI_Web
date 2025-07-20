import pefile
import sys
import json
import os
import hashlib
from datetime import datetime

def get_sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def extract_headers(path):
    try:
        pe = pefile.PE(path)

        # SHA256 및 컴파일 시간
        sha256 = get_sha256(path)
        timestamp = datetime.utcfromtimestamp(pe.FILE_HEADER.TimeDateStamp).strftime('%Y-%m-%d %H:%M:%S')

        headers = {
            "file_name": os.path.basename(path),
            "sha256": sha256,
            "entry_point": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
            "compilation_timestamp": timestamp,
            "machine": hex(pe.FILE_HEADER.Machine),
            "number_of_sections": pe.FILE_HEADER.NumberOfSections,
            "pointer_to_symbol_table": hex(pe.FILE_HEADER.PointerToSymbolTable),
            "number_of_symbols": pe.FILE_HEADER.NumberOfSymbols,
            "size_of_optional_header": pe.FILE_HEADER.SizeOfOptionalHeader,
            "characteristics": hex(pe.FILE_HEADER.Characteristics),
            "image_base": hex(pe.OPTIONAL_HEADER.ImageBase),
            "section_alignment": hex(pe.OPTIONAL_HEADER.SectionAlignment),
            "file_alignment": hex(pe.OPTIONAL_HEADER.FileAlignment),
            "subsystem": hex(pe.OPTIONAL_HEADER.Subsystem),
            "dll_characteristics": hex(pe.OPTIONAL_HEADER.DllCharacteristics),
            "file_type": "DLL" if pe.is_dll() else "Executable",
            "sections": [],
            "imports": [],
            "resources": []
        }

        # 섹션 정보
        for section in pe.sections:
            headers["sections"].append({
                "name": section.Name.decode(errors="ignore").strip('\x00'),
                "virtual_address": hex(section.VirtualAddress),
                "virtual_size": hex(section.Misc_VirtualSize),
                "raw_size": hex(section.SizeOfRawData),
                "pointer_to_raw_data": hex(section.PointerToRawData),
                "characteristics": hex(section.Characteristics)
            })

        # 임포트 DLL
        if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                dll = entry.dll.decode(errors="ignore")
                functions = [imp.name.decode(errors="ignore") if imp.name else f"Ordinal_{imp.ordinal}" for imp in entry.imports]
                headers["imports"].append({
                    "dll": dll,
                    "functions": functions
                })

        # 리소스 정보
        if hasattr(pe, "DIRECTORY_ENTRY_RESOURCE"):
            try:
                for resource_type in pe.DIRECTORY_ENTRY_RESOURCE.entries:
                    name = str(resource_type.name) if resource_type.name else str(resource_type.struct.Id)
                    headers["resources"].append(name)
            except Exception as e:
                headers["resources"].append(f"Error parsing resources: {e}")

        # 임포트 DLL 및 함수 추출
        if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                dll_name = entry.dll.decode(errors="ignore") if entry.dll else "<Unnamed DLL>"
                func_list = []
                for imp in entry.imports:
                    if imp.name:
                        func_list.append(imp.name.decode(errors="ignore"))
                    else:
                        func_list.append(f"Ordinal_{imp.ordinal}")
                headers["imports"].append({
                    "dll": dll_name,
                    "functions": func_list
                })        

        return headers

    except Exception as e:
        print(f"❌ PE 파싱 실패: {e}")
        return {}

def merge_into_metadata_json(pe_path, headers):
    basename = os.path.splitext(os.path.basename(pe_path))[0]
    json_path = os.path.join("meta_json", f"{basename}.json")

    if not os.path.exists(json_path):
        print(f"❌ JSON 파일이 없습니다: {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    metadata["pe_headers"] = headers

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(f"✅ PE 헤더 병합 완료 → {json_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_pe_headers.py <path_to_pe_file>")
        sys.exit(1)

    pe_path = sys.argv[1]
    headers = extract_headers(pe_path)
    if headers:
        merge_into_metadata_json(pe_path, headers)
