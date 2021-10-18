# A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.

with open("python_course/chapter-09/word.txt","r") as f:
    text= f.read()

text= text.replace("donkey","####")

with open("python_course/chapter-09/word.txt","w") as f:
     f.write(text)
        
