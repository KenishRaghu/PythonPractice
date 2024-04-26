# sum of n numbers using while
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)

# sum of n numbers using For
n = 5
sum = 0
i = 1
for i in range(n+1):
    sum += i
print(sum)

# factorial of a number
n = 3
fact = 1
i = 0
for i in range (1,n+1):
    fact *= i
print(fact)
