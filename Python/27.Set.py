# Set = {} unordered and immutable,  but Add/Remove OK. NO duplicates

fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)

print(dir(fruits))
print(help(fruits))

print(f"Length of the set: {len(fruits)}")

fruits.add("pineapple")
print(fruits)

fruits.remove("pineapple")
print(fruits)

fruits.pop() # It removes random word in set
print(fruits)

print(fruits.clear())