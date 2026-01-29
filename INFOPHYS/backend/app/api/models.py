from pydantic import BaseModel
from typing import List, Optional

class ParticlesTelemetry(BaseModel):
    h_t: List[List[float]]
    attention_entropy: Optional[float] = None

class FieldsTelemetry(BaseModel):
    phi_t: List[List[float]]
    energy: Optional[float] = None

class GeometryTelemetry(BaseModel):
    z_t: List[List[float]]
    manifold_spread: Optional[float] = None

class SynapsesTelemetry(BaseModel):
    delta_W: Optional[float] = None
    plasticity_level: Optional[float] = None

class AgentTelemetry(BaseModel):
    action: List[float]
    log_prob: Optional[float] = None
    estimated_return: Optional[float] = None

class WorldTelemetry(BaseModel):
    reward: float
    done: bool

class TelemetryEvent(BaseModel):
    t: int
    run_id: str
    particles: ParticlesTelemetry
    fields: FieldsTelemetry
    geometry: GeometryTelemetry
    synapses: SynapsesTelemetry
    agent: AgentTelemetry
    world: WorldTelemetry