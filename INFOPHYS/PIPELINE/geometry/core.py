import torch
import torch.nn as nn

class GeometryDynamics(nn.Module):
    """
    Embed particle state h_t into a low-dimensional manifold z_t
    and track a simple manifold spread.

        z_t = W h_t
        spread = ||z_t||^2
    """

    def __init__(self, input_dim=16, latent_dim=2):
        super().__init__()
        self.input_dim = input_dim
        self.latent_dim = latent_dim

        self.linear = nn.Linear(input_dim, latent_dim)

    def forward(self, h_t: torch.Tensor):
        # h_t: (dim,)
        z = self.linear(h_t)          # (latent_dim,)
        spread = (z**2).sum().item()  # simple scalar curvature proxy

        return z, spread
    