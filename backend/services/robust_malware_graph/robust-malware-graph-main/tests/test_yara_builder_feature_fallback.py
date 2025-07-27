import pytest
from src.rulegen.yara_builder import YaraBuilder


def test_build_uses_short_token_when_no_features():
    builder = YaraBuilder()
    # previously rejected because len < 3
    rule = builder.build(["pe"])
    assert "pe" in rule

