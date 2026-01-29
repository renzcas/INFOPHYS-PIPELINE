from fastapi import APIRouter, WebSocket
from app.api.models import TelemetryEvent
from app.core.pipeline_core.telemetry_bus import TelemetryBus

router = APIRouter()
bus = TelemetryBus()

@router.websocket("/stream")
async def telemetry_stream(ws: WebSocket):
    await ws.accept()

    # Subscribe this websocket to the telemetry bus
    queue = bus.subscribe()

    try:
        while True:
            event = await queue.get()
            model = TelemetryEvent(**event)
            await ws.send_json(event)
    except Exception:
        bus.unsubscribe(queue)