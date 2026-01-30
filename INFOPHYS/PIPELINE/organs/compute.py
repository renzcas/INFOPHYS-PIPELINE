from core.frequency import dominant_frequency

class ComputeOrgan:
    def analyze_signal(self, signal):
        freq, power = dominant_frequency(signal)
        return {"dominant_freq": freq, "power": power}