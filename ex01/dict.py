print("1. dictionary")
## used for key-value-pairs
## changeable

print("1.1 syntax")

## dict = {}
shopping_dict = {
	"article_name": "apple",
	"price": 2,
	"end_date": 2024,
	"color": ["yellow", "brown"]
}
print(shopping_dict)

print("1.2 access")
print(shopping_dict["price"])
print(shopping_dict["color"][0])

print("1.3 functions for keys & values")
print(shopping_dict.keys())
print(type(shopping_dict.keys()))
print(shopping_dict.values())

