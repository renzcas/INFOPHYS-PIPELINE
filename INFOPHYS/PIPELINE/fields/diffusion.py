# fields/diffusion.py

import torch
import torch.nn as nn
import torch.nn.functional as F


class FieldDiffusion(nn.Module):
    """
    Implements:
        ∂φ/∂t = D ∇²φ - ∂U(φ)/∂φ

    Discretized:
        φ_{t+1} = φ_t + dt * ( D * Laplacian(φ_t) - dU_dphi(φ_t) )
    """

    def __init__(self, dim, D=0.1, dt=0.1, learn_potential=True):
        super().__init__()
        self.D = D
        self.dt = dt

        # Optional learnable potential U(φ)
        if learn_potential:
            self.potential = nn.Sequential(
                nn.Linear(dim, dim),
                nn.Tanh(),
                nn.Linear(dim, dim)
            )
        else:
            self.potential = None

    def laplacian(self, phi):
        """
        Discrete Laplacian using 2nd‑order finite differences.
        Assumes phi shape: (batch, seq, dim)
        """
        # 1D Laplacian along sequence dimension
        # pad left/right with replication
        phi_pad = F.pad(phi, (0, 0, 1, 1), mode="replicate")

        # φ_{i+1} - 2φ_i + φ_{i-1}
        lap = phi_pad[:, 2:, :] - 2 * phi_pad[:, 1:-1, :] + phi_pad[:, :-2, :]
        return lap

    def dU_dphi(self, phi):
        """
        Gradient of potential U(φ).
        If potential is learnable, compute ∂U/∂φ via autograd.
        Otherwise return zero.
        """
        if self.potential is None:
            return torch.zeros_like(phi)

        phi = phi.clone().detach().requires_grad_(True)
        U = self.potential(phi).sum()  # scalar potential energy
        grad = torch.autograd.grad(U, phi, create_graph=False)[0]
        return grad

    def forward(self, h_t, phi_prev=None):
        """
        h_t: input from attention layer
        phi_prev: previous field state (optional)
        """
        # Initialize φ_t from h_t if no previous field exists
        if phi_prev is None:
            phi_prev = h_t

        # Compute Laplacian
        lap = self.laplacian(phi_prev)

        # Compute potential gradient
        dU = self.dU_dphi(phi_prev)

        # PDE update
        phi_next = phi_prev + self.dt * (self.D * lap - dU)

        return phi_next