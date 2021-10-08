class emp:
    company = "Google"
    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
            print("Good Morning, Sir")
    
    @staticmethod
    def time():
            print("The time is 9AM in the morning")

harry = emp()
harry.salary = 100000
harry.getSalary("Thanks !")
harry.greet()
harry.time()