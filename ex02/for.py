print("1. for - loop")
## usage: for element in sequence:
print("1.1 loop through list")
list = ["apple", "orange", "banana"]

for element in list:
	print(element)

print("1.1 loop through string")
name = "Hello"

for i in name:
	print(i)

print("1.1 loop through list with conditions")
list_price = [1500, 1000, 500, 4000, 3000, 200]
interesting_price = []
print(list_price)
for i in list_price:
	if i <= 1000:
		interesting_price.append(i)
	else:
		print(i, "to expensive")
	print(interesting_price)