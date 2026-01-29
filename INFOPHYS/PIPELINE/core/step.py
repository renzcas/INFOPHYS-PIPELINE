from PIPELINE.fields import FieldDynamics
from PIPELINE.particles import ParticleDynamics
from PIPELINE.geometry import GeometryDynamics
from PIPELINE.synapses import SynapseDynamics
from PIPELINE.agent import AgentDynamics
from PIPELINE.discriminant import DiscriminantDetector

import torch

class PipelineStep:
    def __init__(self):
        self.fields = FieldDynamics()
        self.particles = ParticleDynamics()
        self.geometry = GeometryDynamics(input_dim=self.particles.dim, latent_dim=2)
        self.agent = AgentDynamics(dim=self.particles.dim)
        self.discriminant = DiscriminantDetector()

    def step(self, t):
        # Update fields
        phi_t = self.fields()

        # Update particles
        h_t, entropy = self.particles()

        # Geometry: embed h_t into manifold
        if not isinstance(h_t, torch.Tensor):
            h_t = torch.tensor(h_t)
        z_t, spread = self.geometry(h_t)
        delta_W, plasticity = self.synapses(h_t)
        agent_out = self.agent(h_t)
        disc_score, regime_shift = self.discriminant(
            entropy,
            spread,
            plasticity,
            agent_out["action"]
        )


        return {
            "t": t,
            "fields": phi_t.detach().cpu().tolist(),
            "particles": {
                "h_t": h_t.detach().cpu().tolist(),
                "attention_entropy": entropy
            },
            "geometry": {
                "z_t": z_t.detach().cpu().tolist(),
                "manifold_spread": spread
            
            "synapses": {
                "delta_W": delta_W.detach().cpu().tolist(),
                "plasticity_level": plasticity
            }

            "agent": {
                "action": agent_out["action"],
                "log_prob": agent_out["log_prob"],
                    "estimated_return": agent_out["estimated_return"]
            }

            self.agent = AgentDynamics(dim=self.particles.dim)
            
            }

            "discriminant": {
                "score": disc_score,
                "regime_shift": regime_shift
            }
        }