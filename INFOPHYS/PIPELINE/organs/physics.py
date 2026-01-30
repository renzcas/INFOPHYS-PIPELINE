from core.energy import kinetic, potential
from core.lagrangian import lagrangian

class PhysicsOrgan:
    def compute_state_energy(self, mass, velocity, height):
        T = kinetic(mass, velocity)
        V = potential(mass, height)
        L = lagrangian(T, V)
        return {"T": T, "V": V, "L": L}