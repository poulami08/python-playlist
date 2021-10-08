# Write a program to print the multiplication table of a given number using for loop.

n=int(input("Enter the number:"))
print("the table of "+ str(n) + " is :")
for i in range(1,11):
    # print(str(n )+ " X " + str(i )+ "=" + str(n*i))
    # or
    print(f"{n}X{i}={n*i}")
