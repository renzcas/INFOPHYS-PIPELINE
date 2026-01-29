import math
import random
import time

class STDPOrgan:
    def __init__(self):
        self.v = 0.0
        self.threshold = 1.0
        self.last_spike = None
        self.weights = [random.uniform(0.1, 0.5) for _ in range(32)]
        self.learning_rate = 0.01

    def step(self, signal):
        # integrate membrane potential
        self.v += sum(s * w for s, w in zip(signal[:32], self.weights))

        spike = False
        if self.v >= self.threshold:
            spike = True
            self.v = 0.0
            now = time.time()

            if self.last_spike is not None:
                dt = now - self.last_spike
                # STDP: strengthen if close in time
                for i in range(len(self.weights)):
                    self.weights[i] += self.learning_rate * math.exp(-dt)
            self.last_spike = now

        return {
            "membrane": self.v,
            "spike": spike,
            "weights": self.weights[:8]  # preview
        }