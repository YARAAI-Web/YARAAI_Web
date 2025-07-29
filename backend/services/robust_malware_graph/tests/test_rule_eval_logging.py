import json
import types
import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")
pytest.importorskip("gymnasium")
pytest.importorskip("evaluation")

from torch_geometric.data import HeteroData
from src.rulegen.rl_env import RuleGenEnv

@pytest.fixture
def env(tmp_path):
    clean = [HeteroData()]
    dummy = [HeteroData()]
    vocab = {"A":0, "<PAD>":1, "<END>":2}
    torch = pytest.importorskip('torch')
    torch.save(clean, tmp_path/'clean.pt')
    torch.save(dummy, tmp_path/'dummy.pt')
    (tmp_path/'vocab.json').write_text(json.dumps(vocab))
    e = RuleGenEnv(rule_type='yara', vocab_file=tmp_path/'vocab.json', dataset_dir=tmp_path, max_len=4, classifier_checkpoint=tmp_path/'clf.pt', device='cpu')
    return e

def test_callback_and_history(env, monkeypatch):
    logs = []
    env.set_rule_eval_callback(lambda r,m: logs.append((r,m)))
    monkeypatch.setattr(env.evaluator, 'evaluate_rule', lambda *a,**k: (0.1,0.2,2.0,(1,1,0,0)))
    env._compute_reward('A', update_stats=True)
    hist = env.get_rule_eval_history()
    assert len(hist) == 1
    assert logs and logs[0][0] == 'A'
