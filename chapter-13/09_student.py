# write a program to input name, marks and phone number of a student and format it using the format function like below:
# "the name of the student is harry, his marks are 72 and phone number is 99999888 "

name = input("enter the name : ")
marks = int(input("enter the marks : "))
phone = int(input("enter the phone number : "))
a = "the name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone)
print(a)