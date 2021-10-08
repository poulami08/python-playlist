# Attempt problem 1 using a while loop.

n=int(input("Enter the number:"))
print("the table of "+ str(n) + " is :")
i=1
while(i<=10):
    print(str(n )+ " * " + str(i )+ "=" + str(n*i))
    i+=1
