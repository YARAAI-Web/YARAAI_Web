import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")
pytest.importorskip("matplotlib")
pytest.importorskip("gymnasium")

import torch
from torch.utils.data import DataLoader
from torch_geometric.data import Data, Batch
from torch_geometric.nn import global_mean_pool

from src.cli.finetune_supcon import train_one_epoch, evaluate
from src.models.contrast.sup_con import SupContrastHead

class DummyDataset:
    def __init__(self, num_graphs=8):
        self.graphs = []
        self.labels = []
        for i in range(num_graphs):
            x = torch.randn(3, 1) + i
            g = Data(x=x, edge_index=torch.tensor([[0, 1], [1, 2]]), num_nodes=3)
            self.graphs.append(g)
            self.labels.append(i % 2)
            
    def __len__(self):
        return len(self.graphs)

    def __getitem__(self, idx):
        return self.graphs[idx], self.labels[idx], f"id{idx}"


def collate(batch):
    return {"graph": Batch.from_data_list([b[0] for b in batch]),
            "label": torch.tensor([b[1] for b in batch], dtype=torch.long),
            "ids": [b[2] for b in batch]}

class DummyEncoder(torch.nn.Module):
    def __init__(self, in_dim=1, out_dim=2):
        super().__init__()
        self.lin = torch.nn.Linear(in_dim, out_dim)
        self.out_dim = out_dim

    def forward(self, batch):
        h = self.lin(batch.x.float())
        return global_mean_pool(h, batch.batch)


def make_model():
    enc = DummyEncoder()
    head = SupContrastHead(in_dim=enc.out_dim, proj_dim=enc.out_dim)
    model = torch.nn.Module()
    model.encoder = enc
    model.head = head
    return model


def test_train_dict_batches():
    ds = DummyDataset()
    loader = DataLoader(ds, batch_size=4, collate_fn=collate)
    model = make_model()
    opt = torch.optim.SGD(model.parameters(), lr=0.1)
    loss = train_one_epoch(model, loader, opt, torch.device("cpu"))
    assert isinstance(loss, float)


def test_ppo_train_logging(caplog):
    import numpy as np
    import gymnasium as gym
    from src.rulegen.rl_agent import PPORuleAgent, _LOG as RL_LOG

    class TinyEnv(gym.Env):
        PAD = "<PAD>"
        END = "<END>"

        def __init__(self):
            self.action_space = gym.spaces.Discrete(3)
            self.observation_space = gym.spaces.Box(low=0, high=2, shape=(4,), dtype=np.int64)
            self.token2id = {"A": 0, self.PAD: 1, self.END: 2}
            self.id2token = {v: k for k, v in self.token2id.items()}
            self.reward_weights = {
                "f1_clean": 0.5,
                "f1_dummy": 0.5,
                "rule_len": 0.0,
                "certified_bonus": 0.0,
            }
            self.max_len = 4

        def reset(self, *, seed=None, options=None):
            self._tokens = []
            obs = np.full(self.max_len, self.token2id[self.PAD], dtype=np.int64)
            return obs, {}

        def step(self, action):
            self._tokens.append(action)
            obs = np.full(self.max_len, self.token2id[self.PAD], dtype=np.int64)
            done = len(self._tokens) >= 1
            info = {"metrics": {"f1_clean": 0.0, "f1_dummy": 0.1}}
            return obs, 0.0, done, False, info

        def get_action_mask(self, tokens=None, hint_tokens=None):
            return np.ones(self.action_space.n, dtype=np.int8)

    env = TinyEnv()
    agent = PPORuleAgent(
        env,
        n_steps=1,
        minibatch_size=1,
        batch_size=1,
        n_epochs=1,
        device="cpu",
    )
    caplog.set_level("INFO", logger=RL_LOG.name)
    agent.train(total_timesteps=1, log_interval=1)
    messages = [rec.message for rec in caplog.records if rec.name == RL_LOG.name]
    assert any("f1_dummy" in m and "weights" in m for m in messages)
