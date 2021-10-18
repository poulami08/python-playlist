# Write a program to find out the line number where python is present from question 6.
text= True
i=1
with open("python_course/chapter-09/log.txt","r") as f:
    
    while text:
        text= f.readline().lower()
        if "python" in text:
            print("yes it is present on line:")
            print(i)
        # else:
        #     print("no it is not present")
        i+=1