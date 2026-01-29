export default function FieldsPanel({ phi }) {
  return (
    <div className="panel">
      <h3>Fields — Diffusion</h3>
      <pre>{JSON.stringify(phi.slice(0, 3), null, 2)}</pre>
    </div>
  );
}