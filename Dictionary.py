info = {
    "Name" : "Kenish",
    "Age" : 25,
    "Gender" : "Male",
    "Family" : ["Mom","Dad","Brother"]
}

print(info)
print(info["Name"])

#appending
info["surname"] = "Raghu"

print(info)

null_dict = {} # Empty dict

print(null_dict)

# Nested Dict
student = {
    "name" : "Kenish",
    "subjects" : {
        "chem" : 98,
        "phy" : 90,
        "math" : 100

    }
}
print(student)

print(student["subjects"]) # {Printing only subjetcs}

print(student.keys())
print(student.values())
print(student.items())
print(student.keys())

# Updating
student.update({"city":"Bangalore"})

print(student)

