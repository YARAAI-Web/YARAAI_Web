import json
import random
import pytest
import sys
import types

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")
pytest.importorskip("gymnasium")

import src.evaluation as evaluation

sys.modules.setdefault("evaluation", evaluation)

import torch
from torch_geometric.data import HeteroData

# older PyTorch versions may miss this helper
if not hasattr(torch.serialization, "add_safe_globals"):
    setattr(torch.serialization, "add_safe_globals", lambda *a, **k: None)

from src.rulegen.rl_env import RuleGenEnv
import src.rulegen.rl_env as rl_env
import src.models.gnn.res_wrapper as res_wrapper
import models.gnn.res_wrapper as res_wrapper_pkg


class DummyClf(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.calls = 0
        self.encoder = types.SimpleNamespace(
            attr_names={},
            attr_dim=1,
            input_proj={},
            meta_embed=None,
        )

    def forward(self, data):
        self.calls += 1
        return torch.zeros(len(data), dtype=torch.float)

    def reinit_input_dims(self, in_dims, attr_names=None, vocab_size=0):
        self.encoder.attr_names = attr_names or {}
        if vocab_size:
            self.encoder.meta_embed = torch.nn.Embedding(vocab_size, self.encoder.attr_dim)


dummy_clf = DummyClf()
res_wrapper.RESGCLClassifier.load_pretrained = classmethod(
    lambda cls, path, map_location=None: dummy_clf
)
res_wrapper_pkg.RESGCLClassifier.load_pretrained = (
    res_wrapper.RESGCLClassifier.load_pretrained
)


def test_env_instantiates(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=8,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
    )

    assert env.action_space.n == len(env.token2id)
    assert env.token2id[env.PAD] != 0


def test_reset_with_hints(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        hint_features=["A"],
    )

    obs, _ = env.reset()
    assert obs[0] == env.token2id["A"]


def test_reset_multiple_hints(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "B": 1, "<PAD>": 2, "<END>": 3}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        hint_features=["A", "B"],
    )

    obs, _ = env.reset()
    assert obs[0] == env.token2id["A"]
    assert obs[1] == env.token2id["B"]


def test_action_mask_parentheses(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "(": 1, ")": 2, "<PAD>": 3, "<END>": 4}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
    )

    env.reset()
    mask = env.get_action_mask()
    assert mask[env.token2id[")"]] == 0

    env._tokens = [env.token2id["("]]
    mask = env.get_action_mask()
    assert mask[env.token2id[")"]] == 1


def test_action_mask_length(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=2,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
    )

    env.reset()
    env._tokens = [env.token2id["A"], env.token2id["A"]]
    mask = env.get_action_mask()
    assert mask.sum() == 1
    assert mask[env.token2id[env.END]] == 1


def test_rule_tokenize_subtokens():
    result = RuleGenEnv._rule_tokenize("CreateFileW")
    assert result == ["Create", "File", "W"]


def test_pad_index_nonzero(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 5, "<END>": 6}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
    )

    obs, _ = env.reset()
    assert (obs == env.token2id[env.PAD]).sum() > 0


def test_compute_reward_penalizes_invalid_rule(tmp_path, monkeypatch):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
    )

    monkeypatch.setattr(
        env.evaluator,
        "evaluate_rule",
        lambda *args, **kwargs: (0.0, 0.0, -1.0, (0, 0, 0, 0)),
    )
    reward, metrics, _ = env._compute_reward("", update_stats=False)
    assert metrics["invalid_rule"]
    assert reward <= -1.0


