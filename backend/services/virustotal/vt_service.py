from .vt_client import vt_get

def get_vt_data(sha256: str) -> dict:
    js = vt_get(f"/files/{sha256}")
    attrs = js["data"]["attributes"]

    # 해시 정보
    hashes = {
        "md5": attrs.get("md5"),
        "sha1": attrs.get("sha1"),
        "sha256": attrs.get("sha256"),
        "vhash": attrs.get("vhash"),
        "authentihash": attrs.get("authentihash"),
        "imphash": attrs.get("imphash"),
        "rich_pe_header_hash": attrs.get("rich_pe_header_hash"),
        "ssdeep": attrs.get("ssdeep"),
        "tlsh": attrs.get("tlsh"),
        "trid": attrs.get("trid") or attrs.get("TrID"),
    }

    # PE packer 정보
    pe_info = attrs.get("pe_info", {})
    packer = pe_info.get("packer") or pe_info.get("compiler") or None

    # 백신 탐지 결과 (엔진별)
    vt_results = attrs.get("last_analysis_results", {})

    # 🧠 주요 분석 도구 결과 추출
    def extract_result(name):
        return vt_results.get(name, {}).get("result")

    analysis = {
        "detectiteasy": { "result": extract_result("DetectItEasy") },
        "magika":       { "result": extract_result("Magika") },
        # 필요시 다른 엔진도 추가 가능
    }

    return {
        "hashes": hashes,
        "file_type":   attrs.get("type_description"),
        "magic":       attrs.get("magic"),
        "file_size":   attrs.get("size"),
        "packer":      packer,
        "analysis":    analysis,
    }
