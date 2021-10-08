class employee:
    company = "Google"
    salary =100

harry = employee()
rajni = employee()
harry.salary = 300
rajni.salary = 400
print(harry.company)
print(rajni.company)
employee.company = "YouTube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)