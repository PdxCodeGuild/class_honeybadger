# guess_number_adv2.py

import random

# this will determine how many times the game is played
tries = int()

# welcome
print("*" *10 + "\nLet's play a number game!")

# begin game

game_play = "yes"
while game_play in ["yes", "y"]:
    c_numb = random.randint(1,10)
    print(f"\n*** The computer picked {c_numb} ***")
    u_numb = input("\nPlease type a number between 1 and 10: ")
    tries += 1
    u_numb = int(u_numb)

    if u_numb == c_numb:
        print("\nYou got it right!\n")
    elif u_numb > c_numb:
        print("\nYour number is too high!\n")
    elif u_numb < c_numb:
        print("\nYour number is too low!\n")
    else:
        print("\nNope, that's not it.\n")
    game_play = input("Would you like to play again? ").lower()

else:
    if tries == 1:
        print(f"\nYou played the game {tries} time.")
    else:
        print(f"\nYou played the game {tries} times.")
