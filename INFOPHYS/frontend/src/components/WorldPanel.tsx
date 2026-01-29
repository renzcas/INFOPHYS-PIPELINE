export default function WorldPanel({ reward, done }) {
  return (
    <div className="panel">
      <h3>World</h3>
      <p>Reward: {reward}</p>
      <p>Done: {String(done)}</p>
    </div>
  );
}