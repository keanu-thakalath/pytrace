class Material:
    def __init__(self, color, ambient, diffuse, specular, reflect, get_color_at=None):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflect = reflect
        self.get_color_at = get_color_at or (lambda hit_pos: color)