import json
import pytest

pytest.importorskip("torch")

from src.graphs.loaders.syscall_loader import SysCallLoader


def test_parse_adds_token_nodes_and_edges():
    sample = {
        "syscalls": [
            {"id": 0, "name": "open"},
            {"id": 1, "name": "read"},
        ],
        "edges": [
            {"src": 0, "dst": 1, "type": "seq"}
        ],
    }
    raw = json.dumps(sample).encode()
    loader = SysCallLoader()
    data = loader._parse(raw)
    # original syscall names preserved
    assert data.sc_name == ["open", "read"]
    # token texts added
    assert hasattr(data, "token_text")
    assert set(data.token_text) >= {"open", "read"}
    # token nodes increase node count
    assert data.num_nodes == 4
    # edges include seq edge and token edges
    assert data.edge_index.size(1) == 3

