import torch
import torch.nn as nn

class SynapseDynamics(nn.Module):
    """
    Simple STDP-like synaptic update:
        ΔW = η * (h_t ⊗ h_t - W)
    Tracks:
        - synaptic weight matrix W
        - plasticity level (mean absolute ΔW)
    """

    def __init__(self, dim=16, eta=0.01):
        super().__init__()
        self.dim = dim
        self.eta = eta

        # Synaptic weight matrix
        self.W = nn.Parameter(torch.randn(dim, dim) * 0.1)

    def forward(self, h_t: torch.Tensor):
        # Outer product h_t ⊗ h_t
        hebb = torch.outer(h_t, h_t)

        # STDP-like update
        delta_W = self.eta * (hebb - self.W)

        # Apply update
        self.W.data += delta_W.detach()

        # Plasticity metric
        plasticity_level = delta_W.abs().mean().item()

        return delta_W, plasticity_level