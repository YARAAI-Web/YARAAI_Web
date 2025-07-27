import sys
import subprocess
import shutil
from pathlib import Path

from src.rulegen.capa_builder import CapaBuilder


def test_match_file_cli(monkeypatch, tmp_path):
    rule_file = tmp_path / "rule.yml"
    rule_file.write_text(
        """rule:\n  meta:\n    name: test\n  features:\n    - or:\n      - string: foo\n"""
    )
    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")

    builder = CapaBuilder()
    builder.load(rule_file)

    monkeypatch.setitem(sys.modules, "capa", None)
    monkeypatch.setattr(shutil, "which", lambda name: name)

    class DummyProc:
        def __init__(self):
            self.returncode = 0
            self.stdout = '{"rules": ["test"]}'

    called = {}

    def fake_run(cmd, capture_output, text, check):
        called["cmd"] = cmd
        return DummyProc()

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert builder.match_file(sample)
    assert called["cmd"][0] == "capa"
    assert called["cmd"][1] == str(sample)
