# Can you change the self parameter inside a class to something else (say ‘harry’)? Try changing self to ‘slf’ or ‘harry’ and see the effects.

class sample:
   
    def __init__(h,name):
        h.name = name

        

obj = sample("harry")
print(obj.name)
