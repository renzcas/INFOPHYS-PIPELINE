from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import pipeline

app = FastAPI(title="INFOPHYS PIPELINE API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pipeline.router, prefix="/pipeline", tags=["pipeline"])
app.include_router(telemetry_old_REST.router, prefix="/telemetry", tags=["telemetry"])