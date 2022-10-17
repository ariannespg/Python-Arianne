currency_dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency_input = input("Please enter a currency name: euro, dollar or yen")

print (currency_dic.get(currency_input.lower(), "Currency not found"))