import numpy as np


class Vec3:
    @staticmethod
    def from_numpy(vec: np.ndarray):
        x, y, z = vec[0], vec[1], vec[2]

        return Vec3(x, y, z)

    def __init__(self, x: float, y: float, z: float):
        self.vec = np.array([x, y, z])

    @property
    def x(self):
        return self.vec[0]

    @property
    def y(self):
        return self.vec[1]

    @property
    def z(self):
        return self.vec[2]

    def __neg__(self):
        return Vec3.from_numpy(-self.vec)

    def __add__(self, other: "Vec3"):
        return Vec3.from_numpy(self.vec + other.vec)

    def __sub__(self, other: "Vec3"):
        return Vec3.from_numpy(self.vec - other.vec)

    def __mul__(self, scalar: float):
        return Vec3.from_numpy(scalar * self.vec)

    def __rmul__(self, scalar: float):
        return self * scalar

    def __truediv__(self, scalar: float):
        return Vec3.from_numpy(self.vec / scalar)

    def length(self):
        return np.sqrt((self.vec**2).sum())

    def unit_vec(self):
        return Vec3.from_numpy(self.vec / self.length())

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"


if __name__ == "__main__":
    a = Vec3(1, 2, 1)
    b = Vec3(0, 5, 3)

    print(a.x, a.y, a.z)

    c = a + b
    print(c)

    d = 2 * c
    print(d)

    print(d.length())

    print(Vec3(3, 4, 0).length())
