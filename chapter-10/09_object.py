# Create a class with a class attribute a; create an object from it and set a directly using object.a=0 Does this change the class attribute?

class sample:
    a = "Harry"

obj = sample()
obj.a = "vickey"
print(sample.a)
print(obj.a)