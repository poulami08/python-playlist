# Write a program to print the following star pattern.
#   *

#  ***  

# ***** for n=3

n=int(input("enter the number:"))
k=n-1
for i in range(n):
    for j in range(k):
        print(end=" ")
    k=k-1
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

