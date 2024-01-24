from vec3 import Vec3


class Color(Vec3):
    pass


def format(color: Color):
    r = int(255.999 * color.x)
    g = int(255.999 * color.y)
    b = int(255.999 * color.z)

    return f"{r} {g} {b}"
