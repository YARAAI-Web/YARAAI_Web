import json
from pathlib import Path

from concurrent.futures import ProcessPoolExecutor

from src.cli.explainer_rule_eval.fp_token_utils import _save_fp_exclude, _load_fp_exclude


def test_save_and_load_fp_exclude(tmp_path):
    fp = tmp_path / "tokens.json"
    _save_fp_exclude(fp, {"b": 1, "a": 2})
    counts = _load_fp_exclude(fp)
    assert counts == {"b": 1, "a": 2}

    _save_fp_exclude(fp, {"c": 1, "a": 3})
    counts = _load_fp_exclude(fp)
    assert counts == {"a": 5, "b": 1, "c": 1}

    data = json.loads(fp.read_text())
    assert list(data.keys()) == ["a", "b", "c"]


def _worker(args):
    fp, tokens = args
    _save_fp_exclude(Path(fp), tokens)


def test_fp_exclude_concurrent(tmp_path):
    fp = tmp_path / "tokens.json"
    inputs = [
        (str(fp), {"a": 1}),
        (str(fp), {"b": 1}),
        (str(fp), {"c": 1}),
        (str(fp), {"a": 2}),
    ]

    with ProcessPoolExecutor(max_workers=4) as exe:
        list(exe.map(_worker, inputs))

    counts = _load_fp_exclude(fp)
    assert counts == {"a": 3, "b": 1, "c": 1}
