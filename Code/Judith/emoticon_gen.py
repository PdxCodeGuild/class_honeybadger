#filename: emoticon_gen.py

import random

eyes=[";",":",":'",">:","X"]
noses=["^","-"]
mouths=[")","(","O","P","D"]

eye=random.choice(eyes)
nose=random.choice(noses)
mouth=random.choice(mouths)

face=(eye+nose+mouth)

print(face)

answer=input("Would you like another face? Y or N: ")
if answer==("Y"):
    eye=random.choice(eyes)
    nose=random.choice(noses)
    mouth=random.choice(mouths)

    face=(eye+nose+mouth)
    print(face)

elif answer==("N"):
    print("Have a goodun'")
else:
    print("okay wierdo...")
