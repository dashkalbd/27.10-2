class Airplane:
    def __init__(self, plane_type, max_passengers, passengers=0):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.passengers = passengers

    def _check_limits(self):
        if self.passengers > self.max_passengers:
            print(f"Забагато! Максимум {self.max_passengers} місць")
            self.passengers = self.max_passengers
        if self.passengers < 0:
            print("Пасажирів не може бути менше 0")
            self.passengers = 0

    def __str__(self):
        return f"{self.plane_type}: пасажирів {self.passengers} з {self.max_passengers}"

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, number):
        new_plane = Airplane(self.plane_type, self.max_passengers, self.passengers + number)
        new_plane._check_limits()
        return new_plane

    def __sub__(self, number):
        new_plane = Airplane(self.plane_type, self.max_passengers, self.passengers - number)
        new_plane._check_limits()
        return new_plane

    def __iadd__(self, number):
        self.passengers = self.passengers + number
        self._check_limits()
        return self

    def __isub__(self, number):
        self.passengers = self.passengers - number
        self._check_limits()
        return self

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers


plane1 = Airplane("Boeing 737", 180, 100)
plane2 = Airplane("Airbus A320", 150, 50)
plane3 = Airplane("Boeing 737", 180)

print(plane1)
print(plane2)
print(plane3)

print()
print("plane1 == plane3:", plane1 == plane3)
print("plane1 == plane2:", plane1 == plane2)

print()
plane4 = plane1 + 30
print("plane1 + 30 →", plane4)
plane5 = plane1 - 20
print("plane1 - 20 →", plane5)
print("plane1 не змінився:", plane1)

print()
plane2 += 40
print("plane2 += 40 →", plane2)
plane2 -= 100
print("plane2 -= 100 →", plane2)
plane2 += 500
print("plane2 += 500 →", plane2)

print()
print("plane1 > plane2:", plane1 > plane2)
print("plane1 < plane2:", plane1 < plane2)
print("plane1 >= plane3:", plane1 >= plane3)
print("plane2 <= plane1:", plane2 <= plane1)