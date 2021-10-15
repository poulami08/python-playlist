class person:
    def __init__(self):
        print("initializing person...")

    country = "india"

    def takebreak(self):
        print("i am breathing .....")

class employee(person):
    def __init__(self):
        super().__init__()
        print("initializing employee...")
    company = "honda"

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takebreak(self):
        print("i am an employee so i am luckily breathing...")

class programmer(employee):
    def __init__(self):
        super().__init__()
        print("initializing programmer...")
    
    company = "fiverr"

    def getsalary(self):
        print(f"no salary to programmers")

    def takebreak(self):
        super().takebreak()
        print("i am a programmer and i am breathing...")

p = person()
p.takebreak()

e = employee()
e.takebreak()

pr = programmer()
pr.takebreak()
