# While loops
count = 1
while count <= 5:
    print("ken",count)
    count = count+1

i = 1
while i <= 10:
    print("Kenish",i)
    i+=1

# Numbers from 1-5 :
n = 1
while n<=5:
    print(n)
    n = n+1

print("Loop Ended")

# Numbers from 5-1:
p = 5
while p>=1:
    print(p)
    p -= 1
    

# Break and continue
i = 0
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("Out of Loop")

# Continue : Removing number 3

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue # Skip
    print(i)
    i += 1

# For Loops - can use else in FOR condition
list = [1,2,3]
for i in list:
    print("For loops:",i)
else:
    print("END of loop")

# Letter in a string
name = "Kenish"
for char in name:
    if(char == "n"):
        print("Letter found")
        break
    print(char)
else:
    print("END")

#Range function (Start, stop, steps)
for i in range(10): # range(stop)
    print(i)
for i in range(1,10): # range(start, stop)
    print(i)
for i in range(0,10,2): # range(Start, stop, steps))
    print(i)