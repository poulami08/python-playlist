# Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

e=int(input("Enter the marks in english:"))
h=int(input("Enter the marks in hindi:"))
m=int(input("Enter the marks in maths:"))
te=int(input("Enter the  total marks in english:"))
th=int(input("Enter the  total marks in hindi:"))
tm=int(input("Enter the  total marks in maths:"))
n=((e+h+m)/th+tm+te)*100
if(n>=(40/te+th+tm)*100)and (e>=33/te*100) and (h>=33/th*100) and (m>=33/tm*100) :
    print("pass")
else:
    print("fail")
