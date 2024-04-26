# Appending 3 items to a list
a = input("Enter Movie 1:")
b = input("Enter Movie 2:")
c = input("Enter Movie 3:")


list = []
list.append(a)
list.append(b)
list.append(c)

print(list)

# If a list is palindrome or not
pali1 = [1,2,1]


copy_pali1 = pali1.copy()
copy_pali1.reverse()

if copy_pali1 == pali1:
    print("It is a palindrome")
else:
    print("Not a palindrome")

#sorting a List
alpha = ["A", "C", "D", "B", "A"]
alpha.sort()
print(alpha)

