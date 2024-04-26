name = input("Please Enter Your name:")
print(len(name))

#Even or Odd
num = int(input("Enter the number:"))
if (num%2 == 0):
    print("It is an Even Number")
else:
    print("It is an Odd Number")

#Greatest of the three numbers

a = int(input("Enter the a:"))
b = int(input("Enter the b:"))
c = int(input("Enter the c:"))

if (a > b and a > c):
    print("a is greatest")
elif (b > a and b > c):
    print("b is greatest")
elif (c > a and c > b):
    print("c is greatest")
else:
    print("Wrong number")

# Multiple of 7 or NOT

p = int(input("Enter the number :"))
q = p%7
if (q == 0):
    print("Multiple of 7")
else:
    print("Not multiple of 7")
