import pytest

from src.rulegen.yara_builder import tokens_to_yara, YaraBuilder
from src.rulegen.capa_builder import tokens_to_capa

def test_chain_tokens_to_yara():
    rule = tokens_to_yara(["chain:CreateFileW\u2192ReadFile"])
    assert "$s0" in rule
    assert "$s1" in rule
    assert "any of them" in rule
    ok, err = YaraBuilder().validate(rule)
    assert ok, err


def test_chain_tokens_to_capa():
    rule = tokens_to_capa(["chain:CreateFileW\u2192ReadFile"])
    assert "sequence:" in rule

@pytest.mark.parametrize(
    "cond,expected",
    [
        ("any", "any of them"),
        ("all", "all of them"),
        ("percentage", "2 of them"),
    ],
)
def test_chain_tokens_condition_types(cond, expected):
    builder = YaraBuilder(condition_type=cond)
    rule = builder.build(["chain:CreateFileW\u2192ReadFile"])
    assert expected in rule
    ok, err = builder.validate(rule)
    assert ok, err
