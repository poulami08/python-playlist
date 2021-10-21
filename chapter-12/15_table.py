num = int(input("enter your number:"))
table = [num*i for i in range(1,11)]
print(table)

with open("python_course/chapter-12/tables.txt","a") as f:
    f.write(str(table))
    f.write('\n')