import pytest
import json

pytest.importorskip("torch")

from src.graphs.loaders.fcg_loader import FCGLoader, _EDGE_KIND_CONTAINS


def test_convert_pejson_to_fcg():
    sample = {
        "get_current_function": {"size": "0x50"},
        "pe_headers": {
            "entry_point": "0x1000",
            "number_of_sections": 3,
            "sections": [
                {"name": ".text", "virtual_address": "0x1000", "virtual_size": "0x100"},
                {"name": ".data", "virtual_address": "0x2000", "virtual_size": "0x200"},
                {"name": ".rsrc", "virtual_address": "0x3000", "virtual_size": "0x300"},
            ],
        },
    }

    fcg = FCGLoader._convert_pejson_to_fcg(sample)

    assert set(["functions", "calls", "entry_id"]).issubset(fcg)

    num_sections = sample["pe_headers"]["number_of_sections"]
    section_funcs = [f for f in fcg["functions"] if f["id"] != 0 and f.get("kind") != "token"]
    assert len(section_funcs) == num_sections

    for idx in range(1, num_sections + 1):
        assert fcg["calls"][idx - 1] == {"src": 0, "dst": idx, "type": "calls"}


def test_convert_pejson_to_fcg_adds_tokens():
    sample = {
        "pe_headers": {
            "entry_point": "0x1000",
            "sections": [
                {"name": ".text", "virtual_address": "0x1000", "virtual_size": "0x100"}
            ],
        },
        "get_current_function": {"size": "0x50"},
    }

    fcg = FCGLoader._convert_pejson_to_fcg(sample)
    tokens = [f for f in fcg["functions"] if f.get("kind") == "token"]
    assert tokens
    token_ids = {t["id"] for t in tokens}
    for t in tokens:
        edge = next(e for e in fcg["calls"] if e["dst"] == t["id"])
        assert edge["type"] == _EDGE_KIND_CONTAINS
        assert edge["src"] not in token_ids


def test_convert_pejson_to_fcg_section_name():
    sample = {
        "pe_headers": {
            "entry_point": "0x1000",
            "sections": [
                {"name": ".sec", "virtual_address": "0x1000", "virtual_size": "0x100"}
            ],
        },
        "get_current_function": {"size": "0x20"},
    }

    fcg = FCGLoader._convert_pejson_to_fcg(sample)
    sec_func = next(f for f in fcg["functions"] if f["id"] == 1)
    assert sec_func.get("section_name") == ".sec"


def test_parse_preserves_kind_and_text():
    sample = {
        "functions": [
            {"id": 0, "name": "main", "addr": "0x0"},
            {"id": 1, "name": "helper_func", "addr": "0x10"},
        ],
        "calls": [{"src": 0, "dst": 1, "type": "calls"}],
        "entry": 0,
    }
    raw = json.dumps(sample).encode()
    data = FCGLoader()._parse(raw)
    assert hasattr(data, "kind_str")
    assert hasattr(data, "text")
    assert "main" in data.text
    assert any(k == "token" for k in data.kind_str)

