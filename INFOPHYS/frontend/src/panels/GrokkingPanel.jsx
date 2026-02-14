export default function GrokkingPanel({ data }) {
  const signal = data?.grokking?.signal ?? 0
  const event = data?.grokking?.event ?? false

  const entropy = data?.particles?.attention_entropy ?? 0
  const spread = data?.geometry?.manifold_spread ?? 0
  const plasticity = data?.synapses?.plasticity_level ?? 0
  const disc = data?.discriminant?.score ?? 0

  return (
    <div className="grokking-panel">
      <h2>Grokking Monitor</h2>

      <SignalChart value={signal} />

      <CollapseBars
        entropy={entropy}
        spread={spread}
        plasticity={plasticity}
        disc={disc}
      />

      {event && <GrokkingBanner />}
    </div>
  )
}