# write a program to find the maximum of the numbers in a list using reduce function

from functools import reduce

# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b


l = [1,2,3,20,45,4,5]
val = reduce(max,l)
print(val)