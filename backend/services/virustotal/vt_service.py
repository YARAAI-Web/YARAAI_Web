# backend/services/virustotal/vt_service.py
from .vt_client import vt_get

def get_vt_data(sha256: str) -> dict:
    """
    sha256 해시로 Virustotal 정보 가져와
    필요한 해시 + 백신 검사 결과만 뽑아서 리턴.
    """
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

    # 백신 벤더별 탐지 결과
    analysis = attrs.get("last_analysis_results", {})

    return {
        "hashes": hashes,
        "file_type":   attrs.get("type_description"),
        "magic":       attrs.get("magic"),
        "file_size":   attrs.get("size"),
        "packer":      packer,
        "analysis":    analysis,
    }
