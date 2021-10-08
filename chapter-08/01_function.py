def percent(marks):
    p = ((marks[0] + marks[1] + marks[2]+ marks[3] )/n)*100
    return p

n= int(input("Enter the total number:"))
marks1 = [45,78,86,77]
percentage1 =percent(marks1)

marks2 =[75,98,88,78]
percentage2 =percent(marks2)

print(percentage1,percentage2)