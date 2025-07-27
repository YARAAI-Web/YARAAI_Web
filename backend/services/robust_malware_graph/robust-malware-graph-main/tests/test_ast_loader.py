import pytest
pytest.importorskip("torch")

from src.graphs.loaders.ast_loader import ASTLoader
import json
import logging



def test_convert_pejson_extracts_tokens():
    sample = {
        "pe_headers": {},
        "c_code": ["int main() { sub_1003A53B(); }"]
    }
    ast = ASTLoader._convert_pejson_to_ast(sample)
    token_nodes = [n for n in ast["nodes"] if n["kind"] == "token"]
    texts = {n["text"] for n in token_nodes}
    assert "main" in texts
    assert "sub_1003A53B" in texts
    for n in token_nodes:
        root_edges = [e for e in ast["edges"] if e[1] == n["id"]]
        assert root_edges and root_edges[0][0] == 0


def test_parse_missing_kind_assigns_unknown(tmp_path, caplog):
    sample = {"nodes": [{"id": 0, "kind": "file"}, {"id": 1}], "edges": [[0, 1]]}
    path = tmp_path / "ast.json"
    path.write_text(json.dumps(sample))
    loader = ASTLoader()
    caplog.set_level(logging.WARNING)
    data = loader._parse(path)
    assert any("node missing 'kind'" in rec.message for rec in caplog.records)
    assert "unknown" in data.kind_str


def test_convert_pejson_section_name():
    sample = {
        "pe_headers": {
            "sections": [
                {"name": ".foo", "virtual_size": "0x10", "raw_size": "0x10"}
            ]
        }
    }
    ast = ASTLoader._convert_pejson_to_ast(sample)
    sec_nodes = [n for n in ast["nodes"] if n["kind"] == "section"]
    assert sec_nodes and sec_nodes[0].get("name") == ".foo"

