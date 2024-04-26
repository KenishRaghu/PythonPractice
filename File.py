# f = open("File_name", "Mode")
# mode = r or w
#File_name = sample.txt
# Always close a file once open

import os # For deleting a file

f = open("/Users/kenishr/Desktop/Coding/Python/sample.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

# Reading only 6 char from the document & Reading different lines
f = open("/Users/kenishr/Desktop/Coding/GitDemo/demo.txt","r")
data = f.read(6)
print(data)
line1 = print(f.readline())
line2 = print(f.readline())
f.close()

# How to write a program in a file
f = open("/Users/kenishr/Desktop/Coding/GitDemo/demo.txt","a")
data = f.write("\nThis is a write program, 123")
f.close()

#creating a new file and adding text to it
f = open("sample2.txt","a")
f.write("This is the first line of code")
f.close()

#Right way to write file code:
with open("sample3.txt","a") as p:
    p.write("Final file that has been created")

#deleting a file
os.remove("sample2.txt")
