f = open("python_course/chapter-09/sample.txt","r")

#read first line
text=f.readline()
print(text)

#read second line
text=f.readline()
print(text)
f.close()