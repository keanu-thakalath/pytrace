from vector import Vector
from sphere import Sphere
from plane import Plane
from material import Material
from color import Color
from engine import Engine

camera = Vector(0, -.5, -7)
sphere1 = Sphere(Vector(-3, -.5, 0), 1.5, Material(Color(0, 255, 255), .1, .8, 100, 1))
sphere2 = Sphere(Vector(.2, 0, 1.5), 1, Material(Color(0, 255, 0), .1, .8, 100, 1))
sphere3 = Sphere(Vector(0, .4, -1.8), .6, Material(Color(255, 0, 0), .1, .8, 100, 1))
sphere4 = Sphere(Vector(3, -.5, 0), 1.5, Material(Color(255, 255, 255), .1, .8, 100, 1))

def get_floor_color(hit_pos):
    if (hit_pos.x1 % 2 < 1) != (hit_pos.x3 % 2 < 1):
        return Color(0, 0, 0)
    return Color(255, 255, 255)
floor = Plane(Vector(0, -1, 0), -1, Material(None, .1, .3, 500, 1, get_floor_color))

light = Vector(-10, -5, -5)
light_color = Color(255, 255, 255)

screen_width, screen_height = 3840, 2160

engine = Engine(camera, [sphere1, sphere2, sphere3, sphere4, floor], [light], [light_color], screen_width, screen_height)
print(f'rendered in {engine.render()[1]} seconds')
engine.show_rendered_image()
engine.save_rendered_image('image.png')
