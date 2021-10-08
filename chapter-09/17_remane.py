# Write a python program to rename a file to “renamed_by_python.txt.”
import os
old="chapter-9/rename.txt"
new ="chapter-9/renamed_by_python.txt"

with open(old) as f:
    t=f.read()
with open(new,"w") as f:
    f.write(t)
os.remove(old)