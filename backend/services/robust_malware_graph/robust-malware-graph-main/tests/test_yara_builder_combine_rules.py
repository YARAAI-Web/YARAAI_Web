import re
import itertools
from src.rulegen.yara_builder import YaraBuilder


def test_combine_rules_or_and():
    b = YaraBuilder()
    r1 = b.build(["foo"])
    r2 = b.build(["bar"])
    txt_or = b.combine_rules([r1, r2], mode="or", wrapper_name="combined_rule")
    assert "combined_rule" in txt_or
    assert re.search(r"\b(or|and)\b", txt_or)
    ok, err = b.validate(txt_or)
    assert ok, err

    txt_and = b.combine_rules([r1, r2], mode="and", wrapper_name="combined_rule")
    assert "combined_rule" in txt_and
    assert " and " in txt_and
    ok, err = b.validate(txt_and)
    assert ok, err


def test_combine_rules_min_ratio():
    b = YaraBuilder()
    r1 = b.build(["foo"])
    r2 = b.build(["bar"])
    r3 = b.build(["baz"])
    txt = b.combine_rules([r1, r2, r3], min_match_ratio=0.6, wrapper_name="combined_rule")

    names = [re.search(r"rule\s+(\w+)", t).group(1) for t in (r1, r2, r3)]
    m = re.search(r"rule combined_rule \{\n  condition:\n    (.+)\n\}", txt)
    assert m, "wrapper rule missing"
    cond = m.group(1)
    assert cond.count(" or ") >= 2
    for a, bname in itertools.combinations(names, 2):
        assert f"{a} and {bname}" in cond

    ok, err = b.validate(txt)
    assert ok, err


def test_combine_rules_single_rule():
    b = YaraBuilder()
    r = b.build(["foo"])
    txt = b.combine_rules([r])
    assert txt.strip() == r.strip()
