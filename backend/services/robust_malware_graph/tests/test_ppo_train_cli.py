import argparse
import logging
import sys
import types
import importlib
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

# Provide lightweight psutil stub for common.utils
sys.modules.setdefault("psutil", types.ModuleType("psutil"))
sys.modules.setdefault("numpy", types.ModuleType("numpy"))
sys.modules.setdefault("pandas", types.ModuleType("pandas"))
tg_stub = types.ModuleType("torch_geometric")
tg_data = types.ModuleType("torch_geometric.data")
tg_data.Data = object
tg_data.HeteroData = object
tg_stub.data = tg_data
sys.modules.setdefault("torch_geometric", tg_stub)
sys.modules.setdefault("torch_geometric.data", tg_data)


def test_ppo_train_checks_dataset(tmp_path, caplog, monkeypatch):
    # Provide dummy modules so rulegen_cli imports without heavy deps
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")
    tf = tmp_path / "train.jsonl"
    tf.write_text("[]")

    args = argparse.Namespace(
        train_features=tf,
        val_features=None,
        config=None,
        dataset_dir=tmp_path,
        epochs=1,
        checkpoint=None,
        plot_path=None,
        cpu=True,
    )

    caplog.set_level(logging.ERROR)
    with pytest.raises(SystemExit) as exc:
        rulegen_cli.cmd_ppo_train(args)

    assert exc.value.code == 1
    assert (
        "Dataset directory missing required files clean.pt and dummy.pt" in caplog.text
    )


