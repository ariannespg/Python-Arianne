n1 = float(input ("Escribe un número"))
n2 = float(input ("Escribe un número"))
Is_valid = True

if n1.isnumeric():
    n1 = float(n1)

if n2.isnumeric():
    n2 = float(n2)

else:
    Is_valid = False

if Is_valid:
    if n2 == 0:
        print ("Error")
    else:   print (n1/n2)
else: print ("Error")