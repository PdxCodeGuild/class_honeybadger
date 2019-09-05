########## program starts here
import random

answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

print("\n")
print("*-" *12)
user_play = input("\nDo you want to play 'Magic 8 Ball'?\n\n")

if user_play == "yes":
    print("\nGreat!")
else:
    print("\nOk, maybe next time.\n")

while user_play == "yes":
    user_question = input("\nPlease ask a 'yes or no' question: ")
    print(f"\nYou asked: {user_question}")
    response = random.choice(answers)
    print(f"\nThe Magic 8 Ball says: {response}\n")

    user_play = input("Do you want to play again?\n\n")
    if user_play == "no":
        print("\nOk, have a great day!\n")
    else:
        continue
