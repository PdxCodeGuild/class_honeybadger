# emoticons_nicole_adv_4.py

import random

# HORIZONTAL face parts:

h_eyes = [":", ";", "X", "#", "%"]
h_noses = ["-", "~", "^", "=", "•"]
h_mouths = [")", "D", "o", "|", ")"]

# VERTICAL face parts:

v_eyes = ["o", "--", "''", "*", ">"]
v_noses = ["_", "•", "."]
v_mouths = ["o", "--", "''", "*", ">"]

# MULTI-LINE face parts:

m_eyes = ["o o\n", "o -\n", "- -\n", "• •\n", "* *\n"]
m_noses = [" | \n", " . \n", " # \n", " • \n", " ! \n"]
m_mouths = [" o ", " _ ", " ~ "]

# let user choose the type of face

print("\n*" * 5)

face_question = input("\nWould you like to see a face?\n\n")

if face_question == "yes":
    format_user = input("\nWhich type of face would you like to see: horizontal, vertical, or multi-line face?\n\n")
    format_user = (f"{format_user.lower()}")
else:
    print("\nOk, maybe next time.\n")

while face_question == "yes":
    if format_user == "horizontal":
        final_face = random.choice(h_eyes) + random.choice(h_noses) + random.choice(h_mouths)
        print(f"\nHere is your face: {final_face}\n")

    elif format_user == "vertical":
        final_face = random.choice(v_eyes) + random.choice(v_noses) + random.choice(v_mouths)
        print(f"\nHere is your face: {final_face}\n")

    elif format_user == "multi-line":
        final_face = random.choice(m_eyes) + random.choice(m_noses) + random.choice(m_mouths)
        print(f"\nHere is your face: {final_face}\n")

    else:
        format_user = input("Please type either vertical, horizontal, or multi-line.)\n\n")
        continue

    face_question = input(f"Would you like to see another {format_user} face?\n\n")
    if face_question == "no":
        print("\nOk, have a great day!\n")
