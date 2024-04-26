house = {
    "table" : ["wood", "wood2"],
    "cat" : "a small animal"
}
print(house)

set = {"Python", "java", "C++", "Python", "javascript", "java", "Python", "java", "C++", "C"}

print(len(set))
# Input of marks and putting in DICT
marks = {}
a= input("Enter Chem marks:")
b= input("Enter Phy marks:")
c= input("Enter Math marks:")
marks.update({"Chem" : a})
marks.update({"Phy" : b})
marks.update({"Math" : c})


print(marks)