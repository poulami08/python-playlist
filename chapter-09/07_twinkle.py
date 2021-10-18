# Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.

f = open("python_course/chapter-09/poems.txt","r")
text= f.read()

if "twinkle" in text:
    print("it contains the word ‘twinkle’")
else:
    print("it  does not contains the word ‘twinkle’")

f.close()