## 1. age / amount of tickets
age = -1
amount = -1
while amount < 0:
	amount = int(input("How many tickets do you want? "))
i = 0
young = 0
adult = 0
old = 0
while i < amount:
	##while age < 0:
	age = int(input("How old are you? "))
	if age < 18:
		young += 1
	elif age >= 18 and age <= 65:
		adult += 1
	else:
		old += 1
	i += 1

result = young * 5 + adult * 10 + old * 7.5
print("the price for ", young, " U18, ", adult, " adult, ", old, " over65 is", result, ".")