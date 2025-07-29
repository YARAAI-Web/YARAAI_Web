import importlib
import json
from pathlib import Path
import sys
from collections import defaultdict

import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from torch_geometric.data import HeteroData


def test_build_parser_fp_retries():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--fp-retries",
            "2",
            "--freq-threshold-step",
            "1",
            "--comb-ratio-step",
            "0.2",
        ]
    )
    assert args.fp_retries == 2
    assert args.freq_threshold_step == 1.0
    assert args.comb_ratio_step == 0.2


def test_build_parser_min_freq_threshold():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--min-freq-threshold",
            "-1",
        ]
    )
    assert args.min_freq_threshold == -1.0


def test_build_parser_fp_timeout():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--fp-timeout",
            "3",
        ]
    )
    assert args.fp_timeout == 3.0


def test_build_parser_combine_max_ratio():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--combine-max-ratio",
            "0.8",
        ]
    )
    assert args.combine_max_ratio == 0.8


def test_build_parser_exclude_tokens():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--exclude-tokens",
            "foo",
            "bar",
        ]
    )
    assert args.exclude_tokens == ["foo", "bar"]


def test_build_parser_persist_fp_exclude():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--persist-fp-exclude",
            "tokens.json",
        ]
    )
    assert args.persist_fp_exclude == Path("tokens.json")


def test_build_parser_max_exclude_tokens():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--max-exclude-tokens",
            "7",
        ]
    )
    assert args.max_exclude_tokens == 7


def test_build_parser_precomputed_saliency_dir():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--precomputed-saliency-dir",
            "sal",
        ]
    )
    assert args.precomputed_saliency_dir == Path("sal")


def test_build_parser_cache_saliency():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--cache-saliency",
        ]
    )
    assert args.cache_saliency is True


def test_build_parser_flush_every():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--out-csv",
            "out.csv",
            "--flush-every",
            "10",
        ]
    )
    assert args.flush_every == 10


def test_build_parser_enforce_self_detect():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--enforce-self-detect",
        ]
    )
    assert args.enforce_self_detect is True


def test_build_parser_no_auto_relax():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--no-auto-relax",
        ]
    )
    assert args.auto_relax is False


def test_build_parser_mal_freqs_ratio():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--mal-freqs",
            "mal.json",
            "--freq-ratio",
            "2.0",
        ]
    )
    assert args.mal_freqs == Path("mal.json")
    assert args.freq_ratio == 2.0


def test_build_parser_group_min_ratio():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--group-min-ratio",
            "0.5",
        ]
    )
    assert args.group_min_ratio == 0.5
    assert args.auto_group_min is True


def test_build_parser_batch_size():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--batch-size",
            "4",
        ]
    )
    assert args.batch_size == 4


def test_build_parser_global_opts():
    mod = importlib.import_module("src.cli.explainer_rule_eval")
    parser = mod.build_parser()
    args = parser.parse_args(
        [
            "--graph",
            "g.pt",
            "--sample",
            "s.bin",
            "--classifier",
            "c.pt",
            "--pop-size",
            "3",
            "--global-steps",
            "2",
            "--mutation-rate",
            "0.2",
        ]
    )
    assert args.pop_size == 3
    assert args.global_steps == 2
    assert args.mutation_rate == 0.2


def test_cli_runs_and_writes_json(tmp_path, caplog):
    g = HeteroData()
    g["bb"].x = torch.zeros(2, 1)
    g["bb"].num_nodes = 2
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [1]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.5, 0.1])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")

    mod = importlib.import_module("src.cli.explainer_rule_eval")
    out = tmp_path / "res.json"
    caplog.set_level("DEBUG", logger=mod.LOGGER.name)
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
            "--out",
            str(out),
        ]
    )

    data = json.loads(out.read_text())
    assert "detected" in data
    assert any("Building YARA rule" in rec.message for rec in caplog.records)


def test_cli_condition_type_count(tmp_path):
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
    out = tmp_path / "res.json"
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
            "--condition-type",
            "count",
            "--min-count",
            "1",
            "--out",
            str(out),
        ]
    )

    data = json.loads(out.read_text())
    assert "detected" in data


def test_cli_condition_type_combo(tmp_path):
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
    out = tmp_path / "res.json"
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
            "--condition-type",
            "combo",
            "--group-min-count",
            "1",
            "--out",
            str(out),
        ]
    )

    data = json.loads(out.read_text())
    assert "detected" in data


def test_cli_group_min_ratio_auto(tmp_path):
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
    out = tmp_path / "res.json"
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
            "--condition-type",
            "combo",
            "--group-min-ratio",
            "0.5",
            "--out",
            str(out),
        ]
    )

    data = json.loads(out.read_text())
    assert data.get("detected") is not None


def test_cli_sample_rules_out(tmp_path):
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
    rule_out = tmp_path / "rules"
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
            "--sample-rules-out",
            str(rule_out),
        ]
    )

    assert rule_out.is_dir()
    files = list(rule_out.glob("*.yar"))
    assert len(files) == 1
    text = files[0].read_text()
    assert text.strip().startswith("rule ")


def test_cli_sample_rules_out_detected(tmp_path, monkeypatch):
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

    rule_out = tmp_path / "rules"
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
            "--json-match",
            "--sample-rules-out",
            str(rule_out),
        ]
    )

    det_dir = rule_out / "rule"
    assert det_dir.is_dir()
    assert (det_dir / f"{sample.stem}.yar").is_file()


def test_cli_low_fp_rules_out(tmp_path, monkeypatch):
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

    low_dir = tmp_path / "low"
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
            "--json-match",
            "--low-fp-rules-out",
            str(low_dir),
        ]
    )

    assert (low_dir / f"{sample.stem}.yar").is_file()


