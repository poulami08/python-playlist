# Write a program to make a copy of a text file “this.txt.”

with open("chapter-9/this.txt","r") as f:
    text= f.read()

with open("chapter-9/copy.txt","w") as f:
    f.write(text)