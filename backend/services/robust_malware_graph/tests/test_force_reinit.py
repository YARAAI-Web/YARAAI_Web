import pytest

pytest.importorskip("torch")
pytest.importorskip("torch_geometric")

import torch
from src.models.gnn.encoder import RGCNEncoder
from src.common.utils import filter_state_dict


def test_force_reinit_filters_mismatched(tmp_path):
    # encoder trained with feature dim 4
    enc_old = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 4},
        hidden_dim=4,
        num_layers=1,
        out_dim=8,
    )
    ckpt = {"model": enc_old.state_dict()}
    path = tmp_path / "enc.pt"
    torch.save(ckpt, path)

    # new dataset requires feature dim 6
    new_enc = RGCNEncoder(
        metadata=(["n"], [("n", "r0", "n")]),
        in_dims={"n": 6},
        hidden_dim=4,
        num_layers=1,
        out_dim=8,
    )
    orig_weight = new_enc.input_proj["n"].weight.clone()

    state = ckpt["model"]
    filtered = filter_state_dict(new_enc, state)
    new_enc.load_state_dict(filtered, strict=False)

    # mismatched weight should remain unchanged
    assert torch.allclose(new_enc.input_proj["n"].weight, orig_weight)

