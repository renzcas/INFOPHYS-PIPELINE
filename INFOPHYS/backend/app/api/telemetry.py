from fastapi import APIRouter, WebSocket
from app.core.telemetry_bus import bus
from app.api.models import TelemetryEvent

router = APIRouter()

@router.websocket("/stream")
async def telemetry_stream(ws: WebSocket):
    await ws.accept()
    queue = bus.subscribe()

    try:
        while True:
            event = await queue.get()
            model = TelemetryEvent(**event)
            await ws.send_json(model.dict())
    except Exception:
        bus.unsubscribe(queue)