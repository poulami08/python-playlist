class employee:
    company = "camel"
    salary = 1000
    location = "delhi"

    # def changesalary(self, sal):
    #     self.__class__.salary = sal
    #     or

    @classmethod
    def changesalary(cls, sal):
        cls.salary = sal

e = employee()
print(e.salary)
e.changesalary(4500)
print(e.salary)
print(employee.salary)