# Create a class Employee and add salary and increment properties to it.Write a method SalaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.

class employee:
    
    salary = 5600
    increment = 1.5
    
    @property
    def totalsalary(self):
        return self.salary * self.increment

    @totalsalary.setter
    def totalsalary(self, val):
         self.increment = val / self.salary

e = employee()
print(e.totalsalary)
print(e.increment)
e.totalsalary = 88000
print(e.increment)
