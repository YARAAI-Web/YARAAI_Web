import importlib
import pytest

pytest.importorskip("pandas")
pytest.importorskip("torch")

import pandas as pd
import torch
import src.models.gnn.res_wrapper as res_wrapper


def test_optimize_multiworker_updates_params(tmp_path, monkeypatch):
    csv = tmp_path / "meta.csv"
    pd.DataFrame(
        {"sha256": ["a", "b"], "label": [1, 1], "filename": ["a.bin", "b.bin"]}
    ).to_csv(csv, index=False)

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

    monkeypatch.setenv("RMG_TEST_EVAL_SINGLE", "tests.helpers:fake_eval")

    opt_path = tmp_path / "opt.pkl"
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
            "--precomputed-saliency-dir",
            str(sal_dir),
            "--batch-size",
            "2",
            "--save-optimizer",
            str(opt_path),
        ]
    )

    state = torch.load(opt_path)
    assert any(t.abs().sum() > 0 for t in state["logits"].values())
