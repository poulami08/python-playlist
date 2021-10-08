# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100	Ex
# 80-90	A
# 70-80	B
# 60-70	C
# 50-60	D
# <50	F

m= int(input("Enter the marks:"))
if(m>90 and m<=100):
    print("Ex")
elif(m>80 and m<=90):
    print("A")
elif(m>70 and m<=80):
    print("B")
elif(m>60 and m<=70):
    print("C")
elif(m>50 and m<=60):
    print("D")
else:
    print("F")
