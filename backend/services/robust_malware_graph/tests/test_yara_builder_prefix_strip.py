import pytest
from src.rulegen.yara_builder import YaraBuilder


def test_prefix_and_module_removed_by_default():
    builder = YaraBuilder()
    rule = builder.build(["call:kernel32!CreateFileW", "import:WS2_32.dll"])
    assert 'call:' not in rule
    assert 'import:' not in rule
    assert 'kernel32!' not in rule
    assert '"CreateFileW" nocase ascii' in rule
    assert '"WS2_32.dll" nocase ascii' in rule
    ok, err = builder.validate(rule)
    assert ok, err
