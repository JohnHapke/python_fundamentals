print("1. STRING")

print("1.1 string slicing")
x = "Hello world!!!"
print(x[6:])
print(x[:6])
print(x[6:10])
print(len(x))

print("1.2 print manipulation")
y = "ciao"
print("the string " + x + "is ", len(y), " long")

print("1.3 print manipulation")
z = "Hello"
print(z * 10)

print("1.4 split()")
x = "Hello world"
print(x.split())
z = "hello, I want to find a comma, ..."
print(z.split(","))

print("1.5 find()")
x = "I love Python"
print(x[x.find("P"):])

print("------------------------------")
print("2. INT & FLOAT")

print("2.1 type()")
print(type(10 / 2))

print("2.2 rest after division")
print(10 / 3)
print("modulo")
print(10 % 3)
print("power")
print(100 ** 2)
print("sqrt")
print(100 ** 0.5)

print("------------------------")
print("3. iostream")
##x = input("name: ")
print("3.1 input()")
print("Hallo " + x)

print("3.2 salary tool")
##x = int(input("actual salary: "))
##y = x * 1.1
##print("salary after 10% raise: ", y)

print("------------------------")
print("4. boolean")
print("4.1 different boolean use cases")
print(type(True))
print(2 > 1)
print(2 < 1)
print(2 == 1)

print("------------------------")
print("4. if-else-statement")

distanceInKm = 3

if distanceInKm < 3:
	print("you better walk")
elif distanceInKm == 3:
	print("take the good shoes")
else:
	print("go by bike")