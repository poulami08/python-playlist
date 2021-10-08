# Write a program to find out whether a file is identical and matches the content of another file.

f1="chapter-9/this.txt"
f2="chapter-9/another.txt"
with open(f1,"r") as f:
    t= f.read()

with open(f2,"r") as f:
    text= f.read()

if t==text:
    print("files are identical")
else:
    print("files are not identical")