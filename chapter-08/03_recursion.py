def recursion(n):
    if(n==1 or n==0):
        return 1
    else:
        return n *recursion(n-1)

num= int(input("Enter the number :"))
f=recursion(num)
print(f)