def _build_env_for_mask(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab = {
        "call": 0,
        ":": 1,
        "foo": 2,
        '"BAR"': 3,
        "42": 4,
        "(": 5,
        ")": 6,
        "<PAD>": 7,
        "<END>": 8,
    }
    vocab_file = tmp_path / "vocab.json"
    json.dump(vocab, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=6,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
    )
    env.reset()
    return env


def test_action_mask_colon_and_strings(tmp_path):
    env = _build_env_for_mask(tmp_path)

    mask = env.get_action_mask()
    assert mask[env.token2id[":"]] == 0
    assert mask[env.token2id['"BAR"']] == 0
    assert mask[env.token2id["42"]] == 0

    env._tokens = [env.token2id["call"]]
    mask = env.get_action_mask()
    assert mask[env.token2id[":"]] == 1

    env._tokens = [env.token2id["("]]
    mask = env.get_action_mask()
    assert mask[env.token2id[":"]] == 0

    env._tokens = [env.token2id["call"], env.token2id[":"]]
    mask = env.get_action_mask()
    assert mask[env.token2id['"BAR"']] == 1
    assert mask[env.token2id["42"]] == 1

    env._tokens = [env.token2id["call"], env.token2id[":"], env.token2id["42"]]
    mask = env.get_action_mask()
    assert mask[env.token2id["42"]] == 1


def test_reward_weights_override(tmp_path, monkeypatch):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        reward_weights={
            "f1_clean": 1.0,
            "f1_dummy": 0.0,
            "rule_len": 0.0,
            "certified_bonus": 0.0,
        },
    )
    monkeypatch.setattr(
        env.evaluator, "evaluate_rule", lambda *a, **k: (0.5, 0.2, 3.0, (0, 0, 0, 0))
    )
    r, m, _ = env._compute_reward("", update_stats=False)
    assert pytest.approx(r) == 0.5


def test_fp_penalty_curriculum(tmp_path, monkeypatch):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        fp_penalty_start=1.0,
        fp_penalty_end=0.0,
        curriculum_steps=10,
        fp_penalty_delay=5,
    )
    monkeypatch.setattr(
        env.evaluator, "evaluate_rule", lambda *a, **k: (0.5, 0.5, 0.0, (0, 1, 0, 0))
    )
    env.total_steps = 5
    r1, m1, _ = env._compute_reward("", update_stats=False)
    env.total_steps = 15
    r2, m2, _ = env._compute_reward("", update_stats=False)
    assert r2 > r1
    assert m1["fp_penalty"] > m2["fp_penalty"]
    env.total_steps = 3
    _, m0, _ = env._compute_reward("", update_stats=False)
    assert m0["fp_penalty"] == 0.0


def test_rule_len_penalty_curriculum(tmp_path, monkeypatch):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        rule_len_penalty_start=0.0,
        rule_len_penalty_end=-1.0,
        rule_len_steps=10,
    )

    monkeypatch.setattr(
        env.evaluator,
        "evaluate_rule",
        lambda *a, **k: (0.0, 0.0, 0.0, (0, 0, 0, 0)),
    )
    env.total_steps = 0
    r1, m1, _ = env._compute_reward("A", update_stats=False)
    env.total_steps = 10
    r2, m2, _ = env._compute_reward("A", update_stats=False)
    assert r2 < r1
    assert m1["rule_len_weight"] > m2["rule_len_weight"]


def test_rule_len_penalty_delay(tmp_path, monkeypatch):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        rule_len_penalty_start=0.0,
        rule_len_penalty_end=-1.0,
        rule_len_steps=10,
        rule_len_penalty_delay=5,
    )

    monkeypatch.setattr(
        env.evaluator,
        "evaluate_rule",
        lambda *a, **k: (0.0, 0.0, 0.0, (0, 0, 0, 0)),
    )
    env.total_steps = 2
    _, m_before, _ = env._compute_reward("A", update_stats=False)
    env.total_steps = 7
    _, m_after, _ = env._compute_reward("A", update_stats=False)
    assert m_before["rule_len_weight"] == 0.0
    assert m_after["rule_len_weight"] < m_before["rule_len_weight"]


def test_lookahead_reward(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        use_lookahead=True,
    )

    env.reset()
    dummy_clf.calls = 0
    _, r, done, tr, info = env.step(env.token2id["A"])
    assert dummy_clf.calls == 0
    assert not done
    assert "lookahead_prob" in info


