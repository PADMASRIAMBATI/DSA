# While loop = execute some code WHILE some condition remains true

#Example-1
name = input("Enter your name: ")
while name == "":
    print("You did not enter yor name: ")
    name = input("Enter your name: ")
print(f"Welcome {name}")

#Example-2
age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative")
    age = input("Enter your age: ")
print(f"Your are {age} years old")

# Example-3
food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")
print("bye")

# Example-3
num = int(input("Enter a number between 1-10: "))
while num<1 or num>10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))
print(f"Your number is {num}")