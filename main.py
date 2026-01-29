from engine.registry import OrganRegistry
from engine.pipeline import Pipeline
from cockpit.dashboard import render_step
import numpy as np

def main():
    registry = OrganRegistry()
    pipeline = Pipeline(registry)

    for _ in range(5):
        mass = 1.0
        velocity = 2.0
        height = 1.0
        prediction_error = 0.3
        signal = np.sin(np.linspace(0, 2 * np.pi, 128))

        step_data = pipeline.step(
            mass, velocity, height, prediction_error, signal
        )
        render_step(step_data)

if __name__ == "__main__":
    main()