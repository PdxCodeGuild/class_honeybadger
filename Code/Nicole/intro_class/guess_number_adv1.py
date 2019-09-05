# guess_number_adv1.py

import random

print("*" *10 + "\nLet's play a number game!")
game_play = "yes"
while game_play in ["yes", "y"]:
    c_numb = random.randint(1,10)
    print(f"\n*** The computer picked {c_numb} ***")
    u_numb = input("\nPlease type a number between 1 and 10: ")
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
        print("\nGoodbye.\n")
