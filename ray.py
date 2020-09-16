class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.dir = direction.norm()

    def get_value(self, t):
        return self.origin + t * self.dir