# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.

def game():
    return 6

score = game()
with open("chapter-9/Hiscore.txt","r") as f:
    a =f.read()


if a=="":
    with open("chapter-9/Hiscore.txt","w") as f:
        f.write(str(score))
elif int(a)<score :
    with open("chapter-9/Hiscore.txt","w") as f:
        f.write(str(score))  

