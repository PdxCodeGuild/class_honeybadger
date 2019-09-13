import random

print('Hello, welcome to magic 8 ball!')


game_in_session = input('What question do you want to ask the Magic 8 Ball?: ')
while game_in_session != 'done':

    predictions = ['yes','no','maybe','my sources say no','cannot preditct now',]
    magic_answer = random.choice(predictions)
    print(magic_answer)
    game_in_session = input('Do you have another question? if not type "done" to exit: ')