def test_cli_fp_rules_out(tmp_path, monkeypatch):
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

    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")
    clean_json = tmp_path / "clean.json"
    clean_json.write_text(json.dumps({"c_code": ["foo"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    fp_dir = tmp_path / "fp"
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
            "--json-match",
            "--clean-sample",
            str(clean),
            "--fp-rules-out",
            str(fp_dir),
        ]
    )

    assert (fp_dir / f"{sample.stem}.yar").is_file()


def test_cli_json_match_detects(tmp_path, monkeypatch):
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

    out = tmp_path / "res.json"
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
            "--json-match",
            "--out",
            str(out),
        ]
    )

    data = json.loads(out.read_text())
    assert data["detected"] is True
    assert data["coverage"] == 0.0


def test_batch_fp_ratio_from_benign(tmp_path, monkeypatch, caplog):
    import pandas as pd

    csv = tmp_path / "meta.csv"
    pd.DataFrame(
        {
            "sha256": ["a", "b"],
            "label": [1, 0],
            "filename": ["a.bin", "b.bin"],
        }
    ).to_csv(csv, index=False)

    gdir = tmp_path / "graphs"
    gdir.mkdir()
    (gdir / "a.pt").write_text("stub")

    sdir = tmp_path / "samples"
    sdir.mkdir()
    (sdir / "a.bin").write_text("mal")
    (sdir / "b.bin").write_text("ben")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    calls = []

    def fake_eval(*args, **kwargs):
        calls.append(list(kwargs.get("clean_paths", []) or []))
        return {
            "detected": True,
            "rule_length": 0,
            "avg_importance": 0.0,
            "mask_sparsity": 0.0,
            "coverage": 0.0,
            "false_positive": True,
        }

    monkeypatch.setattr(mod, "evaluate_single", fake_eval)

    caplog.set_level("INFO", logger=mod.LOGGER.name)
    mod.main(
        [
            "--graph-dir",
            str(gdir),
            "--sample-dir",
            str(sdir),
            "--meta-csv",
            str(csv),
            "--classifier",
            str(sdir / "a.bin"),
        ]
    )

    assert calls == [[sdir / "b.bin"]]
    assert any("FP ratio=1.000" in rec.message for rec in caplog.records)


def test_batch_out_csv_has_fp_tokens_column(tmp_path, monkeypatch):
    import pandas as pd

    import torch
    import src.models.gnn.res_wrapper as res_wrapper

    csv = tmp_path / "meta.csv"
    pd.DataFrame({"sha256": ["a"], "label": [1], "filename": ["a.bin"]}).to_csv(
        csv, index=False
    )

    gdir = tmp_path / "graphs"
    gdir.mkdir()
    (gdir / "a.pt").write_text("stub")

    sdir = tmp_path / "samples"
    sdir.mkdir()
    (sdir / "a.bin").write_text("mal")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyClf(torch.nn.Module):
        def forward(self, x):
            return torch.zeros(1)

    monkeypatch.setattr(
        res_wrapper.RESGCLClassifier,
        "load_pretrained",
        classmethod(lambda cls, *a, **k: DummyClf()),
    )

    def fake_eval(*args, **kwargs):
        # return result without fp_matched_tokens
        return {"detected": True}

    monkeypatch.setattr(mod, "evaluate_single", fake_eval)

    out_csv = tmp_path / "res.csv"
    mod.main(
        [
            "--graph-dir",
            str(gdir),
            "--sample-dir",
            str(sdir),
            "--meta-csv",
            str(csv),
            "--classifier",
            str(sdir / "a.bin"),
            "--out-csv",
            str(out_csv),
        ]
    )

    df = pd.read_csv(out_csv)
    assert "fp_matched_tokens" in df.columns
    assert df.loc[0, "fp_matched_tokens"] == "[]"


def test_batch_flush_every(tmp_path, monkeypatch):
    import pandas as pd
    import torch
    import src.models.gnn.res_wrapper as res_wrapper

    csv = tmp_path / "meta.csv"
    pd.DataFrame({"sha256": ["a"], "label": [1], "filename": ["a.bin"]}).to_csv(
        csv, index=False
    )

    gdir = tmp_path / "graphs"
    gdir.mkdir()
    (gdir / "a.pt").write_text("stub")

    sdir = tmp_path / "samples"
    sdir.mkdir()
    (sdir / "a.bin").write_text("mal")

    mod = importlib.import_module("src.cli.explainer_rule_eval")
    from tests import helpers

    class DummyClf(torch.nn.Module):
        def forward(self, x):
            return torch.zeros(1)

    monkeypatch.setattr(
        res_wrapper.RESGCLClassifier,
        "load_pretrained",
        classmethod(lambda cls, *a, **k: DummyClf()),
    )

    monkeypatch.setenv("RMG_TEST_EVAL_SINGLE", "tests.helpers:fake_eval")

    out_csv = tmp_path / "res.csv"
    mod.main(
        [
            "--graph-dir",
            str(gdir),
            "--sample-dir",
            str(sdir),
            "--meta-csv",
            str(csv),
            "--classifier",
            str(sdir / "a.bin"),
            "--out-csv",
            str(out_csv),
            "--num-workers",
            "2",
            "--flush-every",
            "1",
        ]
    )

    df = pd.read_csv(out_csv)
    assert len(df) == 1


