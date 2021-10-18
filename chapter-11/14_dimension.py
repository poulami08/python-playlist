# Write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and the dot product of them.

class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
           sum+= self.vec[i] * vec2.vec[i]
        return sum

v1 = vector([1,4,6,2])
v2 = vector([2,5,7,9])
print(v1+v2)
print(v1*v2)