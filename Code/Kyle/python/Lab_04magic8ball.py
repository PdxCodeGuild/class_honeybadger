#magic 8 ball

#variables

import random

print("Welcome to Magic 8 Ball")

choices = ["Uncertain", "Possibly", "No", "Yes"]

question = input("Ask a question  ")
print(f"Answer {random.choice(choices)}")
