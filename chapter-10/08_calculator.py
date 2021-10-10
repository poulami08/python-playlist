# Write a class calculator capable of finding square, cube, and the square root of a number.

class calculator:
    def __init__(self,num):
         self.num = num

    def square(self):
        print(f"the value of {self.num} square is {self.num**2}")

    def cube(self):
        print(f"the value of {self.num} square is {self.num**3}")

    def sroot(self):
         print(f"the value of {self.num} square is {self.num**0.5}")

a= calculator(3)
a.square()
a.cube()
a.sroot()