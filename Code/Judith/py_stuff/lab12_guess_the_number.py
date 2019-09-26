#filename: lab12_guess_the_number.py

#modules
import random

#set of 1 to 10
numbers=[1,2,3,4,5,6,7,8,9,10]

#greetings
print("Hello, you will get 10 tries to guess the number between 1 and 10...."" Lets see if you can do it :)")

#number chosen at random by pc
pc_num=random.choice(numbers)
print(pc_num)

#variables set up outside loop
attempts = 0
last_guess = False

while True:
    user_input = int(input('choose a number between one and ten... '))
    attempts += 1
    if user_input not in numbers:
        print('invalid input')
        print('thats guess number ',attempts)
        continue
    if user_input == pc_num:
        print('you won in ',attempts,' guesses')
        exit()
    if user_input > pc_num:
        print('too high!')
    else:
        print('too low!')
    if last_guess:
        if abs(last_guess-pc_num) > abs(user_input-pc_num):
            print('getting warmer!')
        if abs(last_guess-pc_num) < abs(user_input-pc_num):
            print('little chilly')
    last_guess = user_input

