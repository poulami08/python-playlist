# Write a python function to remove a given word from a string and strip it at the same time.

def remove(a,b):
    if(b in a):
        new=a.replace(b, "")
        return new.strip()
    else:
        print("word not found")



list="hi how are you i am xyz"
word = input("enter the word :")
c=remove(list,word)
print(c)