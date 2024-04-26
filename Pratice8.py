with open("Pratices.txt","r") as f:
    data = f.read()

newdata = data.replace("java","Python")
print(newdata)