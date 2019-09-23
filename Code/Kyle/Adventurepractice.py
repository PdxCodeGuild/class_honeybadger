



import random


choices = ["quick attack", "heavy attack", "dodge"]
user_health = 30
cpu_health = 30
miss = 0
dodged_attack = 1

cpu_choice = random.choice(choices)


# user_wins = ["rock vs scissors", "paper vs rock", "scissors vs paper"]
# cpu_win = ["rock vs paper", "scissors vs rock", "paper vs scissors"]

play_again = "yes"

print("Welcome to adventure battle!")

print("Health: " (user_health), "Enemy: "

# while play_again == "yes":

user_choice = input("CHOOSE YOUR ACTION >>> 'QUICK ATTACK', 'HEAVY ATTACK', 'DODGE' ").lower()
cpu_choice = random.choice(choices)


if user_choice == 'Q':
    cpu_health -= 3
    print(cpu_health)
# elif user_choice == 'D' cpu_choice == miss or cpu_choice = dodged_attack
# if cpu_choice == dodged_attack:
#     user_health -= 1
else:
    exit()





    # outcome = user_choice + " vs " + cpu_choice

    # print(outcome)

    # # if outcome in tie_outcomes:
    # #     print("IT'S A TIE")
    # if outcome in user_wins:
    #     print("You Won!!")
    # elif outcome in cpu_win:
    #     print("Oof! you lost")

    # else:
    #     print("Please enter rock, paper or scissors.")
    # play_again = input("Would you like to play again? yes/no ").lower()

# while play_again not in ["yes", "no"]:
#     play_again = input("Do you want to play again? (yes/no) ").lower()
#
# else:
#     print("Come back soon!")
