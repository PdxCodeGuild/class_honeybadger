import random

choices = ["rock", "paper", "scissors"]
comp_choice = random.choice(choices)

user_choice = input("Rock, paper or scissors? ")

print(comp_choice)

game_instance = (f"{user_choice} vs {comp_choice}")

print(game_instance)

print(f"{user_choice} vs {comp_choice}")


win = ["paper vs rock", "rock vs scissors", "scissors vs paper"]


if user_choice == comp_choice:
    print("Tie")
elif game_instance in win:
    print("Win")
else:
    print("Loose")
