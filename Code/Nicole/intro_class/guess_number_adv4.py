# guess_number_adv4.py

import random

# this will determine how many times the game is played
tries = int()

# welcome
print("*" *10 + "\nLet's play a number game! See if you can guess what the computer picks.")

# begin game

game_play = "yes"
c_numb = random.randint(1,10)

# function to determine how many digits away they guessed

def calc_numb_diff(u_numb, c_numb):

    numb_diff = u_numb - c_numb
    numb_diff = abs(numb_diff)
    numb_diff = str(numb_diff)
    return numb_diff

# this is what the computer picks, for checking the code
print(f"\n*** The computer picked {c_numb} ***")

u_numb = input("\nPlease guess a number between 1 and 10: ")


for tries in range(1, 10):
    print(f"\nThis is round {tries}.")
    u_numb = int(u_numb)
    diff = calc_numb_diff(u_numb, c_numb)
    # direction = calc_numb_dir()
    # direction = str(direction)
    if u_numb != c_numb:
        print(f"\nThat is not correct. You are {diff} digits from the correct answer. You have {10 - tries} guesses remaining.")
        u_numb = input("\nPlease guess again: ")
    else:
        print("\nYou got it right!\n")
        break
else:
    print("Sorry, you lose. Thanks for playing!")
