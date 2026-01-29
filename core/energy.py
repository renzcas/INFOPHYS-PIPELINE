def kinetic(mass: float, velocity: float) -> float:
    return 0.5 * mass * velocity**2

def potential(mass: float, height: float, g: float = 9.81) -> float:
    return mass * g * height

def free_energy(prediction_error: float, temperature: float = 1.0) -> float:
    return prediction_error**2 / (2 * temperature)