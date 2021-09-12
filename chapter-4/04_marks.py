# Write a program to accept the marks of 6 students and display them in a sorted manner.


a=int(input("Enter the 1st student's marks in the list :"))
b=int(input("Enter the 2st student's marks in the list :"))
c=int(input("Enter the 3st student's marks in the list :"))
d=int(input("Enter the 4st student's marks in the list :"))
e=int(input("Enter the 5st student's marks in the list :"))
f=int(input("Enter the 6st student's marks in the list :"))

l1=[a,b,c,d,e,f]
l1.sort()
print(l1) 