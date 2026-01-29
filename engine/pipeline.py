import time

class Pipeline:
    def __init__(self, registry):
        self.registry = registry
        self.last_time = time.time()

    def step(self, mass, velocity, height, prediction_error, signal):
        now = time.time()
        dt = now - self.last_time
        self.last_time = now

        out = {
            "t": now,
            "dt": dt,
        }

        # Physics organ
        if "physics" in self.registry.organs:
            phys = self.registry.organs["physics"].step(mass, velocity, height)
            out.update(phys)

        # Compute organ
        if "compute" in self.registry.organs:
            comp = self.registry.organs["compute"].step(prediction_error)
            out.update(comp)

        # Mind organ
        if "mind" in self.registry.organs:
            mind = self.registry.organs["mind"].step(signal)
            out.update(mind)

        # STDP organ
        if "stdp" in self.registry.organs:
            stdp = self.registry.organs["stdp"].step(signal)
            out["stdp"] = stdp

        return out