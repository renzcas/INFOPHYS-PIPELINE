export function connectTelemetry(onEvent: (data: any) => void) {
  const ws = new WebSocket("ws://localhost:8000/telemetry/stream");

  ws.onmessage = (msg) => {
    const data = JSON.parse(msg.data);
    onEvent(data);
  };

  return ws;
}