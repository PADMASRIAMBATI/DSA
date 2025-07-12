# collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable,  but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)
print(fruits[2])
print(fruits[:3])
print(fruits[::-1])

for fruit in fruits:
    print(fruit, end = ' ')
print()

print(dir(fruits))

print(help(fruits))

print(len(fruits))

print("apple" in fruits)
print("mango" in fruits)

fruits[0] = "mango"
for i in fruits:
    print(i ,end=" ")
print()

# Methods in a list
fruits.append("apple")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.insert(0,"apple")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits.index("apple"))

fruits.append("banana")
print(fruits)

print(f"Number of Banana's in list : {fruits.count("banana")}")

fruits.clear()
print(fruits)