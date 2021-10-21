# write a program to open three files 1.txt ,2.txt and 3.txt . if any of these files are not present, a message without exiting the program must be printed prompting the same.

def read(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} is not found")
    

read("python_course/chapter-12/1.txt")
read("python_course/chapter-12/2.txt")
read("python_course/chapter-12/3.txt")