import importlib
import json
from pathlib import Path
import sys

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

    class DummyClf(torch.nn.Module):
        def forward(self, x):
            return torch.zeros(1)

    monkeypatch.setattr(
        res_wrapper.RESGCLClassifier,
        "load_pretrained",
        classmethod(lambda cls, *a, **k: DummyClf()),
    )

    def fake_eval(*args, **kwargs):
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
            "--flush-every",
            "1",
        ]
    )

    df = pd.read_csv(out_csv)
    assert len(df) == 1


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
    )

    assert res["false_positive"] is True


def test_evaluate_single_uses_clean_json_cache(tmp_path, monkeypatch):
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

    cache = {clean: json.loads(clean_json.read_text())}

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
        clean_json_cache=cache,
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


def test_verify_features_return_matched(tmp_path):
    mod = importlib.import_module("src.cli.explainer_rule_eval")

    js = tmp_path / "s.json"
    js.write_text(json.dumps({"c_code": ["foo", "bar"]}))

    feats = ["call:foo", "call:baz"]

    result, matched = mod.verify_features(js, feats, return_matched=True)

    assert result is True
    assert matched == ["call:foo"]


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
    assert res["false_positive"] is True
    assert res["rule_length"] == 1


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
        combine_min_ratio=0.5,
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
        combine_min_ratio=0.5,
        combine_max_ratio=1.0,
        comb_ratio_step=0.5,
        fp_retries=1,
    )

    assert res_no["false_positive"] is True
    assert res_yes["false_positive"] is False


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
    )

    assert res_no["false_positive"] is True
    assert res_yes["false_positive"] is False


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
