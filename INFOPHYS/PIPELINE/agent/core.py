import torch
import torch.nn as nn
import torch.nn.functional as F

class AgentDynamics(nn.Module):
    """
    Minimal agent:
      - Computes an action a_t from particle state h_t
      - Computes a simple Lagrangian L = K - V
      - Euler–Lagrange update on an internal momentum p_t
    """

    def __init__(self, dim=16, action_dim=1):
        super().__init__()
        self.dim = dim
        self.action_dim = action_dim

        # Policy network
        self.policy = nn.Linear(dim, action_dim)

        # Internal momentum state
        self.p_t = torch.zeros(action_dim)

    def forward(self, h_t: torch.Tensor):
        # Policy: action distribution
        logits = self.policy(h_t)
        action = torch.tanh(logits)

        # Log prob (treat logits as Gaussian mean)
        log_prob = -0.5 * (logits**2).sum().item()

        # Simple Lagrangian: K - V
        K = 0.5 * (action**2).sum()
        V = 0.5 * (h_t**2).sum()
        L = K - V

        # Euler–Lagrange update on momentum
        self.p_t = self.p_t + action.detach()

        # Estimated return (placeholder)
        estimated_return = L.item()

        return {
            "action": action.detach().cpu().tolist(),
            "log_prob": log_prob,
            "estimated_return": estimated_return
        }