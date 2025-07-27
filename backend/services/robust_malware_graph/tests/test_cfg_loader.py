import json
import pytest

pytest.importorskip("torch")

from src.graphs.loaders.cfg_loader import CFGLoader, _EDGE_KIND_CONTAINS


def test_convert_pejson_to_cfg_extracts_tokens():
    sample = {
        "pe_headers": {
            "sections": [
                {
                    "virtual_address": "0x1000",
                    "virtual_size": "0x200",
                    "asm_code": ["mov eax, ebx", "call sub_1000"],
                },
                {
                    "virtual_address": "0x2000",
                    "virtual_size": "0x200",
                    "code": ["int main() { return 0; }"]
                },
            ]
        }
    }

    cfg = CFGLoader._convert_pejson_to_cfg(sample)
    token_nodes = [n for n in cfg["nodes"] if n.get("kind") == "token"]
    texts = {n["text"] for n in token_nodes}
    assert "mov" in texts
    assert "sub_1000" in texts
    assert "main" in texts
    bb_ids = {n["id"] for n in cfg["nodes"] if n["kind"] == "bb"}
    for t in token_nodes:
        edge = next(e for e in cfg["edges"] if e["dst"] == t["id"])
        assert edge["src"] in bb_ids
        assert edge["type"] == _EDGE_KIND_CONTAINS


def test_parse_preserves_kind_and_text():
    sample = {
        "pe_headers": {
            "sections": [
                {
                    "virtual_address": "0x1000",
                    "virtual_size": "0x200",
                    "code": ["int main() {}"]
                }
            ]
        }
    }
    raw = json.dumps(sample).encode()
    loader = CFGLoader()
    data = loader._parse(raw)
    assert hasattr(data, "kind_str")
    assert hasattr(data, "text")
    assert "main" in data.text


def test_convert_pejson_to_cfg_section_name():
    sample = {
        "pe_headers": {
            "sections": [
                {"name": ".x", "virtual_address": "0x1000", "virtual_size": "0x10", "raw_size": "0x10"}
            ]
        }
    }

    cfg = CFGLoader._convert_pejson_to_cfg(sample)
    secs = [n for n in cfg["nodes"] if n["kind"] == "section"]
    assert secs and secs[0].get("name") == ".x"
