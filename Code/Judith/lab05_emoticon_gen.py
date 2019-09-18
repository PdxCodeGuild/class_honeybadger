#filename: lab05_emoticon_gen.py

import random

flag = True

while flag:
    i = 0
    eyes=[";",":",":'",">:","X"]
    noses=["^","-"]
    mouths=[")","(","O","P","D"]

    while i < 5:
        print(random.choice(eyes)+random.choice(noses)+random.choice(mouths))
        i += 1

    answer=input("Would you like more faces? Y or N: ")
    if answer==("Y"):
        continue
    elif answer==("N"):
        print("Have a goodun'")
        flag = False
    else:
        print("okay wierdo...")
        continue
