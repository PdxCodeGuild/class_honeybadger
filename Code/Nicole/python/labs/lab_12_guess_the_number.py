# lab_12_guess_the_number.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab12-guess_the_number.md

import random

def guess_number_v1():
    computer_num = random.randint(1, 10)
    print(f"The computer guessed {computer_num}")
    tries = 10
    while tries > 0:
        user_num = input("Guess a number between 1 and 10: ")
        user_num = int(user_num)
        if user_num == computer_num:
            print("You win!")
            tries = 0

def guess_number_v2():
    computer_num = random.randint(1, 10)
    print(f"The computer guessed {computer_num}")
    tries = 1
    while True:
        user_num = input("Guess a number between 1 and 10: ")
        user_num = int(user_num)
        if user_num == computer_num:
            tries += 0
            print(f"You win! It took you {tries} guesses to get the correct number.")
            break
        else:
            tries += 1
            

def guess_number_v3():
    computer_num = random.randint(1, 10)
    print(f"The computer guessed {computer_num}")
    tries = 1
    while True:
        user_num = input("Guess a number between 1 and 10: ")
        user_num = int(user_num)
        if user_num == computer_num:
            tries += 0
            print(f"You win! It took you {tries} guesses to get the correct number.")
            break
        elif user_num < computer_num:
            print(f"Your number is too low.")
            tries += 1
        elif user_num > computer_num:
            print(f"Your number is too high.")
            tries += 1
            
    
guess_number_v3()