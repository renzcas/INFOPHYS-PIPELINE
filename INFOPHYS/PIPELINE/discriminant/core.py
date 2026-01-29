import torch

class DiscriminantDetector:
    """
    Detects regime shifts by combining:
      - particle entropy
      - geometry spread
      - synaptic plasticity
      - agent action magnitude

    Outputs:
      - discriminant score
      - regime_shift (bool)
    """

    def __init__(self, threshold=1.5):
        self.threshold = threshold

    def __call__(self, entropy, spread, plasticity, action):
        # action magnitude
        if isinstance(action, list):
            action = torch.tensor(action)
        action_mag = action.abs().mean().item()

        # discriminant score
        score = entropy + spread + plasticity + action_mag

        # regime shift detection
        regime_shift = score > self.threshold

        return score, regime_shift