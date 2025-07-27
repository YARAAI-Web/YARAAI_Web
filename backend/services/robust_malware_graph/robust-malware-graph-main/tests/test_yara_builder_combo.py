from src.rulegen.yara_builder import YaraBuilder


def test_combo_basic():
    builder = YaraBuilder(condition_type="combo")
    rule = builder.build(["call:CreateFileW", "import:WS2_32.dll"])
    assert "1 of ($c*)" in rule
    assert "1 of ($i*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_combo_group_min_count():
    builder = YaraBuilder(condition_type="combo", group_min_count=2)
    rule = builder.build(["call:A", "call:B", "import:X", "import:Y"])
    assert "2 of ($c*)" in rule
    assert "2 of ($i*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_combo_group_min_count_caps_at_len():
    builder = YaraBuilder(condition_type="combo", group_min_count=2)
    rule = builder.build(["call:A", "import:X", "feat"])
    assert "1 of ($o*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_combo_group_min_count_falls_back_any():
    builder = YaraBuilder(condition_type="combo", group_min_count=2)
    rule = builder.build(["call:A", "call:B", "call:C"])
    assert "2 of ($c*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_combo_percentage_falls_back_any():
    builder = YaraBuilder(condition_type="combo", group_percentage=50)
    rule = builder.build(["call:A", "call:B"])
    assert "1 of ($c*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_combo_group_min_count_small_feat():
    builder = YaraBuilder(condition_type="combo", group_min_count=2)
    rule = builder.build(["call:A", "call:B"])
    assert "2 of ($c*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_combo_percentage_single_feature():
    builder = YaraBuilder(condition_type="combo", group_percentage=60)
    rule = builder.build(["call:A"])
    assert "1 of ($c*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_combo_adjust_group_percentage():
    feats = [f"call:A{i}" for i in range(5)] + [f"import:I{i}" for i in range(5)]
    builder = YaraBuilder(
        condition_type="combo",
        group_percentage=50,
        adjust_group_percentage=True,
    )
    rule = builder.build(feats)
    assert "2 of ($c*)" in rule
    assert "2 of ($i*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err


def test_combo_marker_group_mandatory():
    builder = YaraBuilder(condition_type="combo")
    rule = builder.build(["call:A", "import:X", "marker:.foo"])
    assert "1 of ($m*)" in rule
    ok, err = builder.validate(rule)
    assert ok, err
