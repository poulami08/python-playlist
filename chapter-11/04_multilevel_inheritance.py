class person:
    country = "india"

    def takebreak(self):
        print("i am breathing .....")

class employee(person):
    company = "honda"

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takebreak(self):
        print("i am an employee so i am luckily breathing...")

class programmer(employee):
    company = "fiverr"

    def getsalary(self):
        print(f"no salary to programmers")

p = person()
p.takebreak()
e = employee()
e.takebreak()
print(e.company)
pr = programmer()
pr.takebreak()
print(pr.company)
print(pr.country)