x = ""
while x != "YES" and x != "NO":
	print("Please, answer with 'YES' or 'NO'")
	x = input("Do you want to convert Euro in Bath? ")
currency = "BATH"
if x == "YES":
	currency = "EURO"
amount = float(input("amount of " + currency + ": "))
if currency == "EURO":
	print("Info: 1 Euro = 38.11 THB)")
	result = amount * 38153
	print("result: ", result)
else:
	print("Info: 1 Bath = 0.026 Euro")
	result = amount * 0.026
	print("result: ", result)

