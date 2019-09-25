import random

choices = ["rock", "paper", "scissors"]
comp_choice = random.choice(choices)

user_choice = input("Rock, paper or scissors? ")

print(f"Computer chose {comp_choice}")

game_instance = (f"{user_choice} vs {comp_choice}")

print(game_instance)

win = ["paper vs rock", "rock vs scissors", "scissors vs paper"]


if user_choice == comp_choice:
    print("It's a tie")
elif game_instance in win:
    print("YOU Win!")
else:
    print("Looser...computer beat you!")
