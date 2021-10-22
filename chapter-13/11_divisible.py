# write a program to filter a list of numbers which are divisible by 5

def func(d):
    if d%5 == 0:
        return True
    else:
        return False
    

l = [ 5,41,52,20,43,15,50,725]

print(list(filter(func,l)))
