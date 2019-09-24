import random

play_again = "y"
random_number = random.randint(1, 10)

user_input = int(input("Please enter a number between 1 and 10: "))

while play_again == "y":
    if user_input != random_number:
        print("Try again!")
        user_input = int(input("Please enter a number between 1 and 10: "))
    elif user_input == random_number:
        print("You won!")
        play_again = input("Would you like to play again? (y/n)")
    else:
        input("Please select a number between 1 and 10: ")

while play_again not in ["y", "n"]:
    play_again = input("Would you like to play again? (y/n)")

else:
    print("Peace out")
