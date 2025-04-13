import math

class vector:
    def __init__(self, *components):
        self.components=tuple(components)
    def __repr__(self):
        return f"Vector{self.components}"
