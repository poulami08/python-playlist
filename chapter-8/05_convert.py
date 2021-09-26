# Write a python program using the function to convert Celsius to Fahrenheit.

def convert(a):
    f=((a*9/5)+32)
    return f

c=float(input("enter the number:"))
g=convert(c)
print(g)