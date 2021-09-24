# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter the number 1:"))
b =int(input("Enter the number 2:"))
c =int(input("Enter the number 3:"))
d =int(input("Enter the number 4:"))
if((a>b and a>c) and a>d):
    print("the greatest no. is :" + str(a))
elif((a<b and b>c) and b>d):
    print("the greatest no. is :" + str(b))
elif((a<c and b<c) and c>d):
    print("the greatest no. is :" + str(c))
elif((a<d and b<d) and c<d):
    print("the greatest no. is :" + str(d))


