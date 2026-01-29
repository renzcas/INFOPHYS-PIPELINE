from fastapi import FastAPI
from pydantic import BaseModel
from engine.registry import OrganRegistry
from engine.pipeline import Pipeline
import numpy as np

app = FastAPI(title="INFOPHYS Pipeline")

registry = OrganRegistry()
pipeline = Pipeline(registry)

class StepInput(BaseModel):
    mass: float = 1.0
    velocity: float = 2.0
    height: float = 1.0
    prediction_error: float = 0.3
    signal_points: int = 128

@app.post("/step")
def step(input_data: StepInput):
    x = np.linspace(0, 2 * np.pi, input_data.signal_points)
    signal = np.sin(x)

    step_data = pipeline.step(
        input_data.mass,
        input_data.velocity,
        input_data.height,
        input_data.prediction_error,
        signal,
    )
    return step_data