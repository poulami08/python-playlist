# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n>0):
        return n + sum(n-1)
    else:
        return 0
num=int(input("enter the number:"))
s=sum(num)
print(s)