def test_hint_file_passed(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            self.env = env

        def train(self, **kw):
            captured["train"] = kw
            return []

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = lambda env=None: DummyAgent(env)
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    y_mod = types.ModuleType("rulegen.yara_builder")
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")
    (ds / "sel.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")
    hint_fp = tmp_path / "hint.json"
    hint_fp.write_text('["H1"]')

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--hint-file",
            str(hint_fp),
            "--classifier-ckpt",
            str(ds / "clf.pt"),
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["hint_features"] == ["H1"]
    assert captured["classifier_ckpt"] == str(ds / "clf.pt")


def test_use_explainer_hints(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            self.env = env

        def train(self, **kw):
            captured["train"] = kw
            return []

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = lambda env=None: DummyAgent(env)
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    y_mod = types.ModuleType("rulegen.yara_builder")
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text('[{"features": ["A"]}, {"features": ["B", "C"]}]')

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--use-explainer-hints",
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert set(captured["hint_features"]) == {"A", "B", "C"}


def test_use_explainer_hints_env_instance(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        env = types.SimpleNamespace(**kw)
        captured["env"] = env
        return env

    class DummyAgent:
        def __init__(self, env):
            captured["agent_env"] = env

        def train(self, **kw):
            return []

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = lambda env=None: DummyAgent(env)
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    y_mod = types.ModuleType("rulegen.yara_builder")
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text('[{"features": ["A"]}, {"features": ["B", "C"]}]')

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--use-explainer-hints",
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert set(captured["env"].hint_features) == {"A", "B", "C"}
    assert captured["agent_env"] is captured["env"]


def test_reward_weights_cli(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            captured["agent_env"] = env

        def train(self, **kw):
            return []

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = lambda env=None: DummyAgent(env)
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    y_mod = types.ModuleType("rulegen.yara_builder")
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")

    parser = rulegen_cli._build_parser()
    weights = '{"f1_clean":1.0,"f1_dummy":0.0,"rule_len":0.0,"certified_bonus":0.0}'
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--reward-weights",
            weights,
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["reward_weights"]["f1_clean"] == 1.0

def test_amp_lora_cli(tmp_path, monkeypatch):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            captured["agent_env"] = env

        def train(self, **kw):
            return []

    def fake_load_agent(**kw):
        captured["agent_kwargs"] = kw.get("agent_kwargs")
        return DummyAgent(kw.get("env"))

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = fake_load_agent
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""
    y_mod = types.ModuleType("rulegen.yara_builder")
    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--amp",
            "--grad-checkpoint",
            "--lora-r",
            "4",
            "--lora-alpha",
            "8",
            "--lora-dropout",
            "0.2",
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["agent_kwargs"]["use_amp"] is True
    assert captured["agent_kwargs"]["checkpoint_layers"] is True
    assert captured["agent_kwargs"]["lora_cfg"]["r"] == 4
    assert captured["agent_kwargs"]["lora_cfg"]["alpha"] == 8.0
    assert captured["agent_kwargs"]["lora_cfg"]["dropout"] == 0.2


def test_agent_hyperparam_cli(tmp_path, monkeypatch):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            captured["agent_env"] = env

        def train(self, **kw):
            return []

    def fake_load_agent(**kw):
        captured["agent_kwargs"] = kw.get("agent_kwargs")
        return DummyAgent(kw.get("env"))

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = fake_load_agent
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod = types.ModuleType("rulegen.yara_builder")
    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--num-steps",
            "2048",
            "--minibatch-size",
            "32",
            "--ppo-epochs",
            "8",
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["agent_kwargs"]["n_steps"] == 2048
    assert captured["agent_kwargs"]["minibatch_size"] == 32
    assert captured["agent_kwargs"]["n_epochs"] == 8


def test_use_lookahead_cli(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            captured["agent_env"] = env

        def train(self, **kw):
            return []

    def fake_load_agent(**kw):
        return DummyAgent(kw.get("env"))

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = fake_load_agent
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod = types.ModuleType("rulegen.yara_builder")
    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--use-lookahead",
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["use_lookahead"] is True


def test_meta_path_cli(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            captured["agent_env"] = env

        def train(self, **kw):
            return []

    def fake_load_agent(**kw):
        return DummyAgent(kw.get("env"))

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = fake_load_agent
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod = types.ModuleType("rulegen.yara_builder")
    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")
    meta_fp = tmp_path / "enc.meta.pkl"
    meta_fp.write_text("x")

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--meta-path",
            str(meta_fp),
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["meta_path"] == str(meta_fp)


def test_max_hint_tokens_cli(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            captured["agent_env"] = env

        def train(self, **kw):
            return []

    def fake_load_agent(**kw):
        return DummyAgent(kw.get("env"))

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = fake_load_agent
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod = types.ModuleType("rulegen.yara_builder")
    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--max-hint-tokens",
            "7",
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["max_hint_tokens"] == 7


def test_rule_len_penalty_cli(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            captured["agent_env"] = env

        def train(self, **kw):
            return []

    def fake_load_agent(**kw):
        return DummyAgent(kw.get("env"))

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = fake_load_agent
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod = types.ModuleType("rulegen.yara_builder")
    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--rule-len-penalty-start",
            "0.1",
            "--rule-len-penalty-end",
            "-0.1",
            "--rule-len-steps",
            "5",
            "--rule-len-penalty-delay",
            "3",
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["rule_len_penalty_start"] == 0.1
    assert captured["rule_len_penalty_end"] == -0.1
    assert captured["rule_len_steps"] == 5
    assert captured["rule_len_penalty_delay"] == 3


def test_generate_hints_from_explainer(tmp_path, monkeypatch):
    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    captured = {}
    rulegen_stub = types.ModuleType("rulegen")

    def fake_make_env(**kw):
        captured.update(kw)
        return "env"

    class DummyAgent:
        def __init__(self, env):
            captured["env"] = env

        def train(self, **kw):
            return []

    rulegen_stub.make_env = fake_make_env
    rulegen_stub.load_agent = lambda env=None: DummyAgent(env)
    monkeypatch.setitem(sys.modules, "rulegen", rulegen_stub)
    fm_mod = types.ModuleType("rulegen.feature_miner")
    fm_mod.FeatureMiner = object
    monkeypatch.setitem(sys.modules, "rulegen.feature_miner", fm_mod)
    ra_mod = types.ModuleType("rulegen.rl_agent")
    ra_mod.PPORuleAgent = object
    monkeypatch.setitem(sys.modules, "rulegen.rl_agent", ra_mod)
    class _DummyBuilder:
        def __init__(self, *a, **k):
            pass

        def build(self, *a, **k):
            return ""

    y_mod = types.ModuleType("rulegen.yara_builder")
    y_mod.YaraBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.yara_builder", y_mod)
    c_mod = types.ModuleType("rulegen.capa_builder")
    c_mod.CapaBuilder = _DummyBuilder
    monkeypatch.setitem(sys.modules, "rulegen.capa_builder", c_mod)
    gd_mod = types.ModuleType("graphs.dataset.graph_dataset")
    gd_mod.GraphDataset = object
    monkeypatch.setitem(sys.modules, "graphs.dataset.graph_dataset", gd_mod)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")
    monkeypatch.setattr(rulegen_cli, "generate_explainer_hints", lambda *a, **k: ["HX"])

    ds = tmp_path / "ds"
    ds.mkdir()
    (ds / "clean.pt").write_text("x")
    (ds / "dummy.pt").write_text("x")

    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")

    parser = rulegen_cli._build_parser()
    args = parser.parse_args(
        [
            "ppo-train",
            "--train-features",
            str(train_fp),
            "--dataset-dir",
            str(ds),
            "--generate-hints-from-explainer",
            "--explainer-checkpoint",
            str(ds / "sel.pt"),
            "--epochs",
            "1",
            "--cpu",
        ]
    )

    args.func(args)
    assert captured["hint_features"] == ["HX"]


def test_hint_option_conflict(tmp_path, monkeypatch):
    import importlib

    torch_stub = types.SimpleNamespace(
        device=lambda *a, **k: None,
        cuda=types.SimpleNamespace(is_available=lambda: False),
    )
    monkeypatch.setitem(sys.modules, "torch", torch_stub)
    matplotlib_stub = types.ModuleType("matplotlib")
    matplotlib_stub.use = lambda *a, **k: None
    pyplot_stub = types.ModuleType("matplotlib.pyplot")
    monkeypatch.setitem(sys.modules, "matplotlib", matplotlib_stub)
    monkeypatch.setitem(sys.modules, "matplotlib.pyplot", pyplot_stub)
    om_conf = types.ModuleType("omegaconf")
    om_conf.OmegaConf = types.SimpleNamespace(load=lambda *_: {}, create=lambda *_: {})
    monkeypatch.setitem(sys.modules, "omegaconf", om_conf)
    tqdm_stub = types.ModuleType("tqdm")
    tqdm_stub.tqdm = lambda x, **k: x
    monkeypatch.setitem(sys.modules, "tqdm", tqdm_stub)

    rulegen_cli = importlib.import_module("src.cli.rulegen_cli")
    parser = rulegen_cli._build_parser()

    ds = tmp_path / "ds"
    ds.mkdir()
    train_fp = tmp_path / "train.json"
    train_fp.write_text("[]")

    with pytest.raises(SystemExit):
        parser.parse_args(
            [
                "ppo-train",
                "--train-features",
                str(train_fp),
                "--dataset-dir",
                str(ds),
                "--hint-file",
                "h.json",
                "--use-explainer-hints",
            ]
        )


def test_gpt_embedding_resize_warning(monkeypatch, caplog):
    sys.modules.pop("rulegen", None)
    sys.modules.pop("rulegen.rl_agent", None)
    sys.modules.pop("src.rulegen", None)
    sys.modules.pop("src.rulegen.rl_agent", None)

    env = types.SimpleNamespace(vocab_size=5)

    class DummyGPT:
        def __init__(self):
            self.emb_size = 3
            self.resized_to = None

        def get_input_embeddings(self):
            return types.SimpleNamespace(num_embeddings=self.emb_size)

        def resize_token_embeddings(self, n):
            self.resized_to = n

    class DummyAgent:
        def __init__(self, env, **kw):
            self.env = env
            self.policy = types.SimpleNamespace(gpt=DummyGPT())

        def load(self, *a, **k):
            pass

    import importlib
    import src.rulegen as rg
    rg.PPORuleAgent = DummyAgent
    import rulegen as rg_root
    rulegen = importlib.reload(rg_root)

    caplog.set_level(logging.WARNING)
    agent = rulegen.load_agent(env=env, policy_net="gpt2")

    assert agent.policy.gpt.resized_to == env.vocab_size
    assert any("Resized GPT embeddings" in r.message for r in caplog.records)
