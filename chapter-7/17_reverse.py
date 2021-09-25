#  Write a program to print the multiplication table of n using for loop in reversed order.

n=int(input("Enter the number:"))
print("the table of "+ str(n) + " is :")
for i in reversed(range(1,11)):
    print(str(n )+ " * " + str(i )+ "= " + str(n*i))