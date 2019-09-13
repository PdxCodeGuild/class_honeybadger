# filename: calculator.py


import random
print(("*"*10) + "Welcome to the Gambling Calculator Game" + ("*"*10))
num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))

print(f"Your numbers: {num1} & {num2}")

operators_list = ["+", "-", "*", "/"]

chosen_operator = random.choice(operators_list)

print(chosen_operator)


# if/else = 2 conditions
# elif = more than 2 conditions

if chosen_operator == "+":
    results = num1 + num2
elif chosen_operator == "-":
    results = num1 - num2
elif chosen_operator == "*":
    results = num1 * num2
else:
    results = num1 / num2

print(results)
