with open("chapter-9/another.txt","r") as f:
    a = f.read()
with open("chapter-9/another.txt","w") as f:
    a = f.write("me")
print(a)