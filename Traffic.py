#Input
color = input("Color : ")

#Conditions
if (color == "Red"):
    print("Color is RED, STOP")
elif(color == "Yellow"):
    print("Color is YELLOW, HOLD")
elif(color == "Green"):
    print("Color is GREEN, GO!")
else:
    print("Wrong color")

#Input 2
marks = int(input("marks : "))

#Conditions
if (marks >= 90):
    print("A+")
elif (marks > 50 and marks <90):
    print("B+")
else:
    print("FAIL")

# OR - 1 T to be true, Rest all F
# AND - 1 F to be false, Rest all T

Food = input("Food : ")
eat = "Yes" if Food == "cake" else "No"
print(eat)