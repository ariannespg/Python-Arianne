name = input ("What is your name?")
gender = input ("What is your gender (M or F)?")

if gender == "F":
     if name.lower() < "m":
        group = "A"
     else: 
        group = "B"

if gender == "M":
    if name.lower() < "n":
        group = "B"
    else: 
        group = "A"

print (f"Your group is {group}")