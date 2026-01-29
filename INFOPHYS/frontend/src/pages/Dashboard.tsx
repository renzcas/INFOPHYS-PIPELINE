import React, { useEffect, useState } from "react";
import { connectTelemetry } from "../api/telemetry";

import ParticlesPanel from "../components/ParticlesPanel";
import FieldsPanel from "../components/FieldsPanel";
import GeometryPanel from "../components/GeometryPanel";
import SynapsesPanel from "../components/SynapsesPanel";
import AgentPanel from "../components/AgentPanel";
import WorldPanel from "../components/WorldPanel";

export default function Dashboard() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    const ws = connectTelemetry((event) => setData(event));
    return () => ws.close();
  }, []);

  if (!data) return <div>Waiting for telemetry…</div>;

  return (
    <div className="grid">
      <ParticlesPanel h={data.particles.h_t} />
      <FieldsPanel phi={data.fields.phi_t} />
      <GeometryPanel z={data.geometry.z_t} />
      <SynapsesPanel deltaW={data.synapses.delta_W} />
      <AgentPanel action={data.agent.action} ret={data.agent.return} />
      <WorldPanel reward={data.world.reward} done={data.world.done} />
    </div>
  );
}