# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop.
print("LIST:")
numbers= [1, 2, 3, 4, 5]
for num in numbers:
    print(num, end=" ")
print()

print("REVERSED LIST:")

numbers1= [1, 2, 3, 4, 5]
for num1 in reversed(numbers1):
    print(num1, end=" ")
print()

print("TUPLE:")

numbers2= (1, 2, 3, 4, 5)
for num2 in numbers2:
    print(num2, end=" ")
print()

print("SET:")

numbers3= {1, 2, 3, 4, 5}
for num3 in numbers3:
    print(num3, end=" ")
print()

print("STRING:")
name = "Padmasri"
for char in name:
    print(char, end=" ")
print()

print("DICTIONARY:")
my_dictionary = {"A": 1, "B": 2, "C": 3}
for key,value in my_dictionary.items():
    print(f"{key} = {value}")
print()