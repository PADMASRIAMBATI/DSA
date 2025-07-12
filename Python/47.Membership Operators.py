# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in
print("------------ STRING ----------------")
word = "APPLE"
letter = input("Guess a letter in the secret word: ")
if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


letters = input("Guess a letter in the secret word: ")
if letters not in word:
    print(f"{letters} was not found")
else:
    print(f"There is a {letters}")

print("------------ LIST ----------------")
number = [1, 2, 3, 4, 5, 6]
num = int(input("Enter the number: "))
if num in number:
    print(f"{num} in list")
else:
    print(f"{num} is not in list")

nums = int(input("Enter the number: "))
if nums not in number:
    print(f"{nums} is not in list")
else:
    print(f"{nums} in list")


print("------------ TUPLE ----------------")
number1 = (1, 2, 3, 4, 5, 6)
num1 = int(input("Enter the number: "))
if num1 in number1:
    print(f"{num1} in list")
else:
    print(f"{num1} is not in list")

nums2 = int(input("Enter the number: "))
if nums2 not in number1:
    print(f"{nums2} is not in list")
else:
    print(f"{nums2} in list")


print("---------- SET --------------")
students = {"tinku", "padmasri", "devi"}
student = input("Enter the name of the student: ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student}  was not found")

student1 = input("Enter the name of the student: ")
if student1 not in students:
    print(f"{student1}  was not found")
else:
    print(f"{student1} is a student")

print("---------- DICTIONARY --------------")
grades = {"sandy": "A",
          "padmasri": "O",
          "tinku": "B"}

child = input("Enter the name of a student: ")
if child in grades:
    print(f"{child}'s grade is {grades[child]}")
else:
    print(f"{child} is not found")

