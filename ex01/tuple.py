print("1. tuple -> not changeable")
print("1.1 comparison: list vs. tuple")
print("list)")
list = ["chocolate", "cookies", "orange"]
print(list)
list[0] = "choco"
print(list)
print("tuple")
tuple = ("chocolate", "cookies", "orange")
print(tuple)
print(type(tuple))
print(tuple[0])
## tuple[0] = "choco" -> Error, not changeable