# Single line comment for addition

num1 = 40
num2 = 50
sum = num1+num2
print(sum)

#Taking input

name = input("name : ")
age = int(input("age: "))
price = float(input("price: "))

print("my name is", name,"my age is", age, "and i am worth", price)

#Conditional IF statments
if (age >= 18):
    print("Can vote")
elif(18> age >=10):
    print("Underage")
else:
    print("Not fit")

a = 10
# a = a+10
a += 10
print(a)

#Logical Operators
number1 = 10
number2 = 20
print(not (number1>number2))