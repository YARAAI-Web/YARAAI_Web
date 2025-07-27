import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")
pytest.importorskip("transformers")

import torch
from torch_geometric.data import HeteroData
from src.models.llm_embed import embed_corpus
from src.graphs.features.cache import load_tensor

class DummyEncoder(torch.nn.Module):
    def __init__(self, hidden_size=2):
        super().__init__()
        self.hidden_size = hidden_size
    def forward(self, input_ids, attention_mask=None):
        return input_ids.float()


def test_embed_corpus(tmp_path):
    hetero_dir = tmp_path / "hetero"
    hetero_dir.mkdir()
    g = HeteroData()
    g["token"].input_ids = torch.tensor([[1, 2], [3, 4]], dtype=torch.long)
    g["token"].attention_mask = torch.tensor([[1, 1], [1, 1]], dtype=torch.long)
    g["token"].num_nodes = 2
    torch.save(g, hetero_dir / "sample.pt")

    out_dir = tmp_path / "embeds"
    encoder = DummyEncoder()
    embed_corpus(encoder, hetero_dir=hetero_dir, out_dir=out_dir, batch_size=1)

    feat = load_tensor("sample", out_dir)
    assert feat.shape == (2, 2)
    assert torch.all(feat.eq(torch.tensor([[1., 2.], [3., 4.]])))


def test_embed_corpus_no_tokens(tmp_path):
    hetero_dir = tmp_path / "hetero"
    hetero_dir.mkdir()
    g = HeteroData()
    torch.save(g, hetero_dir / "empty.pt")

    out_dir = tmp_path / "embeds"
    encoder = DummyEncoder()
    with pytest.raises(RuntimeError, match="No graphs"):
        embed_corpus(encoder, hetero_dir=hetero_dir, out_dir=out_dir)


def test_embed_corpus_no_files(tmp_path):
    hetero_dir = tmp_path / "hetero"
    hetero_dir.mkdir()

    out_dir = tmp_path / "embeds"
    encoder = DummyEncoder()
    with pytest.raises(RuntimeError, match="No hetero graphs"):
        embed_corpus(encoder, hetero_dir=hetero_dir, out_dir=out_dir)


def test_embed_corpus_bad_text(tmp_path, monkeypatch):
    hetero_dir = tmp_path / "hetero"
    hetero_dir.mkdir()
    g = HeteroData()
    g["token"].text = ["bad"]
    g["token"].num_nodes = 1
    torch.save(g, hetero_dir / "bad.pt")

    out_dir = tmp_path / "embeds"

    class DummyTok:
        def __call__(self, *args, **kwargs):
            raise ValueError("boom")

    class DummyAutoTok:
        @staticmethod
        def from_pretrained(name):
            return DummyTok()

    import src.models.llm_embed as llm_embed

    monkeypatch.setattr(llm_embed, "AutoTokenizer", DummyAutoTok)

    encoder = DummyEncoder()
    with pytest.raises(RuntimeError, match="Tokenization failed for bad"):
        embed_corpus(encoder, hetero_dir=hetero_dir, out_dir=out_dir)


def test_embed_corpus_text_coercion(tmp_path, monkeypatch):
    hetero_dir = tmp_path / "hetero"
    hetero_dir.mkdir()

    g1 = HeteroData()
    g1["token"].text = "hello"
    g1["token"].num_nodes = 1
    torch.save(g1, hetero_dir / "one.pt")

    g2 = HeteroData()
    g2["token"].text = ["a", None, 123]
    g2["token"].num_nodes = 3
    torch.save(g2, hetero_dir / "two.pt")

    out_dir = tmp_path / "embeds"

    class DummyTok:
        def __call__(self, texts, *args, **kwargs):
            ids = torch.tensor([[len(t)] for t in texts], dtype=torch.long)
            mask = torch.ones_like(ids)
            return {"input_ids": ids, "attention_mask": mask}

    class DummyAutoTok:
        @staticmethod
        def from_pretrained(name):
            return DummyTok()

    import src.models.llm_embed as llm_embed

    monkeypatch.setattr(llm_embed, "AutoTokenizer", DummyAutoTok)

    encoder = DummyEncoder()
    embed_corpus(encoder, hetero_dir=hetero_dir, out_dir=out_dir)

    feat1 = load_tensor("one", out_dir)
    feat2 = load_tensor("two", out_dir)

    assert feat1.tolist() == [[5]]
    assert feat2.tolist() == [[1], [0], [3]]


def test_embed_corpus_text_priority(tmp_path, monkeypatch):
    hetero_dir = tmp_path / "hetero"
    hetero_dir.mkdir()

    g = HeteroData()
    g["token"].text = ["abc"]
    g["token"].kind_str = ["should_not_use"]
    g["token"].num_nodes = 1
    torch.save(g, hetero_dir / "both.pt")

    out_dir = tmp_path / "embeds"

    class DummyTok:
        def __call__(self, texts, *args, **kwargs):
            ids = torch.tensor([[len(t)] for t in texts], dtype=torch.long)
            mask = torch.ones_like(ids)
            return {"input_ids": ids, "attention_mask": mask}

    class DummyAutoTok:
        @staticmethod
        def from_pretrained(name):
            return DummyTok()

    import src.models.llm_embed as llm_embed

    monkeypatch.setattr(llm_embed, "AutoTokenizer", DummyAutoTok)

    encoder = DummyEncoder()
    embed_corpus(encoder, hetero_dir=hetero_dir, out_dir=out_dir)

    feat = load_tensor("both", out_dir)

    assert feat.tolist() == [[3]]


def test_embed_corpus_none_zero(tmp_path, monkeypatch):
    hetero_dir = tmp_path / "hetero"
    hetero_dir.mkdir()

    g = HeteroData()
    g["token"].text = [None, "x", None]
    g["token"].num_nodes = 3
    torch.save(g, hetero_dir / "mix.pt")

    out_dir = tmp_path / "embeds"

    class DummyTok:
        def __call__(self, texts, *args, **kwargs):
            ids = torch.tensor([[len(t)] for t in texts], dtype=torch.long)
            mask = torch.ones_like(ids)
            return {"input_ids": ids, "attention_mask": mask}

    class DummyAutoTok:
        @staticmethod
        def from_pretrained(name):
            return DummyTok()

    import src.models.llm_embed as llm_embed

    monkeypatch.setattr(llm_embed, "AutoTokenizer", DummyAutoTok)

    encoder = DummyEncoder()
    embed_corpus(encoder, hetero_dir=hetero_dir, out_dir=out_dir)

    feat = load_tensor("mix", out_dir)

    assert feat.tolist() == [[0], [1], [0]]
