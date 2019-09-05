# emoticons.py

import random

#list of face parts

eyes = [":", ";", "X", "#", "%"]
noses = ["-", "~", "^", "=", "•"]
mouths = [")", "D", "o", "(", "|"]

# let user choose each part of the face

eye_user = input("What would you like the EYES to look like? (Press enter/return to let the computer choose)\n\n")

print("\n")

nose_user = input("What would you like the NOSE to look like? (Press enter/return to let the computer choose)\n\n")

print("\n")

mouth_user = input("What would you like the MOUTH to look like? (Press enter/return to let the computer choose)\n\n")

print("\n")

if eye_user == "":
    eye_user = random.choice(eyes)
else:
    eye_user = eye_user

if nose_user == "":
    nose_user = random.choice(noses)
else:
    eye_user = eye_user

if mouth_user == "":
    mouth_user = random.choice(mouths)
else:
    mouth_user = mouth_user

final_face = eye_user + nose_user + mouth_user
print(f"Here is your face: \n\n{final_face}\n\n")
