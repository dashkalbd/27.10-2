class Flat:
    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price

    def __str__(self):
        return f"Квартира: {self.address}, {self.area} м², {self.price} $"

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price


flat1 = Flat("Київ, вул. Хрещатик 1", 60, 120000)
flat2 = Flat("Львів, пл. Ринок 5", 60, 90000)
flat3 = Flat("Одеса, вул. Дерибасівська 10", 45, 90000)

print(flat1)
print(flat2)
print(flat3)

print()
print("flat1 == flat2:", flat1 == flat2)
print("flat1 == flat3:", flat1 == flat3)
print("flat1 != flat3:", flat1 != flat3)
print("flat1 != flat2:", flat1 != flat2)

print()
print("flat1 > flat2:", flat1 > flat2)
print("flat1 < flat2:", flat1 < flat2)
print("flat2 >= flat3:", flat2 >= flat3)
print("flat3 <= flat1:", flat3 <= flat1)