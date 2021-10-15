class employee:
    company = "Google"

    def showDetails(self):
        print("this is an employee")

class programmer(employee):
    language = "python"
    company = "Youtube"

    def getlanguage(self):
        print(f"the language is {self.language}")

e = employee()
e.showDetails()
p = programmer()
p.showDetails()
print(p.company)