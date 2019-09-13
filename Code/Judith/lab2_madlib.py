#filename: lab2_madlib.py

import random

play_flag = True
while play_flag:
    adj1=input("Give us an adjetive: ")
    adj2=input("Give us another now, come on: ")
    verb1=input("A verb now, an action: ")
    verb2=input("Three more verbs: ")
    nl = "\n"
    txt=verb2.split()

    print(f'{nl}The elder spoke to the child: Inside of you there are two wolves: {nl}one is {adj1}, and the other is {adj2}. {nl}The child asked: Which will {verb1}? {nl}The elder replied: The one you {random.choice(txt)}.')
    play_again_question = 'tree'
    while play_again_question not in ['y','n']:
        play_again_question = input('would you like to play again? y or n... ')
        if play_again_question == 'y':
            continue
        if play_again_question == 'n':
            play_flag = False
            break
        else:
            print('invalid input')