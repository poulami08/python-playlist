# Write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them.

class complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    
    def __add__(self, c):
        return complex(self.real + c.real , self.imaginary + c.imaginary)

    def __mul__(self, c):
        mulreal = self.real*c.real - self.imaginary*c.imaginary
        mulimg = self.real*c.imaginary + self.imaginary*c.real
        return complex(mulreal, mulimg)

    def __str__(self):
        if self.imaginary<0:
            return f"{self.real}-{self.imaginary}i"
        return f"{self.real} + {self.imaginary}i"


c1 = complex(1,4)
c2 = complex(8,5)
print(c1 + c2)
print(c1 * c2)