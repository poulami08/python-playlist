# Write a python function to print the multiplication table of a given number.

def table(t):
    for i in range(1,11):
        print(f"{t} X {i}= {i*t}")
        

num = int(input("enter the number :"))
d=table(num)
print(d)
