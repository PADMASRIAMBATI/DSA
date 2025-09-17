# List Comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

double = []
for x in range(1,11):
    double.append(x * 2)
print(double)

doubles = [x * 2 for x in range(1,11)]
triple = [j * 3 for j in range(1,11)]
square = [z * z for z in range(1,11)]
print(f"Double the numbers: {doubles}")
print(f"Triple the numbers: {triple}")
print(f"Square the numbers: {square}")

fruits = ["apple", "banana", "mango", "orange"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0, -1, -2, -3, -4]
positive_nums = [x for x in numbers if x >= 0]
negative_nums = [y for y in numbers if y < 0]
even_nums = [x for x in numbers if x%2 == 0]
odd_nums = [x for x in numbers if x%2 != 0]
print(f"Positive numbers: {positive_nums}")
print(f"Negative numbers: {negative_nums}")
print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}")

grades = [85, 42, 79, 90, 56, 61, 30, 99]
passing_grades = [grade for grade in grades if grade >= 60]
print(f"Passing Grades are {passing_grades}")