import pytest
from src.rulegen.yara_builder import YaraBuilder


def test_percentage_condition_min_one():
    builder = YaraBuilder(condition_type="percentage", percentage=10)
    rule = builder.build(["featA", "featB", "featC"])
    assert "1 of them" in rule
    ok, err = builder.validate(rule)
    assert ok, err
