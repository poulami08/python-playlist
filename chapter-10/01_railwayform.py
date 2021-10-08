class railwayform:
    formType = "railwayform"
    def date(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication = railwayform()
harrysApplication.name = "zya"
harrysApplication.train = "rajdhani express"
harrysApplication.date()