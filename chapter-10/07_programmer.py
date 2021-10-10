# Create a class programmer for storing information of a few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The product of the employee is {self.product}")
    
harry = Programmer("harry","abc")
harry.getDetails()
alka = Programmer("harry","asd")
alka.getDetails()