def test_metadata_vocab_list_format(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    meta_vocab = tmp_path / "metadata_vocab.json"
    json.dump({"foo": ["x", "y"]}, meta_vocab.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
    )

    assert env.classifier.encoder.attr_names.get("") == ["foo"]


def test_meta_path_overrides_metadata(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    meta_vocab = tmp_path / "metadata_vocab.json"
    json.dump({"bar": ["z"]}, meta_vocab.open("w"))

    meta_path = tmp_path / "enc.meta.pkl"
    torch.save(
        {"attr_names": {"": ["foo"]}, "in_dims": {"": 4}, "vocab_size": 3, "attr_dim": 2},
        meta_path,
    )

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        meta_path=meta_path,
    )

    assert env.classifier.encoder.attr_names.get("") == ["foo"]
    assert env.classifier.encoder.meta_embed is not None
    assert env.classifier.encoder.meta_embed.num_embeddings == 3


def test_single_target_mode_hints(tmp_path, monkeypatch):
    clean = [HeteroData()]
    d1 = HeteroData()
    d1.features = ["A"]
    d2 = HeteroData()
    d2.features = ["B"]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save([d1, d2], tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "B": 1, "<PAD>": 2, "<END>": 3}, vocab_file.open("w"))

    monkeypatch.setattr(random, "randrange", lambda n: 1)

    class DummyFM:
        def __init__(self, *a, **k):
            pass

        def __call__(self, g, sal):
            return getattr(g, "features", [])

    monkeypatch.setattr(rl_env, "FeatureMiner", DummyFM)

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        single_target_mode=True,
    )

    obs, info = env.reset()
    assert info.get("target_idx") == 1
    assert list(info["hint"]) == [env.token2id["B"]]


def test_off_target_penalty(tmp_path, monkeypatch):
    clean = [HeteroData()]
    d1 = HeteroData()
    d2 = HeteroData()
    d3 = HeteroData()
    torch.save(clean, tmp_path / "clean.pt")
    torch.save([d1, d2, d3], tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    monkeypatch.setattr(random, "randrange", lambda n: 0)

    class DummyFM:
        def __init__(self, *a, **k):
            pass

        def __call__(self, g, sal):
            return []

    monkeypatch.setattr(rl_env, "FeatureMiner", DummyFM)

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        single_target_mode=True,
        off_target_penalty=1.0,
    )

    env.reset()

    def eval_rule(rule, clean_set, dummy_set):
        if clean_set:
            return 1.0, 1.0, 3.0, (0, 0, 0, 0)
        else:
            m = len(dummy_set)
            f1 = 2.0 / (m + 1)
            return 0.0, f1, 3.0, (0, 0, 0, 0)

    monkeypatch.setattr(env.evaluator, "evaluate_rule", eval_rule)
    r1, m1, _ = env._compute_reward("A", update_stats=False)

    def eval_rule_no_off(rule, clean_set, dummy_set):
        if clean_set:
            return 1.0, 1.0, 3.0, (0, 0, 0, 0)
        else:
            return 0.0, 0.0, 3.0, (0, 0, 0, 0)

    monkeypatch.setattr(env.evaluator, "evaluate_rule", eval_rule_no_off)
    r2, m2, _ = env._compute_reward("A", update_stats=False)

    assert r1 < r2
    assert m1["off_target_matches"] > 0


