# practice_3_lists_prob1.py

import random

# define function

def random_element(camera):
    pick_camera = random.choice(camera)
    return pick_camera
    
    
# define list

camera = ["Fujifilm", "Canon", "Sony", "Pentax", "Nikon", "Olympus", "Hassleblad"]

print(f"Your random camera choice is: {random_element(camera)}")