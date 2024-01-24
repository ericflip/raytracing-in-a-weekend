from color import Color, format
from point import Point
from ray import Ray
from tqdm import tqdm
from vec3 import Vec3


def hit_sphere(center: Vec3, radius: float, ray: Ray) -> bool:
    a = ray.direction.dot(ray.direction)
    b = 2 * ray.direction.dot((ray.origin - center))
    c = (ray.origin - center).dot((ray.origin - center)) - radius**2

    discriminant = b**2 - 4 * a * c

    return discriminant >= 0


def ray_color(ray: Ray):
    if hit_sphere(Point(0, 0, -1), 0.5, ray):
        return Color(1, 0, 0)

    unit_direction = ray.direction.unit_vec()
    a = 0.5 * (unit_direction.y + 1)

    return (1 - a) * Color(1, 1, 1) + a * Color(0.5, 0.7, 1)


if __name__ == "__main__":
    # image
    aspect_ratio = 16 / 9
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    image_height = 1 if image_height < 1 else image_height

    # viewport
    focal_length = 1
    viewport_height = 2.0
    viewport_width = viewport_height * (image_width / image_height)
    camera_center = Vec3(0, 0, 0)

    # horizontal and vertical viewport edges
    viewport_u = Vec3(viewport_width, 0, 0)
    viewport_v = Vec3(0, -viewport_height, 0)

    # hortizontal and vertical delta vectors from pixel to pixel
    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height

    # upper left pixel
    viewport_upper_left = (
        camera_center - Vec3(0, 0, focal_length) - (viewport_u / 2) - (viewport_v / 2)
    )
    pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

    # render
    with open("output.ppm", "w") as f:
        f.write("P3\n")
        f.write(f"{image_width} {image_height}\n")
        f.write("255\n")
        for j in range(image_height):
            for i in tqdm(range(image_width)):
                pixel_center = pixel00_loc + (i * pixel_delta_u) + (j * pixel_delta_v)
                ray_direction = pixel_center - camera_center
                ray = Ray(camera_center, ray_direction)

                color = ray_color(ray)

                f.write(f"{format(color)}\n")
