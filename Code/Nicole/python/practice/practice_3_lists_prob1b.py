# practice_3_lists_prob1b.py

import random

# define function

def random_element(a):
    camera_pick = random.randint(0, len(a))
    return camera_pick
    
# define list

camera = ["Fujifilm", "Canon", "Sony", "Pentax", "Nikon", "Olympus", "Hassleblad"]

print(camera[random_element(camera)])