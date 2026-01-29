# server.py
import asyncio
import json
import time
from typing import Dict, Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from INFOPHYS.PIPELINE.registry import OrganRegistry
from INFOPHYS.PIPELINE.pipeline import Pipeline
from INFOPHYS.PIPELINE.organs.physics import PhysicsOrgan
from INFOPHYS.PIPELINE.organs.compute import ComputeOrgan
from INFOPHYS.PIPELINE.organs.mind import MindOrgan
from INFOPHYS.PIPELINE.organs.stdp import STDPOrgan
from INFOPHYS.PIPELINE.organs.attention import AttentionOrgan
from INFOPHYS.PIPELINE.organs.symbolic import SymbolicOrgan
from INFOPHYS.PIPELINE.organs.decision import DecisionOrgan

import numpy as np

# ---------------- Organism boot ----------------

def build_organism():
    registry = OrganRegistry()
    registry.register("physics", PhysicsOrgan())
    registry.register("compute", ComputeOrgan())
    registry.register("mind", MindOrgan())
    registry.register("stdp", STDPOrgan())
    registry.register("attention", AttentionOrgan())
    registry.register("symbolic", SymbolicOrgan())
    registry.register("decision", DecisionOrgan())
    pipe = Pipeline(registry)
    return registry, pipe

registry, pipeline = build_organism()
last_state: Dict[str, Any] = {}

# ---------------- FastAPI app ----------------

app = FastAPI(title="Organism Cockpit")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class StepRequest(BaseModel):
    mass: float = 1.0
    velocity: float = 0.0
    height: float = 1.0
    prediction_error: float = 0.1
    signal_dim: int = 16

@app.post("/step")
def step(req: StepRequest):
    global last_state
    signal = np.random.randn(req.signal_dim).tolist()
    out = pipeline.step(
        mass=req.mass,
        velocity=req.velocity,
        height=req.height,
        prediction_error=req.prediction_error,
        signal=signal,
    )
    last_state = out
    return out

@app.get("/state")
def get_state():
    return last_state

@app.get("/organ/{name}")
def get_organ(name: str):
    organ = registry.organs.get(name)
    if organ is None:
        return {"error": "organ not found"}
    return {"name": name, "type": organ.__class__.__name__}

# ---------------- WebSocket telemetry ----------------

class ConnectionManager:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active:
            self.active.remove(websocket)

    async def broadcast(self, message: str):
        for ws in list(self.active):
            try:
                await ws.send_text(message)
            except WebSocketDisconnect:
                self.disconnect(ws)

manager = ConnectionManager()

@app.websocket("/ws/telemetry")
async def websocket_telemetry(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            signal = np.random.randn(16).tolist()
            out = pipeline.step(
                mass=1.0,
                velocity=0.0,
                height=1.0,
                prediction_error=0.1,
                signal=signal,
            )
            global last_state
            last_state = out

            await websocket.send_text(json.dumps(out))
            await asyncio.sleep(0.05)
    except WebSocketDisconnect:
        manager.disconnect(websocket)