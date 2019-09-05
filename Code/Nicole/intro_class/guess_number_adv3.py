# guess_number_adv3.py

import random

# this will determine how many times the game is played
tries = int()

# welcome
print("*" *10 + "\nLet's play a number game! See if you can guess what the computer picks.")

# begin game


game_play = "yes"
c_numb = random.randint(1,10)

# this is what the computer picks, for checking the code
print(f"\n*** The computer picked {c_numb} ***")

u_numb = input("\nPlease guess a number between 1 and 10: ")

for tries in range(1, 10):
    u_numb = int(u_numb)
    if u_numb != c_numb:
        print(f"\nThat is not correct. You have {10 - tries} guesses remaining")
        u_numb = input("\nPlease guess again: ")
    else:
        print("\nYou got it right!\n")
        break
else:
    print("Sorry, you lose. Thanks for playing!")
