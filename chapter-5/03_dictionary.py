# Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!

a=input("Enter the hindi word : ")
b=input("Enter the hindi word : ")
c=input("Enter the hindi word : ")
d=input("Enter the hindi word : ")
e=input("Enter the english meaning : ")
f=input("Enter the english meaning : ")
g=input("Enter the english meaning : ")
h=input("Enter the english meaning : ")

my={
    a:e,
    b:f,
    c:g,
    d:h
    }
print("Options are :", my.keys())
n=input("Enter the hindi word:")
print("The meaning of your word is:", my.get(a))