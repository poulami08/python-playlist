# Create a class of pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.

class animals:
    type ="mammal"

class pets(animals):
    color = "white"

class dog(pets):
    @staticmethod
    def bark():
        print("i am barking")

d = dog()
d.bark()