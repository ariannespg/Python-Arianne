data_dic = {}

while True: 
    data_key = (input ("Please enter the data that you want to save"))
    data_value = (input ("Please enter the value that you want to save"))
    data_dic[data_key] = data_value

    for key, value in data_dic.items():
     print ("Your data is")