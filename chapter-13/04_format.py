name = "harry"
channel = "abc"
type = "code"
#a = f"this is {name}"
# a = "this is {}".format(name)
# a = "this is {} and his channel is {}".format(name, channel)
a = "this is {1} and his channel is {2} and the type is {0}".format(type,name, channel)

print(a)