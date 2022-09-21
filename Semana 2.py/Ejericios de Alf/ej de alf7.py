Extra_pay = 2400
points_earned = float (input ("Please enter your punctuaction, only enter values such as 0.0, 0.4, 0.6 or more"))

if points_earned == 0.0:
    print (f"Your perfomance is unacceptable and your pay is {points_earned * Extra_pay} $")
elif points_earned == 0.4:
    print (f"Your perfomance is aceptable and your pay is {points_earned * Extra_pay} $")
elif points_earned >= 0.6:
    print (f"Your perfomance is meritable and your pay is {points_earned * Extra_pay} $")
if points_earned == "":
    print ("Esta puntuación no es valida")