# Add a static method in problem 2 to greet the user with hello.

class calculator:
    def __init__(self,num):
         self.num = num

    def square(self):
        print(f"the value of {self.num} square is {self.num**2}")

    def cube(self):
        print(f"the value of {self.num} square is {self.num**3}")

    def sroot(self):
         print(f"the value of {self.num} square is {self.num**0.5}")
    @staticmethod
    def greet():
        print("*****hello and welcome***** ")

a= calculator(3)
a.greet()
a.square()
a.cube()
a.sroot()
