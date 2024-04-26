marks = [99.9, 88.6, 76.9, 45.1]

print(marks[0])
print(len(marks))

ken = ["Student", 99, 100.98, "Male"]
Ish = ["Teacher", 100, 67.99, "Male"]

print(ken)
print(Ish)

ken[0] = "Teacher"
print(ken)
Ish[2] = "kenish"
print(Ish)

list = [1,3,2,5,7]
list.append(6)
list.sort() # Acending
list.sort(reverse=True) #Decending
list.reverse()
list.insert(0,0) # Inserting with [Index,value]
list.remove(0)
list.pop(2) #index removing

print(list)