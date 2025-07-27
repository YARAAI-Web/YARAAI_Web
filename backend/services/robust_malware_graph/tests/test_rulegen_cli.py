import pytest
from pathlib import Path

pytest.importorskip("torch")

from src.cli.rulegen_cli import _read_json_lines, _read_labels


def test_read_json_lines_invalid(tmp_path):
    fp = tmp_path / "labels.jsonl"
    fp.write_text('{"sha256": "a", "label": 1}\n{invalid}\n')
    with pytest.raises(ValueError):
        _read_json_lines(fp)


def test_read_labels_csv(tmp_path):
    fp = tmp_path / "labels.csv"
    fp.write_text("sha256,label\na,1\nb,0\n")
    items = _read_labels(fp)
    assert items == [{"sha256": "a", "label": 1}, {"sha256": "b", "label": 0}]


def test_read_json_array(tmp_path):
    fp = tmp_path / "features.json"
    fp.write_text('[{"sha": "a"}, {"sha": "b"}]')
    items = _read_json_lines(fp)
    assert items == [{"sha": "a"}, {"sha": "b"}]


def test_read_string_array(tmp_path):
    fp = tmp_path / "hints.json"
    fp.write_text('["A", "B"]')
    items = _read_json_lines(fp)
    assert items == ["A", "B"]


def test_build_parser_accepts_embed_dir(monkeypatch):
    import importlib

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")
    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "feature-mine",
            "--graph-dir",
            "d",
            "--out",
            "o.json",
            "--embed-dir",
            "embeds",
            "--classifier-ckpt",
            "clf.pt",
        ]
    )
    assert args.embed_dir == "embeds"
    assert args.classifier_ckpt == Path("clf.pt")
    assert args.func == rulegen_cli.cmd_feature_mine


def test_generate_parser_accepts_features(monkeypatch):
    import importlib

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")
    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "generate",
            "--agent-checkpoint",
            "agent.pt",
            "--out",
            "rules.yar",
            "--features",
            "feats.json",
        ]
    )
    assert args.features == "feats.json"
    assert args.func == rulegen_cli.cmd_generate


def test_generate_parser_accepts_target_graph(monkeypatch, tmp_path):
    import importlib

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")
    parser = rulegen_cli._build_parser()
    tg = tmp_path / "g.pt"
    args = parser.parse_args(
        [
            "generate",
            "--agent-checkpoint",
            "agent.pt",
            "--target-graph",
            str(tg),
        ]
    )
    assert args.target_graph == str(tg)
    assert args.func == rulegen_cli.cmd_generate


def test_generate_default_capa_extension(monkeypatch, tmp_path):
    import importlib
    import types
    import argparse

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    class DummyAgent:
        def __init__(self, env, seed=None, use_hint=False):
            pass

        def load(self, ckpt):
            pass

        def sample_rules(self, n, temperature):
            return [["token"]] * n

    class DummyBuilder:
        def build(self, rule):
            return "rule"

    def fake_lazy_imports():
        rulegen_cli.PPORuleAgent = DummyAgent
        rulegen_cli.YaraBuilder = DummyBuilder
        rulegen_cli.CapaBuilder = DummyBuilder
        rulegen_cli.rulegen = types.SimpleNamespace(make_env=lambda **kw: None)

    monkeypatch.setattr(rulegen_cli, "_lazy_imports", fake_lazy_imports)
    monkeypatch.chdir(tmp_path)

    feat_fp = tmp_path / "feats.json"
    feat_fp.write_text('[{"features": ["foo"]}]')

    args = argparse.Namespace(
        agent_checkpoint="agent.pt",
        features=str(feat_fp),
        n_rules=1,
        temperature=1.0,
        out=None,
        rule_type="capa",
        seed=42,
        target_graph=None,
        single_target_mode=False,
        off_target_penalty=None,
        off_target_penalty_start=None,
        off_target_penalty_end=None,
        off_target_steps=None,
        no_tp_penalty=1.0,
        reward_weights=None,
    )

    rulegen_cli.cmd_generate(args)

    out_files = list((tmp_path / "models" / "rulebank" / "capa").glob("generated_*.yml"))
    assert len(out_files) == 1


def test_parser_accepts_combo_options(monkeypatch):
    import importlib

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")
    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            "feats.json",
            "--dataset-dir",
            "d",
            "--condition-type",
            "combo",
            "--group-min-count",
            "2",
        ]
    )
    assert args.condition_type == "combo"
    assert args.group_min_count == 2
    assert args.func == rulegen_cli.cmd_ppo_train
