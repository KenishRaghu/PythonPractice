#Sum of a number
a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))
def calc_sum(a,b):
    p = a + b
    return p
print("The sum is :", calc_sum(a,b))

#Avg of a number
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))

def Avg(num1,num2,num3):
    q = (num1+num2+num3)/3
    return(q)

print(Avg(num1,num2,num3))