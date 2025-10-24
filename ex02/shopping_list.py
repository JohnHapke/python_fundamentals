shopping_list = []

while True:
	action = str(input("Do you want to add, delete, show or exit the shoppactiong list? "))
	if action == "add":
		article = input("Which article do you want to add? ")
		shopping_list.append(article)
	elif action == "delete":
		article = input("What article do you want to delete? ")
		if article in shopping_list:
			shopping_list.remove(article)
			print("article delete")
		else:
			print("article is not action the list")
	elif action == "show":
		print(shopping_list)
	elif action == "exit":
		break
	else:
		print("please type action one of the accepted words")