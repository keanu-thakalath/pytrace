from color import Color
class Plane:
    def __init__(self, normal, d, material):
        self.normal = normal.norm()
        self.d = d
        self.material = material

    def intersects(self, ray):
        t = (self.d - self.normal.dot(ray.origin)) / self.normal.dot(ray.dir)
        if t < 0:
            return None, None, None
        
        return t, ray.get_value(t), self.normal