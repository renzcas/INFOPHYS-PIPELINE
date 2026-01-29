from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/latest")
def latest_step():
    # TODO: pull from in-memory buffer or DB
    sample = {
  "t": 12,
  "run_id": "abc123",
  "obs": [...],
  "particles": {
    "h_t": [...],
    "attention_entropy": 1.23
  },
  "fields": {
    "phi_t": [...],
    "energy": 0.87
  },
  "geometry": {
    "z_t": [...],
    "manifold_spread": 2.1
  },
  "synapses": {
    "delta_W_norm": 0.05
  },
  "agent": {
    "action": [0.1, -0.2],
    "log_prob": -0.34,
    "estimated_return": 3.7
  },
  "world": {
    "reward": 1.0,
    "done": false
  }
}
    return JSONResponse(sample)