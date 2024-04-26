#Length of a list:
list = [1,2,3,4,5,6,7,8,9,9,9]
def length(list):
    p = len(list)
    return p
print(length(list))

# Elements in a list
def ele(list):
    for i in list:
        print(i, end="\n")

print(ele(list))

# Factorial of n
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i 
    print(fact)

factorial(5)

#USD to INR
def convert(p):
    p = int(input("Enter USD you wanna convert : "))
    con = p*83
    return(con)

print(convert(83))

#Even or Odd
def even_odd():
    n = int(input("Enter the number to check even/odd: "))
    if n%2 == 0:
        print("Even")
    else:
        print("odd")

even_odd()