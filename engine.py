import numpy as np
from PIL import Image
from ray import Ray
from vector import Vector
from timer import timer

class Engine:
    def __init__(self, camera, objects, lights, light_colors, width, height):
        self.x1_max = 1
        self.x2_max = height / width
        self.x1_step = 2 * self.x1_max / (width - 1)
        self.x2_step = 2 * self.x2_max / (height - 1)
        self.im_arr = np.zeros((height, width, 3), dtype='uint8')
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.light_colors = light_colors
        self.width = width
        self.height = height

    @timer
    def render(self):
        print(f'rendering {len(self.objects)} objects and {len(self.lights)} lights on screen size {self.width}, {self.height}')
        for i in range(self.height):
            for j in range(self.width):
                x1 = j * self.x1_step - self.x1_max
                x2 = i * self.x2_step - self.x2_max
                ray = Ray(self.camera, Vector(x1, x2, 1))
                min_dist, rendered_color = 100, None
                for obj in self.objects:
                    dist, hit_pos, normal = obj.intersects(ray)
                    if dist:
                        if dist < min_dist:
                            color = self.trace_ray(ray, hit_pos, normal, obj)
                            min_dist = dist
                            rendered_color = color
                if rendered_color:
                    self.im_arr[i][j] = (rendered_color.r, rendered_color.g, rendered_color.b)
            print(f'done rendering row {i}')
        print('done rendering scene')
        self.im = Image.fromarray(self.im_arr, 'RGB')

    def trace_ray(self, ray, hit_pos, normal, obj):
        color = obj.material.ambient * obj.material.get_color_at(hit_pos)
        for light_num in range(len(self.lights)):
            light = self.lights[light_num]
            light_color = self.light_colors[light_num]
            hit2light = light - hit_pos
            dist_to_light = hit2light.dot(hit2light)
            hit2light = hit2light.norm()
            in_shadow = False
            for other_obj in self.objects:
                if other_obj is not obj:
                    dist_to_other_obj = other_obj.intersects(Ray(hit_pos, hit2light))[0]
                    if dist_to_other_obj:
                        if dist_to_other_obj ** 2 < dist_to_light:
                            in_shadow = True
            if not in_shadow:
                if obj.material.diffuse > 0:
                    light_normal_dot = hit2light.dot(normal)
                    # light vector must be facing the same direction as the normal vector
                    if light_normal_dot > 0:
                        color = color + light_normal_dot * obj.material.diffuse * obj.material.get_color_at(hit_pos)

                halfway = (hit2light - ray.dir).norm()
                halfway_normal_dot = halfway.dot(normal)
                if halfway_normal_dot > 0:
                    color = color + halfway_normal_dot ** obj.material.specular * light_color

        if obj.material.reflect > 0:
            reflection_angle = -normal.dot(ray.dir)
            reflected_ray = Ray(hit_pos, ray.dir + 2 * reflection_angle * normal)

            min_dist, reflected_color = 100, None
            for other_obj in self.objects:
                if other_obj is not obj:
                    dist, hit_pos, normal = other_obj.intersects(reflected_ray)
                    if dist:
                        if dist < min_dist:
                            reflected_color = self.trace_ray(reflected_ray, hit_pos, normal, other_obj)
                            min_dist = dist
            if reflected_color:
                color = color + obj.material.reflect * reflected_color
        return color


    def show_rendered_image(self):
        self.im.show()

    def save_rendered_image(self, filename):
        self.im.save(filename)
