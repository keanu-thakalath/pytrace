class Vector:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def dot(self, other):
        return self.x1 * other.x1 + self.x2 * other.x2 + self.x3 * other.x3

    def norm(self):
        return self / self.dot(self) ** .5

    def __mul__(self, other):
        return Vector(other * self.x1, other * self.x2, other * self.x3)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return 1 / other * self

    def __add__(self, other):
        return Vector(self.x1 + other.x1, self.x2 + other.x2, self.x3 + other.x3)

    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        return Vector(-self.x1, -self.x2, -self.x3)

    def __repr__(self):
        return f'<{self.x1}, {self.x2}, {self.x3}>'