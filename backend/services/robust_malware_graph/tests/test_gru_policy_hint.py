import sys
import types
import pytest
torch = pytest.importorskip("torch")

gym_stub = types.ModuleType("gymnasium")
gym_stub.registry = {}
gym_stub.register = lambda *a, **k: None
sys.modules.setdefault("gymnasium", gym_stub)

rl_env_stub = types.ModuleType("src.rulegen.rl_env")
rl_env_stub.RuleGenEnv = object
sys.modules.setdefault("src.rulegen.rl_env", rl_env_stub)

from src.rulegen.rl_agent import GRUPolicy


def test_policy_no_hint():
    policy = GRUPolicy(
        vocab_size=10, embed_dim=8, hidden_size=16, use_hint=False, pad_id=0
    )
    obs = torch.tensor([[1, 2, 0], [3, 0, 0]], dtype=torch.long)
    logits, value = policy(obs)
    assert logits.shape == (2, 10)
    assert value.shape == (2,)


def test_policy_with_hint():
    policy = GRUPolicy(
        vocab_size=10, embed_dim=8, hidden_size=16, use_hint=True, pad_id=0
    )
    obs = torch.tensor([[1, 2, 0], [3, 4, 0]], dtype=torch.long)
    hint = torch.tensor([[5, 6], [7, 8]], dtype=torch.long)
    logits, value = policy(obs, hint)
    assert logits.shape == (2, 10)
    assert value.shape == (2,)


def test_policy_hint_none():
    policy = GRUPolicy(
        vocab_size=10, embed_dim=8, hidden_size=16, use_hint=True, pad_id=0
    )
    obs = torch.tensor([[1, 0, 0]], dtype=torch.long)
    logits, value = policy(obs)
    assert logits.shape == (1, 10)
    assert value.shape == (1,)


def test_policy_single_dim_inputs():
    policy = GRUPolicy(
        vocab_size=10, embed_dim=8, hidden_size=16, use_hint=True, pad_id=0
    )
    obs = torch.tensor([1, 2, 0], dtype=torch.long)
    hint = torch.tensor([5, 6], dtype=torch.long)
    logits, value = policy(obs, hint)
    assert logits.shape == (1, 10)
    assert value.shape == (1,)


def test_policy_vector_hint():
    policy = GRUPolicy(
        vocab_size=10,
        embed_dim=8,
        hidden_size=16,
        use_hint=True,
        hint_size=4,
        pad_id=0,
    )
    obs = torch.tensor([[1, 2, 0]], dtype=torch.long)
    hint = torch.randn(1, 4)
    logits, value = policy(obs, hint)
    assert logits.shape == (1, 10)
    assert value.shape == (1,)


def test_policy_custom_pad_id():
    policy = GRUPolicy(vocab_size=10, embed_dim=8, hidden_size=16, pad_id=1)
    obs = torch.tensor([[1, 2, 1, 1]], dtype=torch.long)
    logits, value = policy(obs)
    assert logits.shape == (1, 10)
    assert value.shape == (1,)
