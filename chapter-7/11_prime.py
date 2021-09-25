# Write a program to find whether a given number is prime or not.

n = int(input("Enter the number:"))
f=0
for i in range(2,n):
    if(n%i==0):
       f=1
       break 
    else:
        f=0
if(f==1):
    print("not a prime number")
else:
    print("prime number")