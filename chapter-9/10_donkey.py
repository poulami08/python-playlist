# A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.

with open("chapter-9/word.txt","r") as f:
    text= f.read()

text= text.replace("donkey","####")

with open("chapter-9/word.txt","w") as f:
     f.write(text)
        
