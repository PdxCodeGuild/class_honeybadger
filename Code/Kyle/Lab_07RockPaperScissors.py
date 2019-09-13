# Rock paper scissors
import random


choices = ["rock", "paper", "scissors"]

tie_outcomes = ["rock vs rock",  "scissors vs scissors", "paper vs paper"]

user_wins = ["TIGER vs scissors", "TIGER vs rock", "TIGER vs paper", "rock vs scissors", "paper vs rock", "scissors vs paper"]
cpu_win = ["rock vs paper", "scissors vs rock", "paper vs scissors"]

play_again = "yes"

print("Welcome to Rock Paper Scissors!")

while play_again == "yes":

    user_choice = input("Rock, paper, or scissors? ").lower()
    cpu_choice = random.choice(choices)

    outcome = user_choice + " vs " + cpu_choice

    print(outcome)

    if outcome in tie_outcomes:
        print("IT'S A TIE")
    elif outcome in user_wins:
        print("You Won!!")
    elif outcome in cpu_win:
        print("Oof! you lost")

    else:
        print("Please enter rock, paper or scissors.")
    play_again = input("Would you like to play again? yes/no ").lower()

while play_again not in ["yes", "no"]:
    play_again = input("Do you want to play again? (yes/no) ").lower()

else:
    print("Come back soon!")
