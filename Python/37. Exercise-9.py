# Game of Rock, Paper, Scissor

import random

options = ("rock", "paper", "scissor")
playing = True
while playing:
    computer = random.choice(options)
    player = None
    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "paper" and computer == "rock":
            print("You WIN!")
        elif player == "rock" and computer == "scissor":
            print("You WIN!")
        elif player == "scissor" and computer == "paper":
            print("You WIN!")
        else:
            print("You LOSS!")

        play_again = input("Play again? (y/n): ").lower()
        if not play_again == "y":
             playing = False
print("Thanks for Playing")
