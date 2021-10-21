a = [3,6,7,8,9,1,7,2,58,25,341,1]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)

b = [i for i in a if i%2==0]
print(b)

t = [1,5,4,1,2,3,4]
s = {i for i in t}
print(s)