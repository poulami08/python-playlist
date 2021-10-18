# Write a program to make a copy of a text file “this.txt.”

with open("python_course/chapter-09/this.txt","r") as f:
    text= f.read()

with open("python_course/chapter-09/copy.txt","w") as f:
    f.write(text)