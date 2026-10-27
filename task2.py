class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        real = round(self.real, 2)
        imag = round(self.imag, 2)
        if imag >= 0:
            return f"{real} + {imag}i"
        return f"{real} - {abs(imag)}i"

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        if denominator == 0:
            print("Ділення на нуль неможливе")
            return None
        return Complex((self.real * other.real + self.imag * other.imag) / denominator,
                       (self.imag * other.real - self.real * other.imag) / denominator)


a = Complex(3, 2)
b = Complex(1, 4)

print("a =", a)
print("b =", b)
print()
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)