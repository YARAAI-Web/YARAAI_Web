import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
import subprocess
from torch_geometric.data import HeteroData
from src.evaluation.rule_evaluator import RuleEvaluator


class DummyClf(torch.nn.Module):
    def forward(self, data):
        return torch.zeros(len(data), dtype=torch.float)


def test_evaluate_rule_failure_returns_negative(tmp_path):
    evaluator = RuleEvaluator(clf=DummyClf())
    clean = [HeteroData()]
    dummy = [HeteroData()]
    f1_clean, f1_dummy, certified_r, counts = evaluator.evaluate_rule(
        "rule foo { condition: true }", clean, dummy
    )
    assert (f1_clean, f1_dummy) == (0.0, 0.0)
    assert certified_r < 0
    assert counts == (0, 0, 0, 0)


def test_evaluate_rule_capa(monkeypatch):
    evaluator = RuleEvaluator(clf=DummyClf())
    clean = [HeteroData()]
    dummy = [HeteroData()]

    class DummyProc:
        def __init__(self):
            self.returncode = 0
            self.stdout = "{}"

    monkeypatch.setattr(subprocess, "run", lambda *a, **k: DummyProc())

    rule = """rule:
  meta:
    name: test
  features:
    - or:
"""

    f1_clean, f1_dummy, certified_r, counts = evaluator.evaluate_rule(rule, clean, dummy)

    assert isinstance(f1_clean, float)
    assert isinstance(f1_dummy, float)

