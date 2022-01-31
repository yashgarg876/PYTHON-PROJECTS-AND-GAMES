with open('currencydata.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(print("Enter amount:\n"))
print("Enter the name of currency you want to convert amount to: Available options: \n")
[print(item) for item in currencyDict.keys()]
currency = input("Enter the name of the place you wana compare the values: \n")
#print(f"{amount} INR is equal to {amount = float(currenctDict[currency])}  {currency}")