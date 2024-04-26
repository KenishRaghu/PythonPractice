# WHILE LOOP SOLVING
# 1 - 100
i = 1
while i <= 100:
    print(i)
    i+=1
# 100 - 1
p = 100
while p >=1:
    print(p)
    p -= 1
# Multiple of 5
n = 5
p = 1
while p <= 10:
    print(n*p)
    p += 1
    
#  Printing a list
num = [1,4,9,16,25,36,49,64,81,100]
s = 0
while s < len(num):
    print(num[s])
    s += 1

# Searching for a number "x" from a tuple:
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
s = 0
while s < len(nums):
    if(nums[s] == x):
        print("found at index", s)
        break
    else:
        print("finding...")
    s += 1
   

   