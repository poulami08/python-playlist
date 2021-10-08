# Repeat program 4 for a list of such words to be censored.


words=["donkey","twinkle","star"]

with open("chapter-9/repeat.txt","r") as f:
    text= f.read()

for word in words:

    text= text.replace(word,"$$$%^@@###")

    with open("chapter-9/repeat.txt","w") as f:
     f.write(text)