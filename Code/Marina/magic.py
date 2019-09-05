import random

answers = ["Yes", "No", "Maybe", "Signs point to yes.", "Cannot predict now.", "My sources say no."]

print("-" * 50)
print("Ask the magic 8 ball anything!\n")

user_question = input("Ask your question: ")

print(f"You asked: {user_question}\n")

answer = random.choice(answers)

print(f"\nMagic 8 Ball Knows All, Your answer is: {answer}")

second_question = input("Would you like a chance to ask another question? ")

print(f"Your second question is {second_question}\n")

answer = random.choice(answers)

print(f"\nMagic 8 Ball Will Now Answer Your Second Question. Your answer is: {answer}")
