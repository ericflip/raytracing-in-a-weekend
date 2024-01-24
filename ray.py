from vec3 import Vec3


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3):
        self.origin = origin
        self.direction = direction

    def at(self, t: float):
        return self.origin + t * self.direction


if __name__ == "__main__":
    origin = Vec3(1, 0, 0)
    direction = Vec3(1, 1, 1)

    ray = Ray(origin, direction)

    print(ray.at(1))
    print(ray.at(2))
    print(ray.at(3))

    print(ray.origin)
    print(ray.direction)
