# Write a program using the function to find the greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

n =int(input("enter the  1st number: "))
m =int(input("enter the 2nd number: "))
o =int(input("enter the 3rd number: "))
h=greatest(n,m,o)
print(h)