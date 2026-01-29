export default function SynapsesPanel({ deltaW }) {
  return (
    <div className="panel">
      <h3>Synapses — STDP</h3>
      <p>ΔW norm: {deltaW.toFixed(4)}</p>
    </div>
  );
}