def test_off_target_penalty_schedule(tmp_path, monkeypatch):
    clean = [HeteroData()]
    d1 = HeteroData()
    d2 = HeteroData()
    torch.save(clean, tmp_path / "clean.pt")
    torch.save([d1, d2], tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        single_target_mode=True,
        off_target_penalty_start=0.0,
        off_target_penalty_end=1.0,
        off_target_steps=10,
    )

    env.reset()

    monkeypatch.setattr(
        env.evaluator,
        "evaluate_rule",
        lambda *a, **k: (0.0, 1.0, 3.0, (0, 0, 0, 0)),
    )

    env.total_steps = 0
    r1, m1, _ = env._compute_reward("A", update_stats=False)
    env.total_steps = 10
    r2, m2, _ = env._compute_reward("A", update_stats=False)

    assert m1["off_target_penalty"] < m2["off_target_penalty"]
    assert r1 > r2


def test_no_tp_penalty(tmp_path, monkeypatch):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        no_tp_penalty=0.5,
    )

    monkeypatch.setattr(
        env.evaluator,
        "evaluate_rule",
        lambda *a, **k: (0.0, 0.0, 0.0, (0, 0, 0, 0)),
    )
    r1, m1, _ = env._compute_reward("A", update_stats=False)

    monkeypatch.setattr(
        env.evaluator,
        "evaluate_rule",
        lambda *a, **k: (0.0, 0.0, 0.0, (1, 0, 0, 0)),
    )
    r2, m2, _ = env._compute_reward("A", update_stats=False)

    assert m1["no_tp"] and not m2["no_tp"]
    assert pytest.approx(r2 - r1) == env.no_tp_penalty


def test_reset_constant_observation_length(tmp_path, monkeypatch):
    clean = [HeteroData()]
    d1 = HeteroData()
    d1.features = ["A"]
    d2 = HeteroData()
    d2.features = ["A", "B", "C"]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save([d1, d2], tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "B": 1, "C": 2, "<PAD>": 3, "<END>": 4}, vocab_file.open("w"))

    class DummyFM:
        def __init__(self, *a, **k):
            pass

        def __call__(self, g, sal):
            return getattr(g, "features", [])

    monkeypatch.setattr(rl_env, "FeatureMiner", DummyFM)

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        single_target_mode=True,
        max_hint_tokens=2,
    )

    lens = set()
    for _ in range(4):
        obs, info = env.reset()
        lens.add(len(obs))
        assert len(obs) == env.observation_space.shape[0]
        assert len(info["hint"]) == env.max_hint_tokens
    assert len(lens) == 1


def test_update_reward_weights_method(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
    )

    old = dict(env.reward_weights)
    env.update_reward_weights(f1_dummy=old["f1_dummy"] + 0.1, f1_clean=old["f1_clean"] - 0.1)

    assert env.reward_weights["f1_dummy"] == pytest.approx(old["f1_dummy"] + 0.1)
    assert env.reward_weights["f1_clean"] == pytest.approx(old["f1_clean"] - 0.1)


def test_f1_dummy_improve_bonus(tmp_path, monkeypatch):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    torch.save(clean, tmp_path / "clean.pt")
    torch.save(dummy, tmp_path / "dummy.pt")

    vocab_file = tmp_path / "vocab.json"
    json.dump({"A": 0, "<PAD>": 1, "<END>": 2}, vocab_file.open("w"))

    env = RuleGenEnv(
        rule_type="yara",
        vocab_file=vocab_file,
        dataset_dir=tmp_path,
        max_len=4,
        classifier_checkpoint=tmp_path / "clf.pt",
        device="cpu",
        improve_bonus=1.0,
    )

    monkeypatch.setattr(
        env.evaluator,
        "evaluate_rule",
        lambda *a, **k: (0.0, 0.0, 0.0, (0, 0, 0, 0)),
    )
    env._compute_reward("", update_stats=False)

    monkeypatch.setattr(
        env.evaluator,
        "evaluate_rule",
        lambda *a, **k: (0.0, 0.2, 0.0, (0, 0, 0, 0)),
    )
    r2, _, _ = env._compute_reward("", update_stats=False)
    expected = env.reward_weights["f1_dummy"] * 0.2 - env.no_tp_penalty
    expected += env.improve_bonus * 0.2
    assert pytest.approx(r2, rel=1e-6) == expected
