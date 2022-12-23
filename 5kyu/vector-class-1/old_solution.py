# https://www.codewars.com/kata/532a69ee484b0e27120000b6
# 5 Kyu
# Vector Class

# My Solution
class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, (list, tuple)):
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        else:
            self.x = x
            self.y = y
            self.z = z
        self.magnitude = pow(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2), 0.5)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x,y,z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x,y,z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def cross(self, other):
        new_x = (self.y * other.z) - (self.z * other.y)
        new_y = (self.z * other.x) - (self.x * other.z)
        new_z = (self.x * other.y) - (self.y * other.x)
        return Vector(new_x, new_y, new_z)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def to_tuple(self):
        return tuple([self.x, self.y, self.z])

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def __repr__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

# Codewards Solution
import math
import operator


class Vector:
    def __init__(self, *args):
        self.x, self.y, self.z = self.args = tuple(args[0] if len(args) == 1 else args)
        self.magnitude = math.sqrt(sum(i ** 2 for i in self.args))

    def __str__(self):
        return '<{}>'.format(', '.join(map(str, self.args)))

    def __eq__(self, other):
        return self.args == other.args

    def __add__(self, other):
        return Vector(*map(operator.add, self.args, other.args))

    def __sub__(self, other):
        return Vector(*map(operator.sub, self.args, other.args))

    def dot(self, other):
        return sum(map(operator.mul, self.args, other.args))

    def to_tuple(self):
        return self.args

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

# codewars solution
import math

class VectorInputCoordsValidationError(Exception):
    """Custom exception class for invalid input args given to the Vector instantiation"""

class Vector:
    def __init__(self, *args):
        try:
            self.x, self.y, self.z = args if len(args) == 3 else args[0]
        except ValueError:
            raise VectorInputCoordsValidationError('Either give single iterable of 3 coords or pass them as *args')

    def __add__(self, other) -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other) -> "Vector":

        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __eq__(self, other) -> bool:
        return all((
            self.x == other.x,
            self.y == other.y,
            self.z == other.z
        ))

    def cross(self, other) -> "Vector":
        return Vector(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )

    def dot(self, other) -> int:
        return self.x*other.x + self.y*other.y + self.z*other.z

    def to_tuple(self) -> tuple:
        return self.x, self.y, self.z

    def __str__(self) -> str:
        return "<{x}, {y}, {z}>".format(**self.__dict__)

    @property
    def magnitude(self) -> float:
        return math.sqrt(
            sum (
                    (
                        self.x ** 2,
                        self.y ** 2,
                        self.z ** 2
                    )
            )
        )