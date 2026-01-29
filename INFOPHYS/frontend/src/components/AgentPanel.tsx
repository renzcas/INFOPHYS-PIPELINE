export default function AgentPanel({ action, ret }) {
  return (
    <div className="panel">
      <h3>Agent — Lagrangian Policy</h3>
      <p>Action: {JSON.stringify(action)}</p>
      <p>Return: {ret.toFixed(3)}</p>
    </div>
  );
}