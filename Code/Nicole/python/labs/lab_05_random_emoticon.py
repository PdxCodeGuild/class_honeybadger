# lab_05_random_emoticon.py

# URL :: https://github.com/PdxCodeGuild/class_honeybadger/blob/master/1%20Python/labs/lab05-random_emoticon_generator.md

import random

def emoticon():
    eyes = [":", ";", "):", ":`", "|:"]
    noses = ["-", "•", ">"]
    mouths = ["D", "|", "P", ")", "("]
    
    count = 0
    while count <= 5:
        print(random.choice(eyes) + random.choice(noses) + random.choice(mouths))
        count += 1
        
emoticon()