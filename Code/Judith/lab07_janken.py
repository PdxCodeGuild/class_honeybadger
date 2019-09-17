#filename: lab07_janken.py

#modules
import random

#set universal variable as True to enable while loop
game_in_session=True

#choose variables
atklist=["rock","paper","scissors"]


while game_in_session==True:

    pcatk=random.choice(atklist)

    usratk=input("One! Two!! Three!!!\n").lower()

    print("you used ",usratk)
    print("your opponent used ",pcatk)

    if usratk==pcatk:
        print("it's a draw!")
    elif usratk==("rock") and pcatk==("scissors"):
        print("you win!")
    elif usratk==("rock") and pcatk==("paper"):
        print("you lose!")
    elif usratk==("scissors") and pcatk==("paper"):
        print("you win!")
    elif usratk==("scissors") and pcatk==("rock"):
        print("you lose!")
    elif usratk==("paper") and pcatk==("rock"):
        print("you win!")
    elif usratk==("paper") and pcatk==("scissors"):
        print("you lose!")
    else:
        print("that aint how this game works...")

    play_again=input("Do you want to play again? Y or N ").lower()
    if play_again in["y","yes"]:
        game_in_session=True
    elif play_again in["n","no"]:
        game_in_session=False
    else:
        print("Invalid input.")
        break
else:
    print("goodbye")
