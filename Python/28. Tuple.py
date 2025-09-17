# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut","orange")
print(fruits)

print(dir(fruits))
print(help(fruits))

print(f"Length of the tuple: {len(fruits)}")

print("pineapple" in fruits)

print(f"Index of banana is {fruits.index("banana")}")

print(f"Number of oranges {fruits.count("orange")}")

for fruit in fruits:
    print(fruit, end=" ")
print()