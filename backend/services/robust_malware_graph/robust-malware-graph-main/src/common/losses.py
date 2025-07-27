import torch
import torch.nn as nn
import torch.nn.functional as F

class FocalLoss(nn.Module):
    """
    Focal Loss for binary classification.
    
    This loss was originally proposed in "Focal Loss for Dense Object Detection"
    (https://arxiv.org/abs/1708.02002). It is designed to address class
    imbalance by down-weighting easy, well-classified examples and focusing
    training on hard-to-classify examples.

    Parameters
    ----------
    alpha : float, default=0.25
        Weighting factor for the positive class. Acts as a way to directly
        balance the importance of positive/negative examples.
    gamma : float, default=2.0
        Focusing parameter. A higher gamma value increases the rate at which
        easy examples are down-weighted.
    reduction : str, default='mean'
        Specifies the reduction to apply to the output: 'none' | 'mean' | 'sum'.
    """
    def __init__(self, alpha: float = 0.25, gamma: float = 2.0, reduction: str = 'mean'):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """
        Parameters
        ----------
        logits : torch.Tensor
            The raw, un-normalized output from the model (before sigmoid).
        targets : torch.Tensor
            The ground truth labels (0 or 1).
        """
        # Use BCEWithLogitsLoss for numerical stability
        bce_loss = F.binary_cross_entropy_with_logits(logits, targets, reduction='none')
        
        # Calculate p_t, the probability of the ground truth class
        p = torch.sigmoid(logits)
        p_t = p * targets + (1 - p) * (1 - targets)
        
        # This is the core of Focal Loss: (1 - p_t)^gamma
        loss_factor = (1 - p_t).pow(self.gamma)
        
        # Apply the alpha balancing factor
        alpha_t = self.alpha * targets + (1 - self.alpha) * (1 - targets)
        
        # The final focal loss
        focal_loss = alpha_t * loss_factor * bce_loss
        
        if self.reduction == 'mean':
            return focal_loss.mean()
        elif self.reduction == 'sum':
            return focal_loss.sum()
        else: # 'none'
            return focal_loss
