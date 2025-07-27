from src.rulegen.yara_builder import YaraBuilder


def test_existing_string_modifiers_kept():
    builder = YaraBuilder()
    feat = '"unsigned" wide ascii nocase'
    rule = builder.build([feat])
    assert '"unsigned" wide ascii nocase" nocase ascii' not in rule
    assert '"unsigned" wide ascii nocase' in rule
    ok, err = builder.validate(rule)
    assert ok, err
