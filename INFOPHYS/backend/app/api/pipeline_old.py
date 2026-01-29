from fastapi import APIRouter
from pydantic import BaseModel

from app.core.pipeline_core import build_pipeline, train_once

router = APIRouter()

class TrainRequest(BaseModel):
    episodes: int = 1
    horizon: int = 100

@router.post("/train")
def train(req: TrainRequest):
    pipeline = build_pipeline({})
    stats = train_once(pipeline, episodes=req.episodes, horizon=req.horizon)
    return {"status": "ok", "stats": stats}