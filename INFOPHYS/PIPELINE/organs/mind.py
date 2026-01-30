from core.energy import free_energy

class MindOrgan:
    def attention_from_error(self, prediction_error: float):
        fe = free_energy(prediction_error)
        attention_gain = 1.0 / (1.0 + fe)
        return {"free_energy": fe, "attention_gain": attention_gain}