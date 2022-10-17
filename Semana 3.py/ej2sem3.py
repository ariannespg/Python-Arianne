num = input ("Please enter a number")
aux = 1

if num.isnumeric():
    num = int(num)
    num = num+1
    for index in range (1,num):
        print ("*"*index)
else:
    print ("error")
