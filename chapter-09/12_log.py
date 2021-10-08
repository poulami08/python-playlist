# Write a program to mine a log file and find out whether it contains ‘python’.

with open("chapter-9/log.txt","r") as f:
    text= f.read().lower()
if "python" in text:
    print("yes it is present")
else:
     print("no it is not present")



