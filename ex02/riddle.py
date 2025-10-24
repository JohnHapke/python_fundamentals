from random import randint

nbr = randint(1,100)
##print(nbr)
x = 1
y = 100
while True:
	print("lowest nbr: ", x, "highest nbr: ", y)
	guessed_nbr = int(input("What is your guessed nbr? "))
	if guessed_nbr > x and guessed_nbr < y:
		if nbr > guessed_nbr and nbr > x:
			x = guessed_nbr
		elif nbr < guessed_nbr and nbr < y:
			y = guessed_nbr
		elif nbr == guessed_nbr:
			print("bingo!")
			break
	else:
		print("Please provide a valid nbr between ", x, " and ", y)
