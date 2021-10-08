# Write a python function to print the first n lines of the following pattern.
# ***

# **       #For n = 3

# *

def pattern(n):
    for i in reversed(range(n+1)):
         print("*" * i)
        


num = int(input("enter the number :"))
c=pattern(num)
print(c)
