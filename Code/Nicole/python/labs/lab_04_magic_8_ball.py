# lab_04_magic_8_ball.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab04-magic_8_ball.md

# versions 1 and 2

import random

def magic_8_ball():
    print("Welcome to the game!")
    magic_dict = {
        1 : "It is certain",
        2 : "It is decidedly so",
        3 : "Without a doubt",
        4 : "Yes, definitely",
        5 : "You may rely on it",
        6 : "As I see it, yes",
        7 : "Most likely",
        8 : "Outlook good",
        9 : "Yes",
        10 : "Signs point to yes",
        11 : "Reply hazy try again",
        12 : "Ask again later",
        13 : "Better not tell you now",
        14 : "Cannot predict now",
        15 : "Concentrate and ask again",
        16 : "Don't count on it",
        17 : "My reply is no",
        18 : "My sources say no",
        19 : "Outlook not so good",
        20 : "Very doubtful"
    }
    num = len(magic_dict)
    again = "yes"
    
    while again == "yes":
        user_question = input("\nPlease ask a 'yes or no' question: \n\n")
        print(f"\nThe Magic 8 Ball Says: \"{magic_dict[random.randint(1, num)]}\"\n")
        again = input("Would you like to ask another question (type 'no' to quit the game or 'yes' to ask again): \n")
    
    print("\nThanks for playing! Don't forget: the future is in your hands and not some stupid 'magic' ball.")
    
magic_8_ball()