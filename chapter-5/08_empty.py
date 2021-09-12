# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.

# If the names of 2 friends are the same; what will happen to the program in Program 6?
# ans- it will only print one name as we cannot have 2 keys with same name. It have unique keys only.

# If the languages of two friends are the same; what will happen to the program in Program 6?
# ans- the program will show all the language as the keys are unique.

a=input("Enter the favorite language : ")
b=input("Enter the favorite language : ")
c=input("Enter the favorite language : ")
d=input("Enter the favorite language : ")
e=input("Enter the name : ")
f=input("Enter the name : ")
g=input("Enter the name : ")
h=input("Enter the name : ")

my={
    e:a,
    f:b,
    g:c,
    h:d
    }
print(my)
