from fastapi import FastAPI
from engine.registry import OrganRegistry
from engine.pipeline import Pipeline

app = FastAPI(title="INFOPHYS Cockpit")

registry = OrganRegistry()
pipeline = Pipeline(registry)

@app.get("/step")
def step_endpoint():
    mass = 1.0
    velocity = 2.0
    height = 1.0
    prediction_error = 0.3
    signal = [0.0] * 128  # placeholder; can be real input later

    data = pipeline.step(mass, velocity, height, prediction_error, signal)
    return data