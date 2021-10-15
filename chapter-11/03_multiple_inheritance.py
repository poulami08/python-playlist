class employee:
    company = "visa"
    ecode = 120

class freelancer:
    company = "fiverr"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

class programmer(employee, freelancer):
    name = "rohit"

p = programmer()
p.upgradelevel()
print(p.level)
print(p.company)