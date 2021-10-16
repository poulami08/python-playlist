class number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):
        print("lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("lets multiply")
        return self.num * num2.num

    def __str__(self):
        return f"decimal number : {self.num}"

    

n = number(9)
print(n)