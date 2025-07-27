# edge-level smoothing
from .edge_smoothing import EdgeDropSmoothing

# differentiable mask via Gumbel-Softmax
from .gumbel_mask import GumbelMask

# attention-based gating (importance-weighted features)
from .attention_gate import AttentionGate

# residual connection + layer normalization
from .residual_norm import ResidualNorm

__all__ = [
    "EdgeDropSmoothing",
    "GumbelMask",
    "AttentionGate",
    "ResidualNorm",
]
