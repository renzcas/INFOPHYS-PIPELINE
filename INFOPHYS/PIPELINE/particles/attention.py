import torch
import torch.nn as nn
import math


class ParticleAttention(nn.Module):
    def __init__(self, dim_in, dim_hidden, n_heads=4):
        super().__init__()
        self.dim_in = dim_in
        self.dim_hidden = dim_hidden
        self.n_heads = n_heads

        self.q_proj = nn.Linear(dim_in, dim_hidden)
        self.k_proj = nn.Linear(dim_in, dim_hidden)
        self.v_proj = nn.Linear(dim_in, dim_hidden)
        self.out_proj = nn.Linear(dim_hidden, dim_hidden)

    def forward(self, x, context=None):
        # x: (batch, seq, dim_in)
        Q = self.q_proj(x)
        K = self.k_proj(x)
        V = self.v_proj(x)

        d_k = Q.size(-1)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
        attn = torch.softmax(scores, dim=-1)
        h = torch.matmul(attn, V)
        h = self.out_proj(h)
        return h