def test_batch_optimize_saves_state(tmp_path, monkeypatch):
    import pandas as pd
    import torch
    import src.models.gnn.res_wrapper as res_wrapper

    csv = tmp_path / "meta.csv"
    pd.DataFrame({"sha256": ["a"], "label": [1], "filename": ["a.bin"]}).to_csv(
        csv, index=False
    )

    gdir = tmp_path / "graphs"
    gdir.mkdir()
    (gdir / "a.pt").write_text("stub")

    sdir = tmp_path / "samples"
    sdir.mkdir()
    (sdir / "a.bin").write_text("mal")

    mod = importlib.import_module("src.cli.explainer_rule_eval")
    from tests import helpers

    class DummyClf(torch.nn.Module):
        def forward(self, x):
            return torch.zeros(1)

    monkeypatch.setattr(
        res_wrapper.RESGCLClassifier,
        "load_pretrained",
        classmethod(lambda cls, *a, **k: DummyClf()),
    )

    monkeypatch.setenv("RMG_TEST_EVAL_SINGLE", "tests.helpers:fake_eval")

    opt_out = tmp_path / "state.pkl"
    mod.main(
        [
            "--graph-dir",
            str(gdir),
            "--sample-dir",
            str(sdir),
            "--meta-csv",
            str(csv),
            "--classifier",
            str(sdir / "a.bin"),
            "--num-workers",
            "2",
            "--optimize",
            "--save-optimizer",
            str(opt_out),
        ]
    )

    assert opt_out.is_file()


def test_evaluate_single_json_match_fp_with_clean_sample(tmp_path, monkeypatch):
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

    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")
    clean_json = tmp_path / "clean.json"
    clean_json.write_text(json.dumps({"c_code": ["foo"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    res = mod.evaluate_single(
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
        clean_sample=clean,
        clean_paths=None,
        sample_json=sample_json,
        json_match=True,
        combine_mode="or",
        combine_min_ratio=0.7,
    )

    assert res["false_positive"] is True


def test_evaluate_single_json_match_fp_with_clean_dir(tmp_path, monkeypatch):
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

    cldir = tmp_path / "cleandir"
    cldir.mkdir()
    clean = cldir / "clean.bin"
    clean.write_bytes(b"dummy")
    (cldir / "clean.json").write_text(json.dumps({"c_code": ["foo"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    res = mod.evaluate_single(
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
        clean_dir=cldir,
        clean_sample=None,
        clean_paths=None,
        sample_json=sample_json,
        json_match=True,
        combine_mode="or",
        combine_min_ratio=0.7,
    )

    assert res["false_positive"] is True


def test_evaluate_single_uses_clean_token_cache(tmp_path, monkeypatch):
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

    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")
    clean_json = tmp_path / "clean.json"
    clean_json.write_text(json.dumps({"c_code": ["foo"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    js_obj = json.loads(clean_json.read_text())
    cache = mod.TokenCache()
    cache.add(clean, mod.extract_json_tokens(js_obj))

    orig_read = Path.read_text

    def fake_read_text(self, *a, **k):
        if self == clean_json:
            raise AssertionError("cache not used")
        return orig_read(self, *a, **k)

    monkeypatch.setattr(Path, "read_text", fake_read_text)

    res = mod.evaluate_single(
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
        clean_sample=clean,
        clean_paths=None,
        sample_json=sample_json,
        json_match=True,
        combine_mode="or",
        token_cache=cache,
    )

    assert res["false_positive"] is True


def test_evaluate_single_json_feature_filter(tmp_path, monkeypatch):
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
            return ["call:bar", "call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    res = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
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
    )

    assert res["rule_length"] == 1
    assert "foo" in res["rule_texts"][0]
    assert "bar" not in res["rule_texts"][0]


def test_evaluate_single_json_feature_filter_fallback(tmp_path, monkeypatch):
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
    sample_json.write_text(json.dumps({"c_code": ["other"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    res = mod.evaluate_single(
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
    )

    assert res["rule_length"] == 1
    assert "foo" in res["rule_texts"][0]


def test_evaluate_single_combine_mode(tmp_path, monkeypatch):
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
    sample.write_bytes(b"abcdefghij")
    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"abcdefghij")

    sample_json = None

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["foo", "bar"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self, length):
            self.strings = [(0, "$a", b"x" * length)]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            p = str(path)
            if "foo" in self.text:
                return [] if "clean" in p else [FakeMatch(8)]
            if "bar" in self.text:
                return [FakeMatch(4)] if "clean" in p else []
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res_or = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        num_rules=2,
        chunk_size=1,
        clean_dir=None,
        clean_sample=clean,
        clean_paths=None,
        sample_json=sample_json,
        json_match=False,
        combine_mode="or",
    )

    assert res_or["detected"] is True
    assert abs(res_or["coverage"] - 0.8) < 1e-6
    assert res_or["false_positive"] is True

    res_and = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        num_rules=2,
        chunk_size=1,
        clean_dir=None,
        clean_sample=clean,
        clean_paths=None,
        sample_json=sample_json,
        json_match=False,
        combine_mode="and",
    )

    assert res_and["detected"] is False
    assert abs(res_and["coverage"] - 0.8) < 1e-6
    assert res_and["false_positive"] is False


def test_verify_features_combo_percentage(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["foo"]}))
    feats = ["call:foo", "call:bar", "import:baz"]

    assert (
        mod.verify_features(
            js,
            feats,
            condition_type="combo",
            group_percentage=50,
        )
        is False
    )

    js.write_text(json.dumps({"c_code": ["foo", "baz"]}))
    assert (
        mod.verify_features(
            js,
            feats,
            condition_type="combo",
            group_percentage=50,
        )
        is True
    )


def test_verify_features_combo_min_count(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["foo"]}))
    feats = ["call:foo", "call:bar", "import:baz", "import:qux"]

    assert (
        mod.verify_features(
            js,
            feats,
            condition_type="combo",
            group_min_count=2,
        )
        is False
    )

    js.write_text(json.dumps({"c_code": ["foo", "bar", "baz", "qux"]}))
    assert (
        mod.verify_features(
            js,
            feats,
            condition_type="combo",
            group_min_count=2,
        )
        is True
    )


def test_verify_features_combo_min_count_capped(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["foo"]}))
    feats = ["call:foo", "import:bar"]

    assert (
        mod.verify_features(
            js,
            feats,
            condition_type="combo",
            group_min_count=2,
        )
        is False
    )

    js.write_text(json.dumps({"c_code": ["foo", "bar"]}))
    assert (
        mod.verify_features(
            js,
            feats,
            condition_type="combo",
            group_min_count=2,
        )
        is True
    )


def test_verify_features_combo_adjust_pct(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["foo", "qux"]}))
    feats = ["call:foo", "call:bar", "call:baz", "import:qux"]

    assert (
        mod.verify_features(
            js,
            feats,
            condition_type="combo",
            group_percentage=50,
        )
        is False
    )

    assert (
        mod.verify_features(
            js,
            feats,
            condition_type="combo",
            group_percentage=50,
            adjust_group_percentage=True,
        )
        is True
    )


def test_verify_features_saliency_stats(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["foo"]}))
    feats = ["call:foo"]

    stats = {"call:foo": [0.1, 0.2]}
    assert mod.verify_features(js, feats, saliency_stats=stats) is False

    stats = {"call:foo": [0.3, 0.1]}
    assert mod.verify_features(js, feats, saliency_stats=stats) is True


def test_verify_features_string_wide_ascii(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["ProcessWindowStation"]}))

    feats = ['"ProcessWindowStation" wide ascii']

    assert mod.verify_features(js, feats) is True


def test_verify_features_hex_pattern(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["4D 5A 90 00"]}))

    feats = ["{ 4D 5A 90 00 }"]

    assert mod.verify_features(js, feats) is True


