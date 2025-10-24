print("1. while - loop")
counter = 0
while counter <= 5:
	print(counter)
	counter += 1

shopping_list = []
flag = "y"

while flag == "y":
	shopping_list.append(input("What do you want to add? "))
	flag = input("Do you want something else? (y / n)")
print(shopping_list)