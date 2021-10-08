class emp:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = emp()
harry.salary = 100000
harry.getSalary()  #emp.getSalary(harry)