import pefile
import sys
import json
import os

def extract_headers(path):
    try:
        pe = pefile.PE(path)

        headers = {
            "file_name": os.path.basename(path),
            "machine": hex(pe.FILE_HEADER.Machine),
            "number_of_sections": pe.FILE_HEADER.NumberOfSections,
            "time_date_stamp": hex(pe.FILE_HEADER.TimeDateStamp),
            "pointer_to_symbol_table": hex(pe.FILE_HEADER.PointerToSymbolTable),
            "number_of_symbols": pe.FILE_HEADER.NumberOfSymbols,
            "size_of_optional_header": pe.FILE_HEADER.SizeOfOptionalHeader,
            "characteristics": hex(pe.FILE_HEADER.Characteristics),
            "entry_point": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
            "image_base": hex(pe.OPTIONAL_HEADER.ImageBase),
            "section_alignment": hex(pe.OPTIONAL_HEADER.SectionAlignment),
            "file_alignment": hex(pe.OPTIONAL_HEADER.FileAlignment),
            "subsystem": hex(pe.OPTIONAL_HEADER.Subsystem),
            "dll_characteristics": hex(pe.OPTIONAL_HEADER.DllCharacteristics),
            "sections": []
        }

        for section in pe.sections:
            headers["sections"].append({
                "name": section.Name.decode(errors="ignore").strip('\x00'),
                "virtual_address": hex(section.VirtualAddress),
                "virtual_size": hex(section.Misc_VirtualSize),
                "raw_size": hex(section.SizeOfRawData),
                "characteristics": hex(section.Characteristics)
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
