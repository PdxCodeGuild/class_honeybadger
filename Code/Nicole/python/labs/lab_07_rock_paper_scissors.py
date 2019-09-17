# lab_07_rock_paper_scissors.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab07-rock_paper_scissors.md

import random


def rock_paper_scissors():
    game = ["rock", "paper", "scissors"]
    
    again = "yes"
    
    while again == "yes":
        user_turn = input("Choose one: 'rock', 'paper', or 'scissors': \n")
        computer_turn = random.choice(game)
        print(f"The computer picked:\t {computer_turn}")
        print(f"You picked:\t\t {user_turn}")
        winner(computer_turn, user_turn)
        again = input("Would you like to play again?\n")
    
    return print("Thanks for playing!")

    
def winner(a, b):
    winner = ""
    if a == b:
        winner = "It's a tie"
    elif a == "paper" and b == "rock":
        winner = "The computer wins!"
    elif a == "rock" and b == "paper":
        winner = "You win!"
    elif a == "scissors" and b == "paper":
        winner = "The computer wins!"
    elif a == "paper" and b == "scissors":
        winner = "You win!"
    elif a == "rock" and b == "scissors":
        winner = "You win!"
    elif a == "scissors" and b == "rock":
        winner = "The user wins!"

    return print(winner)


rock_paper_scissors()