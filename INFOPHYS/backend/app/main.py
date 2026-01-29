from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from INFOPHYS.backend.app.api import pipeline, telemetry, legacy

app = FastAPI(title="INFOPHYS PIPELINE API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pipeline.router, prefix="/pipeline", tags=["pipeline"])
app.include_router(telemetry.router, prefix="/telemetry", tags=["telemetry"])
app.include_router(legacy.router, prefix="/legacy", tags=["legacy"])

@app.get("/")
def root():
    return {"status": "INFOPHYS backend online"}