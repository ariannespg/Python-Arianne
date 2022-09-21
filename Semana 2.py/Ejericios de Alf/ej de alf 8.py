print ("*** Welcome to the Arcade ***")
age = int (input ("How old are you?"))

if age <= 4:
    print ("Free entrance")
elif 4 <= age <= 18:
    print ("Entrance is 5 $")
elif age > 18:
    print ("Entrance is 10 $")
else: "Please enter a valid age"