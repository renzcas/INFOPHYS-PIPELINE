import math
import numpy as np

class AttentionOrgan:
    def __init__(self):
        self.dim = 16
        self.state = np.zeros(self.dim)

    def step(self, signal):
        x = np.array(signal[:self.dim])
        density = np.linalg.norm(x)
        flow = np.gradient(x)
        energy = np.sum(x**2)

        # attention = normalized energy flow
        att = flow / (np.linalg.norm(flow) + 1e-6)

        self.state = 0.9*self.state + 0.1*att

        return {
            "density": float(density),
            "energy": float(energy),
            "attention_vector": self.state.tolist()
        }