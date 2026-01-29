export default function ParticlesPanel({ h }) {
  return (
    <div className="panel">
      <h3>Particles — Attention</h3>
      <pre>{JSON.stringify(h.slice(0, 3), null, 2)}</pre>
    </div>
  );
}