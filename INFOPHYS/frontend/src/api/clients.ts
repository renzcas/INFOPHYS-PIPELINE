export async function fetchLatestTelemetry() {
  const res = await fetch("http://localhost:8000/telemetry/latest");
  return res.json();
}