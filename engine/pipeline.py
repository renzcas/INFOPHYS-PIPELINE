from core.time import now, dt
from core.lagrangian import action

class Pipeline:
    def __init__(self, registry):
        self.registry = registry
        self.last_t = now()
        self.l_history = []

    def step(self, mass, velocity, height, prediction_error, signal):
        t_now = now()
        delta_t = dt(self.last_t)
        self.last_t = t_now

        physics = self.registry.get("physics").compute_state_energy(
            mass, velocity, height
        )
        mind = self.registry.get("mind").attention_from_error(prediction_error)
        compute = self.registry.get("compute").analyze_signal(signal)

        self.l_history.append(physics["L"])
        total_action = action(self.l_history, delta_t)

        return {
            "time": t_now,
            "dt": delta_t,
            "physics": physics,
            "mind": mind,
            "compute": compute,
            "action": total_action,
        }