# guess_number.py

import random

game_play = "yes"
while game_play in ["yes", "y"]:

    c_numb = random.randint(1,10)
    print(f"\n*** The computer picked {c_numb} ***")
    u_numb = int(input("Please type a number between 1 and 10: "))

    if u_numb == c_numb:
        print("You got it right!")
    elif u_numb not in range(1,11):
        print("Sorry, you need to type a number between 1 and 10.")
    else:
        print("Nope, that's not it.")

        game_play = input("Would you like to play again? ").lower()
else:
    print("Goodbye.")
