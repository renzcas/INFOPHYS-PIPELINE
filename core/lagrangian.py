def lagrangian(T: float, V: float) -> float:
    return T - V

def action(l_values, dt: float) -> float:
    return sum(l_values) * dt