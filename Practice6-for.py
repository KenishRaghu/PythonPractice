#Printing elements in a list
list = [1,4,9,16,25,36,49,62,81,100]
for el in list:
    print(el)
    
# Finding a number x using FOR loop
list2 = (1,4,9,16,25,36,49,62,81,100)
x = int(input("Enter the number:"))
for i in list2:
    if (i == x):
        print("Found")
        break
    print(i)
else:
    print("Not found")

# Printing even numbers
for i in range(0,21,2):
    print(i)

for i in range(1,101):
    print(i)
for i in range(100,0,-1):
    print(i)

#Printing tables of n
mul = 3
for n in range(1,11):
    print(n*mul)

