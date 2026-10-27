import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Коло з радіусом {self.radius}, довжина {self.length():.2f}"

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __add__(self, number):
        return Circle(self.radius + number)

    def __sub__(self, number):
        new_radius = self.radius - number
        if new_radius < 0:
            new_radius = 0
        return Circle(new_radius)

    def __iadd__(self, number):
        self.radius = self.radius + number
        return self

    def __isub__(self, number):
        self.radius = self.radius - number
        if self.radius < 0:
            self.radius = 0
        return self


c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(5)

print(c1)
print(c2)
print(c3)

print()
print("c1 == c3:", c1 == c3)
print("c1 == c2:", c1 == c2)

print()
print("c1 > c2:", c1 > c2)
print("c1 < c2:", c1 < c2)
print("c1 >= c3:", c1 >= c3)
print("c2 <= c1:", c2 <= c1)

print()
c4 = c1 + 2
print("c1 + 2 →", c4)
c5 = c1 - 1
print("c1 - 1 →", c5)
print("c1 не змінилось:", c1)

print()
c2 += 4
print("c2 += 4 →", c2)
c2 -= 2
print("c2 -= 2 →", c2)