num1 = (input ("Please write a number"))

if num1.isnumeric():
    num1 = int(num1)

else:
    print ("error")

if num1%2 == 0:
    print (f"El número {num1} es par")

if num1%2 != 0:
    print (f"El número {num1} es impar")
