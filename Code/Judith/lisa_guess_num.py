# filename: guess_the_num.py

# Goal: User to guess the num that the computer randomly chose
# - greet User = print() - D
# - computer choosed num between 1-100 = random.randint(min,max) - D
# - program prompts user to guess a num between 1-100 = input() - D
# - check if user guess is correct =    == - D

# input validation
# - check if digit - D
# - check if number is within range - D

# stretch
# - tell the user their guess is too high or too low = if/else - D
# - quit program after 5 guesses = counter - D
# - tell the user if they are closer than last time = save last guess to a variable after the first round - D

# Modules
import random

# Variables
range_min = 0
range_max = 50
counter = 1

# functions

def guess_diff(last_guess, user_guess, comp_num):
    last_diff = abs(last_guess - comp_num)
    curr_diff = abs(user_guess - comp_num)

    if last_diff < curr_diff:
        print("Last time, you were closer!")
    else:
        print("Closer than last time!")

# greet user
print("Hello, let's play the number guessing game! You have five tries.")
comp_num = random.randint(range_min, range_max)

# use input function to save user guess
user_guess = input(f"Please guess a number between {range_min}-{range_max}...")

# printing to make sure variables are saving properly
# print("comp num: " + str(comp_num))
# print("user_guess: " + str(user_guess))

# as long as counter is less than 5, do the following
while counter < 5:

    # print guess #
    print(f"\nGuess #{counter}")

    # if user guess is a digit
    if user_guess.isdigit():
        # print("Input is a digit.")

        # convert string to integer
        user_guess = int(user_guess)

        # if user guess is within range
        if range_min <= user_guess <= range_max:

            # if user guess is the same as comp num
            if user_guess == comp_num:
                # print winning message
                print("You guessed correct!")
            else: # if user guess is wrong
                # if user guess is greater than comp num
                if user_guess > comp_num:
                    print("You guessed wrong! Too high!")

                    # if guess # 2 or higher
                    if counter > 1:
                        # check for differences
                        guess_diff(last_guess, user_guess, comp_num)
                else: # if user guess is lower than comp num
                    print("You guessed wrong! Too low!")

                    # check for differences
                    if counter > 1:
                        guess_diff(last_guess, user_guess, comp_num)
        else:# if number is out of range
            print(f"Error: Please enter number between {range_min}-{range_max}.")
    else: # if input is not a number
        print(f"Error: Please enter number between {range_min}-{range_max}.")

    # save number to last guess variable so we can check it in the next round before it gets overwritten
    last_guess = user_guess

    # this is where the next round starts
    user_guess = input("\nGuess again...")

    counter += 1
else:
    print(f"Game over. You've used up your five lives. The number was {comp_num}")
