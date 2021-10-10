# Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.

class train:
    def __init__(self,name,seats,fare):
        self.name =name
        self.fare = fare
        self.seats = seats
    
    def getstatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the seats available in the train are {self.seats}")
    
    def getinfo(self):
        print(f"the price of the ticket is : {self.fare}")

    def book(self):
        if(self.seats>0):
            print(f"your ticket has been booked ! your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry currently no ticket avaliable")    
    
    


a = train("rajdhani express :1204", 90,300)
a.getstatus()
a.book()
a.getstatus()
a.getinfo()
