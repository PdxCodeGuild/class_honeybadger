import random

eyes = [':', ';', ':_', '|', '8']
noses = ['-', '.', 'v']
mouths = [')', '(', 'D', '#']
for x in range(5):
    eye_rndm = random.choice(eyes)
    nose_rndm = random.choice(noses)
    mouth_rndm = random.choice(mouths)
    print(f"{eye_rndm}{nose_rndm}{mouth_rndm}")
another_one = input("Do you want to see another one?")
while another_one == "yes":
    print(f"{eye_rndm}{nose_rndm}{mouth_rndm}")
    another_one = input("Do you want to see another one?")  
else:
    print("Later, alligator!")
