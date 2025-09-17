# Dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates
capitals = {"India": "New Delhi",
            "USA": "Washington D.C.",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("India"))

print(dir(capitals))
print(help(capitals))

if capitals.get("Japan"):
    print("That Capital exists")
else:
    print("That Capital doesn't exist")

capitals.update({"Germany": "Berlin"})
print(capitals)

capitals.update({"USA": "Detroit"})
print(capitals)

capitals.pop("USA")    # It removes a specific item using key
print(capitals)

capitals.popitem()     # It removes latest comes key value pair
print(capitals)

# Keys
keys = capitals.keys()
print(keys)
for key in keys:
    print(key)

# Values
values = capitals.values()
print(values)
for value in values:
    print(value)

items = capitals.items()
print(items)

for key1, value1 in capitals.items():
    print(f"{key1} --- {value1}")


capitals.clear()
print(capitals)