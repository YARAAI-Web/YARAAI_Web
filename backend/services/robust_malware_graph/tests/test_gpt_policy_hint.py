import sys
import types
from pathlib import Path
import pytest

torch = pytest.importorskip("torch")

# Provide a lightweight transformers stub
trans_stub = types.ModuleType("transformers")

gym_stub = types.ModuleType("gymnasium")
gym_stub.Env = object


class _Box:
    def __init__(self, *a, **k):
        pass


class _Discrete:
    def __init__(self, *a, **k):
        pass


gym_stub.spaces = types.SimpleNamespace(Box=_Box, Discrete=_Discrete)
gym_stub.registry = {}
gym_stub.register = lambda *a, **k: None
sys.modules.setdefault("gymnasium", gym_stub)


class DummyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.config = types.SimpleNamespace(hidden_size=4)

    def forward(self, input_ids=None, **kwargs):
        bsz, seq_len = input_ids.shape
        hidden = torch.zeros(bsz, seq_len, self.config.hidden_size)
        return types.SimpleNamespace(last_hidden_state=hidden)


trans_stub.AutoModelForCausalLM = types.SimpleNamespace(
    from_pretrained=lambda *a, **k: DummyModel()
)

sys.modules.setdefault("transformers", trans_stub)

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from src.rulegen.rl_agent import GPTPolicy


def test_gpt_policy_hint_forward():
    policy = GPTPolicy("dummy", vocab_size=8, use_hint=True, hint_size=None)
    assert hasattr(policy, "hint_size")
    obs = torch.tensor([[1, 2]], dtype=torch.long)
    hint = torch.tensor([[3, 4]], dtype=torch.long)
    # Ensure forward accepts hint_ids kwarg
    policy(obs, hint_ids=hint)
