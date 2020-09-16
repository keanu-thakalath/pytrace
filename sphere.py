class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        sphere2ray = ray.origin - self.center
        b = 2 * ray.dir.dot(sphere2ray)
        c = sphere2ray.dot(sphere2ray) - self.radius ** 2
        discriminant = b ** 2 - 4 * c
        if discriminant < 0:
            return None, None, None

        t = -(b + discriminant ** .5) / 2
        if t < 0:
            return None, None, None

        hit_pos = ray.get_value(t)
        normal = self.get_normal(hit_pos)
        return t, hit_pos, normal

    def get_normal(self, hit_pos):
        return (hit_pos - self.center).norm()