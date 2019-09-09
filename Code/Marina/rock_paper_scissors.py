import random

choices = ["rock", "paper", "scissors"]
comp_choice = random.choice(choices)

user_choice = input("Rock, paper or scissors? ")

print(comp_choice)

game_instance = (f"{user_choice} vs {comp_choice}")

print(game_instance)

print(f"{user_choice} vs {comp_choice}")

# rock vs rock (tie)
# paper vs paper
# scissors vs scissors

# paper vs rock(win)
# rock vs scissors
# scissors vs paper

# rock vs paper(loose)
# paper vs scissors
# scissors vs rock

# tie = ["rock vs rock", "paper vs paper", "scissors vs scissors"]

win = ["paper vs rock", "rock vs scissors", "scissors vs paper"]

# loose = ["rock vs paper", "paper vs scissors", "scissors vs rock"]

if user_choice == comp_choice:
    print("Tie")
elif game_instance in win:
    print("Win")
else:
    print("Loose")
