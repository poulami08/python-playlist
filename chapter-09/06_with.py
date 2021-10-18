with open("python_course/chapter-09/another.txt","r") as f:
    a = f.read()
with open("python_course/chapter-09/another.txt","w") as f:
    a = f.write("me")
print(a)