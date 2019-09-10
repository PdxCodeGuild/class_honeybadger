import random

again = "yes"
turn_counter = 0
random_number = random.randint(1,10)
print(random_number)

def num_check():
    user_guess = input("The computer has picked a random number between 1 and 10. \nGuess what it is: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Don't be silly, enter a number!")
    return user_guess

user_guess_check = num_check()

if user_guess_check == random_number:
    print("you are some sort of Houdini! You are right.")
elif user_guess_check not in range(1,11):
    print("Please pick a number between 1 and 10")
elif user_guess_check > random_number:
    print("too high!")
else:
    print("too low!")

again = input("Want to play again?: ")
while again == "yes" and turn_counter < 11:
        turn_counter += 1
        print(f"This is your {turn_counter} guess")
else:
    print("No? OK, maybe next time.")
