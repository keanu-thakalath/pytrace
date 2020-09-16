class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.norm()

    def norm(self):
        max_color = max(self.r, self.g, self.b)
        if max_color > 255:
            norm_coefficient = 255 / max_color
            self.r = norm_coefficient * self.r
            self.g = norm_coefficient * self.g
            self.b = norm_coefficient * self.b

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __rmul__(self, other):
        return Color(other * self.r, other * self.g, other * self.b)

    def __repr__(self):
        return f'Color({self.r}, {self.g}, {self.b})'
