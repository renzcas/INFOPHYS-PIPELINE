from organs.physics import PhysicsOrgan
from organs.mind import MindOrgan
from organs.compute import ComputeOrgan

class OrganRegistry:
    def __init__(self):
        self.organs = {
            "physics": PhysicsOrgan(),
            "mind": MindOrgan(),
            "compute": ComputeOrgan(),
        }

    def get(self, name: str):
        return self.organs[name]