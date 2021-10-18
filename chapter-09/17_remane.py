# Write a python program to rename a file to “renamed_by_python.txt.”
import os
old="python_course/chapter-09/rename.txt"
new ="python_course/chapter-09/renamed_by_python.txt"

with open(old) as f:
    t=f.read()
with open(new,"w") as f:
    f.write(t)
os.remove(old)