import pytest
from src.rulegen.yara_builder import YaraBuilder

@pytest.mark.parametrize("cond", ["any", "percentage", "count", "combo"])
def test_single_token_all_condition(cond):
    kwargs = {"condition_type": cond}
    if cond == "count":
        kwargs["min_count"] = 2
    if cond == "percentage":
        kwargs["percentage"] = 50
    builder = YaraBuilder(**kwargs)
    rule = builder.build(["featA"])
    if cond == "combo":
        assert "any of them" in rule
    else:
        assert "all of them" in rule
    ok, err = builder.validate(rule)
    assert ok, err
