import pytest
from src.rulegen.yara_builder import YaraBuilder


def test_count_condition():
    builder = YaraBuilder(condition_type="count", min_count=2)
    rule = builder.build(["featA", "featB", "featC"])
    assert "2 of them" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_count_caps_at_len():
    builder = YaraBuilder(condition_type="count", min_count=3)
    rule = builder.build(["featA", "featB"])
    assert "2 of them" in rule
    ok, err = builder.validate(rule)
    assert ok, err
