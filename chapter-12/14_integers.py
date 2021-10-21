# write a program to display a/b where a and b are integers. if b=0,display infinite by handling the zerodivisionerror.

a = int(input("enter the number 1: "))
b = int(input("enter the number 2: "))
try:
    c=a/b
    print(c)
except:
    print("infinite")