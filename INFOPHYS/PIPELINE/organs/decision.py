import math

class DecisionOrgan:
    def step(self, lagrangian, dt):
        # least-action principle
        action = lagrangian * dt

        # decision = sign of action gradient
        decision = -1 if action > 0 else 1

        return {
            "action_value": action,
            "decision": decision
        }