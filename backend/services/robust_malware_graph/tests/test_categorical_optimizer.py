import importlib
import json
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData

from src.cli.categorical_optimizer import CategoricalOptimizer


def test_build_parser_optimize_args():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args([
        "--graph",
        "g.pt",
        "--sample",
        "s.bin",
        "--classifier",
        "c.pt",
        "--optimize",
        "--optimizer-pkl",
        "opt.pkl",
        "--save-optimizer",
        "out.pkl",
        "--opt-beta",
        "0.7",
    ])
    assert args.optimize is True
    assert args.optimizer_pkl == Path("opt.pkl")
    assert args.save_optimizer == Path("out.pkl")
    assert args.opt_beta == 0.7


def test_default_discrete_params():
    """Optimizer defaults should mirror CLI defaults."""
    opt = CategoricalOptimizer()
    params = opt.discrete_params()
    assert params["condition_type"] == "combo"
    assert params["combine_mode"] == "or"
    assert params["dynamic_k"] is False
    assert params["auto_relax"] is True
    assert params["adjust_group_percentage"] is False
    assert params["group_min_ratio"] == pytest.approx(1e-3, rel=0, abs=1e-6)
    assert params["combine_min_ratio"] == pytest.approx(0.7, rel=0, abs=1e-6)


def test_optimizer_state_roundtrip(tmp_path):
    opt = CategoricalOptimizer(beta=0.8)
    opt.condition_type_logits.data[1] = 1.0
    state = opt.state_dict()
    p = tmp_path / "opt.pkl"
    torch.save(state, p)
    new_opt = CategoricalOptimizer()
    new_opt.load_state_dict(torch.load(p))
    assert new_opt.discrete_params()["condition_type"] == opt.discrete_params()["condition_type"]
    assert new_opt.beta == pytest.approx(0.8)


def test_cli_optimize_saves_state(tmp_path):
    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")
    sample_json = tmp_path / "sample.json"
    sample_json.write_text(json.dumps({"c_code": ["foo"]}))

    opt_out = tmp_path / "state.pkl"
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    mod.main([
        "--graph",
        str(gpath),
        "--sample",
        str(sample),
        "--saliency",
        str(salpath),
        "--classifier",
        str(sample),
        "--json-match",
        "--optimize",
        "--save-optimizer",
        str(opt_out),
    ])
    assert opt_out.is_file()


def test_step_updates_params():
    opt = CategoricalOptimizer()
    init_vals = [p.detach().clone() for p in opt._params]

    cond_prob = torch.nn.functional.gumbel_softmax(
        opt.condition_type_logits, tau=1.0, hard=False
    )
    comb_prob = torch.nn.functional.gumbel_softmax(
        opt.combine_mode_logits, tau=1.0, hard=False
    )
    bool_probs = torch.sigmoid(
        torch.stack([
            opt.dynamic_k_logit,
            opt.auto_relax_logit,
            opt.adjust_group_percentage_logit,
            opt.group_min_ratio_logit,
            opt.combine_min_ratio_logit,
        ])
    )

    cond_indicator = torch.tensor([1.0, 0.0, 0.0, 0.0, 0.0])
    comb_indicator = torch.tensor([0.0, 1.0])

    fp_ratio_benign = 0.5
    fp_weight = 1.0 + fp_ratio_benign
    fp_val = torch.sum(cond_prob * cond_indicator) * bool_probs.mean()
    tp_val = torch.sum(comb_prob * comb_indicator) * bool_probs.mean()
    loss = fp_weight * fp_val + opt.beta * (1.0 - tp_val)

    opt.step(loss)

    for p0, p1 in zip(init_vals, opt._params):
        assert not torch.allclose(p0, p1)

    for p in opt._params:
        assert p.grad is not None and torch.any(p.grad != 0)


def test_evaluate_single_updates_optimizer(tmp_path, monkeypatch):
    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")
    sample_json = tmp_path / "sample.json"
    sample_json.write_text(json.dumps({"c_code": ["foo"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    opt = mod.CategoricalOptimizer()
    init_vals = [p.detach().clone() for p in opt._params]

    mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=1,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        clean_dir=None,
        clean_sample=None,
        clean_paths=None,
        sample_json=sample_json,
        json_match=True,
        combine_mode="or",
        optimizer=opt,
    )

    assert any(not torch.allclose(p0, p1) for p0, p1 in zip(init_vals, opt._params))


def test_optimizer_loss_fp_ratio_weight():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    opt = mod.CategoricalOptimizer()
    trial = {
        "false_positive": True,
        "detected": True,
        "condition_type": "any",
        "combine_mode": "or",
    }

    torch.manual_seed(0)
    low = mod._optimizer_loss(trial, opt, fp_ratio_benign=0.0)
    torch.manual_seed(0)
    high = mod._optimizer_loss(trial, opt, fp_ratio_benign=1.0)

    assert high > low


def test_cli_global_steps_multiple_generations(tmp_path, monkeypatch):
    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    calls: list[str] = []

    def record_mutate(params: dict, key: str) -> None:
        calls.append(key)

    monkeypatch.setattr(mod.PopulationOptimizer, "_mutate_param", staticmethod(record_mutate))

    def fake_eval(*a, optimizer=None, **k):
        trial = {"detected": True, "condition_type": "any", "combine_mode": "or"}
        if optimizer is not None:
            from src.cli.explainer_rule_eval.optimizer_utils import _optimizer_step
            _optimizer_step(trial, optimizer)
        return trial

    monkeypatch.setattr(mod, "evaluate_single", fake_eval)

    mod.main(
        [
            "--graph",
            str(gpath),
            "--sample",
            str(sample),
            "--saliency",
            str(salpath),
            "--classifier",
            str(sample),
            "--optimize",
            "--pop-size",
            "2",
            "--global-steps",
            "3",
            "--mutation-rate",
            "1.0",
        ]
    )

    assert len(calls) == 6


def test_population_optimizer_local_steps(monkeypatch):
    mod = importlib.import_module("src.cli.categorical_optimizer")

    calls: list[int] = []

    def record_step(self, *a, **k):
        calls.append(id(self))

    monkeypatch.setattr(mod.CategoricalOptimizer, "step", record_step)

    pop = mod.PopulationOptimizer(population_size=3, steps=1, local_steps=2)
    result = {"detected": True, "false_positive": False, "fp_ratio_benign": 0.0}
    pop.step([result] * 3)

    assert len(calls) == 3 + 3 * 2

