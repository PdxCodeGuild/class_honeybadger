# guess_number_adv4b.py

import random

# this will determine how many times the game is played
tries = int()

# welcome
print("*" *10 + "\nLet's play a number game! See if you can guess what the computer picks.")

# begin game

# game_play = "yes"

# computer chooses a random number
c_numb = random.randint(1,10)

# define the calculation to determine if the current guess is closer or farther away from the last guess

def calc_close_far(u_numb, last_guess, c_numb):
    if u_numb > last_guess > c_numb:
        print("\nYou are farther from your last guess.")
    elif u_numb < last_guess < c_numb:
        print("\nYou are farther from your last guess.")
    else:
        print("\nYou are closer than your last guess.")

# this is what the computer picks, for checking the code
print(f"\n*** The computer picked {c_numb} ***")

# ask the first question, befor "for" loop
u_numb = input("\nPlease guess a number between 1 and 10: ")
# placeholder for last_guess
last_guess = 0

#begin loop
for tries in range(1, 10):
    # print(f"\nThis is round {tries}.\n")
    u_numb = int(u_numb)
    last_guess = int(last_guess)
    # print(last_guess)
    if tries > 1 and u_numb != c_numb:
        close_far = calc_close_far(u_numb, last_guess, c_numb)
        print(f"\nThat is not correct. You have {10 - tries} guesses remaining.")
        last_guess = u_numb
        u_numb = input("\nPlease guess again: ")
    elif u_numb != c_numb:
        print(f"\nThat is not correct. You have {10 - tries} guesses remaining.")
        last_guess = u_numb
        u_numb = input("\nPlease guess again: ")
    else:
        print("\nYou got it right!\n")
        break
else:
    print("Sorry, you lose. Thanks for playing!")
