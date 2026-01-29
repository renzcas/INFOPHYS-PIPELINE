class OrganRegistry:
    def __init__(self):
        self.organs = {}

    def register(self, name, organ):
        """Register an organ instance under a given name."""
        self.organs[name] = organ

    def get(self, name):
        """Retrieve an organ by name, or None if missing."""
        return self.organs.get(name)