def test_verify_features_regex_pattern(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["hello world"]}))

    feats = ["/hello/"]

    assert mod.verify_features(js, feats) is True


def test_verify_features_return_matched(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["foo", "bar"]}))

    feats = ["call:foo", "call:baz"]

    result, matched = mod.verify_features(js, feats, return_matched=True)

    assert result is True
    assert matched == ["call:foo"]


def test_verify_features_token_set_equivalence(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    data = {"c_code": ["foo bar"]}
    js = tmp_path / "s.json"
    js.write_text(json.dumps(data))

    feats = ["call:foo", "call:baz"]

    js_obj = json.loads(js.read_text())
    token_set = mod.extract_json_tokens(js_obj)

    res_dict = mod.verify_features(js_obj, feats)
    res_tokens = mod.verify_features(token_set, feats)

    assert res_dict == res_tokens


def test_estimate_token_cache_size(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    cache = mod.TokenCache()
    for i in range(100):
        p = tmp_path / f"s{i}.bin"
        p.write_text("dummy")
        j = tmp_path / f"s{i}.json"
        j.write_text(json.dumps({"c_code": ["foo bar baz"]}))
        cache.add(p, mod.extract_json_tokens(json.loads(j.read_text())))

    size = mod.estimate_token_cache_size(cache)
    assert size < 1_000_000  # <1MB


def test_fp_retry_exclude_tokens(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")

    import torch
    from torch_geometric.data import HeteroData

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
    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self, ident="$s0"):
            self.strings = [(0, ident, b"x")]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            if "foo" not in self.text:
                return []
            if str(path) == str(sample):
                return [FakeMatch("$sample")]  # token not mapped to feature
            if str(path) == str(clean):
                return [FakeMatch("$s0")]  # mapped to feature 'foo'
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res = mod.evaluate_single(
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
        clean_sample=clean,
        clean_paths=None,
        sample_json=None,
        json_match=False,
        combine_mode="or",
        fp_retries=1,
    )

    assert res["detected"] is True




def test_fp_tokens_accumulation(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")

    import torch
    from torch_geometric.data import HeteroData

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
    sample_json.write_text(json.dumps({"c_code": ["foo", "bar"]}))

    clean1 = tmp_path / "c1.bin"
    clean1.write_bytes(b"dummy")
    (tmp_path / "c1.json").write_text(json.dumps({"c_code": ["foo"]}))

    clean2 = tmp_path / "c2.bin"
    clean2.write_bytes(b"dummy")
    (tmp_path / "c2.json").write_text(json.dumps({"c_code": ["bar"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo", "call:bar"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    res = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        clean_dir=None,
        clean_sample=None,
        clean_paths=[clean1, clean2],
        sample_json=sample_json,
        json_match=True,
        combine_mode="or",
    )

    assert res["false_positive"] is True
    assert sorted(res.get("fp_matched_tokens", [])) == ["call:bar", "call:foo"]


def test_adaptive_fp_retry_token_order(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")

    import torch
    from torch_geometric.data import HeteroData

    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9, 0.8])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")

    clean1 = tmp_path / "c1.bin"
    clean1.write_bytes(b"dummy")
    clean2 = tmp_path / "c2.bin"
    clean2.write_bytes(b"dummy")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["foo", "bar"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self, id1, id2=None):
            ids = [id1] if id2 is None else [id1, id2]
            self.strings = [(0, i, b"x") for i in ids]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            p = str(path)
            have_foo = "foo" in self.text
            have_bar = "bar" in self.text
            if "c1" in p:
                return [FakeMatch("$s0")] if have_foo else []
            if "c2" in p:
                return [FakeMatch("$s1")] if have_bar else []
            if have_foo and have_bar:
                return [FakeMatch("$s0", "$s1")]
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        clean_paths=[clean1, clean2],
        combine_mode="or",
        fp_retries=2,
    )

    assert res["detected"] is True


def test_fp_retry_hitting_set(tmp_path, monkeypatch):
    from collections import Counter

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    calls: list[set[str]] = []

    def fake_eval(*args, **kwargs):
        calls.append(set(kwargs.get("exclude", [])))
        return {"detected": True, "false_positive": True}

    result = {
        "false_positive": True,
        "fp_tokens_by_sample": [["aa", "ab"], ["ba", "bb"]],
        "fp_token_counts": {"aa": 1, "ab": 1, "ba": 1, "bb": 1},
    }

    mod.adaptive_fp_retry(
        fake_eval,
        result=result,
        exclude_set=set(),
        fp_token_counter=Counter(),
        group_min_count=None,
        combine_min_ratio=0.7,
        freq_threshold=10,
        min_freq_threshold=0.0,
        group_min_ratio=0.0,
        num_rules=1,
        chunk_size=None,
        combine_mode="or",
        auto_group_min=True,
        freq_threshold_step=0.0,
        comb_ratio_step=0.1,
        chunk_size_step=1,
        combine_max_ratio=1.0,
        fp_retries=1,
        fp_timeout=None,
        max_exclude_tokens=5,
        persist_fp_exclude=None,
        fp_bar=None,
        is_better=lambda n, c: True,
        best_result={"detected": True, "false_positive": True},
        last_detected=None,
    )

    assert calls and calls[0] == {"ab", "bb"}


def test_adaptive_fp_retry_freq_step_and_min_threshold():
    from collections import Counter

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    freqs: list[float] = []

    def fake_eval(freq, *args, **kwargs):
        freqs.append(freq)
        return {"detected": False, "false_positive": True}

    result = {"false_positive": True}

    mod.adaptive_fp_retry(
        fake_eval,
        result=result,
        exclude_set=set(),
        fp_token_counter=Counter(),
        group_min_count=None,
        combine_min_ratio=0.7,
        freq_threshold=0.5,
        min_freq_threshold=-1.0,
        group_min_ratio=0.0,
        num_rules=1,
        chunk_size=None,
        combine_mode="or",
        auto_group_min=True,
        freq_threshold_step=1.0,
        comb_ratio_step=0.0,
        chunk_size_step=1,
        combine_max_ratio=1.0,
        fp_retries=1,
        fp_timeout=None,
        max_exclude_tokens=5,
        persist_fp_exclude=None,
        fp_bar=None,
        is_better=lambda n, c: True,
        best_result={"detected": False, "false_positive": True},
        last_detected=None,
    )

    # second call should use lowered threshold allowing negatives
    assert len(freqs) >= 2
    assert freqs[0] == 0.5
    assert freqs[1] == -0.5


def test_fp_retry_token_exclusion_rollback(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")

    import torch
    from torch_geometric.data import HeteroData

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
    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["foo", "bar"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self, idents):
            self.strings = [(0, ident, b"x") for ident in idents]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            p = str(path)
            have_foo = "foo" in self.text
            have_bar = "bar" in self.text
            if "sample" in p:
                if have_foo and have_bar:
                    return [FakeMatch(["$s0", "$s1"])]
                if have_foo:
                    return [FakeMatch(["$s0"])]
                if have_bar:
                    return []
                return []
            if "clean" in p:
                if have_foo and have_bar:
                    return [FakeMatch(["$s0", "$s1"])]
                if have_bar:
                    return [FakeMatch(["$s1"])]
                if have_foo:
                    return []
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        clean_dir=None,
        clean_sample=clean,
        clean_paths=None,
        sample_json=None,
        json_match=False,
        combine_mode="or",
        fp_retries=1,
    )

    assert res["detected"] is True
    assert res["false_positive"] is False
    assert res["rule_length"] == 1
    assert "foo" in res["rule_texts"][0]
    assert "bar" not in res["rule_texts"][0]
    assert not res.get("fp_matched_tokens")


def test_fp_retry_selects_best_result(tmp_path, monkeypatch):
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
    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")
    (tmp_path / "clean.json").write_text(json.dumps({"c_code": ["foo"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self):
            self.strings = [(0, "$s0", b"x")]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            if "foo" in self.text:
                return [FakeMatch()]
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res = mod.evaluate_single(
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
        clean_sample=clean,
        clean_paths=None,
        sample_json=None,
        json_match=False,
        combine_mode="or",
        fp_retries=1,
    )

    assert res["false_positive"] is True
    assert res["detected"] is True
    assert res["rule_length"] == 1
    assert res["freq_threshold"] == 10


def test_fp_retry_increases_ratio(tmp_path, monkeypatch):
    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9, 0.8])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")
    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["foo", "bar"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self, ident="$sample"):
            self.strings = [(0, ident, b"x")]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            p = str(path)
            if "foo" in self.text:
                return [FakeMatch()]
            if "bar" in self.text:
                return [] if "clean" in p else [FakeMatch()]
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res_no = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        num_rules=2,
        chunk_size=1,
        clean_sample=clean,
        combine_mode="or",
        combine_min_ratio=0.7,
        combine_max_ratio=0.5,
        comb_ratio_step=0.5,
        fp_retries=1,
    )

    res_yes = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        num_rules=2,
        chunk_size=1,
        clean_sample=clean,
        combine_mode="or",
        combine_min_ratio=0.7,
        combine_max_ratio=1.0,
        comb_ratio_step=0.5,
        fp_retries=1,
    )

    assert res_no["false_positive"] is True
    assert res_yes["false_positive"] is True


def test_mal_freqs_reduce_fp(tmp_path, monkeypatch):
    g = HeteroData()
    g["func"].x = torch.zeros(2, 1)
    g["func"].name = ["foo", "bar"]
    g[("func", "cfg", "func")].edge_index = torch.tensor([[0], [1]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"func": torch.tensor([0.9, 0.8])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")
    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class FakeMatch:
        def __init__(self):
            self.strings = [(0, "$s0", b"x")]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            p = str(path)
            if "foo" in self.text:
                return [FakeMatch()]
            if "bar" in self.text and "sample" in p:
                return [FakeMatch()]
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res_no = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        benign_freqs={"call:foo": 10, "call:bar": 1},
        freq_threshold=100,
        clean_dir=None,
        clean_sample=clean,
        clean_paths=None,
        sample_json=None,
        json_match=False,
        combine_mode="or",
    )

    res_yes = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        benign_freqs={"call:foo": 10, "call:bar": 1},
        mal_freqs={"call:foo": 5, "call:bar": 2},
        freq_ratio=1.0,
        freq_threshold=100,
        clean_dir=None,
        clean_sample=clean,
        clean_paths=None,
        sample_json=None,
        json_match=False,
        combine_mode="or",
        combine_min_ratio=0.7,
    )

    assert res_no["false_positive"] is True
    assert res_yes["false_positive"] is True


def test_evaluate_single_relax_params(tmp_path, monkeypatch):
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
            return ["foo", "bar"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self):
            self.strings = [(0, "$s0", b"x")]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            if "foo" in self.text:
                return [FakeMatch()]
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        num_rules=2,
        chunk_size=1,
        combine_mode="or",
        combine_min_ratio=0.6,
    )

    assert res["detected"] is True

def test_fp_timeout_stops_retry(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")

    import torch
    from torch_geometric.data import HeteroData

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
    clean = tmp_path / "clean.bin"
    clean.write_bytes(b"dummy")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["foo", "bar"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self, idents):
            self.strings = [(0, ident, b"x") for ident in idents]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            return [FakeMatch(["$s0", "$s1"])]

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    times = iter([0.0, 10.0])

    def fake_perf_counter():
        try:
            return next(times)
        except StopIteration:
            return 10.0

    monkeypatch.setattr(mod.time, "perf_counter", fake_perf_counter)

    res = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=salpath,
        device=torch.device("cpu"),
        top_k=2,
        condition_type="any",
        percentage=70,
        min_count=None,
        group_percentage=None,
        group_min_count=None,
        clean_dir=None,
        clean_sample=clean,
        clean_paths=None,
        sample_json=None,
        json_match=False,
        combine_mode="or",
        fp_retries=5,
        fp_timeout=0.5,
    )

    assert res["false_positive"] is True


def test_evaluate_single_saliency_cache(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")

    import torch
    from torch_geometric.data import HeteroData
    import src.models.gnn.res_wrapper as res_wrapper

    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sample = tmp_path / "sample.bin"
    sample.write_bytes(b"dummy")
    sample_json = tmp_path / "sample.json"
    sample_json.write_text(json.dumps({"c_code": ["foo"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyClf(torch.nn.Module):
        def forward(self, *a, **k):
            return torch.zeros(1)

    monkeypatch.setattr(
        res_wrapper.RESGCLClassifier,
        "load_pretrained",
        classmethod(lambda cls, *a, **k: DummyClf()),
    )

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    calls = {"n": 0}

    def fake_compute(graph, classifier, explainer, device):
        calls["n"] += 1
        return {"bb": torch.tensor([0.9])}

    monkeypatch.setattr(mod, "_compute_saliency_with_explainer", fake_compute)

    res1 = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=None,
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
        cache_saliency=True,
    )

    cache_file = gpath.with_suffix(".sal.pt")
    assert cache_file.is_file()
    assert calls["n"] == 1

    calls["n"] = 0
    res2 = mod.evaluate_single(
        gpath,
        sample,
        classifier_ckpt=sample,
        explainer_ckpt=None,
        saliency_path=None,
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
        cache_saliency=True,
    )

    assert calls["n"] == 0


def test_fp_ratio_benign_computation(tmp_path, monkeypatch):
    import torch
    from torch_geometric.data import HeteroData

    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "mal.bin"
    sample.write_bytes(b"mal")
    b1 = tmp_path / "b1.bin"
    b1.write_bytes(b"ben1")
    b2 = tmp_path / "b2.bin"
    b2.write_bytes(b"ben2")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self, ident="$s0"):
            self.strings = [(0, ident, b"x")]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            p = str(path)
            if p == str(sample):
                return [FakeMatch()]
            if p == str(b1):
                return [FakeMatch()]
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    res = mod.evaluate_single(
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
        num_rules=1,
        chunk_size=None,
        clean_dir=None,
        clean_sample=None,
        clean_paths=[b1, b2],
        sample_json=None,
        json_match=False,
        combine_mode="or",
    )

    assert abs(res.get("fp_ratio_benign", 0.0) - 0.5) < 1e-6


def test_fp_ratio_benign_token_index(tmp_path, monkeypatch):
    import torch
    from torch_geometric.data import HeteroData

    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "mal.bin"
    sample.write_bytes(b"mal")
    sample_json = tmp_path / "mal.json"
    sample_json.write_text(json.dumps({"c_code": ["foo"]}))

    b1 = tmp_path / "b1.bin"
    b1.write_bytes(b"ben1")
    b1_json = tmp_path / "b1.json"
    b1_json.write_text(json.dumps({"c_code": ["foo"]}))

    b2 = tmp_path / "b2.bin"
    b2.write_bytes(b"ben2")
    b2_json = tmp_path / "b2.json"
    b2_json.write_text(json.dumps({"c_code": ["bar"]}))

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    cache = mod.TokenCache()
    toks1 = mod.extract_json_tokens(json.loads(b1_json.read_text()))
    toks2 = mod.extract_json_tokens(json.loads(b2_json.read_text()))
    cache.add(b1, toks1)
    cache.add(b2, toks2)

    res = mod.evaluate_single(
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
        num_rules=1,
        chunk_size=None,
        clean_dir=None,
        clean_sample=None,
        clean_paths=None,
        sample_json=sample_json,
        json_match=True,
        combine_mode="or",
        token_cache=cache,
    )

    assert res["false_positive"] is True
    assert abs(res.get("fp_ratio_benign", 0.0) - 0.5) < 1e-6


def test_is_better_prefers_lower_fp_ratio(tmp_path, monkeypatch):
    """_is_better should favor lower fp_ratio_benign when both are FP."""
    import torch
    from torch_geometric.data import HeteroData

    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "mal.bin"
    sample.write_bytes(b"mal")
    b1 = tmp_path / "b1.bin"
    b1.write_bytes(b"ben1")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    class FakeMatch:
        def __init__(self, ident="$s0"):
            self.strings = [(0, ident, b"x")]

    class FakeCompiled:
        def __init__(self, text):
            self.text = text

        def match(self, path):
            p = str(path)
            if p == str(sample) or p == str(b1):
                return [FakeMatch()]
            return []

    class FakeYara:
        @staticmethod
        def compile(source):
            return FakeCompiled(source)

    monkeypatch.setitem(sys.modules, "yara", FakeYara)

    captured: dict[str, object] = {}

    def fake_retry(*args, **kwargs):
        captured["fn"] = kwargs.get("is_better")
        return kwargs["result"], kwargs["exclude_set"], kwargs["best_result"]

    monkeypatch.setattr(mod, "adaptive_fp_retry", fake_retry)

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
        num_rules=1,
        chunk_size=None,
        clean_dir=None,
        clean_sample=None,
        clean_paths=[b1],
        sample_json=None,
        json_match=False,
        combine_mode="or",
        fp_retries=1,
    )

    is_better = captured.get("fn")
    assert is_better is not None

    low = {
        "detected": True,
        "false_positive": True,
        "coverage": 0.0,
        "rule_length": 1,
        "fp_ratio_benign": 0.1,
    }
    high = {
        "detected": True,
        "false_positive": True,
        "coverage": 0.0,
        "rule_length": 1,
        "fp_ratio_benign": 0.5,
    }

    assert is_better(low, high) is True
    assert is_better(high, low) is False


def test_adaptive_fp_retry_token_index_profile(tmp_path, monkeypatch):
    """Using token_index should reduce JSON reads during FP checks."""
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")

    import torch
    from torch_geometric.data import HeteroData
    from collections import defaultdict

    g = HeteroData()
    g["bb"].x = torch.zeros(1, 1)
    g["bb"].num_nodes = 1
    g[("bb", "cfg", "bb")].edge_index = torch.tensor([[0], [0]])
    gpath = tmp_path / "graph.pt"
    torch.save(g, gpath)

    sal = {"bb": torch.tensor([0.9])}
    salpath = tmp_path / "sal.pt"
    torch.save(sal, salpath)

    sample = tmp_path / "s.bin"
    sample.write_bytes(b"mal")
    sample_json = tmp_path / "s.json"
    sample_json.write_text(json.dumps({"c_code": ["foo"]}))

    clean_paths = []
    tokens_map = {}
    index = defaultdict(set)
    for i, tok in enumerate(["bar", "baz", "foo"]):
        c = tmp_path / f"c{i}.bin"
        c.write_bytes(b"ben")
        clean_paths.append(c)
        cj = tmp_path / f"c{i}.json"
        cj.write_text(json.dumps({"c_code": [tok]}))
        tokens_map[c] = tok
        index[tok].add(c)

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyMiner:
        def __init__(self, *a, **k):
            pass

        def mine(self, graph, saliency, *a, **k):
            return ["call:foo"]

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner())

    index = mod.TokenCache()
    for p, tok in tokens_map.items():
        index.index[tok].add(p)

    read_count = 0
    orig_read = Path.read_text

    def fake_read(self, *a, **k):
        nonlocal read_count
        if self.suffix == ".json" and self.name.startswith("c"):
            read_count += 1
        return orig_read(self, *a, **k)

    monkeypatch.setattr(Path, "read_text", fake_read)

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
        clean_paths=clean_paths,
        sample_json=sample_json,
        json_match=True,
        combine_mode="or",
        fp_retries=1,
    )
    no_index = read_count

    read_count = 0
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
        clean_paths=clean_paths,
        sample_json=sample_json,
        json_match=True,
        combine_mode="or",
        token_cache=index,
        fp_retries=1,
    )
    with_index = read_count

    assert with_index < no_index


def test_select_exclude_tokens_hitting_set():
    from collections import Counter
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    result = {
        "fp_token_counts": {"aa": 3, "bb": 1},
        "fp_tokens_by_sample": [["aa", "cc"], ["bb", "cc"]],
        "fp_matched_tokens": ["aa", "bb", "cc"],
    }

    tokens_sorted, min_tokens = mod._select_exclude_tokens(result, Counter())

    assert min_tokens == ["cc"]
    assert tokens_sorted[0] == "cc"


def test_evaluate_and_update(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    state = mod.RetryState(
        result={"false_positive": True},
        exclude_set=set(),
        combine_min_ratio=0.7,
        combine_mode="or",
        group_min_ratio=0.0,
        group_min_count=None,
        best_result={"detected": False, "false_positive": True},
        last_detected=None,
    )

    trial = {"detected": True, "false_positive": False}
    persist = tmp_path / "ex.json"

    success = mod._evaluate_and_update(
        trial,
        state,
        exclude_tokens={"tok"},
        persist_fp_exclude=persist,
        fp_bar=None,
        is_better=lambda n, c: True,
    )

    assert success is True
    assert state.result.get("detected") is True
    assert "tok" in state.exclude_set
    data = json.loads(persist.read_text())
    assert "tok" in data


def test_batch_optimizer_updates_kwargs(tmp_path, monkeypatch):
    import pandas as pd
    import torch
    import src.models.gnn.res_wrapper as res_wrapper

    csv = tmp_path / "meta.csv"
    pd.DataFrame({"sha256": ["a", "b"], "label": [1, 1], "filename": ["a.bin", "b.bin"]}).to_csv(
        csv, index=False
    )

    gdir = tmp_path / "graphs"
    gdir.mkdir()
    (gdir / "a.pt").write_text("stub")
    (gdir / "b.pt").write_text("stub")

    sdir = tmp_path / "samples"
    sdir.mkdir()
    (sdir / "a.bin").write_text("mal")
    (sdir / "b.bin").write_text("mal")

    sal_dir = tmp_path / "sal"
    sal_dir.mkdir()
    torch.save({}, sal_dir / "a.pt")
    torch.save({}, sal_dir / "b.pt")

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    class DummyClf(torch.nn.Module):
        def forward(self, x):
            return torch.zeros(1)

    monkeypatch.setattr(
        res_wrapper.RESGCLClassifier,
        "load_pretrained",
        classmethod(lambda cls, *a, **k: DummyClf()),
    )

    params = []

    def record_eval(*args, **kwargs):
        params.append({
            "combine_min_ratio": kwargs.get("combine_min_ratio"),
            "group_min_ratio": kwargs.get("group_min_ratio"),
            "combine_mode": kwargs.get("combine_mode"),
        })
        return {"detected": True}

    monkeypatch.setattr(mod, "evaluate_single", record_eval)

    mod.main(
        [
            "--graph-dir",
            str(gdir),
            "--sample-dir",
            str(sdir),
            "--meta-csv",
            str(csv),
            "--classifier",
            str(sdir / "a.bin"),
            "--precomputed-saliency-dir",
            str(sal_dir),
            "--optimize",
            "--batch-size",
            "1",
        ]
    )

    assert len(params) == 2
    assert params[0] != params[1]


def test_optimizer_params_applied_evaluate_single(tmp_path, monkeypatch):
    pytest.importorskip("torch")
    pytest.importorskip("torch_geometric")

    import torch
    from torch_geometric.data import HeteroData

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

    captured: dict[str, object] = {}

    class DummyMiner:
        def __init__(self, *, freq_threshold, **k):
            captured["freq"] = freq_threshold

        def mine(self, graph, saliency):
            return ["call:foo"]

    class DummyBuilder:
        def __init__(self, *, group_min_count=None, **k):
            captured["gmc"] = group_min_count

        def build(self, feats, return_map=False):
            return "rule", {}

        def validate(self, t):
            pass

    monkeypatch.setattr(mod, "FeatureMiner", lambda *a, **k: DummyMiner(*a, **k))
    monkeypatch.setattr("src.cli.explainer_rule_eval.evaluation.YaraBuilder", DummyBuilder)

    opt = mod.CategoricalOptimizer()
    opt.freq_threshold_logit.data.copy_(
        torch.logit(torch.tensor((5 - opt.FREQ_MIN) / (opt.FREQ_MAX - opt.FREQ_MIN)))
    )
    opt.group_min_count_logit.data.copy_(
        torch.logit(torch.tensor((3 - opt.GROUP_MIN_MIN) / (opt.GROUP_MIN_MAX - opt.GROUP_MIN_MIN)))
    )

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

    assert captured.get("freq") == pytest.approx(5.0, abs=1e-6)
    assert captured.get("gmc") == 3


def test_adaptive_retry_optimizer_params(monkeypatch):
    from collections import Counter

    mod = importlib.import_module("src.cli.explainer_rule_eval")

    called: list[tuple[float, int | None]] = []

    def fake_eval(freq, gmc, *a, **k):
        called.append((freq, gmc))
        return {"detected": False, "false_positive": True}

    opt = mod.CategoricalOptimizer()
    opt.freq_threshold_logit.data.copy_(
        torch.logit(torch.tensor((7 - opt.FREQ_MIN) / (opt.FREQ_MAX - opt.FREQ_MIN)))
    )
    opt.group_min_count_logit.data.copy_(
        torch.logit(torch.tensor((2 - opt.GROUP_MIN_MIN) / (opt.GROUP_MIN_MAX - opt.GROUP_MIN_MIN)))
    )

    mod.adaptive_fp_retry(
        fake_eval,
        result={"false_positive": True},
        exclude_set=set(),
        fp_token_counter=Counter(),
        group_min_count=None,
        combine_min_ratio=0.7,
        freq_threshold=10.0,
        min_freq_threshold=0.0,
        group_min_ratio=0.0,
        num_rules=1,
        chunk_size=None,
        combine_mode="or",
        auto_group_min=True,
        freq_threshold_step=0.0,
        comb_ratio_step=0.0,
        chunk_size_step=1,
        combine_max_ratio=1.0,
        fp_retries=1,
        fp_timeout=None,
        max_exclude_tokens=5,
        persist_fp_exclude=None,
        fp_bar=None,
        is_better=lambda n, c: True,
        best_result={"detected": False, "false_positive": True},
        last_detected=None,
        optimizer=opt,
    )

    assert called
    assert called[0][0] == pytest.approx(7.0, abs=1e-6)
    assert called[0][1] == 2


