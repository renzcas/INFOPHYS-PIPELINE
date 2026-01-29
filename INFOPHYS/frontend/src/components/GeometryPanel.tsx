export default function GeometryPanel({ z }) {
  return (
    <div className="panel">
      <h3>Geometry — Embeddings</h3>
      <pre>{JSON.stringify(z.slice(0, 3), null, 2)}</pre>
    </div>
  );
}