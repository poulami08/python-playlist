# this will create an empty dictionary 
a = {}
print(type(a))

# this will create an empty set 
b=set()
print(type(b))

b.add(4)
b.add(6)
b.add(6)
# only unique value accepted
b.add(

    (4,5,3)
)
# we can add tuple inside a set but we cannot add list and dictionary inside a set as we can modify list and dictionary but we cannot change tuple.
print(b)

print(len(b))

b.remove(4)
print(b)

print(b.pop())
print(b)

b.add(56)
print(b)
b.clear()
print(b)