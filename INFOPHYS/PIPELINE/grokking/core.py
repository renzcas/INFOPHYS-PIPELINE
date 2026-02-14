class GrokkingMonitor:
    """
    Detects grokking-like transitions by tracking:
      - entropy decay
      - plasticity stabilization
      - geometry curvature stabilization
      - discriminant score collapse
    """

    def __init__(self, window=20, threshold=0.3):
        self.window = window
        self.threshold = threshold
        self.history = []

    def __call__(self, entropy, plasticity, spread, disc_score):
        # Track combined signal
        signal = entropy + plasticity + spread + disc_score
        self.history.append(signal)

        if len(self.history) < self.window:
            return False, signal

        # Compare recent window to earlier window
        recent = sum(self.history[-self.window:]) / self.window
        earlier = sum(self.history[-2*self.window:-self.window]) / self.window

        grokking_event = (earlier - recent) > self.threshold

        return grokking_event, signal