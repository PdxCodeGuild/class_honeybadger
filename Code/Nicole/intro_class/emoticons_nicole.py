# emoticons.py

import random

#list of face parts

eyes = [":", ";", "X", "#", "%"]
noses = ["-", "~", "^", "=", "•"]
mouths = [")", "D", "o", "(", "|"]

# for loop
for x in range(5):
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    final_face = eye + nose + mouth
    print(final_face)

# question
face_input = input("Would you like to see another random face? (Type 'yes' or 'no')\n")

#while loop
while face_input == "yes":
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    final_face = eye + nose + mouth
    print(f"Here is your face: {final_face}")

    face_input = input("Would you like to see a face? (Type 'yes' or 'no')\n")
