# rock_paper_scissors_nicole_2.py

import random
repeat = "yes"
while repeat in ["yes", "y"]:
    game = ["rock", "paper", "scissors"]
    computer = random.choice(game)
    player = input("Choose one: rock, paper, or scissors\n").lower()

    if player == "rock":
        if computer == "paper":
            print("You lose! The computer chose PAPER")
        elif computer == "scissors":
            print("You win! The computer chose SCISSORS")
        else:
            print("It's a tie!")
    elif player == "paper":
        if computer == "rock":
            print("You win! The computer chose ROCK.")
        elif computer == "scissors":
            print("You lose! The computer chose SCISSORS.")
        else:
            print("It's a tie!")
    elif player == "scissors":
        if computer == "paper":
            print("You win! The computer chose PAPER.")
        elif computer == "rock":
            print("You lose! The computer chose ROCK.")
        else:
            print("It's a tie!")
    else:
        print("Please choose a valid option: rock, paper, or scissors")

    repeat = input("Would you like to play again? (Please type 'yes' or 'no') ").lower()

else:
    print("Goodbye")
