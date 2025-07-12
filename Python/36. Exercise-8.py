# Python number guessing game
import random
lowest_num = 0
highest_num = 100
guesses = 0
is_running = True
answer = random.randint(lowest_num, highest_num)

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter the number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if lowest_num > guess or highest_num < guess:
            print("Number is out of the Range")
            print(f"Please Select a number between {lowest_num} and {highest_num}")
        elif answer < guess:
            print("Too High! Try again!")
        elif answer > guess:
            print("Too Low! Try again!")
        else:
            print(f"CORRECT! the answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid")
        print(f"Please Select a number between {lowest_num} and {highest_num}")

