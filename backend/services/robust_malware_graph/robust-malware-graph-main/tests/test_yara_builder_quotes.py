import pytest
from src.rulegen.yara_builder import YaraBuilder


@pytest.mark.parametrize(
    "feat",
    [
        '"foo',    # leading quote only
        'foo"',    # trailing quote only
        '{AA BB',  # missing closing brace
        'AA BB}',  # missing opening brace
        '/abc',    # missing closing slash
        'abc/',    # missing opening slash
    ],
)
def test_unbalanced_delimiters_compile(feat):
    builder = YaraBuilder()
    rule = builder.build([feat])
    ok, err = builder.validate(rule)
    assert ok, f"Failed to validate YARA rule for {feat}: {err}"

