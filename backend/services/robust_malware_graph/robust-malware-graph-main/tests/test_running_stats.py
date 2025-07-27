import math
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "running_stats",
    Path(__file__).resolve().parents[1] / "src" / "common" / "running_stats.py",
)
running_stats = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(running_stats)
RunningStats = running_stats.RunningStats


def test_running_stats_basic():
    rs = RunningStats()
    values = [1.0, 2.0, 3.0]
    for v in values:
        rs.update(v)

    assert math.isclose(rs.mean, 2.0, rel_tol=1e-7)
    expected_var = 2.0 / 3.0
    assert math.isclose(rs.var, expected_var, rel_tol=1e-7)
    assert math.isclose(rs.std, math.sqrt(expected_var), rel_tol=1e-7)
