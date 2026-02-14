from PIPELINE.core.step import PipelineStep
from INFOPHYS.backend.app.core.telemetry_bus import bus
import asyncio

class Trainer:
    def __init__(self, horizon=100):
        self.horizon = horizon
        self.stepper = PipelineStep()

    async def train(self):
        for t in range(self.horizon):
            out = self.stepper.step(t)

            await bus.publish({
                "t": t,
                "run_id": "fields_particles_geometry_demo",

                "particles": {
                    "h_t": out["particles"]["h_t"],
                    "attention_entropy": out["particles"]["attention_entropy"]
                },

                "fields": {
                    "phi_t": out["fields"],
                    "energy": 0.0
                },

                "geometry": {
                    "z_t": out["geometry"]["z_t"],
                    "manifold_spread": out["geometry"]["manifold_spread"]
                },

                "synapses": {
                    "delta_W": out["synapses"]["delta_W"],
                    "plasticity_level": out["synapses"]["plasticity_level"]
                },
                "agent": {
                    "action": out["agent"]["action"],
                    "log_prob": out["agent"]["log_prob"],
                    "estimated_return": out["agent"]["estimated_return"]
                },
                "world": {"reward": 0.0, "done": False},
                "discriminant": {
                    "score": out["discriminant"]["score"],
                    "regime_shift": out["discriminant"]["regime_shift"]
                }
                   "grokking": {
                        "signal": out["grokking 
                })

        return {"status": "training complete"}